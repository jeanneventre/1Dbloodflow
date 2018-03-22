import sys, getopt
import os
import numpy    as np
import math     as mt
import scipy    as sp

from bfS_libDef import *
from help_Input     import *
from help_Sum       import *
import  help_Output as out
import csv

from sklearn import metrics
import pathlib

from matplotlib import colors, cm
import matplotlib.pyplot as plt

def main(argv) :
 
    liX         = []
    liY         = []
    lFileSep    = []
    lFile       = []

    liX.append(1)
    liY.append([1,2,3,4,5,6,7])
    lFileSep.append(" ")
    lFile.append("mat.csv" )
    nplot = len(lFile)
    for j in range(0,nplot):
        Data = np.genfromtxt(lFile[j], delimiter = str(lFileSep[j]))

    Q = np.array([200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700])    
    Tej = np.array([0.25, 0.3 ,0.35, 0.36, 0.38, 0.4, 0.42, 0.45, 0.48, 0.5, 0.52, 0.55])

    print(len(Tej))
    print(len(Q))

    D = np.delete(Data,len(Tej),1)

    plt.figure()
    levels = np.linspace(-4,1,80)

    C = plt.contourf(Tej,Q,D,levels, cmap = cm.coolwarm,
    	color = ('r', 'g', 'b'),
    	origin = 'lower',
    	extend = 'both')
    C.cmap.set_under('blue')
    C.cmap.set_over('black')

    CS4 = plt.contour(Tej, Q, D, [-1.5,-0.5,0,0.5,0.9],
                  colors=('black',),
                  linewidths=(3,),
                  origin='upper')
    plt.clabel(CS4, fmt='%2.1f', colors='w', fontsize=14)

    plt.title("Post Clamp correlation coefficient R2",fontsize=14)

    plt.xlabel('$T_{ej}$ (% of heart beat)',fontsize=12)
    plt.ylabel('$Q_0$ (cm$^3$/s)',fontsize=12)
    plt.plot(0.36,600, 'k*',label ='post clamp optimum',ms = 14)

    plt.legend()
    plt.colorbar(C)
    plt.savefig('postclamp_phase_diagram.eps')
    plt.show()

if __name__ == "__main__":
	main(sys.argv[1:])
