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
    Cvstr       = "0"
    Knlstr      = "0"

    HRstr       = "HRQ"
    Solverstr   = "KIN_HAT"

    PATH    = PATH2D + "K=" + str(Kstr) + "/" + NNstr + "/Cv=" + str(Cvstr) + "/Knl=" + Knlstr

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

        L1 = "0" ;
        PATH      = PATH2D + "K=" + Kstr + "/" + NNstr + "/Cv=" + Cvstr + "/Knl=" + Knlstr
        Data1     = PATH + "/Nr=" + Nrstr + "/Raf=" + Rafstr + "/Nx=" + Nxstr + "/xOrder=" + xOrderstr + "/dt=" + dtstr + "/tOrder=" + tOrderstr + "/" + str(Solverstr) + "/" + str(HRstr) +  "/Figures/" + dName0 + pName

        L2 = "4000" ;
        PATH      = PATH2D + "K=" + Kstr + "/" + NNstr + "/Cv=" + L2 + "/Knl=" + Knlstr
        Data2     = PATH + "/Nr=" + Nrstr + "/Raf=" + Rafstr + "/Nx=" + Nxstr + "/xOrder=" + xOrderstr + "/dt=" + dtstr + "/tOrder=" + tOrderstr + "/" + str(Solverstr) + "/" + str(HRstr) +  "/Figures/" + dName0 + pName

        L3 = "100e2" ;
        PATH      = PATH2D + "K=" + Kstr + "/" + NNstr + "/Cv=" + Cvstr + "/Knl=" + L3
        Data3     = PATH + "/Nr=" + Nrstr + "/Raf=" + Rafstr + "/Nx=" + Nxstr + "/xOrder=" + xOrderstr + "/dt=" + dtstr + "/tOrder=" + tOrderstr + "/" + str(Solverstr) + "/" + str(HRstr) +  "/Figures/" + dName0 + pName

        L4 = "100e3" ;
        PATH      = PATH2D + "K=" + Kstr + "/" + NNstr + "/Cv=" + Cvstr + "/Knl=" + L4
        Data4     = PATH + "/Nr=" + Nrstr + "/Raf=" + Rafstr + "/Nx=" + Nxstr + "/xOrder=" + xOrderstr + "/dt=" + dtstr + "/tOrder=" + tOrderstr + "/" + str(Solverstr) + "/" + str(HRstr) +  "/Figures/" + dName0 + pName

        Exp1 = PATHEXP + "Straight_mp280_4760.csv"
        Exp2 = PATHEXP + "Straight_mp2520_4760.csv"

        iX = 0;

        ######################################
        ######################################

        lCol        = ["blue","red","green","black","orange"]
        lMark       = ["","","","",""]
        lMarkSize   = [1,1,1,1,1]
        lMarkWidth  = [1,1,1,1,1]
        MarkPoints  = 40

        lLineSize   = [2,2,2,2,2]
        lStyle      = ["-","-","-","-","-"]
        lAlpha      = [1,0.8,0.8,0.8,0.8]

        LegLoc      = 1
        LegPos      = [1.,1.,1.,1.,1.]
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

        lXScale     = [1.,1.,1.,1.,1.]
        lYScale     = [1.e-4,1.,1.,1.,1.]

        lXOffset    = [0.,0.,0.,0.,0.]
        lYOffset    = ["first",0.,0.,0.,0.]

        xLabel=r"$t$ $\left[s\right]$"
        yLabel = pLabel
        lLabel      = [r"$Exp$", r"$N_r$="+str(L1), r"$N_r$="+str(L2), r"$N_r$="+str(L3), r"$N_r$="+str(L4)]

        liX         = [0,0,0,0,0]
        iY = 1
        liY         = [1,iY,iY,iY,iY]

        lFileSep    = [",",",",",",",",","]
        lFile       = [Exp1,Data1,Data2]

        lText       = [r"$N_x$=" + str(Nxstr), r"$Order$ " + str(xOrderstr),
                       r"$K$="+str(Kstr),   NNstr, r"$C_\nu$=" + str(Cvstr)]
        lTextAlign  = ["center", "center", "left", "left", "left"]
        lTextPos    = [[0.25,0.04], [0.75,0.05], [0.05,0.935], [0.30,0.935], [0.6,0.925] ]
        lTextColor  = ["black", "black", "black", "black", "black" ]

        title = pType + "_CV_2D_t.pdf"

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
