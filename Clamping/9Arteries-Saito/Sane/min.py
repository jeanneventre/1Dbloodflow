from help_Input     import *
import sys, getopt
import os
import numpy    as np
import math     as mt
import scipy    as sp

from bfS_libDef import *

from help_Input     import *

from help_Sum       import *
from help_Wave      import *
from help_Geometry  import *
from help_Inlet     import *
from help_Network   import *

import  help_Output as out
import csv

from scipy.interpolate import interp1d

import matplotlib.pyplot as plt

def main(argv) :

	HOME    = "/home/ventre/"
	PATHs   = "Documents/Boulot/Thèse/code/bloodflow/bloodflow/scripts/Clamping/9Arteries-Saito/"
	State   = "Sane/"

	integ = PATHs + State 

	liX         = []
	liY         = []
	lFileSep    = []
	lFile       = []

	os.chdir(HOME)
	liX.append(0)
	liY.append([1,2,3,4,5,6,7,8,9])
	lFileSep.append(",")
	lFile.append( PATHs + State + "res.csv") 
	nplot = len(lFile)
	for j in range(0,nplot):	
		Data = np.genfromtxt(lFile[j], delimiter =  str(lFileSep[j]))

	# -----------------------------------------------------
    # ---- CALCULATIONS 
	R2m   = max(Data[:,5])
	Linfm = min(Data[:,6])
	L1m   = min(Data[:,7])
	L2m   = min(Data[:,8])
	
	print('R2 : ', R2m)
	print('Linf :', Linfm)
	print('L1 : ', L1m)
	print('L2 : ', L2m)
	
	iR2m   = np.argmax(Data[:,5])
	iLinfm = np.argmin(Data[:,6])
	iL1m   = np.argmin(Data[:,7])
	iL2m   = np.argmin(Data[:,8])

	nuv = Data[iL2m,0]
	E   = Data[iL2m,1]
	Rt  = Data[iL2m,2]
	Q   = Data[iL2m,3]
	P1  = Data[iL2m,4]

	print("nu = ", nuv)
	print("E = ", E)
	print("Rt = ", Rt)
	print("Q = ",Q)
	print("P1 = ", P1)

	print('\n')
	print('\n')


if __name__ == "__main__":
	main(sys.argv[1:])
