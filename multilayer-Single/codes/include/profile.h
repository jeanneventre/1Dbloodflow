#ifndef PROFILE_H
#define PROFILE_H

#include <misc.h>
#include <VECT.h>
#include <error.h>

//-----------------------------------
// Profile help functions
//-----------------------------------
SCALAR Profile( const string& profile, const SCALAR r, const SCALAR delta) ;

SCALAR Profile_Polhausen(const SCALAR r, const SCALAR delta) ;

SCALAR Profile_Poiseuille(const SCALAR r) ;

SCALAR Profile_Flat() ;

#endif // PROFILE_H
