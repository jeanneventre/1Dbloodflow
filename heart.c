#include "stdio.h"
#include "stdlib.h"
#include "math.h"

void elastance_ventricule_left(double t, double * E)
{	
	double tvr= 0.3;
	double Tvrp = 0.15;
	double T0 = 1.;
	double tvc= 0.;
	double Tvcp= 0.3;

	double plv = 9.3 ;
	double S = 0.0005 * plv;

	double e;

	if(t>=0) && (t<= Tvcp)
	{
		e = 0.5 * (1-cos(3.1415*t/Tvcp));
	}
	else if (t> Tvcp) && (t<= Tvcp +Tvrp)
	{
		e =0.5*(1+cos(3.1415 *(t-Tvcp)/Tvrp));
	}
	else 
	{
		e = 0.;
	}

	double Ea = 2.75;
	double Eb = 0.08; 

	* E = Ea * e + Eb
}

// void elastance_ventricule_right(double t, double * E)
// {	
// 	double tvr= 0.3;
// 	double Tvrp = 0.15;
// 	double T0 = 1.;
// 	double tvc= 0.;
// 	double Tvcp= 0.3;

// 	double prv = 6.3;
// 	double S = 0.0005 * prv;

// 	double e; 

// 	if(t>=0) && (t<= Tvcp)
// 	{
// 		e = 0.5 * (1-cos(3.1415*t/Tvcp));
// 	}
// 	else if (t> Tvcp) && (t<= Tvcp +Tvrp)
// 	{
// 		e = 0.5*(1+cos(3.1415 *(t-Tvcp)/Tvrp));
// 	}
// 	else 
// 	{
// 		e = 0.;
// 	}

// 	double Ea = 0.55;
// 	double Eb = 0.05;

// 	* Evr = Ea * e + Eb
// }

// void elastance_atrium_left(double t, double * E)
// {
// 	double tar= 0.97;
// 	double Tarp = 0.17;
// 	double T0 = 1.;
// 	double tac= 0.8;
// 	double Tacp= 0.17;

// 	double pla = 8.1;
// 	double S = 0.0005 * pla;

// 	double e;

// 	if(t>=0) && (t<=tar + Tarp -T0)
// 	{
// 		e = 0.5 * (1+cos(3.1415*(t+t0-tar)/Tarp));
// 	}
// 	else if (t> tar+Tarp-T0) && (t<= tac)
// 	{
// 		e = 0.;
// 	}
// 	else if (t>tac) && (t<= tac+Tacp)
// 	{
// 		e = 0.5 * cos(3.1415 *(t-tac)/Tacp);
// 	}
// 	else 
// 	{
// 		e = 0.5 * cos(3.1415 * (t-tar)/Tarp)
// 	}

// 	double Ea = 0.07;
// 	double Eb = 0.09;

// 	* E = Ea * e + Eb
// }


// void elastance_atrium_right(double t, double * E)
// {
// 	double tar= 0.97;
// 	double Tarp = 0.17;
// 	double T0 = 1.;
// 	double tac= 0.8;
// 	double Tacp= 0.17;

// 	double pra = 5.3;
// 	double S = 0.0005 * pra;

// 	double e;

// 	if(t>=0) && (t<=tar + Tarp -T0)
// 	{
// 		e = 0.5 * (1+cos(3.1415*(t+t0-tar)/Tarp));
// 	}
// 	else if (t> tar+Tarp-T0) && (t<= tac)
// 	{
// 		e = 0.;
// 	}
// 	else if (t>tac) && (t<= tac+Tacp)
// 	{
// 		e = 0.5 * cos(3.1415 *(t-tac)/Tacp);
// 	}
// 	else 
// 	{
// 		e =0.5 * cos(3.1415 * (t-tar)/Tarp)
// 	}

// 	double Ea = 0.06;
// 	double Eb = 0.07;

// 	* E = Ea * e + Eb
// }

int main()
{



}
