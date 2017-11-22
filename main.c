#include "stdio.h"
#include "stdlib.h"
#include "math.h"
#include "fluxes.h"
#include <sys/types.h>
#include <sys/stat.h>
#include "help_math.h"
#include "BC.h"

int main(int argc, char *argv[])
{
	int i,it,j,ix;

	double L = 2.;
	int Nx = 200;
	double dx = L/Nx;

	double t=0.;
	double dt = 1e-5;
	int Nt = 800;

	double omega = 1.;
	double amp =0.0001;

	double A[Nx];
	double Q[Nx];
	double P[Nx];
	double Qana[Nx];
	double fa[Nx],fq[Nx];
	double c[Nx];

	double integrale_ana = 0.;
	double integrale_Q = 0.;	
	double err;
	int N = round(1.2/dx);
//----------------------------------------------------------------------------------------------------------			
    int result = mkdir("output", 0777);
 	FILE *fichierA =fopen("output/A_elastic1_amp0_0001.txt", "w");
	FILE *fichierQ =fopen("output/Q_elastic1_amp0_0001.txt", "w");
	// FILE *fichierQana =fopen("output/Qana.txt", "w");
	// FILE *fichierC=fopen("output/C_NH_amp1.txt", "w");
//----------------------------------------------------------------------------------------------------------	
	// void kurganov (double Am, double Ap, double Qm, double Qp,double * fa, double * fq);
	void rusanov (double Am, double Ap, double Qm, double Qp,double * fa, double * fq);
	// void rusanov2 (double Am, double Ap, double Qm, double Qp,double * fa, double * fq);
	// void rusanov_Varga (double Am, double Ap, double Qm, double Qp,double * fa, double * fq);
	// void rusanov_Varga2(double Am, double Ap, double Qm, double Qp,double * fa, double * fq);
	// void rusanov_NeoHooke(double Am, double Ap, double Qm, double Qp,double * fa, double * fq);
//----------------------------------------------------------------------------------------------------------	
	// initial conditions
	for(ix=0; ix<Nx; ix++){
		A[ix]=1.; 
		Q[ix]=0.;
		Qana[ix]=0.;
	}
//----------------------------------------------------------------------------------------------------------		
	double par[4];
	double guess = 1.5;
	double maxIter=10;
	double tol=1e-6;
	double h=1e-3;

	par[0] = 5000; // R
	par[1] = 1.; // A0
	par[2] = 1333; // K
	par[3] = 0.; // Pout
//----------------------------------------------------------------------------------------------------------	
// saving loop 
	for (j=0; j< 1000; j++){
		// time loop 
		for (it=0; it<Nt;it++){

			t+=dt;

			// boundary conditions -------------------------------------------------------------------------
			// x=0 :
			A[0]=A[1];
			Q[0]=  amp *fmax(0,sin(2*3.1415*omega*t*(t<1))); //amp *sin(2*3.1415*omega*t);
			// x=L : 
			// A[Nx-1]= A[Nx-2];
			Q[Nx-1]= Q[Nx-2];	
			A[Nx-1] = Newton(4,f_outlet_R,Q[Nx-1],guess,par,maxIter, tol,h);
			
			// fluxes loop ---------------------------------------------------------------------------------
			for (ix=1; ix<Nx; ix++){
				rusanov(A[ix-1],A[ix],Q[ix-1], Q[ix],&fa[ix],&fq[ix]);
			}
			// resolution loop -----------------------------------------------------------------------------
			for (ix=1; ix<Nx-1; ix++){
				A[ix] = A[ix] + dt/dx *(fa[ix] - fa[ix+1]) ;
				Q[ix] = Q[ix] + dt/dx *(fq[ix] - fq[ix+1])  - dt*e2 * Q[ix]/A[ix];
				
 			}
 			// analytic solution ---------------------------------------------------------------------------
 			for (ix=0; ix<Nx;ix++){
 				Qana[ix]= amp * fmax(0,-sin(2*3.1415*(omega*ix*dx-omega*t)))*exp(-e2/2 *ix*dx);
 				// c[ix] =  sqrt(2*e1/A[ix]/A[ix]);//sqrt(e1 * (3./(A[ix] * sqrt(A[ix])) - 1./sqrt(A[ix])));//sqrt(e1*sqrt(A[ix]))
 			}
 		}

 		// ecriture dans des fichiers texte ----------------------------------------------------------------
	 	for(ix=0;ix<Nx;ix++) {  
	 		fprintf(fichierA, "%1f %1f \n", ix*dx, A[ix]);
	 		fprintf(fichierQ, "%1f %1f \n", ix*dx, Q[ix]/amp);
	 		// fprintf(fichierQana, "%1f %1f \n", ix*dx, Qana[ix]/amp);
      		// fprintf(fichierC, "%1f %1f \n",A[ix], c[ix]);
        }
 		// saut de 2 lignes pour gnuplot
	    fprintf(fichierA,"\n \n");
		fprintf(fichierQ,"\n \n");
		// fprintf(fichierQana, "\n \n");
		// fprintf(fichierC, "\n \n");

	}	
//----------------------------------------------------------------------------------------------------------	
	// calcul de l'intégrale de Q, Qana...
	for (i=1;i<N;i++){
		integrale_ana+= integrale(Qana[i], Qana[i-1],amp,dx);
	}
	for (i=1;i<Nx;i++){
		integrale_Q+= integrale(Q[i], Q[i-1], amp, dx);
 	}

 	err = integrale_ana - integrale_Q;
//----------------------------------------------------------------------------------------------------------	
}
