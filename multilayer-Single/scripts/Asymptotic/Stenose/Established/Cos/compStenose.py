#!/usr/bin/python3
import sys, getopt
from csv_libPlot import *

def main(argv) :

    # PATHS
    ###########

    HOME = "/Users/Arthur/"
    PATH = HOME + "Documents/UPMC/These/Codes/multilayerSingle/example/Well-Balance/Asymptotic/Stenose/Established/Cos/Rvar/"

    PATHSTEN = HOME + "Dropbox/These/Codes/SOURCES_RNSPaxi/Stenosis/"

    # FILE :
    ###########
    dataName = "Artery_0_x_R0_A0_K_R_RmR0_A_Q_U_U0_P_gradP_E_Tw_Cf_a.csv"

    nfig = 1

    Restr       = "100"
    Ustr        = "100"
    Lstr        = "25"
    Lstenstr    = "10"

    Re_c = float(Restr) ;
    U_c = float(Ustr) ;
    R_c = 1. ;
    mu_c = U_c * R_c / Re_c ;

    for Kstr in [ "1e7" ] :

        if (Kstr == "1e6") :
            K_c = r"$10^6$"
        if (Kstr == "1e7") :
            K_c = r"$10^7$"
        if (Kstr == "1e8") :
            K_c = r"$10^8$"

        for dRstr in [ "-0.4","+0.4" ] :

            #Choose number of layers & Choose number of cells

            J1 = "800" ; L1 = "32";
            Sten_1  = PATH + "K=" + str(Kstr) + "/Re=" + str(Restr) + "/U=" + str(Ustr) + "/Length=" + str(Lstr) + "/dR=" + str(dRstr) + "/Lst=" + str(Lstenstr) + "/L=" + str(L1) + "/Raf=0/J=" +str(J1) + "/" + "HRQ/Order=1/KIN_HAT/Figures/" + dataName

            J2 = "1600" ; L2 = "32";
            Sten_2  = PATH + "K=" + str(Kstr) + "/Re=" + str(Restr) + "/U=" + str(Ustr) + "/Length=" + str(Lstr) + "/dR=" + str(dRstr) + "/Lst=" + str(Lstenstr) + "/L=" + str(L2) + "/Raf=0/J=" +str(J2) + "/" + "HRQ/Order=1/KIN_HAT/Figures/" + dataName

            J3 = "3200" ; L3 = "32";
            Sten_3  = PATH + "K=" + str(Kstr) + "/Re=" + str(Restr) + "/U=" + str(Ustr) + "/Length=" + str(Lstr) + "/dR=" + str(dRstr) + "/Lst=" + str(Lstenstr) + "/L=" + str(L3) + "/Raf=0/J=" +str(J3) + "/" + "HRQ/Order=1/KIN_HAT/Figures/" + dataName


            if (dRstr == "-0.4") :
                ANA = PATHSTEN + "Established_Stenose_dR_0p4/T.OUT"
            if (dRstr == "+0.4") :
                ANA = PATHSTEN + "Established_Aneurysm_dR_0p4/T.OUT"

            # PLOTING :
            ###########
            it = 0 ; ix = 1 ; iR0 = 2 ; iA0 = 3 ; iK = 4 ;
            iR = 5 ; iRmR0 = 6 ; iA = 7 ;
            iQ = 8 ; iU = 9 ; iU0 = 10 ;
            iP = 11 ; igradxP = 12 ; iE = 13 ;
            iTw = 14 ; iCf = 15 ; ia = 16 ;

            Store = PATH + "K=" + str(Kstr) + "/Re=" + str(Restr) + "/U=" + str(Ustr) + "/Length=" + str(Lstr) + "/dR=" + str(dRstr) + "/Lst=" + str(Lstenstr) +  "/Figures/"

            lCol        = ["red","black","seagreen","blue"]
            lMark       = ["","^","D","o"]
            lMarkSize   = [1,9,9,9]
            lMarkWidth  = [1,2,2,2]

            MarkPoints  = 40 ;

            lLineSize   = [3,1,1,1]
            lStyle      = ["-","","",""]
            lAlpha      = [1,0.7,0.7,0.7]

            xBins       = 6
            yBins       = 2

            xRange      = [0,0.25]
            yRange      = []

            xMargin     = 0.
            yMargin     = 0.

            lXScale     = [1., Re_c * R_c, Re_c * R_c ,Re_c * R_c]
            pScale      = "linear"
            lXOffset    = [0.,0.,0.,0.]
            lYOffset    = [0.,0.,0.,0.]

            lHline          = [0]
            lHlineColor     = ["black","black"]
            lHlineWidth     = [2,2]
            lHlineStyle     = ["--","--"]

            lVline          = []
            lVlineColor     = []
            lVlineWidth     = []
            lVlineStyle     = []

            lAffline        = []
            lAfflineColor   = ["black"]
            lAfflineStyle   = ["--"]
            lAfflineWidth   = [2]

            LegLoc      = 1
            LegPos      = [1.,1.]
            LegCol      = 1
            LegSize     = 25

            lTextPos    = [[0.15,0.91],[0.25,0.05],[0.75,0.05]]
            lText       = [r"$R_{e,R}$="+str(Restr),r"$K$="+str(K_c),r"$\Delta R$="+str(dRstr)]
            lTextAlign  = ["center","center","center"]
            lTextColor  = ["black","black","black"]

            xLabel=r"$x \times \left[ R_{e,R} R\rvert_{x=0} \right]^{-1}$"

            lLabel = [
                      r"$Steady$",
                      r"$N_x$="+str(J1)+r", $N_r$="+str(L1),
                      r"$N_x$="+str(J2)+r", $N_r$="+str(L2),
                      r"$N_x$="+str(J3)+r", $N_r$="+str(L3)
                      ]

            liX         = [0,ix,ix,ix]

            lFileSep    = [",",",",",",","]
            lFile       = [ANA , Sten_1, Sten_2, Sten_3 ]

            if (dRstr == "-0.4") :
                postTitle = "_Sten_K_"+str(Kstr)+".pdf"
            else :
                postTitle = "_Ane_K_"+str(Kstr)+".pdf"

            #####
            # Tw
            #####
            LegPos  = [1.,1.]
            if (dRstr == "+0.4") :
                LegPos = [1.,0.6]

            yLabel  = r"$\tau_w \times \left[ \mu \frac{u_{x}\rvert_{x=0}}{R\rvert_{x=0}} \right]^{-1}$"
            liY     = [5,iTw,iTw,iTw]
            lYScale = [1., U_c * R_c / float(Restr) * U_c / R_c, U_c * R_c / float(Restr) * U_c / R_c, U_c * R_c / float(Restr) * U_c / R_c]
            lHline  = [0.,4.]

            title   = "Tw" + postTitle
            nfig = plot_csv_adim(
                    pathStore=Store,title=title,lFile=lFile,lFileSep=lFileSep,
                    liX=liX,liY=liY,
                    xLabel=xLabel,yLabel=yLabel,lLabel=lLabel,
                    xBins=xBins,yBins=yBins,
                    xRange=xRange,yRange=yRange,xMargin=xMargin,yMargin=yMargin,lXScale=lXScale,lYScale=lYScale,pScale=pScale,lXOffset=lXOffset,lYOffset=lYOffset,
                    lHline=lHline,lHlineColor=lHlineColor,lHlineStyle=lHlineStyle,lHlineWidth=lHlineWidth,
                    lVline=lVline,lVlineColor=lVlineColor,lVlineStyle=lVlineStyle,lVlineWidth=lVlineWidth,
                    lAffline=lAffline,lAfflineColor=lAfflineColor,lAfflineStyle=lAfflineStyle,lAfflineWidth=lAfflineWidth,
                    LegLoc=LegLoc,LegPos=LegPos,LegCol=LegCol,LegSize=LegSize,
                    lText=lText,lTextPos=lTextPos,lTextAlign=lTextAlign,lTextColor=lTextColor,
                    lCol=lCol,lMark=lMark,
                    lMarkSize=lMarkSize,lMarkWidth=lMarkWidth,MarkPoints=MarkPoints,
                    lLineSize=lLineSize,lStyle=lStyle,lAlpha=lAlpha,nf=nfig)

            # #####
            # # U0
            # #####
            LegLoc  = 1
            LegPos  = [1.,1.]
            if (dRstr == "+0.4") :
                LegLoc = 1
                LegPos = [0.9,0.94]

            yLabel  = r"$u_{x}\rvert_{r=0} \times \left[u_{x}\rvert_{x=0}\right]^{-1}$"
            liY     = [6,iU0,iU0,iU0]
            lYScale = [1., U_c, U_c, U_c]
            lHline  = [2.]
            title   = "U0" + postTitle
            nfig = plot_csv_adim(
                    pathStore=Store,title=title,lFile=lFile,lFileSep=lFileSep,
                    liX=liX,liY=liY,
                    xLabel=xLabel,yLabel=yLabel,lLabel=lLabel,
                    xBins=xBins,yBins=yBins,
                    xRange=xRange,yRange=yRange,xMargin=xMargin,yMargin=yMargin,lXScale=lXScale,lYScale=lYScale,pScale=pScale,lXOffset=lXOffset,lYOffset=lYOffset,
                    lHline=lHline,lHlineColor=lHlineColor,lHlineStyle=lHlineStyle,lHlineWidth=lHlineWidth,
                    lVline=lVline,lVlineColor=lVlineColor,lVlineStyle=lVlineStyle,lVlineWidth=lVlineWidth,
                    lAffline=lAffline,lAfflineColor=lAfflineColor,lAfflineStyle=lAfflineStyle,lAfflineWidth=lAfflineWidth,
                    LegLoc=LegLoc,LegPos=LegPos,LegCol=LegCol,LegSize=LegSize,
                    lText=lText,lTextPos=lTextPos,lTextAlign=lTextAlign,lTextColor=lTextColor,
                    lCol=lCol,lMark=lMark,
                    lMarkSize=lMarkSize,lMarkWidth=lMarkWidth,MarkPoints=MarkPoints,
                    lLineSize=lLineSize,lStyle=lStyle,lAlpha=lAlpha,nf=nfig)

            # #####
            # # P
            # #####
            LegLoc  = 1
            LegPos  = [1.,0.98]

            yLabel  = r"$\left[p-p\rvert_{x=0}\right] \times \left[ \rho u_{x}\rvert_{x=0}^2 \right]^{-1}$"
            liY     = [2,iP,iP,iP]
            lYScale = [1., U_c * U_c, U_c * U_c, U_c * U_c]
            lYOffset = ["first","first","first","first"]
            lHline      = [0.]
            lAffline    = [[-8,[0,0]]]
            title   = "P" + postTitle
            nfig = plot_csv_adim(
                    pathStore=Store,title=title,lFile=lFile,lFileSep=lFileSep,
                    liX=liX,liY=liY,
                    xLabel=xLabel,yLabel=yLabel,lLabel=lLabel,
                    xBins=xBins,yBins=yBins,
                    xRange=xRange,yRange=yRange,xMargin=xMargin,yMargin=yMargin,lXScale=lXScale,lYScale=lYScale,pScale=pScale,lXOffset=lXOffset,lYOffset=lYOffset,
                    lHline=lHline,lHlineColor=lHlineColor,lHlineStyle=lHlineStyle,lHlineWidth=lHlineWidth,
                    lVline=lVline,lVlineColor=lVlineColor,lVlineStyle=lVlineStyle,lVlineWidth=lVlineWidth,
                    lAffline=lAffline,lAfflineColor=lAfflineColor,lAfflineStyle=lAfflineStyle,lAfflineWidth=lAfflineWidth,
                    LegLoc=LegLoc,LegPos=LegPos,LegCol=LegCol,LegSize=LegSize,
                    lText=lText,lTextPos=lTextPos,lTextAlign=lTextAlign,lTextColor=lTextColor,
                    lCol=lCol,lMark=lMark,
                    lMarkSize=lMarkSize,lMarkWidth=lMarkWidth,MarkPoints=MarkPoints,
                    lLineSize=lLineSize,lStyle=lStyle,lAlpha=lAlpha,nf=nfig)


if __name__ == "__main__":
   main(sys.argv[1:])
