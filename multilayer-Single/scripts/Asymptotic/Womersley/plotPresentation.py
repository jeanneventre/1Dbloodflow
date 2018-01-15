#!/usr/bin/python3
import sys, getopt
from csv_libPlot import *

def main(argv) :

    # PATHS
    ###########

    HOME = "/Users/Arthur/"

    PATH    = HOME + "Documents/UPMC/These/Codes/multilayerSingle/example/Well-Balance/Asymptotic/Womersley/"
    PATH1D  = HOME + "Documents/UPMC/These/Codes/bloodflowSingle/example/Well-Balance/Asymptotic/Womersley/"

    PATHWOM_20 = HOME + "Documents/UPMC/These/Codes/multilayerSingle/example/Well-Balance/Asymptotic/Womersley/Womersley/a=20/"
    PATHWOM_15 = HOME + "Documents/UPMC/These/Codes/multilayerSingle/example/Well-Balance/Asymptotic/Womersley/Womersley/a=15/"
    PATHWOM_10 = HOME + "Documents/UPMC/These/Codes/multilayerSingle/example/Well-Balance/Asymptotic/Womersley/Womersley/a=10/"
    PATHWOM_5 = HOME + "Documents/UPMC/These/Codes/multilayerSingle/example/Well-Balance/Asymptotic/Womersley/Womersley/a=5/"

    # FILE :
    ###########
    dataName = "Artery_0_x_R0_A0_K_R_RmR0_A_Q_U_U0_P_gradP_E_Tw_Cf_a.csv"
    dataName1D = "Artery_0_x_R0_A0_K_R_RmR0_A_Q_U_P_gradxP_E_Hrbc_Nrbc_G_fst_Twst_Tw_Fr.csv"

    nfig = 1

    Kstr = "1.e4"
    dRstr = "1e-3"

    NNstr = "Newtonian"

    L_c   = 200.

    Store = PATH + "Presentation/"

    for Womstr in ["5" , "20"] :

        for pType in ["Tw"] :

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
            Nr = "128"

            #Choose number of cells

            Wom    = PATH + "T_12/" + "a="+str(Womstr) + "/K=" + str(Kstr) + "/dR=" + str(dRstr) + "/L=" + str(Nr) + "/Raf=0/J=" +str(Nx) + "/" + "HRQ/Order=1/KIN_HAT/Figures/" + dataName

            phi1 = "-4"
            Wom1_1D   = PATH1D + "a="+str(Womstr) + "/" + "K=" + str(Kstr) + "/dR=" + str(dRstr) + "/" + str(NNstr) + "/phi=" + str(phi1) + "/J=" +str(Nx) + "/" + "HRQ/Order=1/KIN_HAT/Figures/" + dataName1D
            phi2 = "-11"
            Wom2_1D   = PATH1D + "a="+str(Womstr) + "/" + "K=" + str(Kstr) + "/dR=" + str(dRstr) + "/" + str(NNstr) + "/phi=" + str(phi2) + "/J=" +str(Nx) + "/" + "HRQ/Order=1/KIN_HAT/Figures/" + dataName1D
            phi3 = "-21"
            Wom3_1D   = PATH1D + "a="+str(Womstr) + "/" + "K=" + str(Kstr) + "/dR=" + str(dRstr) + "/" + str(NNstr) + "/phi=" + str(phi3) + "/J=" +str(Nx) + "/" + "HRQ/Order=1/KIN_HAT/Figures/" + dataName1D
            phi4 = "-4"
            Wom4_1D   = PATH1D + "a="+str(Womstr) + "/" + "K=" + str(Kstr) + "/dR=" + str(dRstr) + "/" + str(NNstr) + "/phi=" + str(phi4) + "/J=" +str(Nx) + "/" + "HRQ/Order=1/KIN_HAT/Figures/" + dataName1D

            # PLOTING :
            ###########
            it = 0 ; ix = 1 ; iR0 = 2 ; iA0 = 3 ; iK = 4 ;
            iR = 5 ; iRmR0 = 6 ; iA = 7 ;
            iQ = 8 ; iU = 9 ; iU0 = 10 ;
            iP = 11 ; igradxP = 12 ; iE = 13 ;
            iTw = 14 ; iCf = 15 ; ia = 16 ;

            ######################################
            ######################################
            lCol        = [
                            "red","blue","seagreen"
                            ]

            lMark       = [
                            "","",""
                            ]
            lMarkSize   = [ 15 ]
            lMarkWidth  = [ 1 ]

            if (Womstr == "5") :
                MarkPoints = 80 ;
            elif (Womstr == "20") :
                MarkPoints = 100 ;

            lStyle      = [
                            "-","--"
                            ]
            lLineSize   = [ 5 ]
            lAlpha      = [ 1. ]

            LegLoc      = 1
            LegPos      = [1.,1.]
            LegCol      = 1
            LegSize     = 35

            xRange      = []
            if (Womstr == "5" and pType == "Tw") :
                yRange      = [-0.6,0.45]
            elif (Womstr == "20" and pType == "Tw") :
                yRange      = [-0.12,0.12]
            else :
                yRange      = []

            xMargin     = 0.
            yMargin     = 0.2

            xBins       = 3 ;
            yBins       = 4 ;

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

            if (pType == "Tw") :
                ANA = PATHWOM  + "womTwx.csv"
                yLabel=r"$\tau_w$ $\left[ \frac{\mathrm{g}}{\mathrm{cm}.\mathrm{s}^2} \right]$"
                iY = 14
                iY1D = 18
                iYScale1D = -1
            if (pType == "Q") :
                ANA = PATHWOM  + "womQx.csv"
                yLabel=r"$Q$ $\left[ \frac{cm^3}{s} \right]$"
                iY = 8
                iY1D = 8
                iYScale1D = 1
            if (pType == "P") :
                ANA = PATHWOM  + "womPx.csv"
                yLabel=r"$P$ $\left[ \frac{g}{cm.s^2} \right]$"
                iY = 11
                iY1D = 10
                iYScale1D = 1

            lXScale     = [ L_c ]
            lYScale     = [ 1.,1.,iYScale1D ]

            pScale      = "linear"

            lXOffset    = [ 0.]
            lYOffset    = [ 0. ]

            lFileSep    = [ ","]
            liX         = [
                            0,1,1
                            ]
            liY         = [
                            1,iY,iY1D
                            ]

            lText       = [r"$\alpha$="+str(Womstr),r"$N_x$=" + str(Nx) + r" $\rvert$ $N_r$=" + str(Nr)]
            lTextHAlign = [ "left","center"]
            lTextVAlign = [ "top","center"]
            lTextPos    = [ [0.01,0.98],[0.5,0.04] ]
            lTextColor  = [ "black","black" ]
            lTextSize   = [LegSize,LegSize]

            xLabel      =   r"$x \times L^{-1}$"
            LabelSize   = LegSize

            lLabel      = [
                            "Analytic","Multiring"
                            ]

            ###########################################################
            # Reference
            ###########################################################

            lFile       = [
                            ANA
                            ]

            title = "Presentation_" + pType + "_Wom_"+str(Womstr) + "_Reference_" + str(Nx) + "_Nr_" + str(Nr) + ".pdf"

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

            ###########################################################
            # Multiring
            ###########################################################

            lFile       = [
                            ANA ,Wom
                            ]

            title = "Presentation_" + pType + "_Wom_"+str(Womstr) + "_Multiring__" + str(Nx) + "_Nr_" + str(Nr) + ".pdf"

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
