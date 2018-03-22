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
import matplotlib.pyplot as plt
from matplotlib import cm,colors

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
    Tej = np.array([0.25 ,0.3 ,0.35, 0.36, 0.38, 0.4, 0.42, 0.45, 0.48, 0.5, 0.52, 0.55])

    D = np.delete(Data,len(Tej),1)

    # R = np.array([1000, 2000 ,3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000]) 
    # C = np.array([1e-4, 5e-4, 1e-5, 5e-5, 1e-6])

    # D = np.delete(Data,len(C),1)
    # print(D.shape)
    # print(R.shape)
    # print(C.shape)

    X =  Tej 
    Y =  Q
    
    plt.figure()
    levels = np.linspace(-15,1,160)

    Cs = plt.contourf(X,Y,D,levels,cmap = cm.coolwarm,
    	color = ('r', 'g', 'b'),
    	origin = 'lower',
    	extend = 'both')
    Cs.cmap.set_under('blue')
    Cs.cmap.set_over('black')

    CS4 = plt.contour(X,Y, D, [-2,0,0.45],
                  colors=('k',),
                  linewidths=(3,),
                  origin='upper')
    plt.clabel(CS4, fmt='%2.1f', colors='w', fontsize=14)

    plt.title("Pre Clamp correlation coefficient R2",fontsize=14)

    plt.xlabel('$T_{ej}$ (% of heart beat)',fontsize=12)
    plt.ylabel('$Q_0$ (cm$^3$/s)',fontsize=12)
    plt.plot(0.5,300, 'k*',ms=12, label = "Pre Clamp optimum")
    # plt.plot(0.36,600, 'r*',ms=10, label = "Post Clamp optimum")
    plt.legend()
    plt.colorbar(Cs)
    plt.savefig('preclamp_phase_diagram_QTej.eps')
    plt.show()

if __name__ == "__main__":
	main(sys.argv[1:])
