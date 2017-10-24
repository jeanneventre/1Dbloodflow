#include "stdio.h"
#include "stdlib.h"
#include "math.h"
#define e1 0.1
#define e2 1
#define sq(x) x*x

void rusanov (double Am, double Ap, double Qm, double Qp,
      double * fa, double * fq)
{
double um = Qm/Am;
 double up = Qp/Ap;
 double cp = sqrt(2.*e1*Ap), cm = sqrt(2.*e1*Am);
 double a = fmax(fabs(cp), fabs(cm));

 *fa = (Qm + Qp)/2. - a * (Ap - Am)/2.;
 *fq = (sq(Qm)/Am + e1*sq(Am) + sq(Qp)/Ap + e1*sq(Ap) )/2. - a * (Qp - Qm)/2.;
}

void kurganov (double Am, double Ap, double Qm, double Qp,
      double * fa, double * fq)
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
   *fq = (ap*(qm*um + e1*sq(Am)) - am*(qp*up + e1*sq(Ap)) +
  ap*am*(qp - qm))/(ap - am);
 }
 else
   {
     
     *fa = *fq = 0.;
     
   }
}

int main(){

	int i=0, it=0, ix=0;

	double L = 5.;
	int Nt = 2000;
	int Nx = 100;
	double T = 1e-2;
	double dt = 1./Nt; 
	double dx = L/Nx;

	double A[Nt][Nx];
	double Q[Nt][Nx];
	double S[Nt][Nx];
	double fa[Nx],fq[Nx];

	double tt[Nt];
	for (it=0;it<Nt;it++){
		tt[it] = it * dt;
	}

	// resolution loop 
	for (it=1; it<Nt;it++){

		// boundary conditions x=0
		Q[it][0]=fmax(0,sin(tt[it]/T)); // Q at x=0
		if (it>1/T){Q[it][0]=0.;}
		A[it][0]=1.;// A at x=0
		S[it][0]=e2 * Q[it][0]/A[it][0];	
		// S[it][Nx]=e2 * Q[it][Nx]/A[it][Nx];	
		
		// space loop
		for (ix=1; ix<Nx; ix++){
			
			// initial conditions
			A[0][ix]=1.; // A at t=0
			Q[0][ix]=0.; // Q at t=0
			S[0][ix]=e2 * Q[0][ix]/A[0][ix];

			// resolution
			rusanov(A[it-1][ix-1],A[it-1][ix],Q[it-1][ix-1], Q[it-1][ix],&fa[ix],&fq[ix]);
			A[it][ix] = A[it-1][ix] + dt/dx *(fa[ix-1] - fa[ix]) ;
			Q[it][ix] = Q[it-1][ix] + dt/dx *(fq[ix-1] - fq[ix])  - dt*S[it-1][ix];
			S[it][ix] = e2 * Q[it][ix]/A[it][ix];
 		}
 		//
 	}

 	// FILE *fichierA =fopen("A.txt", "w");

 	// if (fichierA != NULL) 
 	// {
 	// 	//for (ix=0; ix<Nx; ix++){
 	// 		for (it=0; it<Nt;it++){
 	// 			fprintf(fichierA, "%1f \n", A[it][Nx]);
 	// 		}
 	// 	//	fprintf(fichierA, "\n");
 	// 	//}
 	// }

 	// fclose(fichierA);

 	FILE *fichierQ =fopen("Q.txt", "w");

 	if (fichierQ != NULL) 
 	{	
 		// int N = Nt;
 		//for (ix=0; ix<Nx; ix++){
 			for (it=0; it<Nt;it++){
 				fprintf(fichierQ, "%1f \n", Q[it][1]);
 			}
 			//fprintf(fichierQ, "\n");
 		//}
 	}

 	fclose(fichierQ);


}