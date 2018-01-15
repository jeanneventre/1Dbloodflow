#include "artery.h"

artery::artery(const vesselProperties& vP, const time_c& timenet) :

  // Numerics
  //#########
  solver(vP.get_solver()), xorder(vP.get_order()), hr(vP.get_hr()),
  profile(vP.get_profile()), initprofile(vP.get_initprofile()),
  nx(vP.get_nx()), nl(vP.get_nl()),
  x(nx,0), dx(vP.get_dx()), r(nl,0), dl(vP.get_dl()), dla(nl,0), dlj(nl,0),
  dt(timenet.get_dt()),

  // Physics
  //#########
  rho(vP.get_rho()), mu(vP.get_mu()), k(vP.get_k()), cv(vP.get_cv()), knl(vP.get_knl()),

  // Geometry
  //#########
  l(vP.get_l()), a0(vP.get_a0()),

  // Boundary conditions
  //####################
  artbc(vP.get_artbc()),

  // Variables
  //##########
  A(vP.get_inita()), Am1(vP.get_inita()), initA(vP.get_inita()),
  initQ(vP.get_initq()),
  Ainlet(1,0), Aoutlet(1,0), Qinlet(nl,0), Qoutlet(nl,0)

  {
    // Define x
    set_x();
    // Define smallest space step for CFL condition
    set_dxmin();
    // Define dimensionless radius
    set_r();
    // Define layer area proportion
    set_dla();
    // Define dlj, used in viscous subproblem
    set_dlj();

    // Define thickness of boundary layer for Polhausen profile
    deltaBL = dl[nl-1] + dl[nl-2] ;

    // Define matrix variables
    initQl  = MATR(nl,nx);
    // Set initQl
    set_initQl();
    // Define Ql & Qlm1
    Ql = initQl;
    Qlm1 = Ql;

    // Define inlet & outlet
    Ainlet[0] = A[0] ;
    Aoutlet[0] = A[nx-1] ;
    for ( int j=0 ; j < nl ; j++) {
      Qinlet[j]   = Ql(j,0) ;
      Qoutlet[j]  = Ql(j,nx-1) ;
    }

  }
//####################################################
// Verbose
//####################################################
void artery::verbose(const time_c& timenet) {

  if (timenet.get_n() == 0) {
    printf("\n#########################################\n") ;
    if (mu!= 0.) {
      printf("Viscosity                   : ON \n");
    }
    else {
      printf("Viscosity                   : OFF \n");
    }
    if (cv[0] != 0.) {
      printf("Viscoelasticity             : ON \n");
    }
    else {
      printf("Viscoelasticity             : OFF \n");
    }
    if (knl[0] != 0.) {
      printf("Nonlinear elasticity        : ON \n");
    }
    else {
      printf("Nonlinear elasticity        : OFF \n");
    }

    if (solver.compare("KIN_HAT")==0) {
      printf("Numerical Flux              : Kinetic Hat \n");
    }

      printf("Space Order                 : %d \n", xorder);

    if (hr.compare("HRQ")==0) {
      printf("Hydrostatic Reconstruction  : HRQ \n");
    }

    if (initprofile.compare("Flat")==0) {
      printf("Initial velocity profile    : Flat \n");
    }
    else if (initprofile.compare("Poiseuille")==0) {
      printf("Initial velocity profile    : Poiseuille \n");
    }
    else if (initprofile.compare("Polhausen")==0) {
      printf("Initial velocity profile    : Polhausen \n");
    }

    if (profile.compare("Flat")==0) {
      printf("Velocity profile            : Flat \n");
    }
    else if (profile.compare("Poiseuille")==0) {
      printf("Velocity profile            : Poiseuille \n");
    }
    else if (profile.compare("Polhausen")==0) {
      printf("Velocity profile            : Polhausen \n");
    }

      printf("Boundary layer thickness    : %Lf \n \n", deltaBL );

  }

}
//####################################################
// Setters Initial Geometry
//####################################################
void artery::set_x() {

  x[0] = ONEsTWO * dx[0];
  for (int i=1 ; i < nx ; i++) {
      x[i] = x[i-1] +  ONEsTWO * (dx[i-1]+dx[i]) ;
  }

  if (abs(kahanSum(dx) - l) > EPSILON_X) {
    printf("sum=%20.20Lf,L=%20.20Lf,sum-L=%20.20Lf,eps=%20.20Lf\n",kahanSum(dx),l,abs(kahanSum(dx)-l),EPSILON_X );
    Error("set_dx: Error in sum(dx)") ;
  }
}
void artery::set_dxmin() {
  SCALAR dmin = dx[0] ;
  for (int i=1 ; i < nx ; i++) {
      dmin = MIN(dmin,dx[i]);
  }
  dxmin = dmin ;
}
//####################################################
// Setters layer constant properties
//####################################################
void artery::set_r() {
  r[0] = ONEsTWO * dl[0];
  for (int j=1 ; j < nl ; j++) {
      r[j] = r[j-1] +  ONEsTWO * (dl[j-1]+dl[j]) ;
  }

  if (abs(r[nl-1] + ONEsTWO*dl[nl-1] - 1.) > EPSILON_X) {
    printf("r+dl/2=%20.20Lf,r+dl/2-1=%20.20Lf,eps=%20.20Lf\n",r[nl-1] + ONEsTWO*dl[nl-1],abs(r[nl-1] + ONEsTWO*dl[nl-1] - 1.),EPSILON_X );
    Error("set_r: Error in r") ;
  }

  if (abs(kahanSum(dl) - 1.) > EPSILON_X) {
    printf("sum=%20.20Lf,sum-1=%20.20Lf,eps=%20.20Lf\n",kahanSum(dl),abs(kahanSum(dl)-1.),EPSILON_X );
    Error("set_r: Error in sum(dl)") ;
  }
}
void artery::set_dla() {
  dla[0] = pow(r[0] + ONEsTWO * dl[0] , TWO) ;
  for (int j=1 ; j < nl ; j++) {
      dla[j] = pow( r[j] + ONEsTWO * dl[j] , TWO) - pow( r[j-1] + ONEsTWO * dl[j-1] , TWO  ) ;
  }
  if (abs(kahanSum(dla) - 1.) > EPSILON_X) {
    printf("sum=%20.20Lf,sum-1=%20.20Lf,eps=%20.20Lf\n",kahanSum(dla),abs(kahanSum(dla)-1.),EPSILON_X );
    Error("set_dla: Error in sum(dla)") ;
  }
}
void artery::set_dlj() {
  // Coefficient of viscous subproblem
  for ( int j=0 ; j < nl-1 ; j++) {
      dlj[j] =  FOUR * PI * mu / rho
                * (r[j] + ONEsTWO * dl[j]) / (dl[j] + dl[j+1]) ;
  }
  // We use the Asymptotic development of U(R) in the last layer
  dlj[nl-1] = TWO * PI * mu / rho
              * (r[nl-1] + ONEsTWO * dl[nl-1])
              / ( - ONEsTHREE
                  + pow( ONE - dl[nl-1], TWO )
                  - TWOsTHREE * pow( ONE - dl[nl-1], THREE )
              );
}
//####################################################
// Setters initial layer flow rate Ql
//####################################################
void artery::set_initQl() {
  for ( int i=0 ; i < nx ; i++) {
      for ( int j=0 ; j < nl ; j++) {
        initQl(j,i) = initQ[i] * dla[j] * Profile( initprofile, r[j], deltaBL) ;
      }
  }
}
//####################################################
// Getters
//####################################################
SCALAR artery::get_Lambdamax() const {

  SCALAR Lmax = ZERO ;
  SCALAR L1 = ZERO, L2 = ZERO ;
  for ( int i=0; i < nx ; i++) {
    for ( int j=0; j < nl ; j++) {
      L1    = MAX(  Lmax, abs( lambda1l(rho,k[i],dla[j],A[i],Ql(j,i)) ) ) ;
      L2    = MAX(  Lmax, abs( lambda2l(rho,k[i],dla[j],A[i],Ql(j,i)) ) ) ;
      Lmax  = MAX(  L1  , L2 ) ;
    }
  }
  return Lmax ;
}
SCALAR artery::get_dtmin() const {

  SCALAR dtmin = ONE ;
  SCALAR Lmax = ZERO;
  SCALAR L1 = ZERO, L2 = ZERO ;
  for ( int i=0; i < nx ; i++) {
    for ( int j=0; j < nl ; j++) {
      L1    = abs( lambda1l(rho,k[i],dla[j],A[i],Ql(j,i)) ) ;
      L2    = abs( lambda2l(rho,k[i],dla[j],A[i],Ql(j,i)) ) ;
      Lmax  = MAX(  L1  , L2 ) ;

      dtmin = MIN( dtmin,
                ( dla[j] * A[i] * dx[i] ) /
                (
                  dla[j] * A[i] * Lmax + dx[i] * (get_G1s2(j+1,i) - get_G1s2(j,i))
                )
              );
    }
  }
  return dtmin ;
}
SCALAR artery::get_resA() const {

    VECT res(nx,ZERO), meanA(nx,ZERO), meanAm1(nx,ZERO) ;
    for (int i=0 ; i < nx ; i++) {
      res[i] = abs(A[i] - Am1[i]) ;
      if (res[i] <= EPSILON) {
        res[i] = ZERO ;
      }
      meanA[i] = abs(A[i]) ;
      meanAm1[i] = abs(Am1[i]) ;
    }

    if (kahanSum(meanA) + kahanSum(meanAm1) <= EPSILON) {
      return ZERO ;
    }
    else {
      return TWO * kahanSum(res) / ( kahanSum(meanA) + kahanSum(meanAm1) );
    }
}
SCALAR artery::get_resQl() const {

  VECT res(nx,ZERO), meanQl(nx,ZERO), meanQlm1(nx,ZERO) ;
  for (int i=0 ; i < nx ; i++) {
    for (int j=0 ; j < nl ; j++) {
      res[i] += abs(Ql(j,i) - Qlm1(j,i)) ;
      if (res[i] <= EPSILON) {
        res[i] = ZERO ;
      }
      meanQl[i] += abs(Ql(j,i)) ;
      meanQlm1[i] += abs(Qlm1(j,i)) ;
    }
  }

  if (kahanSum(meanQl) + kahanSum(meanQlm1) <= EPSILON) {
    return ZERO ;
  }
  else {
    return  TWO * kahanSum(res) / ( kahanSum(meanQl) + kahanSum(meanQlm1) );
  }
}
//####################################################
// Readers
//####################################################
double artery::read_P(int pos, const SCALAR dt) const {
  return    pressure_elast( k[pos],a0[pos],A[pos])
          + pressure_visc(  dt,rho,cv[pos],A[pos],Am1[pos])
          + pressure_nl(    knl[pos],a0[pos],A[pos]);
}
