import sys, getopt
import os
import numpy    as np
import math     as mt
import scipy    as sp

from bfS_libDef import *

from help_Input     import *

import  help_Output as out
import csv

from sklearn import metrics
import pathlib
import matplotlib.pyplot as plt

def main(argv) :    

    # -----------------------------------------------------
    # ---- PATH 
    hd = header()
    hd.headerInput(argv) ; 

    # LINUX
    HOME    = "/home/ventre/"
    PATH1D  = "Documents/Boulot/Thèse/code/bloodflow/bloodflow/Examples/Clamping/9Arteries-Saito/"
    PATHs   = "Documents/Boulot/Thèse/code/bloodflow/bloodflow/scripts/Clamping/9Arteries-Saito/"
    # # MAC 
    # HOME    = "/Users/jeanneventre/"
    # PATH1D  = "Documents/Boulot/Thèse/code/bloodflow/Examples/Clamping/9Arteries-Saito/"
    # PATHs   = "Documents/Boulot/Thèse/code/bloodflow/scripts/Clamping/9Arteries-Saito/"
    
    PATH = argv[1]
    # -----------------------------------------------------
    for pType in ["Q"] :

        pName,pLabel = out.getType(pType)

        # Time properties
        T_c     = 0.57 ;
        ts_c    = 10. * T_c ;
        te_c    = 12. * T_c ; 

        liX         = []
        liY         = []
        lFileSep    = []
        lFile       = []
        for i in [0.] :
            os.chdir(HOME)
            liX.append(0)
            liY.append([1,2,3])
            lFileSep.append(",")
            lFile.append( PATH + "Figures/" + "Artery_" + str(round(i)) + "_t_"  + pName )
            nplot = len(lFile)
            for j in range(0,nplot):
                Data = np.genfromtxt(lFile[j], delimiter = str(lFileSep[j]))
                dx = Data[10,0] - Data[9,0]
    
    Q = np.zeros(Data[:,1].shape)
    Q = Data[:,1]

    V = np.zeros(Q.shape)
    for i in range(0,V.shape[0]):
        V[i] = sp.integrate.trapz(Q[0:i], dx =dx)

    for pType in ["P"] :

        pName,pLabel = out.getType(pType)

        # Time properties
        T_c     = 0.57 ;
        ts_c    = 10. * T_c ;
        te_c    = 12. * T_c ; 

        liX         = []
        liY         = []
        lFileSep    = []
        lFile       = []
        for i in [0.] :
            os.chdir(HOME)
            liX.append(0)
            liY.append([1,2,3])
            lFileSep.append(",")
            lFile.append( PATH + "Figures/" + "Artery_" + str(round(i)) + "_t_"  + pName )
            nplot = len(lFile)
            for j in range(0,nplot):
                Data = np.genfromtxt(lFile[j], delimiter = str(lFileSep[j]))
            Data[:,0] = Data[:,0] - ts_c 
            # Data[:,0] = Data[:,0] - Data[50,0] ,  
            Data[:,[1,2,3]] = Data[:,[1,2,3]]*0.1*0.0075006375541921
            
    t = np.zeros(Data[:,0].shape)
    P = np.zeros(Data[:,1].shape)
    t = Data[:,0]
    P = Data[:,1]

    plt.plot(t,P)
    # plt.plot(t,Q)
    # plt.plot(t, V)
    # plt.plot(V,P)
    ax = plt.gca()
    ax.yaxis.set_tick_params(labelsize=12)
    ax.xaxis.set_tick_params(labelsize=12)
        
    # plt.plot(Data[:,0], Data[:,1], label = pName)
    
    plt.xlim([0,2*0.57])
    # plt.ylim([60,150])
    # plt.xlabel('time (s)', fontsize=12)
    # plt.ylabel('pressure (mmHg)',fontsize=12)
    # plt.text(0.4,95, "E = %d \n Rt = %.2f "%(float(E),float(Rt)), fontsize=14)
    # plt.legend(fontsize=12)
    # plt.title('Pre Clamp pressure in the right radial artery',fontsize=14)
    plt.show()

if __name__ == "__main__":
   main(sys.argv[1:])
