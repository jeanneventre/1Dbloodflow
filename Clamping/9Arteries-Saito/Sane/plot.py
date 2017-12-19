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

from sklearn import metrics
import matplotlib.pyplot as plt

def main(argv) :

    # -----------------------------------------------------
    # ---- PATH 
    hd = header()
    hd.headerInput(argv) ; 

    HOME    = "/home/ventre/"
    PATH1D  = "Documents/Boulot/Thèse/code/bloodflow/bloodflow/Examples/Clamping/9Arteries-Saito/"
    PATHs   = "Documents/Boulot/Thèse/code/bloodflow/bloodflow/scripts/Clamping/9Arteries-Saito/"

    Nx       = hd.Nxstr

    xOrder   = hd.xOrderstr

    dt       = hd.dtstr
    tOrder   = hd.tOrderstr

    NN       = hd.NNstr

    HR       = "HRQ"
    Solver   = "KIN_HAT"

    Conj     = "jS"

    nuv      = hd.Cvstr
    E        = hd.Kstr
    Rt       = hd.Rtstr

    State = "Sane"

    PATH    = PATH1D + State + "/" + NN + "/" + Conj + "/nuv=" + nuv + "/E=" + E + "/Rt=" + Rt + "/Nx=" + Nx + "/xOrder=" + xOrder + "/dt=" + dt + "/tOrder=" + tOrder + "/" + Solver + "/" + HR + "/"
    Store   = PATH1D + "Figures"
    # -----------------------------------------------------
    # ---- PATIENT DATA
    t = np.linspace(0,0.57,num=58) 

    Pexp = np.array([64.90,65.11, 66.11,  67.96,   70.70,   74.74,  79.48,  84.69,   89.68,  94.34,   98.26,   101.64,   104.42,   106.83,108.81,
    110.14,110.91,   111.09,    110.80,    109.90,    108.72,    107.52,    106.09,    104.51,    102.51,    100.20,97.44,    94.54,    91.50,    
    88.64,86.00,    83.69,    81.63,   79.91,    78.40,    77.17,   76.06,   75.23,   74.44,   73.83,   73.23,   72.63,   72.01,   71.47,   71.01,
    70.49,69.99,  69.52,   69.03,  68.58,   68.12,    67.70,    67.17,    66.70,    66.18,    65.71,    65.25,    64.88])
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
            Data[:,[1,2,3]] = Data[:,[1,2,3]]*0.1*0.0075006375541921

            dx = Data[10,0] - Data[9,0]
            a =  sp.integrate.trapz(Data[:,3],axis=0, dx = dx)
            a = a/2;
            Data[:,0] = Data[:,0] - Data[70,0]  
    # -----------------------------------------------------
    # ---- CALCULATIONS
    b = sp.integrate.trapz(Pexp, axis=0, dx=0.01)  

    D  = np.zeros(115)
    tt = np.zeros(115)

    for i in range(115):
        k = round(0.01/dx * i)
        D[i] = Data[int(k),3]
        tt[i] = Data[int(k),0]

    # R2 = np.sum((D[8:66] - np.mean(Q))**2)/ np.sum((Q - np.mean(Q))**2) 
    R2   = metrics.r2_score(Pexp, D[8:66], multioutput ='uniform_average')
    Linf = max(abs(Pexp-D[8:66]))/max(abs(Pexp))
    L1   = sp.integrate.trapz(abs(Pexp-D[8:66]), dx = 0.01)/sp.integrate.trapz(abs(Pexp), dx=0.01) 
    L2   = np.sqrt(sp.integrate.trapz((Pexp-D[8:66])**2, dx=0.01))/np.sqrt(sp.integrate.trapz(Pexp**2,dx=0.01))
    # -----------------------------------------------------
    # ---- WRITE RESULTS IN FILES 
    os.chdir(HOME)
    integ = PATHs + State
    os.chdir(integ)
    fileName = 'res.csv' 

    if (float(nuv) == 5e4) and (float(E) == 0.4e7) and(float(Rt) == 0.5):
        os.remove(fileName)
        # fh = open(fileName, 'w')
        # fh.write(" nuv, \t E, \t Rt, \t a,\t b, \t (a-b) \t \n")

    fh = open(fileName, 'a')
    fh.write("%.20f, \t %20f, \t %.20f, \t %.20f, \t %.20f, \t %.20f,  \t %.20f"%(float(nuv),float(E),float(Rt), R2, Linf, L1,L2) + "\n")
    # -----------------------------------------------------
    # ---- PLOT RESULTS
    # plt.plot(Data[:,0], Data[:,3])
    plt.plot(t,Pexp,label='Experimental')
    plt.plot(tt[8:66],D[8:66],label='Simulated')
    # plt.xlim([-0.1,2*0.57])
    plt.legend()
    plt.show()
if __name__ == "__main__":
	main(sys.argv[1:])
