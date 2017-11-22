#include "stdio.h"
#include "stdlib.h"
#include "math.h"
#define sq(x) x*x

double integrale(double Qm, double Qp, double Q0, double h)
{
	double integrale=0.;
	integrale = (Qp/Q0+Qm/Q0)/2 * h;

 	return integrale ;
}

