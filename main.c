#include "stdio.h"
#include "stdlib.h"
#include "math.h"
#include "fluxes.h"
#include <sys/types.h>
#include <sys/stat.h>

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
	double amp = 2;

	double A[Nx];
	double Q[Nx];
	double P[Nx];
	double fa[Nx],fq[Nx];

	double R=0.005;
	double K= 1e3;
	double c=1;

	// void kurganov (double Am, double Ap, double Qm, double Qp,double * fa, double * fq);
	// void rusanov (double Am, double Ap, double Qm, double Qp,double * fa, double * fq);
	// void rusanov2 (double Am, double Ap, double Qm, double Qp,double * fa, double * fq);
	// void rusanov_Varga (double Am, double Ap, double Qm, double Qp,double * fa, double * fq);
	void rusanov_Varga2(double Am, double Ap, double Qm, double Qp,double * fa, double * fq);
	// void rusanov_NeoHooke (double Am, double Ap, double Qm, double Qp,double * fa, double * fq);

	// initial conditions
	for(ix=0; ix<Nx; ix++){
		A[ix]=1.; 
		Q[ix]=0.;
	}

    int result = mkdir("output", 0777);

    FILE *fichierA =fopen("output/A_Varga_amp2.txt", "w");
	FILE *fichierQ =fopen("output/Q_Varga_amp2.txt", "w");

	// double N = 1000./(2*3.1415*c);
	for (j=0; j< 300; j++){
		// time loop 
		for (it=0; it<Nt;it++){

			t+=dt;

			// boundary conditions 
			// x=0
			A[0]=A[1];
			Q[0]=  amp *fmax(0,sin(2*3.1415*omega*t*(t<1))); //amp *sin(2*3.1415*omega*t);
			// x=L
			A[Nx-1]= A[Nx-2];
			Q[Nx-1]= 0;		
			// fluxes loop
			for (ix=1; ix<Nx; ix++){
				rusanov_Varga2(A[ix-1],A[ix],Q[ix-1], Q[ix],&fa[ix],&fq[ix]);
			}
			for (ix=1; ix<Nx-1; ix++){
				A[ix] = A[ix] + dt/dx *(fa[ix] - fa[ix+1]) ;
				Q[ix] = Q[ix] + dt/dx *(fq[ix] - fq[ix+1])  - dt*e2 * Q[ix]/A[ix];
				// c = sqrt(2*e1*A[ix]);
				// c = sqrt(e1 *sqrt(A[ix]));
				//c = sqrt(e1 * (3./2.*pow(A[ix],-3./2.) -1./2.* pow(A[ix],-1./2. ))),
				// N = 1000/(2*3.1415*c);
				// printf("c = %lf, A= %lf et N = %f \n", c, A[ix], 1000/(2*3.1415*c));
 			}
 		}
	 	for(ix=0;ix<Nx;ix++) {  
	 		fprintf(fichierA, "%1f %1f \n", ix*dx, A[ix]);
	 		fprintf(fichierQ, "%1f %1f \n", ix*dx, Q[ix]/amp);
      	}
	    fprintf(fichierA,"\n \n");
		fprintf(fichierQ,"\n \n");
	}

// printf("c = %lf,  et N = %f \n", c, N);
}