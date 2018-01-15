#ifndef ARTERYBC_H
#define ARTERYBC_H

#include <misc.h>
#include <VECT.h>
#include <helpFunctions.h>
#include <profile.h>
#include <alger.h>

using namespace alger;

  VECT fun_inflow_Q(const VECT& AQ, const VECT& par) ;
  VECT fun_inflow_QA(const VECT& AQ, const VECT& par) ;
  VECT fun_outflow_Q(const VECT& AQ, const VECT& par) ;

  SCALAR interpolateW1(const VECT& prop, const VECT& AQc, const VECT& AQvar);
  SCALAR interpolateW2(const VECT& prop, const VECT& AQc, const VECT& AQvar);
  SCALAR interpolateW1_l(const VECT& prop, const VECT& dla, const VECT& AQc, const VECT& AQvar, const int j);
  SCALAR interpolateW2_l(const VECT& prop, const VECT& dla, const VECT& AQc, const VECT& AQvar, const int j);

  // Inlet
  //######
  VECT inflow_Q(  const VECT& prop, const VECT& dla, const VECT& r, const VECT& AQc, const VECT& AQrec, const VECT& AQvar, const string& profile, const SCALAR inQ) ;
  VECT inflow_U(  const VECT& prop, const VECT& dla, const VECT& r, const VECT& AQc, const VECT& AQrec, const VECT& AQvar, const string& profile, const SCALAR inU) ;
  VECT inflow_QA( const VECT& prop, const VECT& dla, const VECT& r, const VECT& AQc, const VECT& AQrec, const VECT& AQvar, const string& profile, const SCALAR inA, const SCALAR inQ) ;
  VECT inflow_UA( const VECT& prop, const VECT& dla, const VECT& r, const VECT& AQc, const VECT& AQrec, const VECT& AQvar, const string& profile, const SCALAR inA, const SCALAR inU) ;

  VECT inflow_A(const VECT& prop, const VECT& dla, const VECT& AQc, const VECT& AQvar, const SCALAR inA) ;
  VECT inflow_P(const VECT& prop, const VECT& dla, const VECT& AQc, const VECT& AQvar, const SCALAR inP) ;

  VECT inflow_Rt(const VECT& prop, const VECT& dla, const VECT& AQinit, const VECT& AQc, const VECT& AQvar, const SCALAR Rt) ;

  // Outlet
  //#######
  VECT outflow_Q(const VECT& prop, const VECT& dla, const VECT& r, const VECT& AQc, const VECT& AQrec, const VECT& AQvar, const string& profile, const SCALAR outQ) ;
  VECT outflow_U(const VECT& prop, const VECT& dla, const VECT& r, const VECT& AQc, const VECT& AQrec, const VECT& AQvar, const string& profile, const SCALAR outU) ;

  VECT outflow_A(const VECT& prop, const VECT& dla, const VECT& AQc, const VECT& AQvar, const SCALAR outA) ;
  VECT outflow_P(const VECT& prop, const VECT& dla, const VECT& AQc, const VECT& AQvar, const SCALAR outP) ;

  VECT outflow_Rt(const VECT& prop, const VECT& dla, const VECT& AQinit, const VECT& AQc, const VECT& AQvar, const SCALAR Rt) ;

#endif // ARTERYBC_H
