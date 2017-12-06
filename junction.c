#include "stdio.h"
#include "stdlib.h"
#include "math.h"
#include "help.h"
#include "help_math.h"
#define sq(x) x*x

void conj_PD(double *res, double * AQ, double * par)
{
	double Ap = AQ[0], Qp = AQ[1];
	double Ad = AQ[2], Qd = AQ[3];

	double W1p = par[0], W2d = par[1]; 
	double rho = par[2];
	double Kp = par[3], Kd = par[4];
	double A0p = par[5], A0d = par[6]; 

	res[0] = Qp - Qd;
	res[1] = Pt(rho, Kp, A0p, Ap, Qp) - Pt(rho, Kd, A0d, Ad, Qd);
	res[2] = W1(rho, Kp, Ap, Qp) - W1p;
	res[3] = W2(rho, Kd, Ad, Qd) - W2d;
}

void p_conj_PD(double * pres, double *AQ, double * par, double h)
{
	int i,j;
	double f0[4],f1[4];
	double df[4];
	conj_PD(f0,AQ,par);
	// for (i=0;i<4;i++)
	// {
	// 	double temp = AQ[i];
	// 	AQ[i]= temp + h;	
	// 	conj_PD(f1,AQ,par);
	// 	df[i] = (f1[i] - f0[i])/h;
	// 	printf("df : %f", df[i]);
	// 	for (j=0; j<4;j++)
	// 	{
	// 		pres[i][j] = df[i];
	// 		printf("pres : %f", pres[i,j]);
	// 	}

	// 	AQ[i]=temp;
	// }
}

// void Newton (double * x, double * res, double * guess, double *par,double maxIter, double tol, double h)
// {
// 	int i;
// 	double err;
// 	double * pres;

// 	for (i=0; i<4;i++)
// 	{
// 		x[i]=guess[i];
// 	}

// 	for (i=0;i<maxIter;i++)
// 	{
// 		conj_PD(res,x,par);
// 		err = norm_L2(res,4);
// 		if (err <= tol){printf("end");}
// 		p_conj_PD(pres,x,par,h);
// 		x = x + res/pres;
// 	}	
// }

// }
// double Newton(void (*f)(double *res, double * AQ, double * par),
// 			  double * guess, double * par,int maxIter,double tol,double dx)
// {
// 	// Newton's algorithm that returns x satisfying f(x) = 0 with tolerance tol
// 	double xk = guess
// 	int i;
// 	double fval;
// 	double fpval;
// 	double err;

// 	for (i=0;i<maxIter;i++){
// 		fval = (*f)(xk,Q,par);
// 		// printf("fval = %1f \n ",fval);
// 		if (fabs(fval) <= tol ){
// 			printf("xk final = %1f", xk);
// 			return xk;
// 			}
		
// 		fpval= fp(xk,f,Q,par,dx);
// 		// printf("fpval = %1f \n", fpval);
// 		xk1 = xk - fval/fpval;
// 		// printf("xk1= %1f \n \n ",xk1);
// 		xk = xk1;
// 	}
// 	return xk ;
// }



int main(int argc, char *argv[])
{
	double rho=1000.,Kp=1333., Kd=1333.;

	double AQ[4];
	double par[7];

	AQ[0] = 1.;
	AQ[1] = 0.001;
	AQ[2] = 1.1;
	AQ[3] = 0.002;

	par[0] = W1(rho,Kp,0.9,0.);
	par[1] = W2(rho,Kp,0.9,0.);
	par[2] = rho; // rho
	par[3] = Kp; // Kp
	par[4] = Kd; // Kd
	par[5] = 1.; // A0p
	par[6] = 1.; // A0d

	int i;
	double res[4];
	conj_PD(res, AQ,par);

	for (i=0;i<4;i++){
		printf("res :%1F \n ",res[i]);
	}	

	double h = 1e-4;
	double pres[4][4];
	p_conj_PD(pres,AQ,par,h);
}