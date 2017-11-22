#include "stdio.h"
#include "stdlib.h"
#include "math.h"
#define sq(x) x*x


double AtoP(double A, double A0, double K)
{
	// conversion of A (cross section) to P (elastic pressure)
	return K * (sqrt(A)-sqrt(A0));
}

double PtoA(double P, double A0, double K)
{
	// conversion of P (elastic pressure) to A (cross section)
	return sq(P/K + sqrt(A0));
}

