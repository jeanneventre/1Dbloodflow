#!/usr/bin/python3
import  sys, getopt
import  numpy       as np

import  help_Output as out

from    csv_libPlot import *
from    help_Wave   import *

def main(argv) :

    # PATHS
    ###########

    HOME = "/Users/Arthur/"
    PATH1D  = HOME + "Documents/UPMC/These/Codes/bloodflow/Examples/Network/9Arteries-Saito/"
    PATHEXP = HOME + "Documents/UPMC/These/Codes/bloodflow/Examples/Network/9Arteries-Saito/Experimental-Data/"

    nfig = 1

    Nxstr       = "5"
    xOrderstr   = "2"

    dtstr       = "1e-4"
    tOrderstr   = "2"

    Estr        = "170e4"

    HRstr       = "HRQ"
    Solverstr   = "KIN_HAT"
    Conjstr     = "jS"

    Rtstr       = "0.5"

    Store       = PATH1D + "Figures/"

    for pType in ["U","P"] :

        pName,pLabel = out.getType(pType)

        # FILE :
        ###########
        ArtName = "Artery_3_t_"
        PATHEND = "/Nx=" + Nxstr + "/xOrder=" + xOrderstr + "/dt=" + dtstr + "/tOrder=" + tOrderstr + "/" + Solverstr + "/" + HRstr + "/Figures/" + ArtName + pName

        Wave    = PATH1D + "Inviscid"  + "/" + Conjstr + "/Rt=" + Rtstr + "/E=" + Estr + "/phi=" + "0"   + "/Cv=" + "0"    + PATHEND
        Viscous = PATH1D + "Newtonian" + "/" + Conjstr + "/Rt=" + Rtstr + "/E=" + Estr + "/phi=" + "-11" + "/Cv=" + "0"    + PATHEND
        Viscoel = PATH1D + "Newtonian" + "/" + Conjstr + "/Rt=" + Rtstr + "/E=" + Estr + "/phi=" + "-11" + "/Cv=" + "500"  + PATHEND

        # ANALYTIC
        EXP = PATHEXP + "Exp_" + pType + ".csv"
        SIM = PATHEXP + "Sim_" + pType + ".csv"

        ######################################
        ######################################
        lCol        = ["black","blue","red","green"]
        lMark       = ["","s","o","^"]
        lMarkSize   = [5,5,5,5]
        lMarkWidth  = [1,1,1,1]
        MarkPoints  = 30

        lLineSize   = [3,2,2,2]
        lStyle      = ["--","-","-","-"]
        lAlpha      = [1,0.8,0.8,0.8]

        LegLoc      = 1
        LegPos      = [1.,1.,1.,1.]
        LegCol      = 2

        xRange      = [0., 0.8]
        yRange      = []

        xBins       = 2
        yBins       = 2

        lHline      = []
        lHlineColor = []
        lHlineWidth = []
        lHlineStyle = []

        lVline      = []
        lVlineColor = []
        lVlineWidth = []
        lVlineStyle = []

        if (pType == "P") :
            YScale = 1.e-4
            Y1DScale = 1.
        else :
            YScale = 1.
            Y1DScale = 3./4.

        lXScale     = [1.,1.,1.,1.]
        lYScale     = [YScale,Y1DScale,Y1DScale,Y1DScale]

        xOffset = 0.1
        if (pType == "P") :
            yOffset = "first"
        else :
            yOffset = 0.

        lXOffset    = [0.,xOffset,xOffset,xOffset]
        lYOffset    = [yOffset,0.,0.,0.]

        lText       = [ r"$N_x$=" + Nxstr, r"$Order$ " + str(xOrderstr)]
        lTextAlign  = [ "left", "right"]
        lTextPos    = [ [0.01,0.04], [0.99,0.05] ]
        lTextColor  = [ "black", "black" ]

        xLabel      = r"$t$ $\left[s\right]$"
        yLabel      = pLabel
        lLabel      = [r"$Exp$", r"$Inviscid$", r"$Viscous$" , r"$Viscoelastic$"]
        lFileSep    = [",",",",",",","]

        lFile       = [EXP,Wave,Viscous,Viscoel]

        liX         = [0,0,0,0]

        liY         = [1,3,3,3]

        title = pType + "_Effects_t.pdf"

        nfig = plot_csv_adim(pathStore=Store,title=title,lFile=lFile,lFileSep=lFileSep,
                            liX=liX,liY=liY,
                            xLabel=xLabel,yLabel=yLabel,lLabel=lLabel,
                            xRange=xRange,yRange=yRange,
                            xBins=xBins,yBins=yBins,
                            lHline=lHline,lHlineColor=lHlineColor,lHlineWidth=lHlineWidth,lHlineStyle=lHlineStyle,
                            lVline=lVline,lVlineColor=lVlineColor,lVlineWidth=lVlineWidth,lVlineStyle=lVlineStyle,
                            lXScale=lXScale,lYScale=lYScale,lXOffset=lXOffset,lYOffset=lYOffset,
                            LegLoc=LegLoc,LegPos=LegPos,LegCol=LegCol,
                            lText=lText,lTextPos=lTextPos,lTextAlign=lTextAlign,lTextColor=lTextColor,
                            lCol=lCol,lMark=lMark,lMarkSize=lMarkSize,lMarkWidth=lMarkWidth,MarkPoints=MarkPoints,
                            lLineSize=lLineSize,lStyle=lStyle,lAlpha=lAlpha,nf=nfig)

if __name__ == "__main__":
   main(sys.argv[1:])
