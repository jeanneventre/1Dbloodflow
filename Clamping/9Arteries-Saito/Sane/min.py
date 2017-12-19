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
	liY.append([1,2,3,4,5])
	lFileSep.append(",")
	lFile.append( PATHs + State + "integrale.csv")
	nplot = len(lFile)
	for j in range(0,nplot):	
		Data = np.genfromtxt(lFile[j], delimiter =  str(lFileSep[j]))

	a = min(Data[:,5])
	print(a)

if __name__ == "__main__":
	main(sys.argv[1:])
