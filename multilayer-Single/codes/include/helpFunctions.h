#ifndef HELPFUNCTIONS_H
#define HELPFUNCTIONS_H

#include <misc.h>
#include <VECT.h>
#include <alger.h>

//#######
SCALAR kahanSum(VECT& IN) ;
//#######
SCALAR fluxQP   (const SCALAR RHO, const SCALAR K, const SCALAR A_t) ;
SCALAR fluxQ    (const SCALAR RHO, const SCALAR K, const SCALAR A_t, const SCALAR Q_t) ;

SCALAR W1       (const SCALAR RHO, const SCALAR K, const SCALAR A_t, const SCALAR Q_t);
SCALAR W2       (const SCALAR RHO, const SCALAR K, const SCALAR A_t, const SCALAR Q_t);
SCALAR W1l      (const SCALAR RHO, const SCALAR K, const SCALAR dla, const SCALAR A_t, const SCALAR Ql_t);
SCALAR W2l      (const SCALAR RHO, const SCALAR K, const SCALAR dla, const SCALAR A_t, const SCALAR Ql_t);

SCALAR lambda1  (const SCALAR RHO, const SCALAR K, const SCALAR A_t, const SCALAR Q_t);
SCALAR lambda2  (const SCALAR RHO, const SCALAR K, const SCALAR A_t, const SCALAR Q_t);
SCALAR lambda1l (const SCALAR RHO, const SCALAR K, const SCALAR dla, const SCALAR A_t, const SCALAR Ql_t);
SCALAR lambda2l (const SCALAR RHO, const SCALAR K, const SCALAR dla, const SCALAR A_t, const SCALAR Ql_t);

SCALAR cmk      (const SCALAR RHO, const SCALAR K, const SCALAR A_t)  ;

SCALAR pressure_elast(const SCALAR K, const SCALAR A0, const SCALAR A_t) ;
SCALAR pressure_visc(const SCALAR dt, const SCALAR RHO, const SCALAR Cv, const SCALAR A_t, const SCALAR A_tm1 )  ;
SCALAR pressure_nl(const SCALAR Knl, const SCALAR A0, const SCALAR A_t) ;

// Kinetic flux with hat function
VECT flux_Hat_l(const SCALAR RHO, const SCALAR K, const SCALAR Knl, const SCALAR Znl, const SCALAR dla, const SCALAR A_r, const SCALAR A_l, const SCALAR U_r, const SCALAR U_l);

// Second Order
SCALAR minmod(const SCALAR a, const SCALAR b);

#endif // HELPFUNCTIONS_H
