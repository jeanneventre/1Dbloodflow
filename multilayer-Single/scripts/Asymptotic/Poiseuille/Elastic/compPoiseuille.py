#!/usr/bin/python3
import sys, getopt
from csv_libPlot import *

def main(argv) :

    # PATHS
    ###########

    HOME = "/Users/Arthur/"
    PATH = HOME + "Documents/UPMC/These/Codes/multilayerSingle/example/Well-Balance/Asymptotic/Poiseuille/Elastic/"

    PATHPOIS = HOME + "Documents/UPMC/These/Codes/multilayerSingle/example/Well-Balance/Asymptotic/Poiseuille/Elastic/Analytic/"

    # FILE :
    ###########
    dataName = "Artery_0_x_R0_A0_K_R_RmR0_A_Q_U_U0_P_gradP_E_Tw_Cf_a.csv"

    nfig = 1

    Shstr   = "1e-1"
    Lstr    = "10"

    Sh_c    = float(Shstr) ;
    L_c     = float(Lstr) ;

    if (Shstr == "1e-1") :
        Sh_p = r"$10^{-1}$"

    for Kstr in [ "1e2"] :

        if (Kstr == "1e2") :
            K_c = r"$10^2$"
        if (Kstr == "1e3") :
            K_c = r"$10^3$"
        if (Kstr == "1e4") :
            K_c = r"$10^4$"

        for pType in [ "p","Q","R" ] :

            #Choose number of layers & Choose number of cells
            J1 = "200" ; L1 = "16" ;
            Pois_1 = PATH + "K=" + str(Kstr) + "/Sh=" + str(Shstr) + "/Length=" + str(Lstr) +  "/L=" + str(L1) + "/Raf=0/J=" +str(J1) + "/" + "HRQ/Order=1/KIN_HAT/Figures/" + dataName

            J2 = "400" ; L2 = "32" ;
            Pois_2 = PATH + "K=" + str(Kstr) + "/Sh=" + str(Shstr) + "/Length=" + str(Lstr) +  "/L=" + str(L2) + "/Raf=0/J=" +str(J2) + "/" + "HRQ/Order=1/KIN_HAT/Figures/" + dataName

            J3 = "800" ; L3 = "64" ;
            Pois_3 = PATH + "K=" + str(Kstr) + "/Sh=" + str(Shstr) + "/Length=" + str(Lstr) +  "/L=" + str(L3) + "/Raf=0/J=" +str(J3) + "/" + "HRQ/Order=1/KIN_HAT/Figures/" + dataName

            if (pType == "p") :
                ANA = PATHPOIS + "px.csv"
                iY = 11 ;
                yLabel = r"$p$ $\left[ \frac{g}{cm.s^2} \right] $"
            if (pType == "Q") :
                ANA = PATHPOIS + "Qx.csv"
                iY = 8 ;
                yLabel = r"$Q$ $\left[ \frac{cm^3}{s} \right] $"
            if (pType == "R") :
                ANA = PATHPOIS + "Rx.csv"
                iY = 5 ;
                yLabel = r"$R$ $\left[ cm \right] $"



            # PLOTING :
            ###########
            it = 0 ; ix = 1 ; iR0 = 2 ; iA0 = 3 ; iK = 4 ;
            iR = 5 ; iRmR0 = 6 ; iA = 7 ;
            iQ = 8 ; iU = 9 ; iU0 = 10 ;
            iP = 11 ; igradxP = 12 ; iE = 13 ;
            iTw = 14 ; iCf = 15 ; ia = 16 ;

            Store = PATH + "K=" + str(Kstr) + "/Sh=" + str(Shstr) + "/Length=" + str(Lstr) +  "/Figures/"

            lCol = ["red","blue"]
            lMark = ["","o"]
            lMarkSize = [1,9]
            lMarkWidth = [1,2]

            MarkPoints = 60 ;

            lLineSize = [2.5,1]
            lStyle = ["-",""]
            lAlpha = [1,0.7]
            liX = [0,ix]

            xLabel=r"$x \times L^{-1}$"

            lXScale = [L_c, L_c, L_c , L_c]
            lXOffset = [0.,0.,0.,0.]

            LegLoc = 1
            LegPos = [1.,0.97]
            LegCol = 1

            xRange = []
            yRange = []


            lHline      = []
            lHlineColor = []
            lHlineWidth = []
            lHlineStyle = []

            lLabel = [
                      r"$Steady$ $analytic$",
                      r"$Multiring$"
                      ]

            lTextPos = [[0.15,0.91],[0.5,0.04]]
            lText = [r"$\hat{R}$="+str(Sh_p),r"$N_x$=" + str(J3) + r", $N_r$="+str(L3)]
            lTextAlign = ["center","center"]
            lTextColor = ["black","black"]

            lFile = [ANA , Pois_3 ]

            liY = [1,iY,iY,iY]
            lYScale = [ 1.,1.,1.,1. ]
            lYOffset = [0.,0.,0.,0.]

            title = pType + "_x.pdf"

            nfig = plot_csv_adim(
                    pathStore=Store,title=title,lFile=lFile,
                    liX=liX,liY=liY,
                    xLabel=xLabel,yLabel=yLabel,lLabel=lLabel,
                    lXScale=lXScale,lYScale=lYScale,lXOffset=lXOffset,lYOffset=lYOffset,
                    xRange=xRange,yRange=yRange,
                    lHline=lHline,lHlineColor=lHlineColor,lHlineWidth=lHlineWidth,lHlineStyle=lHlineStyle,
                    LegLoc=LegLoc,LegPos=LegPos,LegCol=LegCol,
                    lText=lText,lTextPos=lTextPos,lTextAlign=lTextAlign,lTextColor=lTextColor,
                    lCol=lCol,lMark=lMark,
                    lMarkSize=lMarkSize,lMarkWidth=lMarkWidth,MarkPoints=MarkPoints,
                    lLineSize=lLineSize,lStyle=lStyle,lAlpha=lAlpha,nf=nfig)

if __name__ == "__main__":
   main(sys.argv[1:])
