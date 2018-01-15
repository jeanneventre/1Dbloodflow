#!/usr/bin/python3
import sys, getopt
from csv_libPlot import *

def main(argv) :

    # PATHS
    ###########

    HOME = "/Users/Arthur/"
    PATH = HOME + "Documents/UPMC/These/Codes/multilayerSingle/example/Well-Balance/Asymptotic/Womersley/"

    PATHWOM_20 = HOME + "Documents/UPMC/These/Codes/multilayerSingle/example/Well-Balance/Asymptotic/Womersley/Womersley/a=20/"
    PATHWOM_15 = HOME + "Documents/UPMC/These/Codes/multilayerSingle/example/Well-Balance/Asymptotic/Womersley/Womersley/a=15/"
    PATHWOM_10 = HOME + "Documents/UPMC/These/Codes/multilayerSingle/example/Well-Balance/Asymptotic/Womersley/Womersley/a=10/"
    PATHWOM_5 = HOME + "Documents/UPMC/These/Codes/multilayerSingle/example/Well-Balance/Asymptotic/Womersley/Womersley/a=5/"

    # FILE :
    ###########
    dataName = "Artery_0_t_r_Ux.csv"

    nfig = 1

    Kstr    = "1.e4"
    dRstr   = "1e-3"

    NNstr   = "Newtonian"

    Store   = PATH + "Presentation/"

    for Womstr in ["5", "20"] :

            #Choose Womersley number
            if (Womstr == "5") :
                PATHWOM = PATHWOM_5
            elif (Womstr == "10") :
                PATHWOM = PATHWOM_10
            elif (Womstr == "15") :
                PATHWOM = PATHWOM_15
            elif (Womstr == "20") :
                PATHWOM = PATHWOM_20

            Nx = "1600"
            for Nr in ["4","16","64"] :

                # NUMERICAL
                ###########
                Wom     = PATH + "T_12/" + "a="+str(Womstr) + "/K=" + str(Kstr) + "/dR=" + str(dRstr) + "/L=" + str(Nr) + "/Raf=0/J=" +str(Nx) + "/" + "HRQ/Order=1/KIN_HAT/Figures/" + dataName

                # ANALYTIC
                ##########
                ANA     = PATHWOM + "womProfil.csv"

                ######################################
                ######################################
                lCol        = [
                                "red","red","red",
                                "black","blue","seagreen"
                                ]

                lMark       = [
                                "","","",
                                "^","D","o",
                                ]
                lMarkSize   = [ 15 ]
                lMarkWidth  = [ 2 ]
                MarkPoints  = 2*int(Nr)

                lStyle      = [
                                "-","-","-",
                                "--","--","--"
                                ]
                lLineSize   = [ 5,5,5,
                                2,2,2]
                lAlpha      = [ 1. ]

                LegLoc      = 1
                LegPos      = [1.,0.99]
                LegCol      = 2
                LegSize     = 30

                xRange      = []
                yRange      = []

                xMargin     = 0.
                yMargin     = 0.

                xBins       = 2 ;
                yBins       = 3 ;

                lHline          = []
                lHlineColor     = []
                lHlineWidth     = []
                lHlineStyle     = []

                lVline          = []
                lVlineColor     = []
                lVlineWidth     = []
                lVlineStyle     = []

                lAffline        = []
                lAfflineColor   = []
                lAfflineStyle   = []
                lAfflineWidth   = []

                lXScale     = [ 1. ]
                lYScale     = [ 1. ]

                pScale      = "linear"

                lXOffset    = [ 0.]
                lYOffset    = [ 0.]

                lFileSep    = [ ","]
                liX         = [
                                1,3,4,
                                1,3,4
                                ]
                liY         = [ 0 ]

                xLabel      =r"$u_x$ [cm$\cdot$s$^{-1}$]"
                yLabel      = r"$r \times R^{-1}$"
                LabelSize   = LegSize

                lLabel      = [
                                "Analytic","","",
                                "2D","",""
                                ]

                #######################################################@
                # Analytic solution
                #######################################################@

                lFile       = [
                                ANA,ANA,ANA
                                ]

                lText       = [r"$\alpha$="+str(Womstr)]
                lTextHAlign = [ "left","center"]
                lTextVAlign = [ "top","center"]
                lTextPos    = [ [0.01,0.98],[0.5,0.04] ]
                lTextColor  = [ "black","black" ]
                lTextSize   = [LegSize,LegSize]

                title = "Presentation_Prof_Ux_Wom_"+str(Womstr) + "_Analytic.pdf"

                nfig = plot_csv(    pathStore=Store,title=title,lFile=lFile,lFileSep=lFileSep,
                                    liX=liX,liY=liY,
                                    xLabel=xLabel,yLabel=yLabel,lLabel=lLabel,LabelSize=LabelSize,
                                    xRange=xRange,yRange=yRange,
                                    xMargin=xMargin,yMargin=yMargin,
                                    xBins=xBins,yBins=yBins,
                                    lHline=lHline,lHlineColor=lHlineColor,lHlineWidth=lHlineWidth,lHlineStyle=lHlineStyle,
                                    lVline=lVline,lVlineColor=lVlineColor,lVlineWidth=lVlineWidth,lVlineStyle=lVlineStyle,
                                    lAffline=lAffline,lAfflineColor=lAfflineColor,lAfflineStyle=lAfflineStyle,lAfflineWidth=lAfflineWidth,
                                    lXScale=lXScale,lYScale=lYScale,pScale=pScale,lXOffset=lXOffset,lYOffset=lYOffset,
                                    LegLoc=LegLoc,LegPos=LegPos,LegCol=LegCol,LegSize=LegSize,
                                    lText=lText,lTextPos=lTextPos,lTextSize=lTextSize,lTextHAlign=lTextHAlign,lTextVAlign=lTextVAlign,lTextColor=lTextColor,
                                    lCol=lCol,lMark=lMark,lMarkSize=lMarkSize,lMarkWidth=lMarkWidth,MarkPoints=MarkPoints,
                                    lLineSize=lLineSize,lStyle=lStyle,lAlpha=lAlpha,nf=nfig)

                #######################################################@
                # Multiring solution
                #######################################################@

                lFile       = [
                                ANA,ANA,ANA,
                                Wom,Wom,Wom
                                ]

                lText       = [r"$\alpha$="+str(Womstr),r"$N_x$=" + str(Nx) + r" $\rvert$ $N_r$=" + str(Nr)]
                lTextHAlign = [ "left","center"]
                lTextVAlign = [ "top","center"]
                lTextPos    = [ [0.01,0.98],[0.5,0.04] ]
                lTextColor  = [ "black","black" ]
                lTextSize   = [LegSize,LegSize]

                title = "Presentation_Prof_Ux_Wom_"+str(Womstr) + "_O1_x_25_Nx_" + str(Nx) + "_Nr_" + str(Nr) + ".pdf"

                nfig = plot_csv(    pathStore=Store,title=title,lFile=lFile,lFileSep=lFileSep,
                                    liX=liX,liY=liY,
                                    xLabel=xLabel,yLabel=yLabel,lLabel=lLabel,LabelSize=LabelSize,
                                    xRange=xRange,yRange=yRange,
                                    xMargin=xMargin,yMargin=yMargin,
                                    xBins=xBins,yBins=yBins,
                                    lHline=lHline,lHlineColor=lHlineColor,lHlineWidth=lHlineWidth,lHlineStyle=lHlineStyle,
                                    lVline=lVline,lVlineColor=lVlineColor,lVlineWidth=lVlineWidth,lVlineStyle=lVlineStyle,
                                    lAffline=lAffline,lAfflineColor=lAfflineColor,lAfflineStyle=lAfflineStyle,lAfflineWidth=lAfflineWidth,
                                    lXScale=lXScale,lYScale=lYScale,pScale=pScale,lXOffset=lXOffset,lYOffset=lYOffset,
                                    LegLoc=LegLoc,LegPos=LegPos,LegCol=LegCol,LegSize=LegSize,
                                    lText=lText,lTextPos=lTextPos,lTextSize=lTextSize,lTextHAlign=lTextHAlign,lTextVAlign=lTextVAlign,lTextColor=lTextColor,
                                    lCol=lCol,lMark=lMark,lMarkSize=lMarkSize,lMarkWidth=lMarkWidth,MarkPoints=MarkPoints,
                                    lLineSize=lLineSize,lStyle=lStyle,lAlpha=lAlpha,nf=nfig)

if __name__ == "__main__":
   main(sys.argv[1:])
