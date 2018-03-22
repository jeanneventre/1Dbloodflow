import sys, getopt
import os
from scipy import integrate,optimize
import numpy    as np
import math     as mt
from pylab import *
from windkessel import *

def main(argv)	: 

	HOME    = "/home/ventre/"
	PATH    = "Documents/Boulot/Thèse/Argentine/"
	Code    = "Codes/"
	Data    = "Patient2015/Data/"
	Res     = "Resultats"
	Fig     = "Figures"

	direc_fig = HOME + PATH + Code + Fig
	direc_res = HOME + PATH + Code + Res
	direc_data = HOME + PATH + Code + Data

	State 	= 'pre'
	nPatient = 6

	P = donnees_tot(State,nPatient,direc_data)

	
	# T = np.array([0.57, 1.71,2.83,3.96,5.22,6.46,7.7,8.93])

	T_end = 19.26
	timeSteps = len(P)
	t = np.linspace(0,T_end,num=timeSteps) 
	plot(t,P)
	tf = np.fft
	freq = tf.fftfreq(timeSteps,t[2]-t[1])
	sp = np.fft.fft(P)

	for i in range(0,timeSteps):
		if (freq[i]<0.7) & (freq[i]>0.05) |  (freq[i]<-0.05) & (freq[i]>-0.7) : 
			sp.real[i] = 0
			sp.imag[i] = 0

	# plot(freq,abs(sp))

	Pp = np.fft.ifft(sp)

	plot(t,Pp)

	# [<matplotlib.lines.Line2D object at 0x...>, <matplotlib.lines.Line2D object at 0x...>]
	show()

if __name__ == "__main__":
	main(sys.argv[1:])
