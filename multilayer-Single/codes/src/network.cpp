#include "network.h"

network::network(const string& paraFolder) {

    // Create class to store all file names
    file dataFile ; // Use default constructor

    dataFile.set_dagFile        (paraFolder + "DAG.csv");
    dataFile.set_inoutFile      (paraFolder + "/inout.csv");
    dataFile.set_propertiesFile (paraFolder + "Parameters/systemic_network.csv");
    dataFile.set_dxFile         (paraFolder + "Parameters/dx.csv");
    dataFile.set_dlFile      (paraFolder + "Parameters/layer.csv");
    dataFile.set_a0File         (paraFolder + "Parameters/A0.csv");
    dataFile.set_kFile          (paraFolder + "Parameters/K.csv");
    dataFile.set_cvFile         (paraFolder + "Parameters/Cv.csv");
    dataFile.set_knlFile         (paraFolder + "Parameters/Knl.csv");
    dataFile.set_initaFile      (paraFolder + "Parameters/initA.csv");
    dataFile.set_initqFile      (paraFolder + "Parameters/initQ.csv");
    dataFile.set_outputFile     (paraFolder + "/output.csv");
    dataFile.set_outputProFile  (paraFolder + "/outputProfile.csv");
    dataFile.set_timeFile       (paraFolder + "/time.csv");

    // Parse all input files
    parser fileParser(dataFile);

    // Get the number of arteries and resize vP
    nart  = fileParser.nSet(			(dataFile.get_propertiesFile()).c_str());
  	nconj = nart + 1 ;
  	nbc  = fileParser.nSet(				(dataFile.get_inoutFile()).c_str());

    printf("\nNetwork definition\n") ;
    printf("#########################################\n") ;
		printf("Number of arteries        : %d\n"   , nart );
		printf("Number of conjunctions    : %d\n"   , nconj );
    printf("Number of imposed BC      : %d\n" , nbc );

    vP.resize(nart) ;

    // Set vessel properties
    fileParser.propertiesSet(vP,nart) ;

    // Set boundary properties
    fileParser.bcSet(vP,nbc) ;

    // Set time properties
    timenet.set_n(0) ;
    fileParser.tSet(timenet);
    if ( (int( timenet.get_te()/timenet.get_dt()) != timenet.get_nt()) && (floor( timenet.get_te()/timenet.get_dt()) != timenet.get_nt()) && (ceil( timenet.get_te()/timenet.get_dt()) != timenet.get_nt()) ) {

      if ( (int( timenet.get_te()/timenet.get_dt()) - 1 != timenet.get_nt()) && (int( timenet.get_te()/timenet.get_dt()) + 1 != timenet.get_nt()) ) {
        printf("\nint(te/dt)=%d, ,nt=%d\n", int( timenet.get_te()/timenet.get_dt()), timenet.get_nt() );
        Error("network: int( te/dt) != nt");
      }
    }

    printf("Time definition\n") ;
    printf("#########################################\n") ;
		printf("Number of time steps      : %d\n"       , timenet.get_nt() );
    printf("CFL condition             : %.14Lf\n"   , timenet.get_cfl() );
    printf("Time order                : %d\n"       , timenet.get_order() );
		printf("Time step                 : %.14Lf\n"   , timenet.get_dt() );
    printf("Start time                : %.14Lf\n"   , timenet.get_ts() );
    printf("Final time                : %.14Lf\n"   , timenet.get_te() );

    // Set output
    fileParser.outputSet(outnet);
    printf("Output definition\n") ;
    printf("#########################################\n") ;
		printf("Number of output arteries : %d\n"           , outnet.size_storeArt() );
		printf("Number of output positions: %d\n\n"         , outnet.size_posRecord() );
    printf("Number of profile output positions: %d\n\n" , outnet.size_posProfileRecord() );

    // Create arteries
    arts.resize(nart,0);     // contains pointers to artery
    for (int i=0; i< nart; i++) {
      appointSolver(arts[i],vP[i],timenet);
    }

    // Initialize residu
    resnet.set_resA   ( ZERO ) ;
    resnet.set_resAmax( ZERO ) ;
    resnet.set_resQ   ( ZERO ) ;
    resnet.set_resQmax( ZERO ) ;

}
//####################################################
// Run Sequential
//####################################################
void network::run(){

  // Open data files
  openFile() ;

  int prin = 1;

  // Verbose for arteries
  arts[0]->verbose(timenet);

  // Initialization of arteries
  for(int i=0; i<nart; i++) {
    arts[i]->initialization(timenet);
  }

  // Store initial data
  writeToFile(ZERO);
  writeToProfile(ZERO);

  // Temporal loop
  //###################
  for (int it = 1; it < timenet.get_nt() ; it++){

    // Check if time step verifies CFL condition
    check_dt() ;

    if (it != timenet.get_n()+1) {
      printf("\nit=%d, \t n=%d\n", it, timenet.get_n()+1 );
      Error("network::run it != timenet.get_n()+1");
    }

    if ( abs(timenet.get_t(it) - double(it*timenet.get_dt())) > EPSILON ) {
      printf("\nt=%.14f, \t it*dt=%.14f\n", double(timenet.get_t(it)), double(it*timenet.get_dt()) );
      Error("network::run timenet.get_t(it) != double(it*timenet.get_nt())");
    }

    //   checkSteady() ;

    if ( int(0.01* prin * timenet.get_nt()) == it){
      printf("Completion      : %5.2f %% \n" , 100.*double(it) / double(timenet.get_nt()) );
      printf("      Iteration : %d\n"         , it );
      printf("      Time      : %5.10f\n"        , double( it * timenet.get_dt())  );
      printf("      Time step : dt=%1.8f, dtCFL=%1.8f\n" ,  double(timenet.get_dt()), double(timenet.get_dtcfl()));
      check_residu() ;
      fflush(stdout);
      prin++;
    }

    // Set boundary conditions
    for(int i=0; i < nart; i++) {
      arts[i]->stepBC(timenet);
    }
    // Time advance
    for(int i=0; i < nart; i++) {
      arts[i]->step(timenet);
    }

    // Update n
    timenet.set_n(it);

    if( it%timenet.get_nstore()==0 && timenet.get_t(it) >= timenet.get_ts() ){
      writeToFile(timenet.get_t(it));
    }
    if( it%timenet.get_nstoreprofile()==0 && timenet.get_t(it) >= timenet.get_ts() ){
      writeToProfile(timenet.get_t(it));
    }
  } // END TEMPORAL LOOP

  // Store Final Time
  writeToFile(timenet.get_t( timenet.get_nt()-1 ));
  writeToProfile(timenet.get_t( timenet.get_nt()-1 ));
  closeFile();

  cout<<"End of computation."<<endl;
}
//####################################################
// Appoint Solver
//####################################################
void network::appointSolver(artery*& art, vesselProperties& vP, time_c& timenet ){

        string solver=vP.get_solver();
        if(solver=="RUS" || solver=="HLL" || solver=="KIN_HAT" || solver=="KIN_SQRT")
            art=new arteryNum(vP,timenet);
        else
            cerr<<" solver <"<< solver<<"> not defined"<<endl;

}
//####################################################
// Writters
//####################################################
void network::openFile(){

  string Artdatafile;
  string Profiledatafile;
  string Residudatafile;

  //Open artery files:
  file_record = (FILE **) malloc( (outnet.size_storeArt()) * sizeof(FILE*));
  profile_record = (FILE **) malloc( (outnet.size_storeArt()) * sizeof(FILE*));
  for(int i = 0; i < outnet.size_storeArt() ; ++i) {
    char buf[32];
    // now we build the file name
    snprintf(buf, sizeof(char) * 32, "Artery_%i.csv", outnet.get_storeArt(i));
    Artdatafile = dataFolder + "/" + suffix;
    Artdatafile += buf;
    Profiledatafile = dataFolder + "/" + suffix + "Profil_";
    Profiledatafile += buf;

    // Check if file exists:
    if (fileExist(Artdatafile) == 1) {

      printf("%s\n","Write over file: y/n" );

      string choice;

      getline(cin,choice);
      if (choice == "n" || choice == "N") {
        exit(1);
      }
    }

    // 1D DATA
    file_record[i] = fopen(Artdatafile.c_str(), "w");
    fprintf(file_record[i],
           "%s,\t %s,\t %s,\t %s,\t %s,\t %s,\t %s,\t %s,\t %s,\t %s,\t %s,\t %s \n ",
           "#t [s]","x [cm]","K [g/cm^2/s^2]","A0 [cm^2]",
           "A [cm^2]","Q [cm^3/s]","P [g/cm/s^2]","gradxP [g/cm^2/s^2]",
           "U0 [cm/s]", "Tw [g/cm/s^2]", "alpha", "phi"
            );
    fflush(file_record[i]);

    // PROFIL DATA
    profile_record[i] = fopen(Profiledatafile.c_str(), "w");
    fprintf(profile_record[i],
           "%s,\t %s,\t %s,\t %s,\t %s \n ",
           "#t [s]","x [cm]", "R [cm]", "Ux [cm/s]","Ur [cm/s]"
            );
    fflush(profile_record[i]);
  }

  //Open residu file
  Residudatafile = dataFolder + "/Residu_AQ.csv";
  file_residu = fopen(Residudatafile.c_str(), "w");
  fprintf(file_residu,
         "%s,\t %s,\t %s,\t %s,\t %s \n ",
         "#t [s]","res[A]","res[A_max]","res[Q]","res[Q_max]"
          );
  fflush(file_residu);

}
void network::closeFile(){
  //Close artery files:
  for(int i = 0; i < outnet.size_storeArt() ; ++i) {
    fflush(file_record[i]);
    fclose(file_record[i]);
    fflush(profile_record[i]);
    fclose(profile_record[i]);
  }
  free(file_record) ;
  free(profile_record) ;
  //Close residu file:
  fflush(file_residu);
  fclose(file_residu);
}

void network::writeToFile(const SCALAR _t) const{

  int iArt=0;
  // Loop on all record points
  //#####################
  for(int i=0; i<outnet.size_arteryRecord(); i++) {
    if (outnet.get_arteryRecord(i) != outnet.get_storeArt(iArt) ) {
      fprintf(file_record[iArt], "\n");
      fprintf(file_record[iArt], "\n");
      iArt ++;
    }
    fprintf(file_record[iArt],
        "%20.20f ,\t %20.20f,\t %20.20f,\t %20.20f,\t %20.20f,\t %20.20f,\t %20.20f,\t %20.20f,\t %20.20f,\t %20.20f,\t %20.20f,\t %20.20f  \n",
        double(_t),
        arts[outnet.get_arteryRecord(i)]->read_x      (outnet.get_posRecord(i)),
        arts[outnet.get_arteryRecord(i)]->read_k      (outnet.get_posRecord(i)),
        arts[outnet.get_arteryRecord(i)]->read_a0     (outnet.get_posRecord(i)),
        arts[outnet.get_arteryRecord(i)]->read_A      (outnet.get_posRecord(i)),
        arts[outnet.get_arteryRecord(i)]->read_Q      (outnet.get_posRecord(i)),
        arts[outnet.get_arteryRecord(i)]->read_P      (outnet.get_posRecord(i),timenet.get_dt()),
        arts[outnet.get_arteryRecord(i)]->read_gradxP (outnet.get_posRecord(i)),
        arts[outnet.get_arteryRecord(i)]->read_U0     (outnet.get_posRecord(i)),
        arts[outnet.get_arteryRecord(i)]->read_Tw     (outnet.get_posRecord(i)),
        arts[outnet.get_arteryRecord(i)]->read_alpha  (outnet.get_posRecord(i)),
        arts[outnet.get_arteryRecord(i)]->read_phi    (outnet.get_posRecord(i))
    );
    fflush(file_record[iArt]);
  }

  fprintf(file_record[iArt], "\n");
  fprintf(file_record[iArt], "\n");
  fflush(file_record[iArt]);

  //Write residu
  fprintf(file_residu,
      "%20.20Lf ,\t %20.20Lf ,\t %20.20Lf ,\t%20.20Lf ,\t %20.20Lf \n",
      _t,
      resnet.get_resA(),
      resnet.get_resAmax(),
      resnet.get_resQ(),
      resnet.get_resQmax()
  );
  fflush(file_residu);
}
void network::writeToProfile(const SCALAR _t) const{

  int iArt=0 ;
  int nl = 0 ;
  // Loop on all record points
  //#####################
  for(int i=0; i<outnet.size_arteryProfileRecord(); i++) {
    if (outnet.get_arteryProfileRecord(i) != outnet.get_storeArt(iArt) ) {
      fprintf(profile_record[iArt], "\n");
      fprintf(profile_record[iArt], "\n");
      iArt ++;
    }

    nl = arts[outnet.get_arteryProfileRecord(i)]->get_nl() ;

    // Write r<0
    for (int j=0; j<nl ; j++) {
      fprintf(profile_record[iArt],
          "%20.20f ,\t %20.20f,\t %20.20f,\t %20.20f,\t %20.20f \n",
          double(_t),
            arts[outnet.get_arteryProfileRecord(i)]->read_x    (         outnet.get_posProfileRecord(i)),
          - arts[outnet.get_arteryProfileRecord(i)]->read_Rl   (nl-1 - j,outnet.get_posProfileRecord(i)),
            arts[outnet.get_arteryProfileRecord(i)]->read_Ul   (nl-1 - j,outnet.get_posProfileRecord(i)),
            arts[outnet.get_arteryProfileRecord(i)]->read_Ulr  (nl-1 - j,outnet.get_posProfileRecord(i))
      );
      fflush(profile_record[iArt]);
    }
    // Write r>0
    for (int j=0; j<nl ; j++) {
      fprintf(profile_record[iArt],
          "%20.20f ,\t %20.20f,\t %20.20f,\t %20.20f,\t %20.20f \n",
          double(_t),
          arts[outnet.get_arteryProfileRecord(i)]->read_x    (           outnet.get_posProfileRecord(i)),
          arts[outnet.get_arteryProfileRecord(i)]->read_Rl   (j         ,outnet.get_posProfileRecord(i)),
          arts[outnet.get_arteryProfileRecord(i)]->read_Ul   (j         ,outnet.get_posProfileRecord(i)),
          arts[outnet.get_arteryProfileRecord(i)]->read_Ulr  (j         ,outnet.get_posProfileRecord(i))
      );
      fflush(profile_record[iArt]);
    }
  }

  fprintf(profile_record[iArt], "\n");
  fprintf(profile_record[iArt], "\n");
  fflush(profile_record[iArt]);
}
//####################################################
// Time Step
//####################################################
void network::check_dt() {
  SCALAR dt = ONE ;
  for (uint n = 0; n < arts.size(); n++) {
    if ( ( arts[n]->get_Lambdamax() * timenet.get_dt() ) > timenet.get_cfl() * arts[n]->get_dxmin() ) {
      printf("\nArtery %d, c*dt=%.14Lf, CFL*dx=%.14Lf\n", n, arts[n]->get_Lambdamax() * timenet.get_dt(), timenet.get_cfl() * arts[n]->get_dxmin() );
      Error("network::check_TimeStep Time step is too large.");
    }
    // dt = MIN(dt,timenet.get_cfl() * arts[n]->get_dxmin() / arts[n]->get_Lambdamax());
    dt = MIN(dt,timenet.get_cfl() * arts[n]->get_dtmin() ) ;
  }
  timenet.set_dtcfl(dt);
}
void network::check_residu() {
    SCALAR resA = ZERO , resQl = ZERO ;
    for (uint n = 0; n < arts.size(); n++) {
        resA += arts[n]->get_resA() ;
        resQl += arts[n]->get_resQl() ;
    }
    printf("         Residu A: %20.20e \n", double(resA)   / double(arts.size()) );
    printf("         Residu Ql: %20.20e \n", double(resQl) / double(arts.size()) );
}
//####################################################
// Other
//####################################################
bool network::fileExist (const string& name) {
  return ( access( name.c_str(), F_OK ) != -1 );
}
