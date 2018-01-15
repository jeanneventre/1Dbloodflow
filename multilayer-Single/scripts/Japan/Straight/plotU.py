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

    drCoarsestr = "0.25"
    drFinestr   = "0.01"
    Nxstr       = "800"
    xOrderstr   = "2"

    dtstr       = "1e-4"
    tOrderstr   = "3"

    Kstr        = "212e4"
    NNstr       = "Newtonian"
    Cvstr       = "4350"
    Knlstr      = "0"

    HRstr       = "HRQ"
    Solverstr   = "KIN_HAT"

    PATH    = PATH2D + "K=" + str(Kstr) + "/" + NNstr + "/Cv=" + str(Cvstr) + "/Knl=" + Knlstr

    Store   = PATH2D + "Figures/"

    # FILE :
    ###########
    dName0  = "Artery_0_t_"
    pName   = "r_UxUr.csv"
    pLabel  = r"$\sqrt{U_x^2+U_r^2}$ $\left[\frac{cm}{s}\right]$"

    Data0   = PATH + "/drCoarse=" + drCoarsestr + "-drFine=" + drFinestr + "/Nx=" + str(Nxstr) + "/xOrder=" + str(xOrderstr) + "/dt=" + str(dtstr) + "/tOrder=" + str(tOrderstr) + "/" + str(Solverstr) + "/" + str(HRstr) +  "/Figures/" + dName0 + pName

    Exp1 = PATHEXP + "Velocity_R1mm.csv"
    Exp2 = PATHEXP + "Velocity_R2mm.csv"
    Exp3 = PATHEXP + "Velocity_R3mm.csv"
    Exp4 = PATHEXP + "Velocity_R4mm.csv"
    Exp5 = PATHEXP + "Velocity_R5mm.csv"
    Exp6 = PATHEXP + "Velocity_R6mm.csv"
    Exp7 = PATHEXP + "Velocity_R7mm.csv"

    ######################################
    ######################################


    lCol        = [ "blue","red","green","black","green","red","blue",
                    "blue","red","green","black","green","red","blue"]
    lMark       = [ "","","","","x","x","x",
                    "","","","","s","s","s"]
    lMarkSize   = [ 1,1,1,1,5,5,5,
                    1,1,1,1,5,5,5]
    lMarkWidth  = [ 1,1,1,1,1,1,1,
                    1,1,1,1,1,1,1]
    MarkPoints  = 40

    lLineSize   = [ 2,2,2,2,2,2,2,
                    2,2,2,2,2,2,2]
    lStyle      = [ "-","-","-","-","-","-","-",
                    "--","--","--","--","--","--","--"]
    lAlpha      = [ 0.6,0.6,0.6,0.6,0.6,0.6,0.6,
                    0.8,0.8,0.8,0.8,0.8,0.8,0.8]

    LegLoc      = 1
    LegPos      = [1.,1.]
    LegCol      = 1

    xRange      = [0.,0.6]
    yRange      = []

    lHline      = []
    lHlineColor = []
    lHlineWidth = []
    lHlineStyle = []

    lVline      = []
    lVlineColor = []
    lVlineWidth = []
    lVlineStyle = []

    lXScale     = [ 1.,1.,1.,1.,1.,1.,1.,
                    1.,1.,1.,1.,1.,1.,1.]
    lYScale     = [ 1.e-2,1.e-2,1.e-2,1.e-2,1.e-2,1.e-2,1.e-2,
                    1.,1.,1.,1.,1.,1.,1.]

    lXOffset    = [ 0.,0.,0.,0.,0.,0.,0.,
                    0.5,0.5,0.5,0.5,0.5,0.5,0.5]
    lYOffset    = [ 0.,0.,0.,0.,0.,0.,0.,
                    0.,0.,0.,0.,0.,0.,0.]

    xLabel=r"$t$ $\left[s\right]$"
    yLabel = pLabel
    lLabel      = [ r"$r$=$0.1$", r"$r$=$0.2$", r"$r$=$0.3$", r"$r$=$0.4$", r"$r$=$0.5$", r"$r$=$0.6$", r"$r$=$0.7$",
                    "","","","","","","" ]

    lFileSep    = [ ",",",",",",",",",",",",",",
                    ",",",",",",",",",",",",","]
    lFile       = [ Exp1,Exp2,Exp3,Exp4,Exp5,Exp6,Exp7]#,
                    # Data0,Data0,Data0,Data0,Data0,Data0,Data0]

    liX         = [ 0,0,0,0,0,0,0,
                    0,0,0,0,0,0,0]
    liY         = [ 1,1,1,1,1,1,1,
                    1,2,3,4,5,6,7]

    lText       = []#[r"$N_x$=" + str(Nxstr), r"$Order$ " + str(xOrderstr),
                #    r"$K$="+str(Kstr), NNstr, r"$C_\nu$=" + str(Cvstr)]
    lTextAlign  = [ "center","center",
                    "left", "left", "left"]
    lTextPos    = [ [0.25,0.04],[0.5,0.05],
                    [0.05,0.935], [0.32,0.935], [0.6,0.925] ]
    lTextColor  = [ "black","black",
                    "black", "black", "black" ]

    title = "Ux_r_t.pdf"

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
