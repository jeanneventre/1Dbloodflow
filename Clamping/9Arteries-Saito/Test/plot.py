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
# from    csv_libPlot import *

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
    PATH1D  = "Documents/Boulot/Thèse/code/bloodflow/bloodflow/Examples/Clamping/9Arteries-Saito/"
    PATHs   = "Documents/Boulot/Thèse/code/bloodflow/bloodflow/scripts/Clamping/9Arteries-Saito/"
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
    Rt       = hd.Rtstr
    C        = hd.Cstr
    Q        = hd.Qstr
    R1       = hd.P1
    Rt2      = hd.P2   

    State = "Test"

    # PATH    = PATH1D + State + "/" + NN + "/" + Conj + "/nuv=" + nuv +  "/C=" + C + "/R1=" + R1 + "/R2=" + Rt2 + "/Nx=" + Nx + "/xOrder=" + xOrder + "/dt=" + dt + "/tOrder=" + tOrder + "/" + Solver + "/" + HR + "/"
    # print(PATH)
    # Store   = PATH1D + State + "Figures"

    PATH = argv[1]

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
            Data[:,[1,2,3]] = Data[:,[1,2,3]]*0.1*0.0075006375541921
            dx = Data[10,0] - Data[9,0]
            Data[:,0] = Data[:,0] - Data[50,0]  
    # -----------------------------------------------------
    # ---- CALCULATIONS
    b = sp.integrate.trapz(Pexp, axis=0, dx=0.01)  

    D  = np.zeros(115)
    tt = np.zeros(115)

    for i in range(115):
        k = round(0.01/dx * i)
        D[i] = Data[int(k),3]
        tt[i] = Data[int(k),0]

    # R2 = np.sum((D[5:63] - np.mean(Q))**2)/ np.sum((Q - np.mean(Q))**2) 
    R2   = metrics.r2_score(Pexp, D[5:63], multioutput ='uniform_average')
    Linf = max(abs(Pexp-D[5:63]))/max(abs(Pexp))
    L1   = sp.integrate.trapz(abs(Pexp-D[5:63]), dx = 0.01)/sp.integrate.trapz(abs(Pexp), dx=0.01) 
    L2   = np.sqrt(sp.integrate.trapz((Pexp-D[5:63])**2, dx=0.01))/np.sqrt(sp.integrate.trapz(Pexp**2,dx=0.01))
    # -----------------------------------------------------
    # ---- WRITE RESULTS IN FILES 
    # os.chdir(HOME)
    # integ = PATHs + State
    # os.chdir(integ)
    # fileName = 'res.csv' 

    # if (float(nuv) == 5e4) and(float(C) == 1e-6) and (float(R1) == 4e2) and (float(R2) == 15e2):
    #     os.remove(fileName)
    #     fh = open(fileName, 'w')
    #     # fh.write(" nuv, \t E, \t Rt, \t a,\t b, \t (a-b) \t \n")

    # fh = open(fileName, 'a')
    # fh.write("%.20f, \t %.20f, \t %.20f, \t %.20f, \t %.20f,  \t %.20f"%(float(C),float(Rt), R2, Linf, L1,L2) + "\n")  

    # fh.write("%.20f, \t %.20f, \t %.20f, \t %.20f, \t %.20f"%(float(C), R2, Linf, L1,L2) + "\n")
    # -----------------------------------------------------
    # ---- PLOT RESULTS
        
        # # TEST PLOT
    ax = plt.gca()
    ax.yaxis.set_tick_params(labelsize=12)
    ax.xaxis.set_tick_params(labelsize=12)
    plt.plot(t,Pexp,linewidth= 2, label='Experimental')
    plt.plot(tt[5:63],D[5:63],linewidth=2,label='Simulated')
    # plt.plot(Data[:,0], Data[:,3], label = 'Simulated')
        # plt.xlim([-0.1,2*0.57])

    plt.ylim([60,150])
    plt.xlabel('time (s)', fontsize=12)
    plt.ylabel('pressure (mmHg)',fontsize=12)
    plt.text(0.35,95, "Q = %d \n Tej = %.2f \n R1 = %d \n R2 = %d \n C = %.7f "%(400,0.35, float(R1), float(Rt2), float(C)), fontsize=14)
    plt.legend(fontsize=12)
    plt.title('Pre Clamp pressure in the right radial artery',fontsize=14)
    plt.show()
    # # 

    # pathlib.Path(Store).mkdir(parents=True, exist_ok=True) 
    # os.chdir(HOME)
    # for pType in ["P"] :

    #     pName,pLabel = out.getType(pType)

    #     # FILE :
    #     ###########
    #     # PATHEND     = "/dt=" + dtstr + "/tOrder=" + tOrderstr + "/KIN_HAT" + "/" + HRstr + "/Figures/" + ArtName0 + pName

    #     i=1
    #     PATHEND = PATH + "Figures/" + "Artery_" + str(round(i)) + "_t_"  + pName 

    #     J1 = "100"
    #     Art0_11  = PATHEND
    #     ######################################
    #     nfig = 1

    #     lCol = [    "black"]
    #     lMark = [   "o"]
    #     lMarkSize = [   5]
    #     lMarkWidth = [  1]
    #     MarkPoints = 100

    #     lLineSize = [   2]
    #     lStyle = [      ""]
    #     lAlpha = [  1]

    #     LegLoc      = 1
    #     LegPos      = [1., 1.]
    #     LegCol      = 1
    #     LegSize     = 19

    #     xRange      = []
    #     yRange      = [] 
    #     xMargin = 0 
    #     yMargin = 0

    #     xBins       = 2 ;
    #     yBins       = 2 ;

    #     lHline      = []
    #     lHlineColor = []
    #     lHlineWidth = []
    #     lHlineStyle = []

    #     lVline      = []
    #     lVlineColor = []
    #     lVlineWidth = []
    #     lVlineStyle = []
        
    #     lAffline = []
    #     lAfflineColor = []
    #     lAfflineWidth = []
    #     lAfflineStyle = []

    #     xScale = 10.
    #     lXScale     = [ xScale]
    #     yScale      = 1.
    #     lYScale     = [ yScale]
    #     pScale      = "linear"

    #     xOffset     = xScale/2.
    #     lXOffset    = [ xOffset]
    #     lYOffset    = [ 0.]

    #     lText       = []
    #     lTextAlign  = [ "left"]
    #     lTextPos    = [ [0.02,0.05]]
    #     lTextColor  = [ "black" ]

    #     xLabel=r"$x/L$"
    #     yLabel = pLabel
    #     lLabel = [""]

    #     lFileSep    = [ ","]
    #     liX         = [ 0]
    #     liY         = [ 1]

    #     lFile       = [ Art0_11
    #                     ]
    #     title = pType + "-t.pdf"
    #     nfig = plot_csv_adim(pathStore=Store,title=title,lFile=lFile,lFileSep=lFileSep,
    #                         liX=liX,liY=liY,
    #                         xLabel=xLabel,yLabel=yLabel,lLabel=lLabel,
    #                         xRange=xRange,yRange=yRange,xMargin=xMargin,yMargin=yMargin,
    #                         xBins=xBins,yBins=yBins,
    #                         lHline=lHline,lHlineColor=lHlineColor,lHlineWidth=lHlineWidth,lHlineStyle=lHlineStyle,
    #                         lVline=lVline,lVlineColor=lVlineColor,lVlineWidth=lVlineWidth,lVlineStyle=lVlineStyle,
    #             lAffline=lAffline,lAfflineColor=lAfflineColor,lAfflineWidth=lAfflineWidth,lAfflineStyle=lAfflineStyle,
    #                         lXScale=lXScale,lYScale=lYScale,pScale=pScale,lXOffset=lXOffset,lYOffset=lYOffset,
    #                         LegLoc=LegLoc,LegPos=LegPos,LegCol=LegCol,LegSize=LegSize,
    #                         lText=lText,lTextPos=lTextPos,lTextAlign=lTextAlign,lTextColor=lTextColor,
    #                         lCol=lCol,lMark=lMark,lMarkSize=lMarkSize,lMarkWidth=lMarkWidth,MarkPoints=MarkPoints,
    #                         lLineSize=lLineSize,lStyle=lStyle,lAlpha=lAlpha,nf=nfig)


if __name__ == "__main__":
	main(sys.argv[1:])
