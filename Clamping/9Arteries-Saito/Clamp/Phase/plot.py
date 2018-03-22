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

    # PATH    = PATH1D + State + "/" + NN + "/" + Conj + "/nuv=" + nuv +  "/Q=" + Q + "/P1=" + P1 + "/Nx=" + Nx + "/xOrder=" + xOrder + "/dt=" + dt + "/tOrder=" + tOrder + "/" + Solver + "/" + HR + "/"
    PATH = argv[1]

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

    # # -----------------------------------------------------
    # # ---- CALCULATIONS
    # # b = sp.integrate.trapz(Pexp, axis=0, dx=0.01)  
    D  = np.zeros(125)
    tt = np.zeros(125)
    
    for i in range(125):
        k = round(0.01/dx*i)
        # print(k)  
        D[i] = Data[int(k),3]
        tt[i] = Data[int(k),0]

    Dm = np.mean(D)
    
    R2   = metrics.r2_score(Pexp, D[8:71], multioutput ='uniform_average')
    Linf = max(abs(Pexp-D[8:71]))/max(abs(Pexp))
    L1   = sp.integrate.trapz(abs(Pexp-D[8:71]), dx = 0.01)/sp.integrate.trapz(abs(Pexp), dx=0.01) 
    L2   = np.sqrt(sp.integrate.trapz((Pexp-D[8:71])**2, dx=0.01))/np.sqrt(sp.integrate.trapz(Pexp**2,dx=0.01))
    # -----------------------------------------------------
    # ---- WRITE RESULTS IN FILES 
    os.chdir(HOME)
    integ = PATHs + State
    os.chdir(integ)
    fileName = 'res.csv' 

    if (float(nuv) == 5e4) and (float(Q) == 400)  and (float(Rt2) == 1000) and (float(C) == 1e-4) :
        os.remove(fileName)
        # fh = open(fileName, 'w')
        # fh.write(" nuv, \t E, \t Rt, \t a,\t b, \t (a-b) \t \n")

    fh = open(fileName, 'a')
    fh.write("%d, \t %.2f, \t %.20f, \t %.20f, \t %.20f, \t %.20f, \t %.20f,  \t %.20f"%(float(Q),float(P1), 1750, 1e-06, R2, Linf, L1,L2) + "\n")
    # -----------------------------------------------------
    # ---- PLOT RESULTS
    # # TEST PLOT
    ax = plt.gca()
    ax.yaxis.set_tick_params(labelsize=12)
    ax.xaxis.set_tick_params(labelsize=12)
    plt.plot(t,Pexp,linewidth= 2, label='Experimental')
    plt.plot(tt[8:71],D[8:71],linewidth=2,label= 'Simulated')
    plt.plot(Data[:,0], Data[:,3], label='Simulated') 
    # plt.xlim([-0.1,2*0.57])  
    # plt.ylim([60,150])
    plt.xlabel('time (s)', fontsize=12)
    plt.ylabel('pressure (mmHg)',fontsize=12)
    # plt.text(0.42,100, "Q = %d \n Tej = %.2f \n R1 = %d \n R2 = %d \n C = %.7f "%(float(Q),0.35,float(R1) , float(Rt2), float(C)))
    plt.legend(fontsize=12)
    plt.title("Post Clamp pressure RCR in the right radial artery",fontsize=14)
    
    # plt.show()
    # 

    # # pathlib.Path(Store).mkdir(parents=True, exist_ok=True) 
    # # os.chdir(HOME)
    # # for pType in ["P"] :

    # #     pName,pLabel = out.getType(pType)

    # #     # FILE :
    # #     ###########
    # #     # PATHEND     = "/dt=" + dtstr + "/tOrder=" + tOrderstr + "/KIN_HAT" + "/" + HRstr + "/Figures/" + ArtName0 + pName

    # #     i=1
    # #     PATHEND = PATH + "Figures/" + "Artery_" + str(round(i)) + "_t_"  + pName 

    # #     J1 = "100"
    # #     Art0_11  = PATHEND
    # #     ######################################
    # #     nfig = 1

    # #     lCol = [    "black"]
    # #     lMark = [   "o"]
    # #     lMarkSize = [   5]
    # #     lMarkWidth = [  1]
    # #     MarkPoints = 100

    # #     lLineSize = [   2]
    # #     lStyle = [      ""]
    # #     lAlpha = [  1]

    # #     LegLoc      = 1
    # #     LegPos      = [1., 1.]
    # #     LegCol      = 1
    # #     LegSize     = 19

    # #     xRange      = []
    # #     yRange      = [] 
    # #     xMargin = 0 
    # #     yMargin = 0

    # #     xBins       = 2 ;
    # #     yBins       = 2 ;

    # #     lHline      = []
    # #     lHlineColor = []
    # #     lHlineWidth = []
    # #     lHlineStyle = []

    # #     lVline      = []
    # #     lVlineColor = []
    # #     lVlineWidth = []
    # #     lVlineStyle = []
        
    # #     lAffline = []
    # #     lAfflineColor = []
    # #     lAfflineWidth = []
    # #     lAfflineStyle = []

    # #     xScale = 10.
    # #     lXScale     = [ xScale]
    # #     yScale      = 1.
    # #     lYScale     = [ yScale]
    # #     pScale      = "linear"

    # #     xOffset     = xScale/2.
    # #     lXOffset    = [ xOffset]
    # #     lYOffset    = [ 0.]

    # #     lText       = []
    # #     lTextAlign  = [ "left"]
    # #     lTextPos    = [ [0.02,0.05]]
    # #     lTextColor  = [ "black" ]

    # #     xLabel=r"$x/L$"
    # #     yLabel = pLabel
    # #     lLabel = [""]

    # #     lFileSep    = [ ","]
    # #     liX         = [ 0]
    # #     liY         = [ 1]

    # #     lFile       = [ Art0_11
    # #                     ]
    # #     title = pType + "-t.pdf"
    # #     nfig = plot_csv_adim(pathStore=Store,title=title,lFile=lFile,lFileSep=lFileSep,
    # #                         liX=liX,liY=liY,
    # #                         xLabel=xLabel,yLabel=yLabel,lLabel=lLabel,
    # #                         xRange=xRange,yRange=yRange,xMargin=xMargin,yMargin=yMargin,
    # #                         xBins=xBins,yBins=yBins,
    # #                         lHline=lHline,lHlineColor=lHlineColor,lHlineWidth=lHlineWidth,lHlineStyle=lHlineStyle,
    # #                         lVline=lVline,lVlineColor=lVlineColor,lVlineWidth=lVlineWidth,lVlineStyle=lVlineStyle,
    # #             lAffline=lAffline,lAfflineColor=lAfflineColor,lAfflineWidth=lAfflineWidth,lAfflineStyle=lAfflineStyle,
    # #                         lXScale=lXScale,lYScale=lYScale,pScale=pScale,lXOffset=lXOffset,lYOffset=lYOffset,
    # #                         LegLoc=LegLoc,LegPos=LegPos,LegCol=LegCol,LegSize=LegSize,
    # #                         lText=lText,lTextPos=lTextPos,lTextAlign=lTextAlign,lTextColor=lTextColor,
    # #                         lCol=lCol,lMark=lMark,lMarkSize=lMarkSize,lMarkWidth=lMarkWidth,MarkPoints=MarkPoints,
    # #                         lLineSize=lLineSize,lStyle=lStyle,lAlpha=lAlpha,nf=nfig)


if __name__ == "__main__":
	main(sys.argv[1:])
