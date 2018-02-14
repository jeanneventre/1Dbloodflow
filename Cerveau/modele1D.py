import sys, getopt
import os
import numpy    as np
import math     as mp
from pylab import *
from help_Sum       import *

def mmHg_to_Pa(P):
	return P * 133.322
def Pa_to_mmHg(P):
	return P * 0.0075006375541921
def Pa_to_CGS(P):
	return 10 * P

def Jv (Lp, S, P_F, P_T):
	return Lp * S * (P_F - P_T) 

def P_F (E,V,V0):
	return E * (V/V0)

def SinInput(t,alpha):
    return np.sin(np.pi * t/alpha)*(t<alpha)

def main(argv):

	# time
	N        = 60000
	t_s      = 0
	t_e      = 10
	t        = np.linspace(t_s,t_e,N)
	dt       = (t_e - t_s)/N

	def Qf (t,T, Q0):
		return Q0 * sin(2*np.pi *t/T)

	Q_pulse= np.zeros(N)
	Amp = 0.006*7
	for i in range(N): 
		Q_pulse[i]= Qf(t[i],1,Amp) + 0.006

	print(integrate(t,Q_pulse))

	Q_m =  0.006 *np.ones(N) # ml/min

	K = 1 # ml 
	Rout = 7.5 # mmHg/ml/min

	Pr = 30 # mmHg
	Pd = Pr - Q_pulse[0] / Rout # mmHg

	P = np.zeros(N)
	P[0] = 8

	for i in range(N-1):
		P[i+1] = P[i] + dt * K * (P[i] * Q_pulse[i]  - P[i] * (P[i] - Pd) /Rout)

	Pic = np.zeros(N)
	Pp = P[0]

	for i in range(N):
		Pic[i] = Pp * exp(K*t[i]*Pr/Rout)/(1+Pp/Pr * (exp(K*t[i]*Pr/Rout)-1))

	plot(t,Pic, label='theorique')
	plot(t,P,label='numerique')
	legend()
	show()

if __name__ == '__main__':
	main(sys.argv[1:])


	# def f(t,V, T, Tej, Lp, S,E,V0,P_T): 
	# 	return SinInput(t/T - int(t/T), Tej) - Jv(Lp,S,P_F(E,V,V0),P_T)


	# for i in range(0,N-1):
	# 	k1 = f(t[i],V[i], T, Tej, Lp, S,E,V0,P_T);
	# 	k2 = f(t[i]+dt/2, V[i] + k1 *dt/2, T, Tej, Lp, S,E,V0,P_T)
	# 	k3 = f(t[i]+dt/2, V[i] + k2*dt/2, T, Tej, Lp, S,E,V0,P_T)
	# 	k4 = f(t[i]+dt, V[i] + k3 *dt, T, Tej, Lp, S,E,V0,P_T)
	# 	V[i+1] = V[i] + (k1 + 2 *k2 + 2*k3 + k4) *dt/6