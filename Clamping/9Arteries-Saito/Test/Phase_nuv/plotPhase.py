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

    nuv = np.array([5e4,10e4,15e4,20e4,25e4,30e4,35e4])  

    R = np.array([1000,2000,3000, 4000,5000,6000,7000,8000,9000,10000])

    D = np.delete(Data,len(R),1)

    X =  R 
    Y =  nuv
    
    plt.figure()
    levels = np.linspace(-9,1,110)

    Cs = plt.contourf(X,Y,D,levels,cmap = cm.coolwarm,
    	color = ('r', 'g', 'b'),
    	origin = 'lower',
    	extend = 'both')
    Cs.cmap.set_under('blue')
    Cs.cmap.set_over('black')

    CS4 = plt.contour(X,Y, D, [-5,0,0.5],
                  colors=('k',),
                  linewidths=(3,),
                  origin='upper')
    plt.clabel(CS4, fmt='%2.1f', colors='w', fontsize=14)

    plt.title("Pre Clamp correlation coefficient R2",fontsize=14)

    plt.xlabel('$R_2$ (g.cm$^{-4}$.s$^{-1}$)',fontsize=12)
    plt.ylabel('$C_v$ ',fontsize=12)
    plt.plot(5000,31e4, 'k*',ms=12, label = "Pre Clamp optimum")
    # plt.plot(1750,5e4, 'r*',ms=10, label = "Post Clamp optimum")
    plt.legend()
    plt.colorbar(Cs)
    plt.savefig('preclamp_phase_diagram_nuv.eps')
    plt.show()

if __name__ == "__main__":
	main(sys.argv[1:])
