#include "stdio.h"
#include "stdlib.h"
#include "math.h"
#define sq(x) x*x

double e1= 0.5;
double e2= 0.1;

int main(int argc, char *argv[])
{

	int it,j,ix;

	double L = 2.;
	int Nx = 100;
	double dx = L/Nx;

	double t=0.;
	double dt = 1e-5;
	int Nt = 800;

	double omega = 1.;
	double amp = 0.01;

	double A[Nx];
	double Q[Nx];
	double P[Nx];
	double fa[Nx],fq[Nx];

	double R=0.005;
	double K= 1e3;

	void kurganov (double Am, double Ap, double Qm, double Qp,double * fa, double * fq);
	void rusanov (double Am, double Ap, double Qm, double Qp,double * fa, double * fq);
	void rusanov2 (double Am, double Ap, double Qm, double Qp,double * fa, double * fq);
	void rusanov_Varga (double Am, double Ap, double Qm, double Qp,double * fa, double * fq);

	// initial conditions
	for(ix=0; ix<Nx; ix++){
		A[ix]=1.; 
		Q[ix]=0.;
	}

	FILE *fichierA =fopen("A.txt", "w");
	FILE *fichierQ =fopen("Q.txt", "w");

	for (j=0; j<1000; j++){
		// time loop 
		for (it=0; it<Nt;it++){

			t+=dt;

			// boundary conditions 
			// x=0
			A[0]=A[1];
			Q[0]=  amp *fmax(0,sin(2*3.14*omega*t*(t<1))); //amp *sin(2*3.1415*omega*t);
			// x=L
			A[Nx-1]= A[Nx-2];
			Q[Nx-1]= 0.;
		
			// fluxes loop
			for (ix=1; ix<Nx; ix++){
				rusanov_Varga(A[ix-1],A[ix],Q[ix-1], Q[ix],&fa[ix],&fq[ix]);
			}
			for (ix=1; ix<Nx-1; ix++){
				A[ix] = A[ix] + dt/dx *(fa[ix] - fa[ix+1]) ;
				Q[ix] = Q[ix] + dt/dx *(fq[ix] - fq[ix+1])  - dt*e2 * Q[ix]/A[ix];
 			}
 		}

	 	for(ix=0;ix<Nx;ix++) {  
	 		fprintf(fichierA, "%1f %1f \n", ix*dx, A[ix]);
	 		fprintf(fichierQ, "%1f %1f \n", ix*dx, Q[ix]);
      	}
	    fprintf(fichierA,"\n \n");
		fprintf(fichierQ,"\n \n");
	}
}

void rusanov (double Am, double Ap, double Qm, double Qp, double * fa, double * fq)
{
	// p = K * A
	double um = Qm/Am;
 	double up = Qp/Ap;
 	double cp = sqrt(2.*e1*Ap), cm = sqrt(2.*e1*Am);
 	double a = fmax(fabs(cp), fabs(cm));

	*fa = (Qm + Qp)/2. - a * (Ap - Am)/2.;
 	*fq = (sq(Qm)/Am + e1*sq(Am) + sq(Qp)/Ap + e1*sq(Ap) )/2. - a * (Qp - Qm)/2.;
}

void rusanov2 (double Am, double Ap, double Qm, double Qp, double *fa, double *fq)
{
	// p = K * sqrt(A)
	double um = Qm/Am;
 	double up = Qp/Ap;
 	double cp = sqrt(e1*sqrt(Ap)), cm = sqrt(e1*sqrt(Am));
 	double a = fmax(fabs(cp), fabs(cm));
 	double e3 = 2./3. *e1;

	*fa = (Qm + Qp)/2. - a * (Ap - Am)/2.;
	*fq = (sq(Qm)/Am + e3*pow(Am, 3./2.) + sq(Qp)/Ap + e3*pow(Ap, 3./2.) )/2. - a * (Qp - Qm)/2.;
}

void rusanov_Varga (double Am, double Ap, double Qm, double Qp, double *fa, double *fq)
{
	// p = K (sqrt(A/A0) - sqrt(A0/A))
	double um = Qm/Am;
 	double up = Qp/Ap;
 	
 	double e3 = 2./3. *e1;
 	double K = 1000;
 	double rho = 1e3;
 	double A0 = 1.; 
 	double e4 = K*sqrt(A0)/rho; 

 	double cp = sqrt(e1*(sqrt(Ap/A0)- sqrt(A0/Ap))), cm = sqrt(e1 *(sqrt(Am/A0)- sqrt(A0/Am)));
	double a = fmax(fabs(cp), fabs(cm));
	
	*fa = (Qm + Qp)/2. - a * (Ap - Am)/2.;
	*fq = (sq(Qm)/Am + e3*pow(Am, 3./2.)+ e4/sqrt(Am) + sq(Qp)/Ap + e3*pow(Ap, 3./2.) + e4/sqrt(Ap) )/2. - a * (Qp - Qm)/2.;
}


void kurganov (double Am, double Ap, double Qm, double Qp, double * fa, double * fq)
{

	double um = Qm/Am;
	double up = Qp/Ap;
	double cp = sqrt(2.*e1*Ap), cm = sqrt(2.*e1*Am);
	double ap = fmax(up + cp, um + cm); ap = fmax(ap, 0.);
	double am = fmin(up - cp, um - cm); am = fmin(am, 0.);
	double qm = Am*um, qp = Ap*up;
 	double a = fmax(ap, -am);

	if (a > 0.) {
		*fa = (ap*qm - am*qp + ap*am*(Ap - Am))/(ap - am);
		*fq = (ap*(qm*um + e1*sq(Am)) - am*(qp*up + e1*sq(Ap)) + ap*am*(qp - qm))/(ap - am);
 	}
 	else
   	{
    	*fa = *fq = 0.;
   	}
}