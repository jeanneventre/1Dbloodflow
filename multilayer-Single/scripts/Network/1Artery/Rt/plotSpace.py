#!/usr/bin/python3
import sys, getopt
from csv_libPlot import *
from csv_libData import *

import numpy as np

def main(argv) :

    # PATHS
    ###########

    HOME = "/Users/Arthur/"
    PATH1D = HOME + "/Documents/UPMC/These/Codes/multilayerSingle/example/Well-Balance/Network/1Artery/Rt/"

    nfig = 1

    HRstr   = "HRQ"
    Orderstr= "2"
    Kstr    = "1e4"
    Knlstr  = "8e2"
    dRstr   = "1e-1"

    PATH    = PATH1D + "/dR=" + dRstr + "/K=" + Kstr + "/Knl=" + Knlstr + "/"
    PATHREF = PATH1D + "/dR=" + dRstr + "/K=" + Kstr + "/Knl=" + "0" + "/"
    Store   = PATH1D + "/dR=" + dRstr + "/Figures/"

    for pType in ["Q","P","RmR0"] :

        # FILE :
        ###########
        dName0 = "Artery_0_x_"

        if (pType == "Q") :
            pName = "Q.csv"
            pLabel = r"$Q$ $\left[\frac{cm^3}{s}\right]$"
        if (pType == "P") :
            pName = "P.csv"
            pLabel = r"$p$ $\left[\frac{g}{cm.s^{2}}\right]$"
        if (pType == "RmR0") :
            pName = "RmR0.csv"
            pLabel = r"$R-R_0$ $\left[cm\right]$"

        J1 = "400"
        Data1   = PATH + "Nr=8/Raf=3/" + "Nx=" +J1 + "/xOrder=1" + "/KIN_HAT/HRQ/" + "Figures/" + dName0 + pType + ".csv"
        Data2   = PATH + "Nr=8/Raf=3/" + "Nx=" +J1 + "/xOrder=2" + "/KIN_HAT/HRQ/" + "Figures/" + dName0 + pType + ".csv"

        REF1    = PATHREF + "Nr=8/Raf=3/" + "Nx=" +J1 + "/xOrder=1" + "/KIN_HAT/HRQ/" + "Figures/" + dName0 + pType + ".csv"
        REF2    = PATHREF + "Nr=8/Raf=3/" + "Nx=" +J1 + "/xOrder=2" + "/KIN_HAT/HRQ/" + "Figures/" + dName0 + pType + ".csv"

        iX = 0;

        ######################################
        ######################################

        lCol        = [ "blue","green","red",
                        "blue","green","red",
                        "blue","green","red"]

        lMark       = [ "","","",
                        "","","",
                        "","",""]
        lMarkSize   = [ 5,5,5,
                        5,5,5,
                        5,5,5]
        lMarkWidth  = [ 2,2,2,
                        2,2,2,
                        2,2,2]
        MarkPoints  = 40

        lLineSize   = [ 2,2,2,
                        2,2,2,
                        2,2,2]
        lStyle      = [ "-","-","-",
                        "--","--","--",
                        "-.","-.","-."]
        lAlpha      = [ 1,1,1,
                        1,1,1,
                        1,1,1]

        LegLoc      = 1
        LegPos      = [0.98, 1.1]
        LegCol      = 3

        xRange = []
        yRange = []

        # Reflection coefficient
        Rt = 0.5

        if (pType == "Q") :
            Qmax = 0.59
            lHline = [Qmax,-Rt*Qmax]
        if (pType == "P") :
            Pmax = float(Kstr) * np.sqrt(np.pi) * float(dRstr)
            lHline = [Pmax,Rt*Pmax]
        if (pType == "RmR0") :
            RmR0max = float(dRstr)
            lHline = [RmR0max,Rt*RmR0max]
        lHlineColor = [ "black","blue"]
        lHlineWidth = [ 1,1]
        lHlineStyle = [ "--","--"]

        lVline      = []
        lVlineColor = []
        lVlineWidth = []
        lVlineStyle = []

        lXScale     = [ 1.,1.,1.,
                        1.,1.,1.,
                        1.,1.,1.]
        lYScale     = [ 1.,1.,1.,
                        1.,1.,1.,
                        1.,1.,1.]
        lXOffset    = [ 0.,0.,0.,
                        0.,0.,0.,
                        0.,0.,0.]
        lYOffset    = [ 0.,0.,0.,
                        0.,0.,0.,
                        0.,0.,0.]

        lText       = [ r"$N_x=\left\{\right.$" + str(J1) + r"$\left. \right\}$", r"$Order$ " + str(Orderstr)]
        lTextAlign  = [ "left", "center"]
        lTextPos    = [ [0.05,0.04], [0.75,0.05] ]
        lTextColor  = [ "black", "black" ]

        xLabel=r"$x$ $\left[cm\right]$"
        yLabel=pLabel
        lLabel      = [ r"$1$", r"$2$", r"$3$" ]


        liX         = [ iX,iX,iX,
                        iX,iX,iX,
                        iX,iX,iX]

        iY = 9
        liY         = [ iY, iY, iY ]

        lFileSep    = [",",",",","]
        lFile       = [ REF2,Data1,Data2]

        title = pType + "_Network_x.pdf"

        nfig = plot_csv_adim(pathStore=Store,title=title,lFile=lFile,lFileSep=lFileSep,
                            liX=liX,liY=liY,
                            xLabel=xLabel,yLabel=yLabel,lLabel=lLabel,
                            xRange=xRange,yRange=yRange,
                            lHline=lHline,lHlineColor=lHlineColor,lHlineWidth=lHlineWidth,lHlineStyle=lHlineStyle,
                            lVline=lVline,lVlineColor=lVlineColor,lVlineWidth=lVlineWidth,lVlineStyle=lVlineStyle,
                            lXScale=lXScale,lYScale=lYScale,lXOffset=lXOffset,lYOffset=lYOffset,
                            LegLoc=LegLoc,LegPos=LegPos,LegCol=LegCol,
                            lText=lText,lTextPos=lTextPos,lTextAlign=lTextAlign,lTextColor=lTextColor,
                            lCol=lCol,lMark=lMark,lMarkSize=lMarkSize,lMarkWidth=lMarkWidth,MarkPoints=MarkPoints,
                            lLineSize=lLineSize,lStyle=lStyle,lAlpha=lAlpha,nf=nfig)

if __name__ == "__main__":
   main(sys.argv[1:])
