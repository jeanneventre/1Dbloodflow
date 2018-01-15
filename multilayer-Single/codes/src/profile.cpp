 #include "profile.h"

//-----------------------------------
// Profile help functions
//-----------------------------------
SCALAR Profile(const string& profile, const SCALAR r, const SCALAR delta) {
  if (profile == "Polhausen") { return Profile_Polhausen(r, delta) ;}
  else if (profile == "Poiseuille") { return Profile_Poiseuille(r) ;}
  else if (profile == "Flat") { return Profile_Flat() ;}
  else { Error("profile: Unknown velocity profile"); }
}

SCALAR Profile_Polhausen(const SCALAR r, const SCALAR delta) {

 SCALAR Prof = 0. , Umax = 0. ;
 SCALAR eta = 0. ;
 SCALAR C = 0. , N = 0. ;
 SCALAR fact = 0. ;

 if (delta <= 0. || delta >= 1.) {
   printf("deltaBL=%20.20Lf\n", delta );
   Error("Profile_Polhausen:: Error in delta");
 }

 eta = (1.-r) / delta ;
 N = -12. ;
 C = 1. - N / 6. ;

 // Choice of dimensionless (Uav) max velocity
 fact =  1./30. * (30. - 3. * (5. + C) * delta + (3. + C) *  pow(delta,2.)) ;
 if (fact <= 0.) {
  Error("Profile_Polhausen:: Error in exp velocity profile");
 }

 Umax = 1. / fact ;
 // Velocity Profile
 if (eta > 1. ) {
   Prof = Umax ;
 }
 else {
   Prof = Umax * ( 1. - pow(1.-eta,3.) * (1. + C * eta) ) ;
 }
 return Prof;
}

SCALAR Profile_Poiseuille(const SCALAR r) {

 SCALAR Prof = 1. , Umax = 2. ;
 Prof = Umax * (1. - pow(r,2.)) ;
 return Prof;

}

SCALAR Profile_Flat() {

 SCALAR Prof = 1. ;
 return Prof;

}
