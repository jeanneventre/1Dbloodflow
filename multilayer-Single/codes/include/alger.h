#ifndef ALGER_H
#define ALGER_H

#include "misc.h"
#include "VECT.h"

static const SCALAR sqrtPi=sqrt(PI);

namespace alger
{
        VECT gaussElimin(const MATR& a, const VECT& v);
        VECT gaussPivot(const MATR& a, const VECT& v,SCALAR tol=EPSILON);

        void swapRows(VECT& a, const int i, const int j);
        void swapRows(MATR& a, const int i, const int j);
        void swapCols(MATR& a, const int i, const int j);

        VECT func(const VECT& x);
        MATR Jacobian(const VECT& x);

        MATR Jacobian_approx(VECT (*f)(const VECT&, const VECT & par),const VECT& x,const VECT&, const SCALAR h=HEPS);

        VECT newtonRahpson(VECT (*f)(const VECT&, const VECT& par),const VECT&, const VECT&, int maxIter=int(maxIt),SCALAR tol=EPSILON);
};

#endif // ALGER_H
