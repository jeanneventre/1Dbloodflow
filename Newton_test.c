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
	// printf("P: %1F",P );
	res = Q-(P - PL)/R ;

	return res;
}

// double fp_outlet_R(double A, double Q, double par[4])
// {
// 	double R = par[0];
// 	double A0= par[1];
// 	double K = par[2];
// 	double PL= par[3];
// 	double res;

// 	double P = AtoP(A,A0,K) ;

// 	res = -1/R ;

// 	return res; 
// }

double fp(double x, int n, double (*f)(double x, double Q, double par[n]), double Q,double par[n], double dx)
{
	double f0 = (*f)(x,Q,par);
	double f1 = (*f)(x+dx,Q,par); 
	// printf("f0: %1F \n",f0);
	// printf("f1: %1F \n", f1);
	// printf("f1 - f0 = %1F \n", (f1-f0));
	return (f1 - f0)/dx;

}

double Newton(int n,double(*f)(double A, double Q, double par[n]),
			  double Q, double guess, double par[n],int maxIter,double tol,double dx)
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
			printf("xk final = %1f", xk);
			return xk;
			}
		
		fpval= fp(xk,n,f,Q,par,dx);
		printf("fpval = %1f \n", fpval);
		xk1 = xk - fval/fpval;
		printf("xk1= %1f \n \n ",xk1);
		xk = xk1;
	}
	return xk ;
}

double f_outlet_RC(double Ap1, double Qp1, double * par)
{
	double R = par[0];
	double C = par[1];
	double dt= par[2];
	double A = par[3];
	double A0= par[4];
	double K = par[5];
	double PL= par[6];
	double res;

	double Pp1, P;
	Pp1 = AtoP(Ap1, A0, K);
	P = AtoP(A, A0, K); 

	res = - C * (Pp1 - P) + dt * (Qp1 - (Pp1-PL)/R);

	return res;
}

int main(int argc, char *argv[])
{
	double A,Q;
	A = 1.05;
	Q = 0.01;
	// int size = 4.;
	// double par[size];
	// par[0] = 5.;
	// par[1] = 1.;
	// par[2] = 1333;
	// par[3] = 0.;

	// RC 
	int size=7;
	double par[size];
	par[0] = 10;
	par[1] = 0.01;
	par[2] = 1e-5;
	par[3] = A;
	par[4] = 1.;
	par[5] = 1333.;
	par[6] = 0.;

	// double (* f)(double * AQ, double * par);
	// double (* fp)(double * AQ, double * par);

	// f = &f_outlet_R;
	// fp = &fp_outlet_R;

	// printf("test : %f \n test prime : %f \n", f_outlet_R(A,Q,par));

	double a;
	double tol = 1e-8;
	double dx=1e-5;
	int maxIter=10;
	a= Newton(size,f_outlet_RC,Q,A,par,maxIter, tol,dx);
	
	double b[1000];
	int i;
	double dA = 1e-2;
	A = 0;

	FILE * fichier=fopen("test.txt","w");
	for (i=0;i<1000;i++){
		A +=dA;
		b[i] = f_outlet_RC(A,Q,par);
		fprintf(fichier, "%1f %1F \n", A,b[i]);
	}

	// printf("test %1f \n ", a);
	// printf("test 2 : %1F \n", fp(2, 4, f_outlet_R,Q,par, dx));



}