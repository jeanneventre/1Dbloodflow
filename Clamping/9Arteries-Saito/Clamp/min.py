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
	# -----------------------------------------------------
    # ---- PATH 
	hd = header()
	hd.headerInput(argv) ; 

	# LINUX
	HOME    = "/home/ventre/"
	PATHs   = "Documents/Boulot/Thèse/code/bloodflow/bloodflow/scripts/Clamping/9Arteries-Saito/"
	State   = "Clamp"
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
	R2m   = min(Data[:,3])
	Linfm = min(Data[:,4])
	L1m   = min(Data[:,5])
	L2m   = min(Data[:,6])
	
	print('R2 : ', R2m)
	print('Linf :', Linfm)
	print('L1 : ', L1m)
	print('L2 : ', L2m)
	
	iR2m   = np.argmin(Data[:,3])
	iLinfm = np.argmin(Data[:,4])
	iL1m   = np.argmin(Data[:,5])
	iL2m   = np.argmin(Data[:,6])

	nuv = Data[iL1m,0]
	E   = Data[iL1m,1]
	Rt  = Data[iL1m,2]

	print("nu = ", nuv)
	print("E = ", E)
	print("Rt = ", Rt)



if __name__ == "__main__":
	main(sys.argv[1:])
