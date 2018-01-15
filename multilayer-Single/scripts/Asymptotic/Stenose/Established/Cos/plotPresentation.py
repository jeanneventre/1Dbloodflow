#!/usr/bin/python3
import sys, getopt
from csv_libPlot import *

def main(argv) :

    # PATHS
    ###########

    HOME = "/Users/Arthur/"
    PATH    = HOME + "Documents/UPMC/These/Codes/multilayerSingle/example/Well-Balance/Asymptotic/Stenose/Established/Cos/Rvar/"
    PATH1D  = HOME + "Documents/UPMC/These/Codes/bloodflowSingle/example/Well-Balance/Asymptotic/Stenose/Established/Cos/Rvar/"

    PATH_Steady = HOME + "Dropbox/These/Codes/SOURCES_RNSPaxi/Stenosis/"

    # FILE :
    ###########
    dataName = "Artery_0_x_R0_A0_K_R_RmR0_A_Q_U_U0_P_gradP_E_Tw_Cf_a.csv"
    dataName1D = "Artery_0_x_R0_A0_K_R_RmR0_A_Q_U_P_gradxP_E_Hrbc_Nrbc_G_fst_Twst_Tw_Fr.csv"

    nfig = 1

    Kstr        = "1e7"
    Restr       = "100"
    Ustr        = "100"
    Lstr        = "25"
    Lststr      = "10"

    K_c     = r"$10^7$"
    Re_c    = float(Restr) ;
    U_c     = float(Ustr) ;
    R_c     = 1. ;
    mu_c    = U_c * R_c / Re_c ;

    #Choose number of layers & Choose number of cells
    Nx = "1600" ;
    Nr = "32"

    for dRstr in ["-0.4","+0.4"] :

        Sten  = PATH + "K=" + str(Kstr) + "/Re=" + str(Restr) + "/U=" + str(Ustr) + "/Length=" + str(Lstr) + "/dR=" + str(dRstr) + "/Lst=" + str(Lststr) + "/L=" + str(Nr) + "/Raf=0/J=" +str(Nx) + "/" + "HRQ/Order=1/KIN_HAT/Figures/" + dataName

        phi1 = "-4"
        Sten1_1D   = PATH1D + "K=" + str(Kstr) + "/Re=" + str(Restr) + "/U=" + str(Ustr) + "/Length=" + str(Lstr) + "/dR=" + str(dRstr) + "/Lst=" + str(Lststr) + "/Newtonian" + "/phi=" + str(phi1) + "/J=" +str(Nx) + "/" + "HRQ/Order=1/KIN_HAT/Figures/" + dataName1D

        if (dRstr == "-0.4") :
            Steady = PATH_Steady + "Established_Stenose_dR_0p4/T.OUT"
        if (dRstr == "+0.4") :
            Steady = PATH_Steady + "Established_Aneurysm_dR_0p4/T.OUT"

        # PLOTING :
        ###########
        Store = PATH + "Presentation/"

        for pType in ["Tw","P"] :

            ######################################
            ######################################
            lCol        = [
                            "red","blue","seagreen"
                            ]

            lMark       = [
                            "","^","D"
                            ]
            lMarkSize   = [ 15 ]
            lMarkWidth  = [ 1 ]
            MarkPoints  = 50

            lStyle      = [
                            "-","",""
                            ]
            lLineSize   = [ 5 ]
            lAlpha      = [ 1. ]

            LegLoc      = 1
            LegPos      = [1.,1.]
            LegCol      = 1
            LegSize     = 35

            xRange      = [0,0.25]
            yRange      = []

            xMargin     = 0.
            yMargin     = 0.1

            xBins       = 3 ;
            yBins       = 4 ;

            lHline          = [0]
            lHlineColor     = ["black"]
            lHlineWidth     = [2]
            lHlineStyle     = ["-"]

            lVline          = []
            lVlineColor     = []
            lVlineWidth     = []
            lVlineStyle     = []

            lAffline        = []
            lAfflineColor   = []
            lAfflineStyle   = []
            lAfflineWidth   = []

            if (pType == "Tw") :
                yLabel      = r"$\tau_w \times \left[  \mu \frac{u\rvert_{x=0}}{R\rvert_{x=0}} \right]^{-1}$"
                iYRef       = 5
                iY          = 14
                iY1D        = 18
                YScaleRef   = 1.
                YScale      = mu_c * U_c / R_c
                YScale1D    = - mu_c * U_c / R_c
                YOffsetRef  = 0.
                YOffset     = 0.
                YOffset1D   = 0.

                if (dRstr == "-0.4") :
                    R0Scale     = 4./100.*R_c
                    R0Offset    = -1
                if (dRstr == "+0.4") :
                    R0Scale     = 4./20.*R_c
                    R0Offset    = -0.5

            if (pType == "P") :
                yLabel = r"$\left[p-p\rvert_{x=0}\right] \times \left[ \rho u_{x}^2\rvert_{x=0} \right]^{-1}$"
                iYRef       = 2
                iY          = 11
                iY1D        = 10
                YScaleRef   = 1.
                YScale      = U_c * U_c
                YScale1D    = U_c * U_c
                YOffsetRef  = "first"
                YOffset     = "first"
                YOffset1D   = "first"

            lXScale     = [ 1.,Re_c*R_c,Re_c*R_c ]
            lYScale     = [ YScaleRef,YScale,YScale1D ]

            pScale      = "linear"

            lXOffset    = [ 0.]
            lYOffset    = [ YOffsetRef,YOffset,YOffset1D]

            lFileSep    = [ ","]
            liX         = [
                            0,1,1
                            ]
            liY         = [ iYRef,iY,iY1D ]

            lText       = [r"$R_{e,R}$="+str(Re_c),r"$N_x$=" + str(Nx) + r" $\rvert$ $N_r$=" + str(Nr)]
            lTextHAlign = [ "left","center"]
            lTextVAlign = [ "top","center"]
            lTextPos    = [ [0.01,0.98],[0.5,0.04] ]
            lTextColor  = [ "black","black" ]
            lTextSize   = [LegSize,LegSize]

            xLabel      = r"$x \times \left[R_{e,R} R\rvert_{x=0}\right]^{-1}$"
            LabelSize   = LegSize

            lLabel      = [
                            "Reference","Multiring","1D"
                            ]

            ###########################################################
            # Reference
            ###########################################################

            lFile       = [
                            Steady
                            ]

            lText       = [r"$R_{e,R}$="+str(Re_c)]
            lTextHAlign = [ "left","center"]
            lTextVAlign = [ "top","center"]
            lTextPos    = [ [0.01,0.98],[0.5,0.04] ]
            lTextColor  = [ "black","black" ]
            lTextSize   = [LegSize,LegSize]

            title = "Presentation_" + pType + "_dR_" + dRstr + "_Reference.pdf"

            nfig = plot_csv_adim(pathStore=Store,title=title,lFile=lFile,lFileSep=lFileSep,
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
                            Steady,Sten
                            ]

            lText       = [r"$R_{e,R}$="+str(Re_c),r"$N_x$=" + str(Nx) + r" $\rvert$ $N_r$=" + str(Nr)]
            lTextHAlign = [ "left","center"]
            lTextVAlign = [ "top","center"]
            lTextPos    = [ [0.01,0.98],[0.5,0.04] ]
            lTextColor  = [ "black","black" ]
            lTextSize   = [LegSize,LegSize]

            title = "Presentation_" + pType + "_dR_" + dRstr + "_Multiring.pdf"

            nfig = plot_csv_adim(pathStore=Store,title=title,lFile=lFile,lFileSep=lFileSep,
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
