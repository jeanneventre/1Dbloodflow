#!/usr/bin/python3
import sys, getopt
from csv_libPlot import *

def main(argv) :

    # PATHS
    ###########

    HOME = "/Users/Arthur/"
    PATH2D  = HOME + "Documents/UPMC/These/Codes/multilayerSingle/example/Well-Balance/Japan/Straight/"
    PATHEXP = HOME + "Documents/UPMC/These/Codes/bloodflowSingle/example/Well-Balance/Japan/Experimental-Data/Straight/"

    nfig = 1

    Nrstr       = "8"
    Rafstr      = "3"
    Nxstr       = "800"
    xOrderstr   = "2"

    dtstr       = "1e-4"
    tOrderstr   = "3"

    Kstr        = "212e4"
    NNstr       = "Newtonian"
    Cvstr       = "5000"
    Knlstr      = "100e4"

    HRstr       = "HRQ"
    Solverstr   = "KIN_HAT"

    PATH    = PATH2D + "K=" + str(Kstr) + "/" + NNstr + "/Cv=" + str(Cvstr) + "/Knl=" + Knlstr

    Store   = PATH2D + "Figures/"

    for pType in ["P","U","Q","phi","alpha"] :

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
        if (pType == "U") :
            pName = "U.csv"
            pLabel = r"$U$ $\left[\frac{cm}{s}\right]$"
        if (pType == "phi") :
            pName = "phi.csv"
            pLabel = r"$\phi$"
        if (pType == "alpha") :
            pName = "alpha.csv"
            pLabel = r"$\alpha$"

        Data0     = PATH + "/Nr=" + Nrstr + "/Raf=" + Rafstr + "/Nx=" + str(Nxstr) + "/xOrder=" + str(xOrderstr) + "/dt=" + str(dtstr) + "/tOrder=" + str(tOrderstr) + "/" + str(Solverstr) + "/" + str(HRstr) +  "/Figures/" + dName0 + pName

        ######################################
        ######################################


        lCol        = [ "blue","red","green"]
        lMark       = [ "","",""]
        lMarkSize   = [ 1,1,1]
        lMarkWidth  = [ 1,1,1]
        MarkPoints  = 40

        lLineSize   = [ 2,2,2]
        lStyle      = [ "-","-","-"]
        lAlpha      = [ 1,0.8,0.8]

        LegLoc      = 1
        LegPos      = [1.,1.]
        LegCol      = 1

        xRange      = []

        if (pType=="phi"):
            yRange      = [-50.,50.]
        elif (pType=="alpha"):
            yRange      = [-5.,5.]
        else :
            yRange      = []

        lHline      = []
        lHlineColor = []
        lHlineWidth = []
        lHlineStyle = []

        lVline      = []
        lVlineColor = []
        lVlineWidth = []
        lVlineStyle = []

        lXScale     = [ 1.,1.,1.]
        lYScale     = [ 1.,1.,1.]

        lXOffset    = [ 0.,0.,0.]
        lYOffset    = [ 0.,0.,0.]

        xLabel=r"$t$ $\left[s\right]$"
        yLabel = pLabel
        lLabel      = [ r"$x$=$0$", r"$x$=$28$", r"$x$=$252$"]

        lFileSep    = [ ",",",",","]
        lFile       = [ Data0,Data0,Data0]

        liX         = [ 0,0,0]
        liY         = [ 1,2,3]

        lText       = [r"$N_x$=" + str(Nxstr), r"$Order$ " + str(xOrderstr), r"$N_x$=" + str(Nrstr),
                       r"$K$="+str(Kstr), NNstr, r"$C_\nu$=" + str(Cvstr)]
        lTextAlign  = [ "center","center","center",
                        "left", "left", "left"]
        lTextPos    = [ [0.25,0.04],[0.5,0.05],[0.75,0.04],
                        [0.05,0.935], [0.32,0.935], [0.6,0.925] ]
        lTextColor  = [ "black","black","black",
                        "black", "black", "black" ]

        title = pType + "_Data_2D_t.pdf"

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
