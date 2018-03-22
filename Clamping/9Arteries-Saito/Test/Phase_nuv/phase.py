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

def main(argv) :

    # -----------------------------------------------------
    # ---- PATH 
    hd = header()
    hd.headerInput(argv) ; 

    HOME    = "/home/ventre/"
    PATH1D  = "Documents/Boulot/Thèse/code/bloodflow/bloodflow/Examples/Clamping/9Arteries-Saito/"
    PATHs   = "Documents/Boulot/Thèse/code/bloodflow/bloodflow/scripts/Clamping/9Arteries-Saito/"
    # # MAC 
    # HOME    = "/Users/jeanneventre/"
    # PATH1D  = "Documents/Boulot/Thèse/code/bloodflow/Examples/Clamping/9Arteries-Saito/"
    # PATHs   = "Documents/Boulot/Thèse/code/bloodflow/scripts/Clamping/9Arteries-Saito/"

    Nx       = hd.Nxstr

    xOrder   = hd.xOrderstr

    dt       = hd.dtstr
    tOrder   = hd.tOrderstr

    NN       = hd.NNstr

    HR       = "HRQ"
    Solver   = "KIN_HAT"

    Conj     = "jS"

    nuv      = hd.Cvstr
    Rt       = hd.Rtstr
    C        = hd.Cstr
    Q        = hd.Qstr
    P1       = hd.P1
    Rt2      = hd.P2   

    State = "Test/Phase_nuv"

    PATH = HOME + PATH1D + State + "/" + NN + "/" + Conj + "/nuv=" + nuv +  "/Q=" + Q + "/P1=" + P1 + "/R2=" + Rt2 + "/C=" + C + "/Nx=" + Nx + "/xOrder=" + xOrder + "/dt=" + dt + "/tOrder=" + tOrder + "/" + Solver + "/" + HR + "/"

    # -----------------------------------------------------
    # ---- PATIENT DATA
    t = np.linspace(0,0.57,num=58) 

    Pexp = np.array([63.90,65.11, 66.11,  67.96,   70.70,   74.74,  79.48,  84.69,   89.68,  94.34,   98.26,   101.63,   104.42,   106.83,108.81,
    110.14,110.91,   111.09,    110.80,    109.90,    108.72,    107.52,    106.09,    104.51,    102.51,    100.20,97.44,    94.54,    91.50,    
    88.63,86.00,    83.69,    81.63,   79.91,    78.40,    77.17,   76.06,   75.23,   74.44,   73.83,   73.23,   72.63,   72.01,   71.47,   71.01,
    70.49,69.99,  69.52,   69.03,  68.58,   68.12,    67.70,    67.17,    66.70,    66.18,    65.71,    65.25,    63.88])
    # -----------------------------------------------------
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
        for i in [1.] :
            os.chdir(HOME)
            liX.append(0)
            liY.append([1,2,3])
            lFileSep.append(",")
            lFile.append( PATH + "Figures/" + "Artery_" + str(round(i)) + "_t_"  + pName )
            nplot = len(lFile)
            for j in range(0,nplot):
                Data = np.genfromtxt(lFile[j], delimiter = str(lFileSep[j]))
            Data[:,0] = Data[:,0] - ts_c 
            dx = Data[10,0] - Data[9,0]
            Data[:,[1,2,3]] = Data[:,[1,2,3]]*0.1*0.0075006375541921
    # -----------------------------------------------------
    # ---- CALCULATIONS
    D  = np.zeros(58)
    tt = np.zeros(58)

    k=0
    for i in range(0,58):
        k = round(0.01/dx * i)      
        D[i] = Data[int(k),3]
        tt[i] = Data[int(k),0]

    R2   = metrics.r2_score(Pexp, D, multioutput ='uniform_average')
    # -----------------------------------------------------
    # ---- WRITE RESULTS IN FILES 
    os.chdir(HOME)
    integ = PATHs + State
    os.chdir(integ)
    fileName = 'mat.csv' 
    if (float(nuv)== 5e4) and (float(Q) == 300)  and (float(P1) == 0.45) and (float(Rt2)== 1000) and (float(C)==1e-4):
        os.remove(fileName)

    fh = open(fileName, 'a')
    fh.write("%.20f \t"%(R2))
   
if __name__ == "__main__":
	main(sys.argv[1:])
