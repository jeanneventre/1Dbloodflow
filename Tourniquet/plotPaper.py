#!/usr/bin/python3
import  sys, getopt
import  numpy       as np

import  help_Output as out
import pathlib
from    csv_libPlot import *
from    help_Wave   import *

def main(argv) :

    # PATHS
    ###########
    #LINUX
    HOME = "/home/ventre/"
    PATH1D  = HOME + "/Documents/Boulot/Thèse/code/bloodflow/bloodflow/Examples/Asymptotic/Tourniquet/NonNewtonian/"
    #PATHANA = HOME + "/Documents/Boulot/These/code/bloodflow/bloodflow/Examples/Asymptotic/Tourniquet/NonNewtonian/Analytic/"
    #MAC 
    # HOME = "/home/ventre/"
    # PATH1D  = HOME + "/Documents/Boulot/Thèse/code/bloodflow/bloodflow/Examples/Asymptotic/Tourniquet/NonNewtonian/"

    Fig = PATH1D + "Figures/"
    pathlib.Path(Fig).mkdir(parents=True, exist_ok=True) 
    nfig = 1

    dtstr       = "1e-5"
    tOrderstr   = "2"
    xOrderstr   = "2"

    Kstr        = "1e4"
    NNstr       = "NonNewtonian"

    dRstr       = "1e-1"
    Nxstr       = "10"

    HRstr       = "HRQ"
    Solverstr   = "KIN_HAT"

    PATH    = PATH1D + "K=" + Kstr + "/" + NNstr + "/dR=" + dRstr #+ "/" + "Nx=" + Nxstr + "/" + "xOrder=" + xOrderstr + "/" + "dt=" + dtstr + "/" + "tOrder=" + tOrderstr + "/" + Solverstr + "/" + HRstr + "/"
    Store   = PATH1D + "Figures/"

    for pType in ["Q","A","U"] :

        pName,pLabel = out.getType(pType)

        # FILE :
        ###########
        ArtName0    = "Artery_0_x_"
        PATHEND     = "/dt=" + dtstr + "/tOrder=" + tOrderstr + "/KIN_HAT" + "/" + HRstr + "/Figures/" + ArtName0 + pName

        J1 = "100"
        Art0_11  = PATH + "/Nx=" + Nxstr + "/xOrder=" + "1" + PATHEND
        Art0_12  = PATH + "/Nx=" + Nxstr + "/xOrder=" + "2" + PATHEND

        # ANALYTIC
        ###########
        #ANA = PATHANA + pType + ".csv"

        ######################################
        ######################################
        lCol = [    "black","blue","red","seagreen","purple",
                    "black","blue","red","seagreen","purple"]
        lMark = [   "o","o","o","o","o",
                    "s","s","s","s","s"]
        lMarkSize = [   5,5,5,5,5,
                        5,5,5,5,5]
        lMarkWidth = [  1,1,1,1,1,
                        1,1,1,1,1]
        MarkPoints = 100

        lLineSize = [   2,2,2,2,2,
                        2,2,2,2,2]
        lStyle = [      "","","","","",
                        "","","","",""]
        lAlpha = [  1,1,1,1,1,
                    1,1,1,1,1]

        LegLoc      = 1
        LegPos      = [1.,1.]
        LegCol      = 1
        LegSize     = 19

        xRange      = []
        yRange      = [] 
        xMargin = 0 
        yMargin = 0

        xBins       = 2 ;
        yBins       = 2 ;

        lHline      = []
        lHlineColor = []
        lHlineWidth = []
        lHlineStyle = []

        lVline      = []
        lVlineColor = []
        lVlineWidth = []
        lVlineStyle = []
        
        lAffline = []
        lAfflineColor = []
        lAfflineWidth = []
        lAfflineStyle = []

        xScale = 10.
        lXScale     = [ xScale,xScale,xScale,xScale,xScale,
                        xScale,xScale,xScale,xScale,xScale]
        yScale      = 1.
        lYScale     = [ yScale,yScale,yScale,yScale,yScale,
                        yScale,yScale,yScale,yScale,yScale]
        pScale      = "linear"

        xOffset     = xScale/2.
        lXOffset    = [ xOffset,xOffset,xOffset,xOffset,xOffset,
                        xOffset,xOffset,xOffset,xOffset,xOffset]
        lYOffset    = [ 0.,0.,0.,0.,0.,
                        0.,0.,0.,0.,0.]

        lText       = []
        lTextAlign  = [ "left", "right", "left" ]
        lTextPos    = [ [0.02,0.05],[0.98,0.04],[0.02,0.945] ]
        lTextColor  = [ "black", "black","black" ]

        xLabel=r"$x/L$"
        yLabel = pLabel
        lLabel = [  r"$N_x$="+Nxstr+", order 1","","","","",
                    r"$N_x$="+Nxstr+", order 2","","","",""
                    ]

        lFileSep    = [ ",",",",",",",",",",
                        ",",",",",",",",","]
        liX         = [ 0,0,0,0,0,
                        0,0,0,0,0]
        liY         = [ 1,2,3,4,5,
                        1,2,3,4,5]

        lFile       = [ Art0_11,Art0_11,Art0_11,Art0_11,Art0_11,
                        Art0_12,Art0_12,Art0_12,Art0_12,Art0_12
                        ]

        title = pType + "-x.pdf"
        nfig = plot_csv_adim(pathStore=Store,title=title,lFile=lFile,lFileSep=lFileSep,
                            liX=liX,liY=liY,
                            xLabel=xLabel,yLabel=yLabel,lLabel=lLabel,
                            xRange=xRange,yRange=yRange,xMargin=xMargin,yMargin=yMargin,
                            xBins=xBins,yBins=yBins,
                            lHline=lHline,lHlineColor=lHlineColor,lHlineWidth=lHlineWidth,lHlineStyle=lHlineStyle,
                            lVline=lVline,lVlineColor=lVlineColor,lVlineWidth=lVlineWidth,lVlineStyle=lVlineStyle,
			    lAffline=lAffline,lAfflineColor=lAfflineColor,lAfflineWidth=lAfflineWidth,lAfflineStyle=lAfflineStyle,
                            lXScale=lXScale,lYScale=lYScale,pScale=pScale,lXOffset=lXOffset,lYOffset=lYOffset,
                            LegLoc=LegLoc,LegPos=LegPos,LegCol=LegCol,LegSize=LegSize,
                            lText=lText,lTextPos=lTextPos,lTextAlign=lTextAlign,lTextColor=lTextColor,
                            lCol=lCol,lMark=lMark,lMarkSize=lMarkSize,lMarkWidth=lMarkWidth,MarkPoints=MarkPoints,
                            lLineSize=lLineSize,lStyle=lStyle,lAlpha=lAlpha,nf=nfig)



if __name__ == "__main__":
   main(sys.argv[1:])
