#include "stdio.h"
#include "stdlib.h"
#include "math.h"
#define sq(x) x*x

// double f(double x, double C)
// {
// 	return sq(x) - C ; 
// }

// double fp(double x, double C)
// {
// 	return 2*x;
// }

double AtoP(double A, double A0, double K)
{
// conversion of A (cross section) to P (elastic pressure)
	return K * (sqrt(A)-sqrt(A0));
}

double PtoA(double P, double A0, double K)
{
	return sq(P/K + sqrt(A0));
}


double f_outlet_R(double A, double Q, double par[4])
{
	double R = par[0];
	double A0= par[1];
	double K = par[2];
	double PL= par[3];
	double res;

	double P = AtoP(A,A0,K) ;

	res = Q-(P - PL)/R ;

	return res;
}

double fp_outlet_R(double A, double Q, double par[4])
{
	double R = par[0];
	double A0= par[1];
	double K = par[2];
	double PL= par[3];
	double res;

	double P = AtoP(A,A0,K) ;

	res = -1/R ;

	return res; 
}

double fp(double x, int n, double (*f)(double x, double Q, double par[n]), double Q,double par[n], double dx)
{
	double f0 = (*f)(x,Q,par);
	double f1 = (*f)(x+dx,Q,par); 
	printf("f0: %1F \n",f0);
	printf("f1: %1F \n", f1);
	printf("f1 - f0 = %1F \n", (f1-f0));
	return (f1 - f0)/dx;

}

double Newton(int n,double(*f)(double A, double Q, double par[n]), double (*fp)(double A,double Q,double par[n]),double Q, double guess, double par[n],int maxIter,double tol)
{

	double xk = guess,xk1;
	int i;
	double fval;
	double fpval;
	double err;

	for (i=0;i<maxIter;i++){
		fval = (*f)(xk,Q,par);
		printf("fval = %1f \n ",fval);
		if (fabs(fval) <= tol ){	
			return xk;
			}
		
		fpval= (*fp)(xk,Q,par);
		printf("fpval = %1f \n", fpval);
		xk1 = xk - fval/fpval;
		printf("xk1= %1f \n \n ",xk1);
		xk = xk1;
	}
	return xk ;

	// double f_outlet_R(double * AQ, double * par);
	// double fp_outlet_R(double * AQ, double * par);	

	// for(i=0; i<N;i++)
	// {
	// 	xk1 = xk - f_outlet_R(AQ, par)/fp_outlet_R(AQ, par);
	// 	xk = xk1;
	// }

	// for(i=0; i<N;i++)
	// {
	// 	fval = (*f)(x,par);
	// 	printf("fval = %f \n", fval);
	// 	fpval = (*fp)(x,par);
	// 	dx = fval/ fpval;

	// 	x = x- dx;
	//}

 	// for (i=0;i<2;i++)
 	// {
 	// 	fval = (*f)(xk,par);
 	// 	fpval = (*fp)(xk,par);
 	// 	*xk1 = *xk - fval/fpval;
 	// 	*xk = *xk1;
 	// }
	// // int i,k;
	// // double xk[2];
	// // double xk1[2];
	// // xk[0] = guess[0];
	// // xk[1] = guess[1];
	// double fval=0.,fpval=0.;
	// fval = (*f)(AQ,par);
	// printf("fval : %1f \n ", fval);
	// for (i=0;i<N;i++){
	// 	for (k=0;k<2;k++){
	// 	fval = (*f)(AQ, par);
	// 	printf("fval : %1f \n", fval);
	//  	fpval= (*fp)(AQ,par);
	//  	printf("fpval : %1f \n ", fpval);
	//  	xk1[k] = xk[k] - fval/fpval;
	//  	xk[k] = xk1[k];
	//  	}
	// }
	// printf("ici : %1f  %1f \n ", xk[0], xk[1]);
	// return xk;,
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

	double A,Q;
	A = 1.05;
	Q = 0.01;

	int N=3;

	// double (* f)(double * AQ, double * par);
	// double (* fp)(double * AQ, double * par);

	// f = &f_outlet_R;
	// fp = &fp_outlet_R;

	// printf("test : %f \n test prime : %f \n", f_outlet_R(A,Q,par), fp_outlet_R(A,Q,par));

	double a;
	double tol = 1e-4;
	a= Newton(2,f_outlet_R, fp_outlet_R,Q,A,par,5, tol);
	
	// printf("test %1f \n ", a);
	printf("test 2 : %1F \n", fp(A, 4, f_outlet_R,Q,par, 1e-2));
}