#include "stdio.h"
#include "stdlib.h"
#include "math.h"
#define sq(x) x*x

double f(double x, double C)
{
	return sq(x) - C ; 
}

double fp(double x, double C)
{
	return 2*x;
}

double Newton(double x0, double par, int N)
{
	double xk = x0, xk1; 
	int i;

	for(i=0; i<N;i++)
	{
		xk1 = xk - f(xk, par)/fp(xk, par);
		xk = xk1;
	}
	
	return xk1;
}

double AtoP(double A, double A0, double K)
{
// conversion of A (cross section) to P (elastic pressure)
	return K * (sqrt(A)-sqrt(A0));
}

double f_outlet_RC(double Ap1, double Qp1, int size, double par[size])
{
	double R = par[0];
	double C = par[1];
	double dt= par[2];
	double A = par[3];
	double A0= par[4];
	double K = par[5];
	double PL= par[4];
	double res;

	double Pp1, P;
	Pp1 = AtoP(Ap1, A0, K);
	P = AtoP(A, A0, K); 

	res = - C * (Pp1 - P) + dt * (Qp1 - (Pp1-PL)/R);

	return res;
}

int main(int argc, char *argv[])
{
	printf("f = %f", f(1., 4.));
	printf("fprime = %f", fp(1.,4.));

	printf(" x = %f", Newton(1.,4., 5));
}