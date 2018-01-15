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
	State   = "Test/"

	integ = PATHs + State 

	liX         = []
	liY         = []
	lFileSep    = []
	lFile       = []

	os.chdir(HOME)
	liX.append(0)
	liY.append([1,2,3,4,5,6])
	lFileSep.append(",")
	lFile.append( PATHs + State + "res.csv") 
	nplot = len(lFile)
	for j in range(0,nplot):	
		Data = np.genfromtxt(lFile[j], delimiter =  str(lFileSep[j]))

	# -----------------------------------------------------
    # ---- CALCULATIONS 
	R2m   = max(Data[:,2])
	Linfm = min(Data[:,3])
	L1m   = min(Data[:,4])
	L2m   = min(Data[:,5])
	
	print('R2 : ', R2m)
	print('Linf :', Linfm)
	print('L1 : ', L1m)
	print('L2 : ', L2m)
	
	iR2m   = np.argmax(Data[:,2])
	iLinfm = np.argmin(Data[:,3])
	iL1m   = np.argmin(Data[:,4])
	iL2m   = np.argmin(Data[:,5])

	Rt  = Data[iL2m,0]
	C   = Data[iL2m,1]

	print('R = ', Rt)
	print('C =', C)

	print('\n')
	print('\n')


if __name__ == "__main__":
	main(sys.argv[1:])
