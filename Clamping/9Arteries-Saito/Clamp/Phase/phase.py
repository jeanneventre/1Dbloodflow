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

    State = "Clamp/Phase"

    PATH    = HOME + PATH1D + State + "/" + NN + "/" + Conj + "/nuv=" + nuv +  "/Q=" + Q + "/P1=" + P1 + "/R2=" + Rt2 + "/C=" + C + "/Nx=" + Nx + "/xOrder=" + xOrder + "/dt=" + dt + "/tOrder=" + tOrder + "/" + Solver + "/" + HR + "/"

    # -----------------------------------------------------
    # ---- PATIENT DATA
    t = np.linspace(0,0.62,num=63) 
    Pexp = np.array([66.93, 67.20,67.92,70.15,74.23,80.20,87.22,95.21,103.36,111.38,118.71,125.16,130.58,135.10,138.24,140.45,141.54,141.93,141.40,140.34,
                    138.58,136.65,134.35,132.01,129.30,126.66,123.57,120.17,116.40,112.29,107.91,103.56,99.15,95.13,91.39,88.17,85.34,82.92,80.80,79.15,
                    77.86,76.92,76.09,75.49,74.92,74.50,74.02,73.73,73.32,72.98,72.59,72.27,71.80,71.48,70.96,70.56,70.00,69.49,68.88,68.38,67.76,67.23,66.84])
    Pm = np.mean(Pexp)

    # -----------------------------------------------------
    for pType in ["P"] :

        pName,pLabel = out.getType(pType)

        # Time properties
        T_c     = 0.62 ;
        ts_c    = 10. * T_c ;
        te_c    = 12. * T_c ; 

        liX         = []
        liY         = []
        lFileSep    = []
        lFile       = []
        for i in [1.] :
            liX.append(0)
            liY.append([1,2,3])
            lFileSep.append(",")
            lFile.append(PATH + "Figures/" + "Artery_" + str(round(i)) + "_t_"  + pName )
            nplot = len(lFile)
            for j in range(0,nplot):
                Data = np.genfromtxt(lFile[j], delimiter = str(lFileSep[j]))
            Data[:,0] = Data[:,0] - ts_c 
            Data[:,[1,2,3]] = Data[:,[1,2,3]]*0.1*0.0075006375541921

            dx = Data[10,0] - Data[9,0]
            a =  sp.integrate.trapz(Data[:,3],axis=0, dx = dx)
            a = a/2;
            Data[:,0] = Data[:,0] - Data[70,0]  

    # -----------------------------------------------------
    # ---- CALCULATIONS
    D  = np.zeros(125)
    tt = np.zeros(125)
    
    for i in range(125):
        k = round(0.01/dx*i)
        # print(k)  
        D[i] = Data[int(k),3]
        tt[i] = Data[int(k),0]

    Dm = np.mean(D)
    
    R2   = metrics.r2_score(Pexp, D[8:71], multioutput ='uniform_average')

    # -----------------------------------------------------
    # ---- WRITE RESULTS IN FILES 
    os.chdir(HOME)
    integ = PATHs + State
    os.chdir(integ)
    fileName = 'mat.csv' 
    # if (float(Q) == 200)  and (float(P1) == 0.25):
    #     os.remove(fileName)

    fh = open(fileName, 'a')
    fh.write("%.20f \t"%(R2))
   
if __name__ == "__main__":
	main(sys.argv[1:])
