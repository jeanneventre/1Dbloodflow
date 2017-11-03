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

double AtoP(double A, double A0, double K)
{
// conversion of A (cross section) to P (elastic pressure)
	return K * (sqrt(A)-sqrt(A0));
}

double PtoA(double P, double A0, double K)
{
	return sq(P/K + sqrt(A0));
}


double f_outlet_R(double * AQ, double * par)
{
	double A = AQ[0];
	double Q = AQ[1];

	double R = par[0];
	double A0= par[1];
	double K = par[2];
	double PL= par[3];
	double res;

	double P = AtoP(A,A0,K) ;

	res = Q- (P - PL)/R ;

	return res;
}

double fp_outlet_R(double * AQ, double * par)
{
	double A = AQ[0];
	double Q = AQ[1];

	double R = par[0];
	double A0= par[1];
	double K = par[2];
	double PL= par[3];
	double res;

	double P = AtoP(A,A0,K) ;

	res = -1/R ;

	return res; 
}


double Newton(double x0, double * par, int N)
{
	double xk = x0, xk1; 
	double AQ[2];
	int i;

	double f_outlet_R(double * AQ, double * par);
	double fp_outlet_R(double * AQ, double * par);	

	for(i=0; i<N;i++)
	{
		xk1 = xk - f_outlet_R(AQ, par)/fp_outlet_R(AQ, par);
		xk = xk1;
	}

	return xk1;
}

// double f_outlet_RC(double Ap1, double Qp1, double * par)
// {
// 	double R = par[0];
// 	double C = par[1];
// 	double dt= par[2];
// 	double A = par[3];
// 	double A0= par[4];
// 	double K = par[5];
// 	double PL= par[6];
// 	double res;

// 	double Pp1, P;
// 	Pp1 = AtoP(Ap1, A0, K);
// 	P = AtoP(A, A0, K); 

// 	res = - C * (Pp1 - P) + dt * (Qp1 - (Pp1-PL)/R);

// 	return res;
// }

// double fp_outlet_RC(double Ap1, double Qp1, int size, double par[size])
// {
// 	double R = par[0];
// 	double C = par[1];
// 	double dt= par[2];
// 	double A = par[3];
// 	double A0= par[4];
// 	double K = par[5];
// 	double PL= par[6];
// 	double res;

// 	res = - C - dt/R;

// 	return res;
// }

int main(int argc, char *argv[])
{
	int size = 4.;
	double par[size];
	par[0] = 5000;
	par[1] = 1.;
	par[2] = 1333;
	par[3] = 0.;

	double AQ[2]; 
	AQ[0] = 1.05;
	AQ[1] = 0.01;

	double f_outlet_R(double * AQ, double * par);
	double fp_outlet_R(double * AQ, double *par);

	printf("f = %f \n", f_outlet_R(AQ, par));
	printf("fprime = %f \n",fp_outlet_R(AQ, par));
	
}