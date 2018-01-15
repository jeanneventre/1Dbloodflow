#include "arteryNum.h"

arteryNum::arteryNum(const vesselProperties& vP, const time_c& timenet) :

  artery(vP,timenet),

  // Helpfull variables
  //###################
  Q(vP.get_initq()),
  Tw(nx,0), gradxP(nx,0),
  alpha(nx,0), phi(nx,0),
  // First and Second Order Variables
  //#################################
  A_l(nx,0), A_r(nx,0),
  K_l(nx,0), K_r(nx,0), Z_l(nx,0), Z_r(nx,0), H_l(nx,0), H_r(nx,0),
  HmZ_l(nx,0), HmZ_r(nx,0), A0_l(nx,0), A0_r(nx,0),
  Knl_l(nx,0), Knl_r(nx,0),Znl_l(nx,0), Znl_r(nx,0),
  // Reconstructed Variables
  //########################
  Kst(nx-1,0), Zst(nx-1,0), A0st(nx-1,0),
  Knlst(nx-1,0),Znlst(nx-1,0),
  Kc(nx,0),  Zc(nx,0),  A0c(nx,0),
  A_ll(nx,0), A_rr(nx,0),
  Ac_ll(nx,0), Ac_rr(nx,0),

  // Flux Variables
  //###############
  fluxA(nx+1,0),
  RHS1(nx,0), RHS1_Star(nx,0), RHS1_StarStar(nx,0),

  // TriDiagMatrix
  //##############
  Amatrix(nx), Bmatrix(nx),
  Afmatrix(nl),

  // Boundary conditions
  //####################
  Ainlet_r(1,0) , Aoutlet_l(1,0),
  Qinlet_r(nl,0), Qoutlet_l(nl,0),
  inData1(0)  , inData2(0),
  outData1(0) , outData2(0),
  nInBC(0)    , nOutBC(0)

  {
    // Velocity
    Ul    = MATR(nl,nx) ;
    Ulr   = MATR(nl,nx) ;

    // Up & down velocity
    Ul_u    = MATR(nl,nx) ;
    Ul_d    = MATR(nl,nx) ;
    // Radial mass transfer terms
    G1s2  = MATR(nl+1,nx) ;
    u1s2  = MATR(nl+1,nx) ;

    // Second order flux
    Ql_l  = MATR(nl,nx) ;
    Ql_r  = MATR(nl,nx) ;

    // Hydrostatic flux
    Ql_ll = MATR(nl,nx) ;
    Ql_rr = MATR(nl,nx) ;

    // Fluxes
    fluxAl = MATR(nl,nx+1);
    fluxQl = MATR(nl,nx+1);

    // Right hand side
    RHS2 = MATR(nl,nx)  ;
    RHS2_Star = MATR(nl,nx)  ;
    RHS2_StarStar = MATR(nl,nx)  ;

  }
//####################################################
// Initialization
//####################################################
void arteryNum::initialization(const time_c& timenet) {

  // Update data
  update_Data() ;
  // Set diffusion matrix for parabolic problem
  set_diffusionMatrix(timenet) ;
  // Reconstruction K
  reconstruct_K();
  // Reconstruct K for Hydrostatic reconstruction
  reconstruct_K_HR();

  // Set reconstructed variables used in BC
  A_ll[0] = A[0] ; A_rr[nx-1] = A[nx-1] ;
  for ( int j=0 ; j< nl ; j++) {
    Ql_ll(j,0)    = Ql(j,0);
    Ql_rr(j,nx-1) = Ql(j,nx-1);
  }
}
//####################################################
// Update
//####################################################
void arteryNum::update_Data() {
  update_Q() ;
  update_Ul() ;
  update_Ulr() ;
  update_gradxP() ;
  update_Tw() ;
  update_alpha() ;
  update_phi() ;
}
void arteryNum::update_Q() {
  for (int i=0 ; i < nx ; i++) {
    Q[i] = ZERO ;
    for (int j=0 ; j < nl ; j++) {
      Q[i] += Ql(j,i) ;
    }
  }
}
void arteryNum::update_gradxP() {
  SCALAR rp = ZERO , rm = ZERO ;
  rp = ONEsTWO * (dx[0] + dx[1]) ;
  gradxP[0] = ONE / rp * (pressure_elast(k[1],a0[1],A[1])-pressure_elast(k[0],a0[0],A[0]));
  for(int i=1 ; i < nx-1; i++) {
    rm = ONEsTWO * (dx[i] + dx[i-1]) ;
    rp = ONEsTWO * (dx[i] + dx[i+1]) ;
    gradxP[i] = ONE / ( pow(rm,TWO)*rp + pow(rp,TWO)*rm )
            * ( pow(rm,TWO)                * pressure_elast(k[i+1],a0[i+1],A[i+1])
              + ( pow(rp,TWO)-pow(rm,TWO) ) * pressure_elast(k[i],a0[i],A[i])
              - pow(rp,TWO)                * pressure_elast(k[i-1],a0[i-1],A[i-1])
              ) ;
  }
  rm = ONEsTWO * (dx[nx-2] + dx[nx-1]) ;
  gradxP[nx-1] = ONE / rm * (pressure_elast(k[nx-1],a0[nx-1],A[nx-1])-pressure_elast(k[nx-2],a0[nx-2],A[nx-2]));
}
void arteryNum::update_Tw() {
  // Compute the WSS knowing that U(R)=0, U(R+dR) = -U & U(R-dr)=U
  // which is consistent with the first order asymptotic development of u(R)
  for(int i = 0; i < nx ; i++) {
    SCALAR dr = ONEsTWO * dl[nl-1] * sqrt(A[i]/PI) ;
    SCALAR U1 = Ul(nl-1,i);
    Tw[i] = - mu * ( - U1 / dr ) ;
  }
}
void arteryNum::update_alpha() {
  // Compute the nonlinear correction coefficient (assumed=1 in each ring)
  for(int i = 0; i < nx ; i++) {
    alpha[i] = ZERO ;
    for( int j=0; j < nl; j++) {
      alpha[i] += PI * pow(Ul(j,i),TWO) * pow(sqrt(A[i]/PI) ,TWO) * ( pow(r[j] + ONEsTWO * dl[j] ,TWO) - pow(r[j] - ONEsTWO * dl[j] ,TWO) ) ;
    }

    if ( abs(Q[i]) > EPSILON) {
      alpha[i] = alpha[i] * A[i] / pow(Q[i],TWO) ;
    }
    else {
      alpha[i] = ONE ;
    }

  }
}
void arteryNum::update_phi() {
  // Compute the friction coefficinet 2 Pi nu phi Q/A = 2 Pi nu R du/dr
  for(int i = 0; i < nx ; i++) {
    if ( abs(Q[i]) > EPSILON) {
      phi[i] = ONE/mu * A[i]/Q[i] * sqrt(A[i]/PI) * Tw[i] ;
    }
    else {
      phi[i] = ZERO ;
    }
  }
}
void arteryNum::update_Ul() {
  for( int i = 0; i < nx ; i++) {
    for (int j=0 ; j <  nl ; j++) {
      if ( dla[j] * A[i] < EPSILON ) {
        Ul(j,i) = ZERO;
      }
      else {
        Ul(j,i) = Ql(j,i) / (dla[j] * A[i]) ;
      }
    }
  }
}
void arteryNum::update_Ulr() {
  SCALAR rm     = ZERO , rp     = ZERO ;
  SCALAR dxUl_u = ZERO , dxUl_d = ZERO ;
  SCALAR Ulr_d  = ZERO , Ulr_u  = ZERO ;

  // Compute Ul_u and Ul_d
  reconstruct_Ul();

  // Compute Ulr
  for(int i = 1; i < nx-1; i++) {
    rm = ONEsTWO * (dx[i] + dx[i-1]) ;
    rp = ONEsTWO * (dx[i] + dx[i+1]) ;
    dxUl_u = ONE / ( pow(rm,TWO)*rp + pow(rp,TWO)*rm )
                 * (pow(rm,TWO)               * Ul_u(0,i+1)
                 + (pow(rp,TWO)-pow(rm,TWO) ) * Ul_u(0,i)
                 -  pow(rp,TWO)               * Ul_u(0,i-1) ) ;
    Ulr_d = ZERO ;
    Ulr_u = ONE / (r[0] + ONEsTWO * dl[0]) * ( - sqrt(A[i]/PI) * ONEsTWO * ( r[0] + ONEsTWO * dl[0] ) * ( (r[0] + ONEsTWO * dl[0]) * dxUl_u ) );
    Ulr(0,i) = ONEsTWO * ( Ulr_d + Ulr_u ) ;

    for (int j=1 ; j < nl ; j++) {
      dxUl_u = ONE / ( pow(rm,TWO)*rp + pow(rp,TWO)*rm )
                * (pow(rm,TWO)               * Ul_u(j,i+1)
                + (pow(rp,TWO)-pow(rm,TWO))  * Ul_u(j,i)
                -  pow(rp,TWO)               * Ul_u(j,i-1)) ;
      dxUl_d = ONE / ( pow(rm,TWO)*rp + pow(rp,TWO)*rm )
                * (pow(rm,TWO)               * Ul_d(j,i+1)
                + (pow(rp,TWO)-pow(rm,TWO))  * Ul_d(j,i)
                -  pow(rp,TWO)               * Ul_d(j,i-1)
                ) ;
      Ulr_d = Ulr_u ;
      Ulr_u = ONE / (r[j] + ONEsTWO * dl[j]) *
                 (
                   (r[j-1] + ONEsTWO * dl[j-1]) * Ulr_d
                   - sqrt(A[i]/PI) * ONEsTWO * ( dl[j] ) * ( (r[j] + ONEsTWO * dl[j])*dxUl_u  + (r[j-1] + ONEsTWO * dl[j-1])*dxUl_d)
                 );
      Ulr(j,i) = ONEsTWO * ( Ulr_d + Ulr_u ) ;
    }
  }

  // For i=nx-1
  //####################
  rm = ONEsTWO * (dx[nx-1] + dx[nx-2]) ;
  dxUl_u = ONE / rm * (Ul_u(0,nx-1)-Ul_u(0,nx-2));
  Ulr_d = ZERO ;
  Ulr_u = ONE / (r[0] + ONEsTWO * dl[0]) *
             (
               - sqrt(A[nx-1]/PI) * ONEsTWO * (r[0] + ONEsTWO * dl[0]) * ( (r[0] + ONEsTWO * dl[0]) * dxUl_u )
             );
  Ulr(0,nx-1) = ONEsTWO * ( Ulr_d + Ulr_u ) ;

  for (int j=1 ; j < nl ; j++) {

    dxUl_u = ONE / rm * (Ul_u(j,nx-1)-Ul_u(j,nx-2)) ;
    dxUl_d = ONE / rm * (Ul_d(j,nx-1)-Ul_d(j,nx-2)) ;

    Ulr_d = Ulr_u ;
    Ulr_u = ONE / (r[j] + ONEsTWO * dl[j]) *
               (
                 (r[j-1] + ONEsTWO * dl[j-1]) * Ulr_d
                 - sqrt(A[nx-1]/PI) * ONEsTWO * ( dl[j] ) * ( (r[j] + ONEsTWO * dl[j])*dxUl_u  + (r[j-1] + ONEsTWO * dl[j-1])*dxUl_d)
               );

    Ulr(j,nx-1) = ONEsTWO * ( Ulr_d + Ulr_u ) ;
  }

  // For i=0
  //####################
  rp = ONEsTWO * (dx[1] + dx[0]) ;
  dxUl_u = 1. / rp * (Ul_u(0,1)-Ul_u(0,0));
  Ulr_d = ZERO ;
  Ulr_u = ONE / (r[0] + ONEsTWO * dl[0]) *
             (
               - sqrt(A[0]/PI) * ONEsTWO * (r[0] + ONEsTWO * dl[0]) * ( (r[0] + ONEsTWO * dl[0]) * dxUl_u )
             );
  Ulr(0,0) = ONEsTWO * ( Ulr_d + Ulr_u ) ;

  for (int j=1 ; j < nl ; j++) {

    dxUl_u = ONE / rm * (Ul_u(j,1)-Ul_u(j,0)) ;
    dxUl_d = ONE / rm * (Ul_d(j,1)-Ul_d(j,0)) ;

    Ulr_d = Ulr_u ;
    Ulr_u = ONE / (r[j] + ONEsTWO * dl[j]) *
               (
                 (r[j-1] + ONEsTWO * dl[j-1]) * Ulr_d
                 - sqrt(A[0]/PI) * ONEsTWO * ( dl[j] ) * ( (r[j] + ONEsTWO * dl[j])*dxUl_u  + (r[j-1] + ONEsTWO * dl[j-1])*dxUl_d)
               );

    Ulr(j,0) = ONEsTWO * ( Ulr_d + Ulr_u ) ;
  }
}
//####################################################
// Boundary condition
//####################################################
void arteryNum::stepBC(const time_c& timenet) {

  nInBC = 0, nOutBC = 0;
  inData1 = ZERO; inData2 = ZERO;
  outData1 = ZERO; outData2 = ZERO;

  for (uint ibc = 0 ; ibc < artbc.size() ; ibc++) {

    // Inlet
    if (artbc[ibc].get_type() == "inA" || artbc[ibc].get_type() == "inP" || artbc[ibc].get_type() == "inQ" || artbc[ibc].get_type() == "inU") {
      inBC(timenet,artbc[ibc]) ;
    }

    else if (artbc[ibc].get_type() == "inRt") {
      inBC(timenet,artbc[ibc]) ;
    }

    // Outlet
    else if (artbc[ibc].get_type() == "outA" || artbc[ibc].get_type() == "outP" || artbc[ibc].get_type() == "outQ" || artbc[ibc].get_type() == "outU") {
      outBC(timenet,artbc[ibc]) ;
    }

    else if (artbc[ibc].get_type() == "outRt") {
      outBC(timenet,artbc[ibc]) ;
    }

    else {
      Error("arteryNum::stepBC Unknown inlet or outlet boundary type");
    }
  }

  // printf("\nAinlet=%.14Lf, inData1=%.14Lf\n", Ainlet[0], inData1 );
  // printf("Qinlet=%.14Lf, inData2=%.14Lf\n", Qinlet[0], inData2 );
  // printf("Aoutlet=%.14Lf, outData1=%.14Lf\n", Aoutlet[0], outData1 );
  // printf("Qoutlet=%.14Lf, outData2=%.14Lf\n", Qoutlet[0], outData2 );

}
void arteryNum::inBC(const time_c& timenet, const bc inbc) {

  VECT AQ(1+nl,ZERO) ;
  VECT prop(9,ZERO), AQinit(1 + nl ,ZERO), AQc(1 + nl,ZERO), AQrec(1 + nl,ZERO), AQvar(1 + nl,ZERO);

  prop[0] = rho;
  prop[1] = K_l[0];
  prop[2] = k[0];
  prop[3] = a0[0];

  prop[4] = xorder;
  prop[5] = nl;
  prop[6] = dx[0];
  prop[7] = timenet.get_dt();

  prop[8] = deltaBL;

  AQinit[0]   = initA[0];
  AQc[0]      = A[0];
  AQrec[0]    = A_ll[0];
  AQvar[0]    = Ainlet[0];
  for ( int j=0 ; j < nl ; j++) {
    AQinit[1+j] = initQl(j,0);
    AQc[1+j]    = Ql(j,0);
    AQrec[1+j]  = Ql_ll(j,0);
    AQvar[1+j]  = Qinlet[j];
  }

  if (inbc.get_type() == "inA" || inbc.get_type() == "inP" || inbc.get_type() == "inAAbs" || inbc.get_type() == "inPAbs") {
    inData1 = inbc.get_data(timenet.get_n());
    nInBC ++;
  }
  else if (inbc.get_type() == "inRt" || inbc.get_type() == "inQ" || inbc.get_type() == "inU" || inbc.get_type() == "inUAbs") {
    inData2 = inbc.get_data(timenet.get_n());
    nInBC ++;
  }
  else {
    Error("arteryNum::inBC Unknown boundary type");
  }


  if (nInBC == 1) {

    if (inbc.get_type() == "inA") {
      AQ = inflow_A(prop, dla, AQc, AQvar, inData1);
    }
    if (inbc.get_type() == "inP") {
      AQ = inflow_P(prop, dla, AQc, AQvar, inData1);
    }
    if (inbc.get_type() == "inQ") {
      AQ = inflow_Q(prop, dla, r, AQc, AQrec, AQvar, profile, inData2);
    }
    if (inbc.get_type() == "inU") {
      AQ = inflow_U(prop, dla, r, AQc, AQrec, AQvar, profile, inData2);
    }

    if (inbc.get_type() == "inRt") {
      AQ = inflow_Rt(prop, dla, AQinit, AQc, AQvar, inData2);
    }

  }

  Ainlet[0] = AQ[0] ;
  for( int j=0 ; j < nl ; j++ ) {
    Qinlet[j] = AQ[1+j];
  }

}
void arteryNum::outBC(const time_c& timenet, const bc outbc) {

  VECT AQ(1+nl,ZERO) ;
  VECT prop(9,ZERO), AQinit(1 + nl ,ZERO), AQc(1 + nl,ZERO), AQrec(1 + nl,ZERO), AQvar(1 + nl,ZERO);

  prop[0] = rho;
  prop[1] = K_r[nx-1];
  prop[2] = k[nx-1];
  prop[3] = a0[nx-1];

  prop[4] = xorder;
  prop[5] = nl;
  prop[6] = dx[nx-1];
  prop[7] = timenet.get_dt();

  prop[8] = deltaBL;

  AQinit[0]   = initA[nx-1];
  AQc[0]      = A[nx-1];
  AQrec[0]    = A_rr[nx-1];
  AQvar[0]    = Aoutlet[0];
  for ( int j=0 ; j < nl ; j++) {
    AQinit[1+j] = initQl(j,nx-1);
    AQc[1+j]    = Ql(j,nx-1);
    AQrec[1+j]  = Ql_rr(j,nx-1);
    AQvar[1+j]  = Qoutlet[j];
  }

  if (outbc.get_type() == "outA" || outbc.get_type() == "outP" || outbc.get_type() == "outAAbs" || outbc.get_type() == "outPAbs") {
    outData1 = outbc.get_data(timenet.get_n());
    nOutBC ++;
  }
  else if (outbc.get_type() == "outRt" || outbc.get_type() == "outQ" || outbc.get_type() == "outU" || outbc.get_type() == "outUAbs") {
    outData2 = outbc.get_data(timenet.get_n());
    nOutBC ++;
  }
  else {
    Error("arteryNum::outBC Unknown boundary type");
  }

  if (nOutBC == 1) {

    if (outbc.get_type() == "outA") {
      AQ = outflow_A(prop, dla, AQc, AQvar, outData1);
    }
    if (outbc.get_type() == "outP") {
      AQ = outflow_P(prop, dla, AQc, AQvar, outData1);
    }
    if (outbc.get_type() == "outQ") {
      AQ = outflow_Q(prop, dla, AQc, r, AQrec, AQvar, profile, outData2);
    }
    if (outbc.get_type() == "outU") {
      AQ = outflow_U(prop, dla, AQc, r, AQrec, AQvar, profile, outData2);
    }

    if (outbc.get_type() == "outRt") {
      AQ = outflow_Rt(prop, dla, AQinit, AQc, AQvar, outData2);
    }

  }

  Aoutlet[0] = AQ[0] ;
  for( int j=0 ; j < nl ; j++ ) {
    Qoutlet[j] = AQ[1+j];
  }
}

//####################################################
// Reconstruction
//####################################################
void arteryNum::stepReconstruct() {

  switch(xorder) {
    case 1:
      // First Order reconstruction
      //############################
      reconstruct_1order();
      break;
    case 2:
      // Second Order reconstruction
      //############################
      reconstruct_2order();
      break;
    default:
      Error("arteryNum::stepReconstruct x order choosen not exist");
  }

  // Hydrostatic reconstruction
  //############################
  if (hr.compare("HRQ")==0) {
    reconstruct_Geometry_HR();
    reconstruct_HRQ();
  }
  else {
    Error("arteryNum::stepReconstruct HR choosen not exist");
  }
}
//####################################################
// Time Integration
//####################################################
void arteryNum::step(const time_c& timenet) {

  switch(timenet.get_order()) {
    case 1:
      Euler(timenet);
      break;
    case 2:
      if(timenet.get_n() == 0) {
        printf("\n Adam-Bashforth 2 scheme initialized with Runge Kutta 2 scheme \n");
        RungeKutta_2order(timenet);
      }
      else {
        AdamBashforth_2order(timenet);
      }
      break;
    case 3:
      if(timenet.get_n() == 0 || timenet.get_n() == 1) {
        printf("\n Adam-Bashforth 3 scheme initialized with Runge Kutta 3 scheme \n");
        RungeKutta_3order(timenet);
      }
      else {
        AdamBashforth_3order(timenet);
      }
      break;
        Error("arteryNum::step t order choosen not exist");
    default:
      Error("arteryNum::step t order choosen not exist");
  }

  // Viscous Subproblem
  stepFriction(timenet) ;
  // Parabolic subproblem
  update_Q() ;
  stepParabolic() ;
  // Update data
  update_Data() ;

}
//####################################################
// Time Integration: First Order
//####################################################
void arteryNum::Euler(const time_c& timenet) {

  // Store previous variables
  //############################
  Am1 = A;
  Qlm1 = Ql;
  // Evaluate flux
  //############################
  stepFlux(RHS1,RHS2);

  for(int i = 0; i < nx ; i++) {

    A[i] = A[i] + timenet.get_dt() * RHS1[i];

    for (int j=0; j < nl ; j++) {
      Ql(j,i) = Ql(j,i) + timenet.get_dt() * RHS2(j,i);

      if (Ql(j,i) != Ql(j,i)) {
        printf("Iteration n=%d\n", timenet.get_n());
        printf("Position i=%d, j=%d\n", i,j);
        printf("RHS1=%.14Lf, A=%.14Lf\n", RHS1[i], Ql(j,i));
        printf("RHS2=%.14Lf, Q=%.14Lf\n", RHS2(j,i), Ql(j,i));
        Error("Euler: Q is NaN");
      }
    }
    // Nan
    //#####
    if (A[i] != A[i]) {
      printf("Iteration n=%d\n", timenet.get_n());
      printf("Position i=%d\n", i);
      printf("RHS1=%.14Lf, A=%.14Lf\n", RHS1[i], A[i]);
      Error("Euler: A is NaN");
    }
  }
}
//####################################################
// Time Integration: Second Order
//####################################################
void arteryNum::AdamBashforth_2order(const time_c& timenet){

  // Store previous variables
  //############################
  Am1 = A;
  Qlm1 = Ql;
  // Store RHS of previous time step
  //############################
  RHS1_Star=RHS1;
  RHS2_Star=RHS2;
  // Evaluate flux
  //############################
  stepFlux(RHS1,RHS2);

  // Adam-Bashforth temporale discretization (2nd order)
  //############################
  for(int i=0; i < nx; i++){

    A[i] = A[i] + timenet.get_dt() * (THREEsTWO * RHS1[i] - ONEsTWO * RHS1_Star[i]);

    for (int j=0; j < nl ; j++) {
      Ql(j,i) = Ql(j,i) + timenet.get_dt() * (THREEsTWO * RHS2(j,i) - ONEsTWO * RHS2_Star(j,i));

      if (Ql(j,i) != Ql(j,i)) {
        printf("Iteration n=%d\n", timenet.get_n());
        printf("Position i=%d, j=%d\n", i,j);
        printf("RHS1=%.14Lf, A=%.14Lf\n", RHS1[i], Ql(j,i));
        printf("RHS2=%.14Lf, Q=%.14Lf\n", RHS2(j,i), Ql(j,i));
        Error("AdamBashforth_2order: Q is NaN");
      }
    }
    // Nan
    //#####
    if (A[i] != A[i]) {
      printf("Iteration n=%d\n", timenet.get_n());
      printf("Position i=%d\n", i);
      printf("RHS1=%.14Lf, A=%.14Lf\n", RHS1[i], A[i]);
      Error("AdamBashforth_2order: A is NaN");
    }
  }
}
//####################################################
// Time Integration: Third Order
//####################################################
void arteryNum::AdamBashforth_3order(const time_c& timenet){

  // Store previous variables
  //############################
  Am1 = A;
  Qlm1 = Ql;
  // Store RHS of previous time step
  //############################
  RHS1_StarStar=RHS1_Star;
  RHS2_StarStar=RHS2_Star;

  RHS1_Star=RHS1;
  RHS2_Star=RHS2;

  // Evaluate flux
  //############################
  stepFlux(RHS1,RHS2);

  // Adam-Bashforth temporale discretization (3nd order)
  //############################
  for(int i=0; i < nx ; i++){

    A[i] = A[i] + timenet.get_dt() * (23.L/12.L * RHS1[i] - 16.L/12.L * RHS1_Star[i] + 5.L/12.L * RHS1_StarStar[i]);

    for (int j=0; j < nl ; j++) {
      Ql(j,i) = Ql(j,i) + timenet.get_dt() * (23.L/12.L * RHS2(j,i) - 16.L/12.L * RHS2_Star(j,i) + 5.L/12.L * RHS2_StarStar(j,i));

      if (Ql(j,i) != Ql(j,i)) {
        printf("Iteration n=%d\n", timenet.get_n());
        printf("Position i=%d, j=%d\n", i,j);
        printf("RHS1=%.14Lf, A=%.14Lf\n", RHS1[i], Ql(j,i));
        printf("RHS2=%.14Lf, Q=%.14Lf\n", RHS2(j,i), Ql(j,i));
        Error("AdamBashforth_3order: Q is NaN");
      }
    }

    // Nan
    //#####
    if (A[i] != A[i]) {
      printf("Iteration n=%d\n", timenet.get_n());
      printf("Position i=%d\n", i);
      printf("RHS1=%.14Lf, A=%.14Lf\n", RHS1[i], A[i]);
      Error("AdamBashforth_3order: A is NaN");
    }
  }
}
//####################################################
// Time Integration: Second Order Runge Kutta
//####################################################
void arteryNum::RungeKutta_2order(const time_c& timenet){

  VECT RHS1_1(nx,0), RHS1_2(nx,0) ;
  MATR RHS2_1(nl,nx), RHS2_2(nl,nx) ;

  // Store previous variables
  //############################
  Am1 = A;
  Qlm1 = Ql;

  // First step
  //############################
  stepFlux(RHS1_1,RHS2_1);
  for(int i=0; i < nx;i++){
    A[i] = Am1[i] + TWOsTHREE * timenet.get_dt() * RHS1_1[i] ;
    for (int j=0; j < nl ; j++) {
      Ql(j,i) = Qlm1(j,i) + TWOsTHREE * timenet.get_dt() * RHS2_1(j,i) ;
    }
  }
  // Second step
  //############################
  stepFlux(RHS1_2,RHS2_2);

  // Time advance
  //############################
  for(int i=0; i < nx;i++){
    A[i] = Am1[i] + timenet.get_dt() * (ONEsFOUR * RHS1_1[i] + THREEsFOUR * RHS1_2[i]) ;
    for (int j=0; j < nl ; j++) {
      Ql(j,i) = Qlm1(j,i) + timenet.get_dt() * (ONEsFOUR * RHS2_1(j,i) + THREEsFOUR * RHS2_2(j,i)) ;

      if (Ql(j,i) != Ql(j,i)) {
        printf("Iteration n=%d\n", timenet.get_n());
        printf("Position i=%d, j=%d\n", i,j);
        printf("RHS1=%.14Lf, A=%.14Lf\n", RHS1[i], Ql(j,i));
        printf("RHS2=%.14Lf, Q=%.14Lf\n", RHS2(j,i), Ql(j,i));
        Error("RungeKutta_2order: Q is NaN");
      }
    }

    // Nan
    //#####
    if (A[i] != A[i]) {
      printf("Iteration n=%d\n", timenet.get_n());
      printf("Position i=%d\n", i);
      printf("RHS1=%.14Lf, A=%.14Lf\n", RHS1[i], A[i]);
      Error("RungeKutta_2order: A is NaN");
    }
  }

  RHS1 = RHS1_1;
  RHS2 = RHS2_1;
}
//####################################################
// Time Integration: Third Order Runge Kutta
//####################################################
void arteryNum::RungeKutta_3order(const time_c& timenet){

  // Store previous variables
  //############################
  Am1 = A;
  Qlm1 = Ql;
  RHS1_Star = RHS1;
  RHS2_Star = RHS2;

  VECT RHS1_1(nx,0), RHS1_2(nx,0), RHS1_3(nx,0) ;
  MATR RHS2_1(nl,nx), RHS2_2(nl,nx), RHS2_3(nl,nx) ;

  // First step
  //############################
  stepFlux(RHS1_1,RHS2_1);
  for(int i=0; i < nx; i++){
    A[i] = Am1[i] + ONEsTWO * timenet.get_dt() * RHS1_1[i] ;
    for (int j=0; j < nl ; j++) {
      Ql(j,i) = Qlm1(j,i) + ONEsTWO * timenet.get_dt() * RHS2_1(j,i) ;
    }
  }
  // Second step
  //############################
  stepFlux(RHS1_2,RHS2_2);
  for(int i=0; i < nx;i++){
    A[i] = Am1[i] + timenet.get_dt() * (- RHS1_1[i] + TWO * RHS1_2[i]) ;
    for (int j=0; j < nl ; j++) {
      Ql(j,i) = Qlm1(j,i) + timenet.get_dt() * (- RHS2_1(j,i) + TWO * RHS2_2(j,i)) ;
    }
  }
  // THIRD step
  //############################
  stepFlux(RHS1_3,RHS2_3);

  // Time advance
  //############################
  for(int i=0; i < nx;i++){
    A[i] = Am1[i] + timenet.get_dt() * (ONEsSIX * RHS1_1[i] + TWOsTHREE * RHS1_2[i] + ONEsSIX * RHS1_3[i]) ;
    for (int j=0; j < nl ; j++) {
      Ql(j,i) = Qlm1(j,i) + timenet.get_dt() * (ONEsSIX * RHS2_1(j,i) + TWOsTHREE * RHS2_2(j,i) + ONEsSIX * RHS2_3(j,i)) ;

      if (Ql(j,i) != Ql(j,i)) {
        printf("Iteration n=%d\n", timenet.get_n());
        printf("Position i=%d, j=%d\n", i,j);
        printf("RHS1=%.14Lf, A=%.14Lf\n", RHS1[i], Ql(j,i));
        printf("RHS2=%.14Lf, Q=%.14Lf\n", RHS2(j,i), Ql(j,i));
        Error("RungeKutta_3order: Q is NaN");
      }
    }

    // Nan
    //#####
    if (A[i] != A[i]) {
      printf("Iteration n=%d\n", timenet.get_n());
      printf("Position i=%d\n", i);
      printf("RHS1=%.14Lf, A=%.14Lf\n", RHS1[i], A[i]);
      Error("RungeKutta_3order: A is NaN");
    }
  }

  RHS1 = RHS1_1;
  RHS2 = RHS2_1;
}
//####################################################
// Viscoelastic and Inertial Subproblem
//####################################################
void arteryNum::set_diffusionMatrix(const time_c& timenet) {
  SCALAR  r;
  SCALAR  diagA;
  SCALAR  diagB;
  // Diagonal
  for(int i = 0; i < nx; i++) {
      r =  ONEsTWO * timenet.get_dt() * cv[i] / ( dx[i] * dx[i]);
      diagA =  ONE + TWO * r;
      diagB =  ONE - TWO * r;
      Amatrix.set_b_at(i,diagA);
      Bmatrix.set_b_at(i,diagB);
  }
  // Lower (a) and Upper (c) diagonal
  for(int i = 1; i < nx-1 ; i++) {
      r =  ONEsTWO * timenet.get_dt() * cv[i] / (dx[i] * dx[i]);
      Amatrix.set_a_at( i-1, -r);
      Bmatrix.set_a_at( i-1, r);
      Amatrix.set_c_at( i, -r);
      Bmatrix.set_c_at( i, r);
  }
  // Homogeneous Neumann B.C.
  r =  ONEsTWO * timenet.get_dt() * cv[0] / (dx[0] * dx[0]);
  Amatrix.set_c_at( 0, -  TWO * r);
  Bmatrix.set_c_at( 0,    TWO * r);
  r =  ONEsTWO * timenet.get_dt() * cv[nx-1] / (dx[nx-1] * dx[nx-1]);
  Amatrix.set_a_at( nx - 2, -  TWO * r);
  Bmatrix.set_a_at( nx - 2 ,   TWO * r);
}
void arteryNum::stepParabolic() {
  VECT Qm1(nx,0) ;
  Qm1 = Q;
  // If viscoelastic wall:
  if ( abs(cv[0]) > 0){
      Q = Amatrix.Thomas_solver( Bmatrix * Q );
      // Remove viscoelastic effects from first and last cells
      Q[0] = Qm1[0] ; Q[nx-1] = Qm1[nx-1] ;
      // Restore proportion of flow
      for( int i = 0; i < nx ; i++) {
        for ( int j=0 ; j <  nl ; j++) {
          Ql(j,i) = Ql(j,i) + dl[j] * (Q[i] - Qm1[i]) ;
        }
      }
  }
}
//####################################################
// Viscous Subproblem Treated in a Semi-Implicit Way
//####################################################
void arteryNum::set_frictionMatrix(const time_c& timenet, const int i ) {

  for(int j = 1; j < nl-1 ; j++) {
    Afmatrix.set_a_at( j-1,     - timenet.get_dt() *  dlj[j-1]           / ( dla[j-1] * A[i])  );
    Afmatrix.set_b_at( j  , ONE + timenet.get_dt() * (dlj[j-1] + dlj[j]) / ( dla[j]   * A[i])  );
    Afmatrix.set_c_at( j  ,     - timenet.get_dt() *  dlj[j]             / ( dla[j+1] * A[i])  );
  }
  // First layer j=0: r=0, du/dr=0
  Afmatrix.set_b_at( 0, ONE + timenet.get_dt() * dlj[0] / ( dla[0] * A[i])  );
  Afmatrix.set_c_at( 0,     - timenet.get_dt() * dlj[0] / ( dla[1] * A[i])  );
  // Last layer: Impose Q[nLayer] = 0
  Afmatrix.set_a_at( nl - 2,     - timenet.get_dt() * dlj[nl-2] / ( dla[nl-2] * A[i])  );
  Afmatrix.set_b_at( nl - 1, ONE + timenet.get_dt() * dlj[nl-2] / ( dla[nl-1] * A[i]) - timenet.get_dt() * dlj[nl-1] / A[i] );
}
void arteryNum::stepFriction(const time_c& timenet) {
  VECT Qm1(nl,ZERO) , Qp1(nl,ZERO) ;
  // If Viscous flow :
  if ( abs(mu) > ZERO ){
    for (int i=0 ; i < nx ; i++ ) {
      // Store previous flow rate in cell i
      for ( int j=0; j < nl; j++){
        Qm1[j] = Ql(j,i) ;
      }
      // Set friction matrix
      set_frictionMatrix(timenet, i);
      // Invert friction matrix in cell i
      Qp1 = Afmatrix.Thomas_solver( Qm1 );
      // Update flow rate in cell i
      for ( int j=0; j < nl; j++){
        Ql(j,i) = Qp1[j] ;
      }
    }
  }
}
//####################################################
// Evaluate flux
//####################################################
void arteryNum::stepFlux(VECT& RHS1, MATR& RHS2) {

  // Reconstruct variables (space and HR)
  //############################
  stepReconstruct();
  // Flux evaluation
  //############################
  if (solver.compare("KIN_HAT")==0) {
    fluxKinetic_Hat();
  }
  else {
    Error("arteryNum::stepFlux Flux choosen does not exist");
  }

  // Evaluate mass exchanges
  //############################
  G1s2_u1s2() ;

  // Evaluate new RHS
  //############################
  eval_RHS(RHS1,RHS2);
}
//####################################################
// First and Second Order Reconstruction
//####################################################
// First order reconstruction : We take the average value in the cell.
void arteryNum::reconstruct_1order() {

  for(int i =0; i < nx; i++) {
    //Flow variables
    for(int j=0; j < nl ; j++) {
      Ql_l(j,i) = Ql(j,i) ;
      Ql_r(j,i) = Ql(j,i) ;
    }

    //Geometric variables
    H_l[i]=k[i]*sqrt(A[i]);
    HmZ_l[i]=k[i]*(sqrt(A[i])-sqrt(a0[i]));

    H_r[i]=k[i]*sqrt(A[i]);
    HmZ_r[i]=k[i]*(sqrt(A[i])-sqrt(a0[i]));

    //Posttreated variables
    A_l[i] = A[i];
    A_r[i] = A[i];

    Z_l[i] = k[i]*sqrt(a0[i]);
    Z_r[i] = k[i]*sqrt(a0[i]);

    A0_l[i] = a0[i];
    A0_r[i] = a0[i];
  }
  // Reconstruct at boundaries
  Ainlet_r[0] = Ainlet[0]; Aoutlet_l[0] = Aoutlet[0];
  for(int j=0; j < nl ; j++) {
    Qinlet_r[j]  = Qinlet[j];
    Qoutlet_l[j] = Qoutlet[j];
  }
}
// Second order MUSCL reconstruction
void arteryNum::reconstruct_2order() {

  MATR dQl(nl,nx);
  VECT dH(nx,0);
  VECT dHmZ(nx,0);

  //forward difference
  SCALAR dQ_fw;
  SCALAR dH_fw;
  SCALAR dHmZ_fw;
  //backward difference
  SCALAR dQ_bw;
  SCALAR dH_bw;
  SCALAR dHmZ_bw;

  for ( int j=0 ; j < nl ; j++) {
    dQ_fw = Ql(j,1) - Ql(j,0);
    dQ_bw = Ql(j,0) - Qinlet[j];
    dQl(j,0) = minmod(dQ_fw,dQ_bw);
    dQ_fw = Qoutlet[j] - Ql(j,nx-1);
    dQ_bw = Ql(j,nx-1) - Ql(j,nx-2);
    dQl(j,nx-1) = minmod(dQ_fw,dQ_bw);
  }

  dH_fw = k[1]*sqrt(A[1]) - k[0]*sqrt(A[0]);
  dH_bw = k[0]*sqrt(A[0]) - k[0]*sqrt(Ainlet[0]);
  dH[0] = minmod(dH_fw,dH_bw);
  dH_fw = k[nx-1]*sqrt(Aoutlet[0]) - k[nx-1]*sqrt(A[nx-1]);
  dH_bw = k[nx-1]*sqrt(A[nx-1]) - k[nx-2]*sqrt(A[nx-2]);
  dH[nx-1] = minmod(dH_fw,dH_bw);

  dHmZ_fw = k[1]*( sqrt(A[1])-sqrt(a0[1]) ) - k[0]*( sqrt(A[0])-sqrt(a0[0]) );
  dHmZ_bw = k[0]*( sqrt(A[0])-sqrt(a0[0]) ) - k[0]*( sqrt(Ainlet[0])-sqrt(a0[0]) );
  dHmZ[0] = minmod(dHmZ_fw,dHmZ_bw);
  dHmZ_fw = k[nx-1]*( sqrt(Aoutlet[0])-sqrt(a0[nx-1]) ) - k[nx-1]*( sqrt(A[nx-1])-sqrt(a0[nx-1]) );
  dHmZ_bw = k[nx-1]*( sqrt(A[nx-1])-sqrt(a0[nx-1]) ) - k[nx-2]*( sqrt(A[nx-2])-sqrt(a0[nx-2]) );
  dHmZ[nx-1] = minmod(dHmZ_fw,dHmZ_bw);

  for (int i = 1; i < nx-1; i++) {

    for ( int j=0 ; j < nl ; j++) {
      dQ_fw = Ql(j,i+1) - Ql(j,i);
      dQ_bw = Ql(j,i)   - Ql(j,i-1);
      dQl(j,i) = minmod(dQ_fw,dQ_bw);
    }

    dH_fw = k[i+1]* sqrt(A[i+1]) - k[i]*  sqrt(A[i]);
    dH_bw = k[i]*   sqrt(A[i])   - k[i-1]*sqrt(A[i-1]);
    dH[i] = minmod(dH_fw,dH_bw);

    dHmZ_fw = k[i+1]*( sqrt(A[i+1])-sqrt(a0[i+1]) ) - k[i]*  ( sqrt(A[i])  -sqrt(a0[i]) );
    dHmZ_bw = k[i]*  ( sqrt(A[i])  -sqrt(a0[i]) )   - k[i-1]*( sqrt(A[i-1])-sqrt(a0[i-1]) );
    dHmZ[i] = minmod(dHmZ_fw,dHmZ_bw);
  }

  for(int i = 0; i < nx; i++) {

    for ( int j=0 ; j < nl ; j++) {
     Ql_l(j,i) = Ql(j,i) - ONEsTWO * dQl(j,i);
     Ql_r(j,i) = Ql(j,i) + ONEsTWO * dQl(j,i);
    }

   H_l[i] = k[i]*sqrt(A[i]) - ONEsTWO * dH[i];
   H_r[i] = k[i]*sqrt(A[i]) + ONEsTWO * dH[i];

   HmZ_l[i] = k[i]*( sqrt(A[i])-sqrt(a0[i]) ) - ONEsTWO * dHmZ[i];
   HmZ_r[i] = k[i]*( sqrt(A[i])-sqrt(a0[i]) ) + ONEsTWO * dHmZ[i];

   //Posttreated variables
   Z_l[i] = H_l[i] - HmZ_l[i];
   Z_r[i] = H_r[i] - HmZ_r[i];

   A_l[i] = pow(H_l[i]/K_l[i],TWO);
   A_r[i] = pow(H_r[i]/K_r[i],TWO);

   A0_l[i] = pow(Z_l[i]/K_l[i],TWO);
   A0_r[i] = pow(Z_r[i]/K_r[i],TWO);
  }
  // Reconstruction at boundaries
  Ainlet_r[0] = Ainlet[0] + ONEsTWO * (A[0] - Ainlet[0]);
  Aoutlet_l[0] = Aoutlet[0] - ONEsTWO * (Aoutlet[0] - A[nx-1]);

  for ( int j=0 ; j < nl ; j++) {
    Qinlet_r[j]  = Qinlet[j]  + ONEsTWO * (Ql(j,0) - Qinlet[j]);
    Qoutlet_l[j] = Qoutlet[j] - ONEsTWO * (Qoutlet[j] - Ql(j,nx-1));
  }
}
//####################################################
// Up & down reconstruction of Ul
//####################################################
void arteryNum::reconstruct_Ul() {

  MATR dUl(nl,nx);
  SCALAR dU_uw;
  SCALAR dU_dw;
  SCALAR R;
  SCALAR r,ru,rd;

  for (int i = 0; i < nx ; i++) {
    // Define radius of cell i
    R = sqrt( A[i] / PI) ;

    // j=0 (r=0)
    ru = ONEsTWO * (dl[0] + dl[1]) * R ;
    dUl(0,i)    = (Ul(1,i)    - Ul(0,i))     / ru;
    // j=nl-1 (r=R)
    rd = ONEsTWO * (dl[nl-1] + dl[nl-2]) * R ;
    dUl(nl-1,i) = (Ul(nl-1,i) - Ul(nl-2,i))  / rd;

    for (int j = 1; j < nl-1; j++) {
      ru = ONEsTWO * (dl[j] + dl[j+1]) * R ;
      rd = ONEsTWO * (dl[j] + dl[j-1]) * R ;
      dU_uw     = (Ul(j+1,i) - Ul(j,i))     / ru;
      dU_dw     = (Ul(j,i)   - Ul(j-1,i))   / rd;
      dUl(j,i)  = minmod(dU_uw,dU_dw);
    }
  }

  for(int i = 0; i < nx ; i++) {
    // Define radius of cell i
    R = sqrt( A[i] / PI) ;

    // j=0 (r=0)
    r = dl[0] * R ;
    Ul_u(0,i) = Ul(0,i) + ONEsTWO * r * dUl(0,i) ;
    Ul_d(0,i) = Ul(0,i) - ONEsTWO * r * dUl(0,i) ;

    // j=nl-1 (r=R)
    r = dl[nl-1] * R ;
    Ul_u(nl-1,i) = ZERO ; // No slip boundary condition
    Ul_d(nl-1,i) = Ul(nl-1,i) - ONEsTWO * r * dUl(nl-1,i) ;

    for (int j = 1; j < nl-1; j++) {
      r = dl[j] * R ;
      Ul_u(j,i) = Ul(j,i) + ONEsTWO * r * dUl(j,i) ;
      Ul_d(j,i) = Ul(j,i) - ONEsTWO * r * dUl(j,i) ;
    }
  }
}
 //####################################################
 // Reconstruction of geometry : High Order and Hydrostatic
 //####################################################
 // Second order MUSCL reconstruction
 void arteryNum::reconstruct_K() {

   VECT dK(nx,0);
   SCALAR dK_fw,dK_bw;
   VECT dKnl(nx,0);
   SCALAR dKnl_fw,dKnl_bw;
   VECT dZnl(nx,0);
   SCALAR dZnl_fw,dZnl_bw;

   switch(xorder) {
   case 1:
       for(int i = 0; i < nx; i++) {
         K_l[i]=k[i];
         K_r[i]=k[i];

         Knl_l[i]=knl[i];
         Knl_r[i]=knl[i];

         Znl_l[i]=knl[i] * sqrt(a0[i]);
         Znl_r[i]=knl[i] * sqrt(a0[i]);
       }
       break;
   case 2:
       dK[0]=k[1]-k[0];
       dK[nx-1]=k[nx-1]-k[nx-2];

       dKnl[0]=knl[1]-knl[0];
       dKnl[nx-1]=knl[nx-1]-knl[nx-2];

       dZnl[0]=knl[1]*sqrt(a0[1])-knl[0]*sqrt(a0[0]);
       dZnl[nx-1]=knl[nx-1]*sqrt(a0[nx-1])-knl[nx-2]*sqrt(a0[nx-2]);

       for (int i = 1; i < nx-1; i++) {
           dK_fw = k[i+1] - k[i];
           dK_bw = k[i] - k[i-1];
           dK[i] = minmod(dK_fw,dK_bw);

           dKnl_fw = knl[i+1] - knl[i];
           dKnl_bw = knl[i] - knl[i-1];
           dKnl[i] = minmod(dKnl_fw,dKnl_bw);

           dZnl_fw = knl[i+1]*sqrt(a0[i+1]) - knl[i]*sqrt(a0[i]);
           dZnl_bw = knl[i]*sqrt(a0[i]) - knl[i-1]*sqrt(a0[i-1]);
           dZnl[i] = minmod(dZnl_fw,dZnl_bw);
       }
       for(int i = 0; i < nx; i++) {
          K_l[i] = k[i] - ONEsTWO * dK[i];
          K_r[i] = k[i] + ONEsTWO * dK[i];

          Knl_l[i] = knl[i] - ONEsTWO * dKnl[i];
          Knl_r[i] = knl[i] + ONEsTWO * dKnl[i];

          Znl_l[i] = knl[i]*sqrt(a0[i]) - ONEsTWO * dZnl[i];
          Znl_r[i] = knl[i]*sqrt(a0[i]) + ONEsTWO * dZnl[i];
       }

       break;
   default:
       Error("arteryNum::reconstruct_K order choosen not exist");
   }
}
// Hydrostatic Reconstruction of K
void arteryNum::reconstruct_K_HR() {
   // Convention: Kst[i] is the value at the right interface of the cell i
   //Reconstruction of the geometry
   for (int i = 0; i < nx-1; i++) {
       Kst[i]   = max(K_r[i],K_l[i+1]);
       Knlst[i] = max(Knl_r[i],Knl_l[i+1]);
   }
   // Convention: Kc[i] is the value at the center of the cell i
   //Reconstruction of the geometry for the centered source term
   for (int i=0; i < nx; i++) {
       Kc[i] = sqrt( K_l[i]*K_r[i]);
   }
}
// Hydrostatic Reconstruction of Geometry
void arteryNum::reconstruct_Geometry_HR() {
   // Convention: Kst[i] is the value at the right interface of the cell i
   //Reconstruction of the geometry
   for (int i = 0; i < nx-1; i++) {
       Zst[i]   = min(Z_r[i],Z_l[i+1]);
       A0st[i]  = pow(Zst[i]/Kst[i],TWO);
       Znlst[i] = min(Znl_r[i],Znl_l[i+1]);
   }
   // Convention: Kc[i] is the value at the center of the cell i
   //Reconstruction of the geometry for the centered source term
   for (int i=0; i < nx; i++) {
       Zc[i] = ONEsTWO * ( Z_l[i] + Z_r[i]);
       A0c[i] = pow(Zc[i]/Kc[i],TWO);
   }
}
//####################################################
// Hydrostatic Reconstruction:
//####################################################
void arteryNum::reconstruct_HRQ() {
  // No reconstruction at the interfaces with ficticious boundary cells
  A_ll[0] = A_l[0] ;
  A_rr[nx-1] = A_r[nx-1] ;
  for ( int j=0; j < nl ; j++) {
    Ql_ll(j,0)    = Ql_l(j,0) ;
    Ql_rr(j,nx-1) = Ql_r(j,nx-1) ;
  }

  for (int i = 1; i < nx; i++) {
    //Reconstruction of the flux
    for ( int j=0; j < nl ; j++) {
      Ql_rr(j,i-1) = Ql_r(j,i-1) ;
      Ql_ll(j,i)   = Ql_l(j,i) ;
    }
    //Reconstruction of the section
    A_rr[i-1] = pow( max(ZERO, 1./Kst[i-1]*( Zst[i-1] + HmZ_r[i-1] ) ) , TWO) ;
    A_ll[i]   = pow( max(ZERO, 1./Kst[i-1]*( Zst[i-1] + HmZ_l[i]   ) ) , TWO) ;

    if (Zst[i-1] + HmZ_r[i-1] <= ZERO || Zst[i-1] + HmZ_l[i] <= ZERO) {
      printf("%Lf , %Lf \n", Zst[i-1] + HmZ_r[i-1] , Zst[i-1] + HmZ_l[i] );
      Error("arteryNum::reconstruct_HRQ HRQ: Limit of reconstruction reached -> Exit") ;
    }

    Ac_rr[i-1] = pow( max(ZERO, 1./Kc[i-1]*( Zc[i-1]  + HmZ_r[i-1] ) ) , TWO) ;
    Ac_ll[i-1] = pow( max(ZERO, 1./Kc[i-1]*( Zc[i-1]  + HmZ_l[i-1] ) ) , TWO) ;
   }

   Ac_rr[nx-1] = pow( max(ZERO, 1./Kc[nx-1]*( Zc[nx-1]  + HmZ_r[nx-1] ) ) , TWO) ;
   Ac_ll[nx-1] = pow( max(ZERO, 1./Kc[nx-1]*( Zc[nx-1]  + HmZ_l[nx-1] ) ) , TWO) ;
}
 //####################################################
 // Flux Evaluation
 //####################################################
void arteryNum::eval_RHS(VECT& RHS1, MATR& RHS2) {

  VECT RHS_HR(nx,ZERO);
  for(int i = 0 ; i < nx ; i++) {

    // Verify neglecting nonlinear term is valid
    if ( abs( k[i]*(sqrt(A[i])-sqrt(a0[i])) ) <= TEN * ( knl[i] * pow( sqrt(A[i])-sqrt(a0[i]), TWO ) ) &&  abs(sqrt(A[i])-sqrt(a0[i])) > EPSILON ) {
      printf("%Lf,\t %Lf\n", abs( k[i]*(sqrt(A[i])-sqrt(a0[i])) ), TEN * ( knl[i] * pow( sqrt(A[i])-sqrt(a0[i]), TWO ) ) );
      Error("arteryNum eval_RHS Value of nonlinear elastic term too high") ;
    }

    // Evaluate hydrostatic reconstruction RHS
    if (hr.compare("HRQ")==0) {
      eval_RHS_HR(i, RHS_HR[i]);
    }
    else {
      Error("arteryNum::eval_RHS Unknown hydrostatic reconstruction");
    }

    // Evaluate RHS1 & RHS2
    RHS1[i] = ZERO ;
    for (int j=0 ; j < nl ; j++) {
      RHS1[i]  += - ( fluxAl(j,i+1) - fluxAl(j,i) ) / dx[i] ;
      RHS2(j,i) = - ( fluxQl(j,i+1) - fluxQl(j,i) ) / dx[i]
                    + ( u1s2(j+1,i) * G1s2(j+1,i) - u1s2(j,i) * G1s2(j,i) )
                    + dla[j] * RHS_HR[i] ;
      }
  }
}
//####################################################
// Hydrostatic Reconstruction Additionnal Flux
//####################################################
void arteryNum::eval_RHS_HR(int i, SCALAR& RHS) {
    // For Q
    if (i == 0) {
      RHS = ONE/dx[i]*( fluxQP(rho,Kst[i],A_rr[i]) - fluxQP(rho,K_r[i],A_r[i]) );
    }
    else if (i == nx-1) {
      RHS = ONE/dx[i]*( fluxQP(rho,K_l[i],A_l[i]) - fluxQP(rho,Kst[i-1],A_ll[i]) );
    }
    else {
       RHS = ONE/dx[i]*(
                        fluxQP(rho,Kst[i],A_rr[i]) - fluxQP(rho,K_r[i],A_r[i])
                      + fluxQP(rho,K_l[i],A_l[i]) - fluxQP(rho,Kst[i-1],A_ll[i])
                        );
    }
    RHS +=
            // Centered flux for second order reconstruction
            - ONE/dx[i]*(
                        fluxQP(rho,Kc[i],Ac_rr[i]) - fluxQP(rho,K_r[i],A_r[i])
                      + fluxQP(rho,K_l[i],A_l[i]) - fluxQP(rho,Kc[i],Ac_ll[i])
                        ) ;
}
//####################################################
// Kinetic Flux
//####################################################
void arteryNum::fluxKinetic_Hat() {

  VECT F(4,ZERO) ;
  SCALAR Ur=ZERO , Ul=ZERO ;

  for(int i = 0; i < nx-1; i++) {
    for(int j = 0; j < nl ; j++) {

      if (A_rr[i] < EPSILON) {Ur = ZERO ;}
      else {Ur = Ql_rr(j,i) / dla[j] / A_rr[i] ;}
      if (A_ll[i+1] < EPSILON) {Ul = ZERO ;}
      else {Ul = Ql_ll(j,i+1) / dla[j] / A_ll[i+1] ;}

      F = flux_Hat_l(rho,Kst[i],Knlst[i],Znlst[i],dla[j],A_rr[i],A_ll[i+1],Ur,Ul) ;
      fluxAl(j,i+1) = F[0] + F[1] ;
      fluxQl(j,i+1) = F[2] + F[3] ;
    }
  }
  // Inlet
  //##########
  for(int j = 0; j < nl ; j++) {

    if (Ainlet_r[0] < EPSILON) {Ur = ZERO ;}
    else {Ur = Qinlet_r[j] / dla[j] / Ainlet_r[0] ;}
    if (A_ll[0] < EPSILON) {Ul = ZERO ;}
    else {Ul = Ql_ll(j,0) / dla[j] / A_ll[0] ;}

    F = flux_Hat_l(rho,K_l[0],Knl_l[0],Znl_l[0],dla[j],Ainlet_r[0],A_ll[0],Ur,Ul) ;
    fluxAl(j,0) = F[0] + F[1] ;
    fluxQl(j,0) = F[2] + F[3] ;
  }

  //Outlet
  //##########
  for(int j = 0; j < nl ; j++) {

    if (A_rr[nx-1] < EPSILON) {Ur = ZERO ;}
    else {Ur = Ql_rr(j,nx-1) / dla[j] / A_rr[nx-1] ;}
    if (Aoutlet_l[0] < EPSILON) {Ul = ZERO ;}
    else {Ul = Qoutlet_l[j] / dla[j] / Aoutlet_l[0] ;}

    F = flux_Hat_l(rho,K_r[nx-1],Knl_r[nx-1],Znl_r[nx-1],dla[j],A_rr[nx-1],Aoutlet_l[0],Ur,Ul) ;
    fluxAl(j,nx) = F[0] + F[1] ;
    fluxQl(j,nx) = F[2] + F[3] ;
  }

  // Compute num_fluxA
  //##################
  for(int i = 0; i <= nx ; i++) {
    fluxA[i] = ZERO ;
    for (int j=0 ; j < nl ; j++) {
      fluxA[i] += fluxAl(j,i) ;
    }
  }
}
//####################################################
// Mass exchanges
//####################################################
void arteryNum::G1s2_u1s2() {
  SCALAR dxG = ZERO, sumdla = ZERO, sumFAl = ZERO ;
  for ( int i=0 ; i < nx ; i++) {

    // Compute G1s2
    //####################
    G1s2(0,i) = ZERO ;

    sumFAl    = ZERO ;
    sumdla    = ZERO ;
    for ( int j=1; j <= nl ; j++) {
      sumdla += dla[j-1] ;
      sumFAl += fluxAl(j-1,i+1) - fluxAl(j-1,i) ;
      dxG     = sumFAl - sumdla * ( fluxA[i+1] - fluxA[i] ) ;
      G1s2(j,i) = dxG / dx[i] ;
    }

    // Check if G(nLayer)=0:
    if ( abs(G1s2(nl,i)) > EPSILON_G) {
      printf("G1s2=%.17Lf,\t dxG=%.17Lf,\t i=%d,\t dx=%.17Lf\n",G1s2(nl,i),dxG,i,dx[i]);
      Error("arteryNum::G1s2_u1s2 Error in the computation of G1s2: G1s2(nl,i) != 0") ;
    }

    // Compute u1s2
    //####################
    u1s2(0,i) = ZERO ; u1s2(nl,i) = ZERO ;
    for (int j=1 ; j < nl; j++) {
      if (G1s2(j,i) >= ZERO) {
         u1s2(j,i) = Ql(j,i) / (dla[j] * A[i]) ;
      }
      else {
         u1s2(j,i) = Ql(j-1,i) / (dla[j-1] * A[i]) ;
      }
    }

  }
}
//####################################################
//
//####################################################
