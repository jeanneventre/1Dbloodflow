#include "parser.h"

parser::parser(const file& dataFile) {

	readtoString( (dataFile.get_propertiesFile()).c_str()	, propertiesData	);
	readtoMatrix( (dataFile.get_dxFile()).c_str()					,	dxData					);
	readtoMatrix( (dataFile.get_a0File()).c_str()					,	a0Data					);
	readtoMatrix( (dataFile.get_kFile()).c_str()					,	kData						);
	readtoMatrix( (dataFile.get_cvFile()).c_str()					, cvData					);
	readtoMatrix( (dataFile.get_knlFile()).c_str()			  ,	knlData						);

	readtoMatrix( (dataFile.get_dlFile()).c_str()					, dlData				);

	readtoMatrix( (dataFile.get_initaFile()).c_str()	, initaData	);
	readtoMatrix( (dataFile.get_initqFile()).c_str()	, initqData	);

	readtoMatrix( (dataFile.get_dagFile()).c_str()					, dagData					);
	readtoMatrix( (dataFile.get_outputFile()).c_str()				, outputData			);
	readtoMatrix( (dataFile.get_outputProFile()).c_str()		, outputProfileData			);

	readtoString( (dataFile.get_inoutFile()).c_str()				, inoutData				);

	readtoString( (dataFile.get_timeFile()).c_str()					, timeData				);

}
//####################################################
// Set
//####################################################
int parser::nSet( const char* file ) {

	int nbl=0;
	int j=0;
	string ch;   // store temporarily read strings
	size_t found;

	// Open file
  ifstream entries(file,ios::in);
	if (!entries) {
		cerr << "parser::readtoString: Impossible to open the " << file << " file\n" << endl;
		exit(1);
	}

	// Get nbl
	while (!entries.eof()) {
		getline (entries, ch);

		found = ch.find("#") ;
		j = int(found) ;
		if (j>=0) {
			continue ;
		}

		if (ch=="") {
			continue ;
		}

		nbl ++;
	}

	entries.close();

	return nbl ;
}
void parser::propertiesSet( vector<vesselProperties>& _vP, int n){

	vector<string> tableColumn = split(propertiesData[0],",");

	int nx_pos 			= findPosition_inTable(tableColumn,"<Nx>");
	int nl_pos 			= findPosition_inTable(tableColumn,"<Nl>");
	int l_pos				= findPosition_inTable(tableColumn,"<L>");
	int rho_pos			= findPosition_inTable(tableColumn,"<rho>");
	int mu_pos			= findPosition_inTable(tableColumn,"<mu>");

	int solver_pos			=findPosition_inTable(tableColumn,"<Solver>");
	int order_pos				=findPosition_inTable(tableColumn,"<Order>");
	int hr_pos					=findPosition_inTable(tableColumn,"<HR>");
	int profile_pos			=findPosition_inTable(tableColumn,"<Profile>");
	int initprofile_pos	=findPosition_inTable(tableColumn,"<Init_Profile>");

	vector<string> value;

	// Loop on arteries
	for ( int i=0;i<n; i++) {

		// Scalar properties of artery
  	value=split(propertiesData[i+1],",");

		_vP[i].set_nx( 			atoi((value[nx_pos].c_str())) 					);
		_vP[i].set_nl( 			atoi((value[nl_pos].c_str())) 					);

		_vP[i].set_l( 			strtold( value[l_pos].c_str(),	NULL)	);
		_vP[i].set_rho( 		strtold( value[rho_pos].c_str(),NULL) );
		_vP[i].set_mu( 			strtold( value[mu_pos].c_str(),	NULL) );

  	_vP[i].set_solver( 	value[solver_pos] );
  	_vP[i].set_order( 	atoi((value[order_pos].c_str())) );
		_vP[i].set_hr( 			value[hr_pos] );

		_vP[i].set_profile(	value[profile_pos] );
		_vP[i].set_initprofile(	value[initprofile_pos] );

		// Vector properties of artery
		int nx = _vP[i].get_nx() ;
		int nl = _vP[i].get_nl() ;
		VECT tmp(nx,0) , tmpl(nl,0);

		// dx
		if (dxData.get_numOfCols() != uint(nx + 1)) { Error("setProperties: numOfCols dx != nx + 1");}
		for ( int j=0; j < nx; j++) {
			tmp[j] = double(dxData(i,j+1));
		}
		_vP[i].set_dx(tmp) ;

		// dl
		if (dlData.get_numOfCols() != uint(nl + 1)) { Error("setProperties: numOfCols dl != nl + 1");}
		for ( int j=0; j < nl; j++) {
			tmpl[j] = double(dlData(i,j+1));
		}
		_vP[i].set_dl(tmpl) ;

		// a0
		if (a0Data.get_numOfCols() != uint(nx + 1)) { Error("setProperties: numOfCols a0 != nx + 1");}
		for ( int j=0; j < nx; j++) {
			tmp[j] = double(a0Data(i,j+1));
		}
		_vP[i].set_a0(tmp) ;

		// k
		if (kData.get_numOfCols() != uint(nx + 1)) { Error("setProperties: numOfCols k != nx + 1");}
		for ( int j=0; j < nx; j++) {
			tmp[j] = double(kData(i,j+1));
		}
		_vP[i].set_k(tmp) ;

		// cv
		if (cvData.get_numOfCols() != uint(nx + 1)) { Error("setProperties: numOfCols cv != nx + 1");}
		for ( int j=0; j < nx; j++) {
			tmp[j] = double(cvData(i,j+1));
		}
		_vP[i].set_cv(tmp) ;

		// knl
		if (knlData.get_numOfCols() != uint(nx + 1)) { Error("setProperties: numOfCols knl != nx + 1");}
		for ( int j=0; j < nx; j++) {
			tmp[j] = double(knlData(i,j+1));
		}
		_vP[i].set_knl(tmp) ;

		// inita
		if (initaData.get_numOfCols() != uint(nx + 1)) { Error("setProperties: numOfCols initaData != nx + 1");}
		for ( int j=0; j < nx; j++) {
			tmp[j] = double(initaData(i,j+1));
		}
		_vP[i].set_inita(tmp) ;

		// initq
		if (initqData.get_numOfCols() != uint(nx + 1)) { Error("setProperties: numOfCols initqData != nx + 1");}
		for ( int j=0; j < nx; j++) {
			tmp[j] = double(initqData(i,j+1));
		}
		_vP[i].set_initq(tmp) ;
	}
}
void parser::bcSet( vector<vesselProperties>& _vP, int n){

	vector<string> value ;
	string type ;
	int iart = 0, nt = 0;
	bc tmpbc ;

	value = split(inoutData[0],",");
	nt = value.size() -2 ;

	// Define size of data
	VECT data(nt,0) ;

	// Loop on boundary conditions
	for ( int i=0;i<n; i++) {

		value = split(inoutData[i+1],",");
		if (value.size() -2 != uint(nt)) { Error("parser::bcSet value.size() -2 != nt");}

		iart = atoi(value[0].c_str());
		type = value[1] ;

		for ( int j=0; j<nt; j++){
			data[j] = strtold( value[j+2].c_str(),NULL) ;
		}

		tmpbc = bc(type,data) ;
		_vP[iart].add_bc(tmpbc);

	}
}
void parser::tSet(time_c& timenet){

	vector<string> tableColumn = split(timeData[0],",");

	int ts_pos 						= findPosition_inTable(tableColumn,"<tS>");
	int te_pos						= findPosition_inTable(tableColumn,"<tE>");
	int dt_pos						= findPosition_inTable(tableColumn,"<t_step>");
	int nt_pos						= findPosition_inTable(tableColumn,"<Nt>");
	int nstore_pos				= findPosition_inTable(tableColumn,"<Nstore>");
	int nstoreprofile_pos	= findPosition_inTable(tableColumn,"<NstoreProfile>");
	int cfl_pos						= findPosition_inTable(tableColumn,"<CFL>");
	int order_pos					= findPosition_inTable(tableColumn,"<Order>");

	vector<string> value=split(timeData[1],",");

	timenet.set_ts( 						strtold( value[ts_pos].c_str(),							NULL)	);
	timenet.set_te( 						strtold( value[te_pos].c_str(),							NULL)	);
	timenet.set_dt( 						strtold( value[dt_pos].c_str(),							NULL)	);
	timenet.set_nt( 						strtold( value[nt_pos].c_str(),							NULL)	);
	timenet.set_nstore( 				strtold( value[nstore_pos].c_str(),					NULL) );
	timenet.set_nstoreprofile( 	strtold( value[nstoreprofile_pos].c_str(),	NULL) );
	timenet.set_cfl( 						strtold( value[cfl_pos].c_str(),						NULL) );
	timenet.set_dtcfl( 					strtold( value[dt_pos].c_str(),							NULL) );
	timenet.set_order( 					atoi((value[order_pos].c_str())) 									);

	// Verification
	vector<string> tstmp ;

	tstmp = split(inoutData[0],",");
	if( int(tstmp.size()-2) != timenet.get_nt() ) { Error("parser::tSet nt(tstmp.size()-2) != nt") ;}

	VECT tmp(timenet.get_nt(),0) ;
	for ( int j=0; j<timenet.get_nt(); j++){
		tmp[j] = strtold( tstmp[j+2].c_str(),NULL) ;
	}
	timenet.set_t(tmp) ;

}
void parser::outputSet(output& outnet){

	int nArt = -1;
	int nArttmp = 0 ;

	// Record position for scalar quantities
  for (uint i=0; i < outputData.get_numOfRows() ; i++) {

    outnet.add_arteryRecord( int(outputData(i,0)) );
    outnet.add_posRecord( int(outputData(i,1)) );

    // Store record Artery to open file
    if (nArt != nArttmp) {
    	nArt = nArttmp;
      outnet.add_storeArt( nArt ) ;
    }
	}

	// Record position for velocity profile
	for (uint i=0; i < outputProfileData.get_numOfRows() ; i++) {

    outnet.add_arteryProfileRecord( int(outputProfileData(i,0)) );
    outnet.add_posProfileRecord( int(outputProfileData(i,1)) );

	}

}
//####################################################
// Read
//####################################################
void parser::readtoMatrix(const char* file, MATR& data) {

  string ch;   // store temporarily read strings
	vector<string> str_;
	int j=0, nbl=0;
	uint num_Max=0;
	size_t found;

	// Open file
  ifstream entries(file,ios::in);
	if (!entries) {
		cerr << "parser::readtoMatrix: Impossible to open the " << file << " file\n" << endl;
		exit(1);
	}

	while (!entries.eof()) {
		getline (entries, ch);		// read a line

		found = ch.find("#") ;
		j = int(found) ;
		if (j>=0) {
			continue ;
		}

		if (ch=="") {
			continue ;
		}

		str_.push_back(ch);
    vector<string> chtemp=split(ch,",");
    if (num_Max < chtemp.size()) {
      num_Max = chtemp.size() ;
    }
		nbl ++ ;
	}
	entries.close();

  data = MATR (nbl,num_Max);
  for(int i=0; i< nbl; i++){
    vector<string> temp=split(str_[i],",");
    for (uint j=0; j< temp.size() ; j++) {
      data(i,j) = strtold(temp[j].c_str(),NULL);
    }
  }
}

void parser::readtoString(const char* file, string*& data) {

	int i=0, j=0, nbl=0;
	size_t found;
	string ch;

	// Open file
  ifstream entries(file,ios::in);
	if (!entries) {
		cerr << "parser::readtoString: Impossible to open the " << file << " file\n" << endl;
		exit(1);
	}

	// Get nbl
	while (!entries.eof()) {
		getline (entries, ch);
		if (ch=="") {
			continue ;
		}
		nbl ++;
	}

	// Clear and read again
	entries.clear();
	entries.seekg(0,ios::beg);

	// Create vector to store data
  data = new string[nbl];

	// Loop on lines of file
	while (!entries.eof()){
		getline (entries, ch);

		found = ch.find("#");
		j = int(found);
		if ( j>0){
				ch.erase (ch.begin()+j, ch.end());
		}

		if (ch=="") {
			continue ;
		}

		data[i] = ch;

		i++;
	}

	entries.close();
}
