 #include "helpFunctions.h"

// Kahan Sum
SCALAR kahanSum(VECT& IN) {
 SCALAR sum = IN[0] ;
 SCALAR c = 0. , y = 0., t= 0. ;          //A running compensation for lost low-order bits.
 for (int i = 1 ; i< IN.get_dim() ; i++) {
   y = IN[i] - c  ;    //So far, so good: c is zero.
   t = sum + y ;       //Alas, sum is big, y small, so low-order digits of y are lost.
   c = (t - sum) - y ;  //(t - sum) recovers the high-order part of y; subtracting y recovers -(low part of y)
   sum = t ;           //Algebraically, c should always be zero. Beware eagerly optimising compilers!
 }                    //Next time around, the lost low part will be added to y in a fresh attempt.
 return sum ;
}

//####################################################
// Characteristic structure
//####################################################
SCALAR fluxQP(const SCALAR RHO, const SCALAR K, const SCALAR A_t) {
    return ONEsTHREE * K / RHO * pow(A_t,THREEsTWO) ;
}

SCALAR fluxQ(const SCALAR RHO, const SCALAR K, const SCALAR A_t, const SCALAR Q_t) {
    return pow(Q_t,TWO) / A_t + fluxQP(RHO, K, A_t) ;
}
// Riemann invariants
//###################
SCALAR W1(const SCALAR RHO, const SCALAR K, const SCALAR A_t, const SCALAR Q_t) {
    return Q_t / A_t + FOUR * cmk(RHO,K,A_t);
}
SCALAR W2(const SCALAR RHO, const SCALAR K, const SCALAR A_t, const SCALAR Q_t) {
    return Q_t / A_t - FOUR * cmk(RHO,K,A_t);
}
SCALAR W1l(const SCALAR RHO, const SCALAR K, const SCALAR dla, const SCALAR A_t, const SCALAR Ql_t) {
    return Ql_t / dla / A_t + FOUR * cmk(RHO,K,A_t);
}
SCALAR W2l(const SCALAR RHO, const SCALAR K, const SCALAR dla, const SCALAR A_t, const SCALAR Ql_t) {
    return Ql_t / dla / A_t - FOUR * cmk(RHO,K,A_t);
}
// Eigenvalues
//###################
SCALAR lambda1(const SCALAR RHO, const SCALAR K, const SCALAR A_t, const SCALAR Q_t) {
    return Q_t / A_t + cmk(RHO,K,A_t);
}
SCALAR lambda2(const SCALAR RHO, const SCALAR K, const SCALAR A_t, const SCALAR Q_t) {
    return Q_t / A_t - cmk(RHO,K,A_t);
}
SCALAR lambda1l(const SCALAR RHO, const SCALAR K, const SCALAR dla, const SCALAR A_t, const SCALAR Ql_t) {
    return Ql_t / dla / A_t + cmk(RHO,K,A_t);
}
SCALAR lambda2l(const SCALAR RHO, const SCALAR K, const SCALAR dla, const SCALAR A_t, const SCALAR Ql_t) {
    return Ql_t / dla / A_t - cmk(RHO,K,A_t);
}

// Moens-Korteweg celerity
SCALAR cmk(const SCALAR RHO, const SCALAR K, const SCALAR A_t)  {
    return sqrt( ONEsTWO * K / RHO * sqrt(A_t) );
}
//####################################################
// Pressure
//####################################################
SCALAR pressure_elast(const SCALAR K, const SCALAR A0, const SCALAR A_t) {
    return K * ( sqrt(A_t) - sqrt(A0) ) ;
}
SCALAR pressure_visc(const SCALAR dt, const SCALAR RHO, const SCALAR Cv, const SCALAR A_t, const SCALAR A_tm1 )  {
    return Cv * RHO / A_t * ( A_t - A_tm1 ) / dt ;
}
SCALAR pressure_nl(const SCALAR Knl, const SCALAR A0, const SCALAR A_t) {
    return Knl * pow( sqrt(A_t) - sqrt(A0), TWO ) ;
}
//####################################################
// Flux
//####################################################
// Kinetic flux with Hat function
VECT flux_Hat_l(const SCALAR RHO, const SCALAR K, const SCALAR Knl, const SCALAR Znl, const SCALAR dla, const SCALAR A_r, const SCALAR A_l, const SCALAR U_r, const SCALAR U_l) {

   SCALAR SQRTthree = sqrt(THREE) , oneStwoSQRTthree = ONEsTWO / SQRTthree ;
   SCALAR ci=ZERO , cg=ZERO , Mp=ZERO, Mm=ZERO ;
   SCALAR FAp=ZERO , FAm=ZERO , FQp=ZERO , FQm=ZERO ;

  // F+(U_rr[i])
  //#############
  //  ci = sqrt( ONEsTHREE * K / RHO * sqrt(A_r) ) ;
   ci = sqrt(   ONEsTHREE * K   / RHO * sqrt(A_r)
              + ONEsTHREE * Knl / RHO * sqrt(A_r) * THREEsTWO * sqrt(A_r)
              - ONEsTHREE       / RHO * sqrt(A_r) * TWO * Znl
            ) ;
   cg = oneStwoSQRTthree * dla * A_r / ci ;
   Mp = MAX(ZERO,U_r + SQRTthree * ci) ;
   Mm = MAX(ZERO,U_r - SQRTthree * ci) ;

   FAp = ONEsTWO * cg * ( pow(Mp,TWO) - pow(Mm,TWO) ) ;
   FQp = ONEsTHREE * cg * ( pow(Mp,THREE) - pow(Mm,THREE) ) ;
  // F-(U_ll[i+1])
  //#############
  //  ci = sqrt( ONEsTHREE * K / RHO * sqrt(A_l) ) ;
   ci = sqrt(   ONEsTHREE * K   / RHO * sqrt(A_l)
              + ONEsTHREE * Knl / RHO * sqrt(A_l) * THREEsTWO * sqrt(A_l)
              - ONEsTHREE       / RHO * sqrt(A_l) * TWO * Znl
            ) ;
   cg = oneStwoSQRTthree * dla * A_l / ci ;
   Mp = MIN(ZERO,U_l + SQRTthree * ci) ;
   Mm = MIN(ZERO,U_l - SQRTthree * ci) ;

   FAm = ONEsTWO * cg * ( pow(Mp,TWO) - pow(Mm,TWO) ) ;
   FQm = ONEsTHREE * cg * ( pow(Mp,THREE) - pow(Mm,THREE) ) ;
   //#############
   VECT F(4) ;
   F[0] = FAp ; F[1] = FAm ; F[2] = FQp ; F[3] = FQm ;

   return F;
}
//####################################################
// Second order : minmod
//####################################################
SCALAR minmod(const SCALAR a, const SCALAR b) {
    if (a > 0 && b > 0)
        return min(a,b);
    else if (a < 0 && b < 0 )
        return max(a,b);
    else
        return 0;
}
