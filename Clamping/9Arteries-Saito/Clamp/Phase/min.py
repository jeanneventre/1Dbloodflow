from help_Input     import *
import sys, getopt
import os
import numpy    as np
import math     as mt

from bfS_libDef import *

from help_Input     import *

from help_Sum       import *
from help_Inlet     import *

import  help_Output as out
import csv

from scipy.interpolate import interp1d

def main(argv) :
	# -----------------------------------------------------
    # ---- PATH 
	hd = header()
	hd.headerInput(argv) ; 

	# LINUX
	HOME    = "/home/ventre/"
	PATHs   = "Documents/Boulot/Thèse/code/bloodflow/bloodflow/scripts/Clamping/9Arteries-Saito/"
	State   = "Clamp/Phase"
	# # MAC 
 	# HOME    = "/Users/jeanneventre/"
	# PATHs   = "Documents/Boulot/Thèse/code/bloodflow/scripts/Clamping/9Arteries-Saito/"

	integ = PATHs + State 
	# -----------------------------------------------------
    # ---- READ RESULTS IN FILES 
	liX         = []
	liY         = []
	lFileSep    = []
	lFile       = []

	os.chdir(HOME)
	liX.append(0)
	liY.append([1,2,3,4,5,6,7,8,9])
	lFileSep.append(",")
	lFile.append( PATHs + State + "/" + "res.csv")
	nplot = len(lFile)
	for j in range(0,nplot):	
		Data = np.genfromtxt(lFile[j], delimiter =  str(lFileSep[j]))

	# -----------------------------------------------------
    # ---- CALCULATIONS 
	rows = Data.shape[0]
	cols = Data.shape[1]

	R2m   = max(Data[:,cols-4])
	Linfm = min(Data[:,cols-3])
	L1m   = min(Data[:,cols-2])
	L2m   = min(Data[:,cols-1])
	
	print('R2 : ', R2m)
	print('Linf :', Linfm)
	print('L1 : ', L1m)
	print('L2 : ', L2m)
	
	iR2m   = np.argmin(Data[:,cols-4])
	iLinfm = np.argmin(Data[:,cols-3])
	iL1m   = np.argmin(Data[:,cols-2])
	iL2m   = np.argmin(Data[:,cols-1])

	Q     = Data[iL2m,0]
	Tej   = Data[iL2m,1]
	Rt2   = Data[iL2m,2]
	C     = Data[iL2m,3]
	print('Q    = ', Q)
	print('Tej  = ', Tej)
	print('R2   = ', Rt2)
	print('C    = ', C)

if __name__ == "__main__":
	main(sys.argv[1:])
