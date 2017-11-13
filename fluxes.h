#include "stdio.h"
#include "stdlib.h"
#include "math.h"
#define sq(x) x*x

double e1= 0.5;
double e2= 0.1;

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
 	double e4 = K/rho; 

 	double cp = sqrt(e1*sqrt(Ap) + e1 /sqrt(Ap)), cm = sqrt(e1 *sqrt(Am) + e1/ sqrt(Am));
	double a = fmax(fabs(cp), fabs(cm));
	
	*fa = (Qm + Qp)/2. - a * (Ap - Am)/2.;
	*fq = (sq(Qm)/Am + e3*pow(Am, 3./2.)+ e4* sqrt(Am) + sq(Qp)/Ap + e3*pow(Ap, 3./2.) +e4 * sqrt(Ap))/2. - a * (Qp - Qm)/2.;
}

void rusanov_Varga2 (double Am, double Ap, double Qm, double Qp, double *fa, double *fq)
{
	// p = K/A (sqrt(A/A0) - sqrt(A0/A))
	double um = Qm/Am;
	double up = Qp/Ap;

	double cp = sqrt(e1 * (3.*pow(Ap,-3./2.) - 1./sqrt(Ap))), cm = sqrt(e1 * (3.*pow(Am,-3./2.) - 1./sqrt(Am)));
	double a = fmax(fabs(cp), fabs(cm));

	*fa = (Qm + Qp)/2. - a * (Ap - Am)/2.;
	*fq = (sq(Qm)/Am - 2.*e1*sqrt(Am) - 6.*e1/sqrt(Am) + sq(Qp)/Ap -2.* e1* sqrt(Ap) -6* e1/sqrt(Ap))/2. - a * (Qp - Qm)/2.;
}

void rusanov_NeoHooke (double Am, double Ap, double Qm, double Qp, double * fa, double *fq)
{
	// p = K/2 *(1 - (A/A0)²)
	
	double um = Qm/Am;
	double up = Qp/Ap;
	double cp = sqrt(2.*e1/(Ap*Ap)), cm = sqrt(2.*e1/(Am*Am));
	double a = fmax(fabs(cp), fabs(cm));

	*fa = (Qm + Qp)/2. - a * (Ap - Am)/2.;
	*fq = (sq(Qm)/Am -2.*e1/Am + sq(Qp)/Ap -2.*e1/Ap)/2. - a * (Qp - Qm)/2.;
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