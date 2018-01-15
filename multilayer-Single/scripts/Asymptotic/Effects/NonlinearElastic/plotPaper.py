#!/usr/bin/python3
import sys, getopt
from csv_libPlot import *

def main(argv) :

    # PATHS
    ###########

    HOME = "/Users/Arthur/"
    PATH1D = HOME + "/Documents/UPMC/These/Codes/multilayerSingle/example/Well-Balance/Asymptotic/Effects/NonlinearElastic/"

    # FILE :
    ###########
    dataName = "Artery_0_x_Q.csv"

    nfig = 1

    dRstr   = "1e-1"

    Kstr    = "1e4"
    Knlstr  = "1e3"

    PATH    = PATH1D + "/dR=" + dRstr + "/K=" + Kstr + "/Knl=" + Knlstr + "/"
    PATHREF = PATH1D + "/dR=" + dRstr + "/K=" + Kstr + "/Knl=" + "0" + "/"

    Data1   = PATH + "Nr=8/Raf=3/Nx=400/xOrder=1" + "/KIN_HAT/HRQ/" + "Figures/" + dataName
    Data2   = PATH + "Nr=8/Raf=3/Nx=400/xOrder=2" + "/KIN_HAT/HRQ/" + "Figures/" + dataName

    REF1    = PATHREF + "Nr=8/Raf=3/Nx=400/xOrder=1" + "/KIN_HAT/HRQ/" + "Figures/" + dataName
    REF2    = PATHREF + "Nr=8/Raf=3/Nx=400/xOrder=2" + "/KIN_HAT/HRQ/" + "Figures/" + dataName

    Store = PATH1D + "/dR=" + dRstr + "/Figures/"

    ######################################
    ######################################


    lCol = [    "blue","blue","blue","blue","blue",
                "red","red","red","red","red"]
    lMark = [   "","","","","",
                "o","s","h","^","*"]
    lMarkSize = [   1,1,1,1,1,
                    5,5,5,5,5]
    lMarkWidth = [  1,1,1,1,1,
                    2,2,2,2,2]
    MarkPoints = 20

    lLineSize = [   2,2,2,2,2,
                    1,1,1,1,1]

    lStyle = [      "-","-","-","-","-",
                    "--","--","--","--","--"]
    lAlpha = [  1,1,1,1,1,
                1,1,1,1,1]

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

    lXScale     = [ 1,1,1,1,1,
                    1,1,1,1,1]
    lYScale     = [ 1,1,1,1,1,
                    1,1,1,1,1]

    lXOffset    = [ 0.,0.,0.,0.,0.,
                    0.,0.,0.,0.,0.]
    lYOffset    = [ 0.,0.,0.,0.,0.,
                    0.,0.,0.,0.,0.]

    lText = [ r"$t=0.1$, $t=0.2$, $t=0.3$, $t=0.4$, $t=0.5$"]
    lTextAlign = ["center"]
    lTextPos = [[0.5,1.05]]
    lTextColor = ["black"]

    xLabel=r"$x$ $\left[cm\right]$"
    yLabel=r"$Q$ $\left[\frac{cm^3}{s}\right]$"

    lLabel = [  r"$1$","","","","",
                r"$2$","","","",""]

    liX = [ 0,0,0,0,0,
            0,0,0,0,0]

    liY = [ 1,2,3,4,5,
            1,2,3,4,5]

    lFileSep    = [ ",",",",",",",",",",
                    ",",",",",",",",","]

    lFile = [   REF2,REF2,REF2,REF2,REF2,
                Data2,Data2,Data2,Data2,Data2]

    title = "Q_t.pdf"
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
