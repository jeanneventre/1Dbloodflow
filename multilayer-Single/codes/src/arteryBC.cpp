#include "arteryBC.h"

//####################################################
// HELP FUNCTIONS
//####################################################
VECT fun_inflow_Q(const VECT& AQ, const VECT& par){

  // Physical & numerical parameters
  SCALAR  rho    = par[0]      , k  = par[1];
  int     order  = int(par[2]) , nl = int(par[3]) ;
  // Layer proportion
  VECT    dla(nl,ZERO)  ; for (int j=0; j < nl ; j++) { dla[j] = par[3 + 1+j] ;}
  // Centered inner variable
  SCALAR  Ac = par[3 + 1*(nl+1)] ;
  VECT    Qc(nl,ZERO)   ; for (int j=0; j < nl ; j++) { Qc[j]  = par[3 + 1*(nl+1) + 1+j] ;}
  // Flow rate residu
  VECT    QmF(nl,ZERO)  ; for (int j=0; j < nl ; j++) { QmF[j] = par[3 + 2*(nl+1) +j] ;}
  // Outgoing Riemann invariant
  SCALAR  W = par[2 + 3*(nl+1)] ;

  // Quantities to be determined
  SCALAR  Avar = AQ[0];
  VECT    Qvar(nl,ZERO) ; for (int j=0; j < nl ; j++) { Qvar[j] = AQ[1+j] ;}

  // Reconstructed quantities:
  SCALAR  Arec = ZERO ;
  VECT    Qrec(nl,ZERO) ;
  if (order == 1) {
    Arec = Avar;
    Qrec = Qvar;
  }
  else if (order == 2) {
    Arec = Avar + ONEsTWO * (Ac - Avar) ;
    for (int j=0; j < nl ; j++) {
      Qrec[j] = Qvar[j] + ONEsTWO * (Qc[j] - Qvar[j]) ;
    }
  }
  else {
    printf("Order=%d\n", order );
    Error("arteryBC::fun_inflow_Q Unknown order");
  }

  // Compute sum of QmF and sum of Qvar
  SCALAR sQmF = ZERO , sQvar = ZERO ;
  for ( int j=0 ; j < nl ; j++) {
     sQmF   += QmF[j] ;
     sQvar  += Qvar[j] ;
  }

  // Residu
  VECT res(1+nl,ZERO);

  VECT F(4,ZERO) ;
  SCALAR FA = ZERO , FQ = ZERO ;
  SCALAR Urec = ZERO, Uc = ZERO;

  // Upwind decentering of the boundary condition:
  if (sQmF <= ZERO) {
    for ( int j=0 ; j<nl ; j++) {
      // Compute the speed
      if (Ac < EPSILON) {Uc = ZERO ;}
      else {Uc = Qc[j] / dla[j] / Ac ;}
      if (Arec < EPSILON) {Urec = ZERO ;}
      else {Urec = Qrec[j] / dla[j] / Arec ;}
      // Not necessary to reconstruct Uc as the flux is splitted
      F = flux_Hat_l(rho,k,ZERO,ZERO,dla[j],Arec,Ac,Urec,Uc) ;
      FA = F[0] ; FQ = F[2] ;
      res[j]  =   FQ;
      res[nl] +=  FA;
    }
  }
  else {
    for ( int j=0 ; j<nl ; j++) {
      // Compute the speed
      if (Ac < EPSILON) {Uc = ZERO ;}
      else {Uc = Qc[j] / dla[j] / Ac ;}
      if (Arec < EPSILON) {Urec = ZERO ;}
      else {Urec = Qrec[j] / dla[j] / Arec ;}
      // Not necessary to reconstruct Uc as the flux is splitted
      F = flux_Hat_l(rho,k,ZERO,ZERO,dla[j],Arec,Ac,Urec,Uc) ;
      FA = F[0];
      // FAp + Fam = Q at the interface
      res[j] = FA - QmF[j];
    }
    // Matching of the outgoing characteristic
    res[nl] = W2(rho,k,Avar,sQvar) - W ;
  }

  return res;
}
VECT fun_inflow_QA(const VECT& AQ, const VECT& par){

  // Physical & numerical parameters
  SCALAR  rho    = par[0]      , k  = par[1];
  int     order  = int(par[2]) , nl = int(par[3]) ;
  // Layer proportion
  VECT    dla(nl,ZERO)  ; for (int j=0; j < nl ; j++) { dla[j] = par[3 + 1+j] ;}
  // Centered inner variable
  SCALAR  Ac = par[3 + 1*(nl+1)] ;
  VECT    Qc(nl,ZERO)   ; for (int j=0; j < nl ; j++) { Qc[j]  = par[3 + 1*(nl+1) + 1+j] ;}
  // Flow rate residu
  VECT    QmF(nl,ZERO)  ; for (int j=0; j < nl ; j++) { QmF[j] = par[3 + 2*(nl+1) +j] ;}
  // Outgoing Riemann invariant
  SCALAR  A = par[2 + 3*(nl+1)] ;

  // Quantities to be determined
  SCALAR  Avar = AQ[0];
  VECT    Qvar(nl,ZERO) ; for (int j=0; j < nl ; j++) { Qvar[j] = AQ[1+j] ;}

  // Reconstructed quantities:
  SCALAR  Arec = ZERO ;
  VECT    Qrec(nl,ZERO) ;
  if (order == 1) {
    Arec = Avar;
    Qrec = Qvar;
  }
  else if (order == 2) {
    Arec = Avar + ONEsTWO * (Ac - Avar) ;
    for (int j=0; j < nl ; j++) {
      Qrec[j] = Qvar[j] + ONEsTWO * (Qc[j] - Qvar[j]) ;
    }
  }
  else {
    printf("Order=%d\n", order );
    Error("arteryBC::fun_inflow_Q Unknown order");
  }

  // Compute sum of QmF
  SCALAR sQmF = ZERO ; for ( int j=0 ; j < nl ; j++) { sQmF += QmF[j] ; }

  // Residu
  VECT res(1+nl,ZERO);

  VECT F(4,ZERO) ;
  SCALAR FA = ZERO, FQ = ZERO ;
  SCALAR Urec = ZERO, Uc = ZERO;

  // Upwind decentering of the boundary condition:
  if (sQmF <= ZERO) {
    for ( int j=0 ; j<nl ; j++) {
      // Compute the speed
      if (Ac < EPSILON) {Uc = ZERO ;}
      else {Uc = Qc[j] / dla[j] / Ac ;}
      if (Arec < EPSILON) {Urec = ZERO ;}
      else {Urec = Qrec[j] / dla[j] / Arec ;}
      // Not necessary to reconstruct Uc as the flux is splitted
      F = flux_Hat_l(rho,k,ZERO,ZERO,dla[j],Arec,Ac,Urec,Uc) ;
      FA = F[0]; FQ = F[2] ;
      res[j]  =   FQ ;
      res[nl] +=  FA ;
    }
  }
  else {
    for ( int j=0 ; j<nl ; j++) {
      // Compute the speed
      if (Ac < EPSILON) {Uc = ZERO ;}
      else {Uc = Qc[j] / dla[j] / Ac ;}
      if (Arec < EPSILON) {Urec = ZERO ;}
      else {Urec = Qrec[j] / dla[j] / Arec ;}
      // Not necessary to reconstruct Uc as the flux is splitted
      F = flux_Hat_l(rho,k,ZERO,ZERO,dla[j],Arec,Ac,Urec,Uc) ;
      FA = F[0];
      // FAp + Fam = Q at the interface
      res[j]  = FA - QmF[j];
    }
    // Set cross section
    res[nl]   = Avar - A ;
  }

  return res;
}
VECT fun_outflow_Q(const VECT& AQ, const VECT& par){

  // Physical & numerical parameters
  SCALAR  rho    = par[0]      , k  = par[1];
  int     order  = int(par[2]) , nl = int(par[3]) ;
  // Layer proportion
  VECT    dla(nl,ZERO)  ; for (int j=0; j < nl ; j++) { dla[j] = par[3 + 1+j] ;}
  // Centered inner variable
  SCALAR  Ac = par[3 + 1*(nl+1)] ;
  VECT    Qc(nl,ZERO)   ; for (int j=0; j < nl ; j++) { Qc[j]  = par[3 + 1*(nl+1) + 1+j] ;}
  // Flow rate residu
  VECT    QmF(nl,ZERO)  ; for (int j=0; j < nl ; j++) { QmF[j] = par[3 + 2*(nl+1) +j] ;}
  // Outgoing Riemann invariant
  SCALAR  W = par[2 + 3*(nl+1)] ;

  // Quantities to be determined
  SCALAR  Avar = AQ[0];
  VECT    Qvar(nl,ZERO) ; for (int j=0; j < nl ; j++) { Qvar[j] = AQ[1+j] ;}

  // Reconstructed quantities:
  SCALAR  Arec = ZERO ;
  VECT    Qrec(nl,ZERO) ;
  if (order == 1) {
    Arec = Avar;
    Qrec = Qvar;
  }
  else if (order == 2) {
    Arec = Avar - ONEsTWO * (Avar - Ac) ;
    for (int j=0; j < nl ; j++) {
      Qrec[j] = Qvar[j] - ONEsTWO * (Qvar[j] - Qc[j]) ;
    }
  }
  else {
    printf("Order=%d\n", order );
    Error("arteryBC::fun_inflow_Q Unknown order");
  }

  // Compute sum of QmF and sum of Qvar
  SCALAR sQmF = ZERO , sQvar = ZERO ;
  for ( int j=0 ; j < nl ; j++) {
     sQmF   += QmF[j] ;
     sQvar  += Qvar[j] ;
  }


  // Residu
  VECT res(1+nl,ZERO);

  VECT F(4,ZERO) ;
  SCALAR FA = ZERO , FQ = ZERO ;
  SCALAR Urec = ZERO, Uc = ZERO;

  // Upwind decentering of the boundary condition:
  if (sQmF >= ZERO) {
    for ( int j=0 ; j<nl ; j++) {
      // Compute the speed
      if (Ac < EPSILON) {Uc = ZERO ;}
      else {Uc = Qc[j] / dla[j] / Ac ;}
      if (Arec < EPSILON) {Urec = ZERO ;}
      else {Urec = Qrec[j] / dla[j] / Arec ;}
      // Not necessary to reconstruct Uc as the flux is splitted
      F = flux_Hat_l(rho,k,ZERO,ZERO,dla[j],Ac,Arec,Uc,Urec) ;
      FA = F[1]; FQ = F[3] ;
      res[j]  =   FQ;
      res[nl] +=  FA;
    }
  }
  else {
    for ( int j=0 ; j<nl ; j++) {
      // Compute the speed
      if (Ac < EPSILON) {Uc = ZERO ;}
      else {Uc = Qc[j] / dla[j] / Ac ;}
      if (Arec < EPSILON) {Urec = ZERO ;}
      else {Urec = Qrec[j] / dla[j] / Arec ;}
      // Not necessary to reconstruct Uc as the flux is splitted
      F = flux_Hat_l(rho,k,ZERO,ZERO,dla[j],Ac,Arec,Uc,Urec) ;
      FA = F[1];
      // FAp + Fam = Q at the interface
      res[j] = FA - QmF[j];
    }
    // Matching of the outgoing characteristic
    res[nl] = W1(rho,k,Avar,sQvar) - W ;
  }

  return res;
}
SCALAR interpolateW1(const VECT& prop, const VECT& AQc, const VECT& AQvar) {
  SCALAR rho    = prop[0] , k   = prop[1];
  int     nl    = int(prop[5]) ;
  SCALAR dx     = prop[6] , dt  = prop[7];

  SCALAR Avar   = AQvar[0], Ac  = AQc[0] ;
  SCALAR Qvar   = ZERO    ; for ( int j=0 ; j < nl ; j++) { Qvar += AQvar[1+j];}
  SCALAR Qc     = ZERO    ; for ( int j=0 ; j < nl ; j++) { Qc   += AQc[1+j];}

  return W1(rho,k,Avar,Qvar) - dt/dx * lambda1(rho,k,Avar,Qvar) * ( W1(rho,k,Avar,Qvar) - W1(rho,k,Ac,Qc) );
  // return W1(rho,k,Ac,Qc) ;
}
SCALAR interpolateW2(const VECT& prop, const VECT& AQc, const VECT& AQvar) {
  SCALAR rho    = prop[0] , k   = prop[1];
  int     nl    = int(prop[5]) ;
  SCALAR dx     = prop[6] , dt  = prop[7];

  SCALAR Avar   = AQvar[0], Ac  = AQc[0] ;
  SCALAR Qvar   = ZERO    ; for ( int j=0 ; j < nl ; j++) { Qvar += AQvar[1+j];}
  SCALAR Qc     = ZERO    ; for ( int j=0 ; j < nl ; j++) { Qc   += AQc[1+j];}

  return W2(rho,k,Avar,Qvar) - dt/dx * lambda2(rho,k,Avar,Qvar) * ( W2(rho,k,Ac,Qc) - W2(rho,k,Avar,Qvar) );
  // return W2(rho,k,Ac,Qc) ;
}
SCALAR interpolateW1_l(const VECT& prop, const VECT& dla, const VECT& AQc, const VECT& AQvar, const int j) {
  SCALAR rho    = prop[0] , k   = prop[1];
  SCALAR dx     = prop[6] , dt  = prop[7];

  SCALAR Avar   = AQvar[0]  , Ac  = AQc[0] ;
  SCALAR Qvar   = AQvar[1+j], Qc  = AQc[1+j] ;

  return W1l(rho,k,dla[j],Avar,Qvar) - dt/dx * lambda1l(rho,k,dla[j],Avar,Qvar) * ( W1l(rho,k,dla[j],Avar,Qvar) - W1l(rho,k,dla[j],Ac,Qc) );
  // return W1l(rho,k,dla[j],Ac,Qc) ;
}
SCALAR interpolateW2_l(const VECT& prop, const VECT& dla, const VECT& AQc, const VECT& AQvar, const int j) {
  SCALAR rho    = prop[0] , k   = prop[1];
  SCALAR dx     = prop[6] , dt  = prop[7];

  SCALAR Avar   = AQvar[0]  , Ac  = AQc[0] ;
  SCALAR Qvar   = AQvar[1+j], Qc  = AQc[1+j] ;

  return W2l(rho,k,dla[j],Avar,Qvar) - dt/dx * lambda2l(rho,k,dla[j],Avar,Qvar) * ( W2l(rho,k,dla[j],Ac,Qc) - W2l(rho,k,dla[j],Avar,Qvar) );
  // return W2l(rho,k,dla[j],Ac,Qc) ;
}
//####################################################
// INLET
//####################################################

//##################  Q  #######################
VECT inflow_Q(const VECT& prop, const VECT& dla, const VECT& r, const VECT& AQc, const VECT& AQrec, const VECT& AQvar, const string& profile, const SCALAR inQ){

  SCALAR rho    = prop[0]      , k  = prop[1] ;
  int    order  = int(prop[4]) , nl = int(prop[5]) ;
  SCALAR deltaBL = prop[8];

  VECT AQ(1+nl,ZERO);
  VECT guess(1+nl,ZERO), par(2 + 3*(nl+1) + 1,ZERO), F(4,ZERO) ;

  // Use previous values as initial guesses
  guess[0] = AQvar[0] ;
  for (int j=0; j < nl; j++) { guess[1+j] = AQvar[1+j] ; }

  // Parameters
  par[0] = rho ;
  par[1] = k ;
  par[2] = order ;
  par[3] = nl;
  // Layer proportion
  for (int j=0; j < nl; j++) { par[ 3 + 1+j] = dla[j] ; }
  // Centered inner variable
  par[3 + 1*(nl+1)] = AQc[0] ;
  for (int j=0; j < nl; j++) { par[3 + 1*(nl+1) + 1+j] = AQc[1+j] ; }

  SCALAR Urec = ZERO , Uvar = ZERO , FA = ZERO;
  for (int j=0; j < nl; j++) {

    if (AQrec[0] < EPSILON) {Urec = ZERO ;}
    else {Urec = AQrec[1+j] / dla[j] / AQrec[0] ;}
    if (AQvar[0] < EPSILON) {Uvar = ZERO ;}
    else {Uvar = AQvar[1+j] / dla[j] / AQvar[0] ;}

    // We do not reconstruct AQvar as it is not used to compute FA (split flux)
    F = flux_Hat_l(rho,k,ZERO,ZERO,dla[j],AQvar[0],AQrec[0],Uvar,Urec) ;
    FA = F[1];

    par[3 + 2*(nl+1)  + j] = inQ * dla[j] * Profile(profile, r[j], deltaBL) - FA ;
  }

  par[2 + 3*(nl+1) ] = interpolateW2(prop,AQc,AQvar) ;

  AQ = newtonRahpson(fun_inflow_Q, guess, par, int(maxIt), EPSILON);

  // Nan
  //#####
  if (AQ[0] != AQ[0]) {
    Error("inflow_Q: A is NaN");
  }

  // Verifiy the criticity of the flow
  //########################
  for (int j=0; j < nl; j++) {
    if (AQ[0] < EPSILON) {Uvar = ZERO ;}
    else {Uvar = AQ[1+j] / dla[j] / AQ[0] ;}
    if (abs(Uvar) >= cmk(rho,k,AQ[0])) {
      printf("U=%.14Lf, c=%.14Lf\n", Uvar, cmk(rho,k,AQ[0])  );
      Error("inflow_Q: Flow is supercritical at the inlet boundary");
    }
  }

  // Reconstruct A & Q
  SCALAR  Arec = ZERO ;
  VECT    Qrec(nl,ZERO) ;
  if (order == 1) {
    Arec = AQ[0];
    for (int j=0; j < nl; j++) {
      Qrec[j] = AQ[1+j];
    }
  }
  else if (order == 2) {
    Arec = AQ[0] + ONEsTWO * (AQc[0] - AQ[0]) ;
    for (int j=0; j < nl; j++) {
      Qrec[j] = AQ[1+j] + ONEsTWO * (AQc[1+j] - AQ[1+j]) ;
    }
  }
  else {
    printf("Order=%d\n", int(order) );
    Error("arteryBC::inflow_Q Unknown order");
  }

  // Get the flux
  //########################
  for (int j=0; j < nl; j++) {
    F = flux_Hat_l(rho,k,ZERO,ZERO,dla[j],Arec,AQrec[0],Qrec[j]/dla[j]/Arec,AQrec[j+1]/dla[j]/AQrec[0]) ;
    if ( abs( F[0] + F[1] - inQ * dla[j] * Profile(profile, r[j], deltaBL) ) >= EPSILON_BC) {
      printf("F[0]+F[1]=%.20Lf\t , inQ=%.20Lf \n", F[0] + F[1], inQ * dla[j] * Profile(profile, r[j], deltaBL));
      Error("inflow_Q: Error in the computation of inflow Q");
    }
  }

  return AQ;

}

//##################  U  #######################
VECT inflow_U(const VECT& prop, const VECT& dla, const VECT& r, const VECT& AQc, const VECT& AQrec, const VECT& AQvar, const string& profile, const SCALAR inU) {
  VECT AQ = inflow_Q( prop, dla, r, AQc, AQrec, AQvar, profile, inU * AQc[0] );
  return AQ;
}

//##################  QA  ######################
VECT inflow_QA(const VECT& prop, const VECT& dla,  const VECT& r, const VECT& AQc, const VECT& AQrec, const VECT& AQvar, const string& profile, const SCALAR inA, const SCALAR inQ) {

  SCALAR rho    = prop[0]      , k  = prop[1] ;
  int    order  = int(prop[4]) , nl = int(prop[5]) ;
  SCALAR deltaBL = prop[8];

  VECT AQ(1+nl,ZERO);
  VECT guess(1+nl,ZERO), par(2 + 3*(nl+1) + 1,ZERO), F(4,ZERO) ;

  // Use previous values as initial guesses
  guess[0] = AQvar[0] ;
  for (int j=0; j < nl; j++) { guess[1+j] = AQvar[1+j] ; }

  // Parameters
  par[0] = rho ;
  par[1] = k ;
  par[2] = order ;
  par[3] = nl;
  // Layer proportion
  for (int j=0; j < nl; j++) { par[ 3 + 1+j] = dla[j] ; }
  // Centered inner variable
  par[3 + 1*(nl+1)] = AQc[0] ;
  for (int j=0; j < nl; j++) { par[3 + 1*(nl+1) + 1+j] = AQc[1+j] ; }

  SCALAR Urec = ZERO , Uvar = ZERO , FA = ZERO;
  for (int j=0; j < nl; j++) {

    if (AQrec[0] < EPSILON) {Urec = ZERO ;}
    else {Urec = AQrec[1+j] / dla[j] / AQrec[0] ;}
    if (AQvar[0] < EPSILON) {Uvar = ZERO ;}
    else {Uvar = AQvar[1+j] / dla[j] / AQvar[0] ;}

    // We do not reconstruct AQvar as it is not used to compute FA (split flux)
    F = flux_Hat_l(rho,k,ZERO,ZERO,dla[j],AQvar[0],AQrec[0],Uvar,Urec) ;
    FA = F[1];

    par[3 + 2*(nl+1)  + j] = inQ * dla[j] * Profile(profile, r[j], deltaBL) - FA ;
  }
  par[2 + 3*(nl+1) ] = inA ;

  AQ = newtonRahpson(fun_inflow_QA, guess, par, int(maxIt), EPSILON);

  // Nan
  //#####
  if (AQ[0] != AQ[0]) {
    printf("Ac=%.14Lf, Arec=%.14Lf, Aoutlet=%.14Lf\n", AQc[0], AQrec[0], AQ[0] );
    Error("inflow_QA: A is NaN");
  }

  // Verifiy the criticity of the flow
  //########################
  for (int j=0; j < nl; j++) {
    if (AQ[0] < EPSILON) {Uvar = ZERO ;}
    else {Uvar = AQ[1+j] / dla[j] / AQ[0] ;}
    if (abs(Uvar) <= cmk(rho,k,AQ[0])) {
      printf("U=%.14Lf, c=%.14Lf\n", Uvar, cmk(rho,k,AQ[0])  );
      Error("inflow_QA: Flow is subcritical at the inlet boundary");
    }
  }

  // Reconstruct A & Q
  SCALAR  Arec = ZERO ;
  VECT    Qrec(nl,ZERO) ;
  if (int(order) == 1) {
    Arec = AQ[0];
    for (int j=0; j < nl; j++) {
      Qrec[j] = AQ[1+j];
    }
  }
  else if (int(order) == 2) {
    Arec = AQ[0] + ONEsTWO * (AQc[0] - AQ[0]) ;
    for (int j=0; j < nl; j++) {
      Qrec[j] = AQ[1+j] + ONEsTWO * (AQc[1+j] - AQ[1+j]) ;
    }
  }
  else {
    printf("Order=%d\n", int(order) );
    Error("arteryBC::inflow_QA Unknown order");
  }

  // Get the flux
  //########################
  for (int j=0; j < nl; j++) {
    F = flux_Hat_l(rho,k,ZERO,ZERO,dla[j],Arec,AQrec[0],Qrec[j]/dla[j]/Arec,AQrec[j+1]/dla[j]/AQrec[0]) ;
    if ( abs( F[0] + F[1] - inQ * dla[j] * Profile(profile, r[j], deltaBL) ) >= EPSILON_BC) {
      printf("F[0]+F[1]=%.20Lf\t , inQ=%.20Lf \n", F[0] + F[1], inQ * dla[j] * Profile(profile, r[j], deltaBL));
      Error("inflow_QA: Error in the computation of inflow Q");
    }
  }

  return AQ;
}

//##################  UA  ######################
VECT inflow_UA(const VECT& prop, const VECT& dla, const VECT& r, const VECT& AQc, const VECT& AQrec, const VECT& AQvar, const string& profile, const SCALAR inA, const SCALAR inU){
  VECT AQ = inflow_QA( prop, dla, r, AQc, AQrec, AQvar, profile, inA, inU * inA );
  return AQ;
}

//##################  A  #######################
VECT inflow_A(const VECT& prop, const VECT& dla, const VECT& AQc, const VECT& AQvar, const SCALAR inA) {
  // Suppose no mass exchanges at the inlet
  // Profile is reconstructed in each layer over time
  SCALAR  rho = prop[0] , k = prop[1] ;
  int     nl  = prop[5] ;

  VECT AQ(nl+1,ZERO) ;
  SCALAR W1n = ZERO,  W2n = ZERO ;

  AQ[0] = inA ;

  for (int j=0 ; j < nl ; j++) {
    W2n = interpolateW2_l(prop,dla,AQc,AQvar,j);
    W1n = W2n + EIGHT * cmk(rho,k,inA) ;
    AQ[1+j] = dla[j] * AQ[0] * ONEsTWO * ( W1n + W2n ) ;
  }

  // Nan
  //#####
  if (AQ[0] != AQ[0]) {
    printf("inA=%.14Lf, Ac=%.14Lf, Ainlet=%.14Lf\n", inA, AQc[0], AQ[0] );
    Error("inflow_A: A is NaN");
  }

  // Verifiy the criticity of the flow
  //########################
  SCALAR Uvar = ZERO ;
  for (int j=0; j < nl; j++) {
    if (AQ[0] < EPSILON) {Uvar = ZERO ;}
    else {Uvar = AQ[1+j] / dla[j] / AQ[0] ;}
    if (abs(Uvar) >= cmk(rho,k,AQ[0])) {
      printf("U=%.14Lf, c=%.14Lf\n", Uvar, cmk(rho,k,AQ[0])  );
      Error("inflow_A: Flow is supercritical at the inlet boundary");
    }
  }

  return AQ;

}

//##################  P  #######################
VECT inflow_P(const VECT& prop, const VECT& dla, const VECT& AQc, const VECT& AQvar, const SCALAR inP) {
  SCALAR k = prop[2], a0 = prop[3] ;
  SCALAR inA = pow( inP/k + sqrt(a0) , TWO);
  VECT AQ = inflow_A(prop, dla, AQc, AQvar, inA) ;
  return AQ;
}

//##################  Rt #######################
VECT inflow_Rt(const VECT& prop, const VECT& dla, const VECT& AQinit, const VECT& AQc, const VECT& AQvar, const SCALAR Rt) {

  SCALAR rho = prop[0], k = prop[1];
  int nl = int(prop[5]) ;

  SCALAR Qinit = ZERO ;  for ( int j=0; j < nl ; j++) {Qinit += AQinit[1+j] ;}
  SCALAR W2n  = interpolateW2(prop,AQc,AQvar) ;
  SCALAR W10  = W1(rho,k,AQinit[0],Qinit);
  SCALAR W20  = W2(rho,k,AQinit[0],Qinit);
  SCALAR W1n  = W10 - Rt * (W2n - W20);

  SCALAR inA = pow( rho/( 32.0L * k) , TWO ) * pow( W1n - W2n, FOUR );

  VECT AQ = inflow_A(prop, dla, AQc, AQvar, inA) ;

  return AQ;
}

//####################################################
// OUTLET
//####################################################

//##################  Q  #######################
VECT outflow_Q(const VECT& prop, const VECT& dla, const VECT& r, const VECT& AQc, const VECT& AQrec, const VECT& AQvar, const string& profile, const SCALAR outQ){

  SCALAR rho    = prop[0]      , k  = prop[1] ;
  int    order  = int(prop[4]) , nl = int(prop[5]) ;
  SCALAR deltaBL = prop[8];

  VECT AQ(1+nl,ZERO);
  VECT guess(1+nl,ZERO), par(2 + 3*(nl+1) + 1,ZERO), F(4,ZERO) ;

  // Use previous values as initial guesses
  guess[0] = AQvar[0] ;
  for (int j=0; j < nl; j++) { guess[1+j] = AQvar[1+j] ; }

  // Parameters
  par[0] = rho ;
  par[1] = k ;
  par[2] = order ;
  par[3] = nl;
  // Layer proportion
  for (int j=0; j < nl; j++) { par[ 3 + 1+j] = dla[j] ; }
  // Centered inner variable
  par[3 + 1*(nl+1)] = AQc[0] ;
  for (int j=0; j < nl; j++) { par[3 + 1*(nl+1) + 1+j] = AQc[1+j] ; }

  SCALAR Urec = ZERO , Uvar = ZERO , FA = ZERO;
  for (int j=0; j < nl; j++) {

    if (AQrec[0] < EPSILON) {Urec = ZERO ;}
    else {Urec = AQrec[1+j] / dla[j] / AQrec[0] ;}
    if (AQvar[0] < EPSILON) {Uvar = ZERO ;}
    else {Uvar = AQvar[1+j] / dla[j] / AQvar[0] ;}

    // We do not reconstruct AQvar as it is not used to compute FA (split flux)
    F = flux_Hat_l(rho,k,ZERO,ZERO,dla[j],AQrec[0],AQvar[0],Urec,Uvar) ;
    FA = F[0];

    par[3 + 2*(nl+1)  + j] = outQ * dla[j] * Profile(profile, r[j], deltaBL) - FA ;
  }

  par[2 + 3*(nl+1) ] = interpolateW1(prop,AQc,AQvar) ;

  AQ = newtonRahpson(fun_outflow_Q, guess, par, int(maxIt), EPSILON);

  // Nan
  //#####
  if (AQ[0] != AQ[0]) {
    printf("Ac=%.14Lf, Arec=%.14Lf, Aoutlet=%.14Lf\n", AQc[0], AQrec[0], AQ[0] );
    Error("outflow_Q: A is NaN");
  }

  // Verifiy the criticity of the flow
  //########################
  for (int j=0; j < nl; j++) {
    if (AQ[0] < EPSILON) {Uvar = ZERO ;}
    else {Uvar = AQ[1+j] / dla[j] / AQ[0] ;}
    if (abs(Uvar) >= cmk(rho,k,AQ[0])) {
      printf("U=%.14Lf, c=%.14Lf\n", Uvar, cmk(rho,k,AQ[0])  );
      Error("outflow_Q: Flow is supercritical at the inlet boundary");
    }
  }

  // Reconstruct A & Q
  SCALAR  Arec = ZERO ;
  VECT    Qrec(nl,ZERO) ;
  if (int(order) == 1) {
    Arec = AQ[0];
    for (int j=0; j < nl; j++) {
      Qrec[j] = AQ[1+j];
    }
  }
  else if (int(order) == 2) {
    Arec = AQ[0] - ONEsTWO * (AQ[0] - AQc[0]) ;
    for (int j=0; j < nl; j++) {
      Qrec[j] = AQ[1+j] - ONEsTWO * (AQ[1+j] - AQc[1+j]) ;
    }
  }
  else {
    printf("Order=%d\n", int(order) );
    Error("arteryBC::outflow_Q Unknown order");
  }

  // Get the flux
  //########################
  for (int j=0; j < nl; j++) {
    F = flux_Hat_l(rho,k,ZERO,ZERO,dla[j],AQrec[0],Arec,AQrec[j+1]/dla[j]/AQrec[0],Qrec[j]/dla[j]/Arec) ;
    if ( abs( F[0] + F[1] - outQ * dla[j] * Profile(profile, r[j], deltaBL) ) >= EPSILON_BC) {
      printf("F[0]+F[1]=%.20Lf\t , outQ=%.20Lf \n", F[0] + F[1], outQ * dla[j] * Profile(profile, r[j], deltaBL) );
      Error("outflow_Q: Error in the computation of outflow Q");
    }
  }

  return AQ;
}

//##################  U  #######################
VECT outflow_U(const VECT& prop, const VECT& dla, const VECT& r, const VECT& AQc, const VECT& AQrec, const VECT& AQvar, const string& profile, const SCALAR outU) {
  VECT AQ = outflow_Q( prop, dla, r, AQc, AQrec, AQvar, profile, outU * AQc[0] );
  return AQ;
}

//##################  A  #######################
VECT outflow_A(const VECT& prop, const VECT& dla, const VECT& AQc, const VECT& AQvar, const SCALAR outA) {

  SCALAR rho = prop[0], k = prop[1] ;
  int nl = int(prop[5]) ;

  VECT AQ(nl+1,ZERO) ;
  SCALAR W2n = ZERO,  W1n = ZERO ;

  AQ[0] = outA ;

  for (int j=0 ; j < nl ; j++) {
    W1n = interpolateW1_l(prop,dla,AQc,AQvar,j);
    W2n = W1n - EIGHT * cmk(rho,k,outA) ;
    AQ[1+j] = dla[j] * AQ[0] * ONEsTWO * ( W1n + W2n ) ;
  }

  // Verifiy the criticity of the flow
  //########################
  SCALAR Uvar = ZERO ;
  for (int j=0; j < nl; j++) {
    if (AQ[0] < EPSILON) {Uvar = ZERO ;}
    else {Uvar = AQ[1+j] / dla[j] / AQ[0] ;}
    if (abs(Uvar) >= cmk(rho,k,AQ[0])) {
      printf("U=%.14Lf, c=%.14Lf\n", Uvar, cmk(rho,k,AQ[0])  );
      Error("outflow_A: Flow is supercritical at the outlet boundary");
    }
  }

  // Nan
  //#####
  if (AQ[0] != AQ[0]) {
    printf("outA=%.14Lf, Ac=%.14Lf, Aoutlet=%.14Lf\n", outA, AQc[0], AQ[0] );
    Error("outflow_A: A is NaN");
  }

  return AQ;
}

//##################  P  #######################
VECT outflow_P(const VECT& prop, const VECT& dla, const VECT& AQc, const VECT& AQvar, const SCALAR outP) {
  SCALAR k = prop[2], a0 = prop[3] ;
  SCALAR outA = pow( outP/k + sqrt(a0) , TWO);
  VECT AQ = outflow_A(prop, dla, AQc, AQvar, outA) ;
  return AQ;
}

//##################  Rt #######################
VECT outflow_Rt(const VECT& prop, const VECT& dla, const VECT& AQinit, const VECT& AQc, const VECT& AQvar, const SCALAR Rt) {

  SCALAR rho = prop[0], k = prop[1];
  int nl = int(prop[5]) ;

  SCALAR Qinit = ZERO ;  for ( int j=0; j < nl ; j++) {Qinit += AQinit[1+j] ;}
  SCALAR W1n  = interpolateW1(prop,AQc,AQvar) ;
  SCALAR W10  = W1(rho,k,AQinit[0],Qinit);
  SCALAR W20  = W2(rho,k,AQinit[0],Qinit);
  SCALAR W2n  = W20 - Rt * (W1n - W10);

  SCALAR outA = pow( rho/( 32.0L * k) , TWO ) * pow( W1n - W2n, FOUR );

  VECT AQ = outflow_A(prop, dla, AQc, AQvar, outA) ;

  return AQ;

}
