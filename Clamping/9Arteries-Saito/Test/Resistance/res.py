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
import pathlib
import matplotlib.pyplot as plt

def main(argv) :

    # -----------------------------------------------------
    # ---- PATH 
    hd = header()
    hd.headerInput(argv) ; 

    # LINUX
    HOME    = "/home/ventre/"
    PATH1D  = "Documents/Boulot/Thèse/code/bloodflow/bloodflow/Examples/Clamping/9Arteries-Saito/Test/Resistance/"
    PATHs   = "Documents/Boulot/Thèse/code/bloodflow/bloodflow/scripts/Clamping/9Arteries-Saito/Test/Resistance/"
    # # MAC 
    # HOME    = "/Users/jeanneventre/"
    # PATH1D  = "Documents/Boulot/Thèse/code/bloodflow/Examples/Clamping/9Arteries-Saito/"
    # PATHs   = "Documents/Boulot/Thèse/code/bloodflow/scripts/Clamping/9Arteries-Saito/"

    # for Nx in ["5","10","15"]:

    Nx       = hd.Nxstr

    xOrder   = hd.xOrderstr

    dt       = hd.dtstr
    tOrder   = hd.tOrderstr

    NN       = hd.NNstr

    HR       = "HRQ"
    Solver   = "KIN_HAT"

    Conj     = "jS"

    nuv      = hd.Cvstr
    
    State = "PostClamp"

    # PATH    = PATH1D + State + "/" + NN + "/" + Conj + "/nuv=" + nuv +  "/C=" + C + "/R1=" + R1 + "/R2=" + Rt2 + "/Nx=" + Nx + "/xOrder=" + xOrder + "/dt=" + dt + "/tOrder=" + tOrder + "/" + Solver + "/" + HR + "/"
    # print(PATH)
    # Store   = PATH1D + State + "Figures"

    PATH = argv[1]
    # -----------------------------------------------------
    for pType in ["R"] :

        pName,pLabel = out.getType(pType)

        # Time properties
        T_c     = 0.57 ;
        ts_c    = 0. * T_c ;
        te_c    = 10. * T_c ; 

        liX         = []
        liY         = []
        lFileSep    = []
        lFile       = []
        
        R_int = np.zeros(3)
        for i in [0., 1.,2.] :
            os.chdir(HOME)
            liX.append(0)
            liY.append([1,2,3])
            lFileSep.append(",")
            lFile.append( PATH + "Figures/" + "Artery_" + str(round(i)) + "_x_"  + pName )
            nplot = len(lFile)
            for j in range(0,nplot):
                Data = np.genfromtxt(lFile[j], delimiter = str(lFileSep[j]))
            nb = Data.shape[0]
            k = round(i)
            R_int[k] = np.sum(Data[1:nb,1])/(nb-1)

    # 3 artères
    mu = 5e-2 # g cm^-1 s^-2 == 0.1 * Pa.s == 0.1* kg m^-1 s^-2 
    L = np.array([10,10,10])
    R = np.array([1.5,1.5,1.5])

    Res = 8 * mu * L /(np.pi * R**4)
    print('resistance avant :', Res)

    # Res = 8 * mu * L /(np.pi * R_int**4)
    # print('resistance apres :', Res)

    r1 = 1/(1/Res[1] + 1/Res[2])
    Restot = Res[0] + r1
    print('resistance totale : ', Restot)

    # if (i != 0) :
    #     L = np.array( [ 4.0, 72.5, 2.0, 38.5, 3.9, 69.1, 34.5, 96.9, 96.9 ] ) # cm
    #     
    #     R = np.array( [ 1.5, 0.5, 1.3, 0.4, 1.2, 0.4, 0.8, 0.5, 0.5] ) # cm
    #     R1    = 8 * mu * L[0] /(np.pi * R[0]**4) # g cm^-4 s^-1
    #     R2    = 8 * mu * L[1] /(np.pi * R[1]**4)
    #     R3    = 8 * mu * L[2] /(np.pi * R[2]**4)
    #     R4    = 8 * mu * L[3] /(np.pi * R[3]**4)
    #     R5    = 8 * mu * L[4] /(np.pi * R[4]**4)
    #     R6    = 8 * mu * L[5] /(np.pi * R[5]**4)
    #     R7    = 8 * mu * L[6] /(np.pi * R[6]**4)
    #     R8    = 8 * mu * L[7] /(np.pi * R[7]**4)
    #     R9    = 8 * mu * L[8] /(np.pi * R[8]**4)
    #     r1 = 1/(1/R8 + 1/R9)
    #     r2 = R7 + r1
    #     r3 = 1/(1/r2 + 1/R6)
    #     r4 = R5 + r3
    #     r5 = 1/(1/R4 + 1/r4)
    #     r6 = R3 + r5
    #     r7 = 1/(1/r6 + 1/R2)
    #     r8 = R1 + r7

    #     r8 =  r8 #* 0.0075006375541921
    #     if State == "PreClamp" : 
    #         print(r8)

    #     r1 = R5 + R6
    #     r2 = 1/(1/R4 + 1/r1)
    #     r3 = r2 + R3
    #     r4 = 1/(1/R2 + 1/r3)
    #     r5 = R1 + r4
    #     if State == "PostClamp" : 
    #         print(r5)

    #     R1    = 8 * mu * L[0] /(np.pi * R_int[0]**4) # g cm^-4 s^-1
    #     R2    = 8 * mu * L[1] /(np.pi * R_int[1]**4)
    #     R3    = 8 * mu * L[2] /(np.pi * R_int[2]**4)
    #     R4    = 8 * mu * L[3] /(np.pi * R_int[3]**4)
    #     R5    = 8 * mu * L[4] /(np.pi * R_int[4]**4)
    #     R6    = 8 * mu * L[5] /(np.pi * R_int[5]**4)
    #     R7    = 8 * mu * L[6] /(np.pi * R_int[6]**4)
    #     R8    = 8 * mu * L[7] /(np.pi * R_int[7]**4)
    #     R9    = 8 * mu * L[8] /(np.pi * R_int[8]**4)

    #     if State == "PreClamp" : 
    #         r1 = 1/(1/R8 + 1/R9)
    #         r2 = R7 + r1
    #         r3 = 1/(1/r2 + 1/R6)
    #         r4 = R5 + r3
    #         r5 = 1/(1/R4 + 1/r4)
    #         r6 = R3 + r5
    #         r7 = 1/(1/r6 + 1/R2)
    #         r8 = R1 + r7
    #         Res = r8
    #     elif State == "PostClamp" :
    #         r1 = R5 + R6
    #         r2 = 1/(1/R4 + 1/r1)
    #         r3 = r2 + R3
    #         r4 = 1/(1/R2 + 1/r3)
    #         r5 = R1 + r4
    #         Res = r5
    #     print(State, ':' , Res)

    # else : 
    #     #####  1 artère
    #     mu = 5e-2 
    #     L = 10
    #     R = 1.5
    #     Res = 8 * mu * L / (np.pi * R**4)
    #     print(Res)
    #     Res = 8 * mu * L / (np.pi * R_int[0]**4)
    #     print(Res)

if __name__ == "__main__":
	main(sys.argv[1:])
