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

	a = min(Data[:,3])
	b = min(Data[:,4])
	c = min(Data[:,5])
	d = min(Data[:,6])
	
	print('R2 : ', a)
	print('Linf :', b)
	print('L1 : ', c)
	print('L2 : ', d)
	
if __name__ == "__main__":
	main(sys.argv[1:])
