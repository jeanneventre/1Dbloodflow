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
	int Nx = 200;
	double dx = L/Nx;

	double t=0.;
	double dt = 1e-5;
	int Nt = 800;

	double omega = 1.;
	double amp =1.5;

	double A[Nx];
	double Q[Nx];
	double P[Nx];
	double Qana[Nx];
	double fa[Nx],fq[Nx];

	double R=0.005;
	double K= 1e3;
	double c=1;

	// void kurganov (double Am, double Ap, double Qm, double Qp,double * fa, double * fq);
	// void rusanov (double/ Am, double Ap, double Qm, double Qp,double * fa, double * fq);
	void rusanov2 (double Am, double Ap, double Qm, double Qp,double * fa, double * fq);
	// void rusanov_Varga (double Am, double Ap, double Qm, double Qp,double * fa, double * fq);
	// void rusanov_Varga2(double Am, double Ap, double Qm, double Qp,double * fa, double * fq);
	// void rusanov_NeoHooke(double Am, double Ap, double Qm, double Qp,double * fa, double * fq);

	// iniital conditions
	for(ix=0; ix<Nx; ix++){
		A[ix]=1.; 
		Q[ix]=0.;
		Qana[ix]=0.;
	}

    int result = mkdir("output", 0777);

 //    FILE *fichierA =fopen("output/A_elastic1_amp0_0001.txt", "w");
	// FILE *fichierQ =fopen("output/Q_elastic1_amp0_0001.txt", "w");
	// FILE *fichierQana =fopen("output/Qana1.txt", "w");

	int i=0;
	double integrale, integrale2;	
	double err;
	FILE *f_err=fopen("output/err_amp2.txt", "w");
	int k=0;
// while(k<3){
// 	amp = amplitude[k];
	for (j=0; j< 101; j++){
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
				rusanov(A[ix-1],A[ix],Q[ix-1], Q[ix],&fa[ix],&fq[ix]);
			}
			for (ix=1; ix<Nx-1; ix++){
				A[ix] = A[ix] + dt/dx *(fa[ix] - fa[ix+1]) ;
				Q[ix] = Q[ix] + dt/dx *(fq[ix] - fq[ix+1])  - dt*e2 * Q[ix]/A[ix];
 			}
 			for (ix=0; ix<Nx;ix++){
 				Qana[ix]= amp * fmax(0,-sin(2*3.1415*(omega*ix*dx-omega*t)))*exp(-0.05 *ix*dx);
 			}
 		}

 	// 	// ecriture dans des fichiers texte :
	 // 	for(ix=0;ix<Nx;ix++) {  
	 // 		fprintf(fichierA, "%1f %1f \n", ix*dx, A[ix]);
	 // 		fprintf(fichierQ, "%1f %1f \n", ix*dx, Q[ix]/amp);
	 // 		fprintf(fichierQana, "%1f %1f \n", ix*dx, Qana[ix]/amp);
  //     	}
 	// 	// 
 	// 	// saut de 2 lignes pour gnuplot
	 //    fprintf(fichierA,"\n \n");
		// fprintf(fichierQ,"\n \n");
		// fprintf(fichierQana, "\n \n");
 	// 	//
	}

	integrale=0.;
	integrale2=0.;

	for (i=1;i<126;i++){
		integrale += (Qana[i]/amp+Qana[i-1]/amp)/2 * dx;
	}

	for (i=1;i<126;i++){
		integrale2+= (Q[i]/amp+Q[i-1]/amp)/2 * dx;
 	}

 	err = integrale2 - integrale;

	printf("%1f %1f ",amp,integrale );
	printf("%1f %1f \n", integrale2, err);

		
 	// fprintf(f_err, "%1f %1f  \n",amp, integrale2);
// k++;
// }
} // fin main 
