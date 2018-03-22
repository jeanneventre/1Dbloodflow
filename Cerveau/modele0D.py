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

def SinInput(t,alpha):
    return np.sin(np.pi * t/alpha)*(t<alpha)

def Sine(t,T, Q0,C):
		return Q0 * sin(2*np.pi *t/T) + C

def main(argv):

	#############
	# time
	#############
	N        = 60000
	t_s      = 0
	t_e      = 10
	t        = np.linspace(t_s,t_e,N)
	dt       = (t_e - t_s)/N
	
	#############
	# Production
	#############
	Amp      = 0.006*7
	C        = 0.006
	T        = 1
	Q_cst    = C * np.ones(N)
	Q_pulse  = np.zeros(N)

	for i in range(N): 
		Q_pulse[i] = Sine(t[i],T,Amp,C)

	#############
	K        = 0.5 # ml 
	Pr       = 30 # mmHg
	
	#############
	# Absorption 
	#############
	Rout     = 7.5 # mmHg/ml/min
	Pd       = Pr - Q_pulse[0] * Rout # mmHg

	#############
	# Pression intracranienne 
	#############
	P        = np.zeros(N)
	P[0]     = 8 # mmHg

		# Euler explicite
	for i in range(N-1):
		P[i+1] = P[i] + dt * K * (P[i] * Q_pulse[i]  - P[i] * (P[i] - Pd) /Rout)

		# Runge Kutta 4 
	def f(t,P,K,T,Amp,Pd,Rout):
		return K * P * (Sine(t,T,Amp,C) - (P - Pd)/Rout)

	PRK4     = np.zeros(N)
	PRK4[0]  = 8

	for i in range(0,N-1):
		k1 = f(t[i],PRK4[i],K,T,Amp,Pd,Rout);
		k2 = f(t[i]+dt/2, PRK4[i] + k1 *dt/2,K,T,Amp,Pd,Rout)
		k3 = f(t[i]+dt/2, PRK4[i] + k2*dt/2,K,T,Amp,Pd,Rout)
		k4 = f(t[i]+dt, PRK4[i] + k3 *dt,K,T,Amp,Pd,Rout)
		PRK4[i+1] = PRK4[i] + (k1 + 2 *k2 + 2*k3 + k4) *dt/6

	
	#############
	# Pathologie 
	#############
	Qinf     = 0.025
	Q_ex     = Qinf * np.ones(N)
	V_ex     = integrate(t,Q_ex)

	P        = np.zeros(N)
	P[0]     = 8 # mmHg

	for i in range(N-1):
		P[i+1] = P[i] + dt * K * (P[i] * (Q_pulse[i]+Q_ex[i])  - P[i] * (P[i] - Pd) /Rout)

	#############
	# Théorie
	#############

		# saine
	Pic      = np.zeros(N)
	Pp       = P[0]

	for i in range(N):
		Pic[i] = Pp * exp(K*t[i]*Pr/Rout)/(1+Pp/Pr * (exp(K*t[i]*Pr/Rout)-1))


		# pathologique 
	Pth      = np.zeros(N)
	Pth[0]   = 8

	for i in range(N):
		Pth[i] = Pr * (Pr + Rout * Qinf)/(Pr + Rout * Qinf * exp(-K/Rout * (Pr + Rout * Qinf)*t[i]))

	#############
	# figures 
	#############

	# plot(t,P,'r',lw = 2, label='Sane')
	# plot(t[0:N:2000],Pic[0:N:2000],'kx',ms=7,mew = 2, label='Theoretical')
	# xlabel('time (s)')
	# ylabel ('Intracranial pressure (mmHg)')
	# title ('Comparison between analytical and numerical solution for ICP')
	# plot(t,PRK4,'b--', label = 'RK4')
	# plot(t, Pth)
	# figure()
	# plot(t,P,'b',lw = 2, label='Pathological')

	# savefig('icp_constant.eps')
	legend()
	show()



if __name__ == '__main__':
	main(sys.argv[1:])


	