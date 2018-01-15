#!/usr/bin/python3
import sys, getopt
from csv_libPlot import *

def main(argv) :

    # PATHS
    ###########

    HOME = "/Users/Arthur/"
    PATH2D  = HOME + "Documents/UPMC/These/Codes/multilayerSingle/example/Well-Balance/Japan/Stenosis/"
    PATHEXP = HOME + "Documents/UPMC/These/Codes/bloodflowSingle/example/Well-Balance/Japan/Experimental-Data/Stenosis/"

    nfig = 1

    drCoarsestr = "0.25"
    drFinestr   = "0.01"
    Nxstr       = "800"
    xOrderstr   = "2"

    dtstr       = "1e-5"
    tOrderstr   = "3"

    Kstr        = "211e4"
    NNstr       = "Newtonian"
    Cvstr       = "5000"
    Knlstr      = "0"
    dKstr       = "0"

    HRstr       = "HRQ"
    Solverstr   = "KIN_HAT"

    PATH    = PATH2D + "K=" + str(Kstr) + "/" + NNstr + "/Cv=" + str(Cvstr) + "/Knl=" + Knlstr + "/dKst=" + dKstr

    Store   = PATH2D + "Figures/"

    for pType in ["P"] :

        # FILE :
        ###########
        dName0 = "Artery_0_t_"

        if (pType == "Q") :
            pName = "Q.csv"
            pLabel = r"$Q$ $\left[\frac{cm^3}{s}\right]$"
        if (pType == "P") :
            pName = "P.csv"
            pLabel = r"$p$ $\left[\frac{g}{cm.s^{2}}\right]$"
        if (pType == "RmR0") :
            pName = "RmR0.csv"
            pLabel = r"$R-R_0$ $\left[cm\right]$"

        Data0     = PATH + "/drCoarse=" + drCoarsestr + "-drFine=" + drFinestr + "/Nx=" + str(Nxstr) + "/xOrder=" + str(xOrderstr) + "/dt=" + str(dtstr) + "/tOrder=" + str(tOrderstr) + "/" + str(Solverstr) + "/" + str(HRstr) +  "/Figures/" + dName0 + pName

        Exp1 = PATHEXP + "Stenosis_mp280_4760.csv"
        Exp2 = PATHEXP + "Stenosis_mp2520_4760.csv"

        lCol        = [ "blue","blue"]
        lMark       = [ "",""]
        lMarkSize   = [ 1,1]
        lMarkWidth  = [ 1,1]
        MarkPoints  = 40

        lLineSize   = [ 2,2]
        lStyle      = [ "--","-"]
        lAlpha      = [ 1,0.8]

        LegLoc      = 1
        LegPos      = [1.,1.]
        LegCol      = 1

        xRange      = []
        yRange      = []

        lHline      = []
        lHlineColor = []
        lHlineWidth = []
        lHlineStyle = []

        lVline      = []
        lVlineColor = []
        lVlineWidth = []
        lVlineStyle = []

        lXScale     = [ 1.,1.]
        lYScale     = [ 1.e-4,1.]

        lXOffset    = [ 0.,0.]
        lYOffset    = [ "first",0.]

        lText       = [r"$N_x$=" + str(Nxstr), r"$Order$ " + str(xOrderstr),
                       r"$K$="+str(Kstr), r"$Newtonian$", r"$C_\nu$=" + str(Cvstr)]
        lTextAlign  = [ "center","center",
                        "left", "left", "left"]
        lTextPos    = [ [0.25,0.04],[0.75,0.05],
                        [0.05,0.935], [0.3,0.935], [0.6,0.925] ]
        lTextColor  = [ "black","black",
                        "black", "black", "black" ]

        xLabel=r"$t$ $\left[s\right]$"
        yLabel = pLabel
        lLabel      = [ r"$Exp$", r"$1D$"]

        ######################################
        # Upstream (28)
        ######################################

        liX         = [ 0,0 ]
        liY         = [ 1,2 ]
        lFileSep    = [ ",",","]
        lFile       = [ Exp1,Data0]

        title = pType + "_2D_Upstream_t.pdf"

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

        ######################################
        # Downstream (252)
        ######################################

        lCol        = [ "red","red" ]

        lFile       = [ Exp2,Data0]

        liY         = [ 1,4 ]

        title = pType + "_2D_Dowstream_t.pdf"

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
