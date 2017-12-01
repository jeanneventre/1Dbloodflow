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

double Pt(double rho, double K, double A0, double A, double Q)
{
	// total pressure for point junction
	return 1./2. * rho * sq(Q/A) + AtoP(A,A0,K);
}

double cmk(double rho, double K, double A)
{
	// Moens-Korteweg velocity
	return sqrt(K/(2.*rho) * sqrt(A));
}

double W1(double rho, double K, double A, double Q)
{
	return Q/A + 4. * cmk(rho,K,A);
}

double W2(double rho, double K, double A, double Q)
{
	return Q/A - 4. * cmk(rho,K,A); 
}