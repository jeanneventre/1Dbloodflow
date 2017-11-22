#include "stdio.h"
#include "stdlib.h"
#include "math.h"
#include "help.h"
#define sq(x) x*x

double fp(double x, int n, double (*f)(double x, double Q, double par[n]),
		  double Q,double par[n], double dx)
{
	// f' = (f1-f0)/dx --> finite differences to calculate derivative of f in point x
	double f0 = (*f)(x,Q,par);
	double f1 = (*f)(x+dx,Q,par); 
	return (f1 - f0)/dx;
}

double f_outlet_R(double A, double Q, double par[4])
{
	// boundary condition on the resistance : P - Pout = R Q
	double R = par[0];
	double A0= par[1];
	double K = par[2];
	double PL= par[3];
	double res;

	double P = AtoP(A,A0,K) ;
	res = Q-(P - PL)/R ;

	return res;
}

double Newton(int n,double(*f)(double A, double Q, double par[n]),
			  double Q, double guess, double par[n],int maxIter,double tol,double dx)
{
	// Newton's algorithm that returns x satisfying f(x) = 0 with tolerance tol
	double xk = guess,xk1;
	int i;
	double fval;
	double fpval;
	double err;

	for (i=0;i<maxIter;i++){
		fval = (*f)(xk,Q,par);
		// printf("fval = %1f \n ",fval);
		if (fabs(fval) <= tol ){
			// printf("xk final = %1f", xk);
			return xk;
			}
		
		fpval= fp(xk,n,f,Q,par,dx);
		// printf("fpval = %1f \n", fpval);
		xk1 = xk - fval/fpval;
		// printf("xk1= %1f \n \n ",xk1);
		xk = xk1;
	}
	return xk ;
}
