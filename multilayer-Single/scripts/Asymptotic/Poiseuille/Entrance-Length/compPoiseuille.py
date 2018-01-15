#!/usr/bin/python3
import sys, getopt
from csv_libPlot import *

def main(argv) :

    # PATHS
    ###########

    HOME = "/Users/Arthur/"
    PATH = HOME + "Documents/UPMC/These/Codes/multilayerSingle/example/Well-Balance/Asymptotic/Poiseuille/Entrance-Length/"

    PATHPOIS = HOME + "Dropbox/These/Codes/SOURCES_RNSPaxi/Entrance_Poiseuille/"

    # FILE :
    ###########
    dataName = "Artery_0_x_R0_A0_K_R_RmR0_A_Q_U_U0_P_gradP_E_Tw_Cf_a.csv"

    nfig = 1

    Restr = "100"
    Ustr = "100"
    Lstr = "25"

    Re_c = float(Restr) ;
    U_c = float(Ustr) ;
    R_c = 1. ;
    mu_c = U_c * R_c / Re_c ;

    for Kstr in [ "1e7"] :

        if (Kstr == "1e6") :
            K_c = r"$10^6$"
        if (Kstr == "1e7") :
            K_c = r"$10^7$"
        if (Kstr == "1e8") :
            K_c = r"$10^8$"

        #Choose number of layers & Choose number of cells
        J1 = "800" ; L1 = "32" ;
        Pois_1    = PATH + "K=" + str(Kstr) + "/Re=" + str(Restr) + "/U=" + str(Ustr) + "/Length=" + str(Lstr) +  "/L=" + str(L1) + "/Raf=0/J=" +str(J1) + "/" + "HRQ/Order=1/KIN_HAT/Figures/" + dataName

        J2 = "1600" ; L2 = "32" ;
        Pois_2    = PATH + "K=" + str(Kstr) + "/Re=" + str(Restr) + "/U=" + str(Ustr) + "/Length=" + str(Lstr) +  "/L=" + str(L2) + "/Raf=0/J=" +str(J2) + "/" + "HRQ/Order=1/KIN_HAT/Figures/" + dataName

        J3 = "3200" ; L3 = "32" ;
        Pois_3    = PATH + "K=" + str(Kstr) + "/Re=" + str(Restr) + "/U=" + str(Ustr) + "/Length=" + str(Lstr) +  "/L=" + str(L3) + "/Raf=0/J=" +str(J3) + "/" + "HRQ/Order=1/KIN_HAT/Figures/" + dataName

        ANA = PATHPOIS + "T.OUT"

        # PLOTING :
        ###########
        it = 0 ; ix = 1 ; iR0 = 2 ; iA0 = 3 ; iK = 4 ;
        iR = 5 ; iRmR0 = 6 ; iA = 7 ;
        iQ = 8 ; iU = 9 ; iU0 = 10 ;
        iP = 11 ; igradxP = 12 ; iE = 13 ;
        iTw = 14 ; iCf = 15 ; ia = 16 ;

        Store = PATH + "K=" + str(Kstr) + "/Re=" + str(Restr) + "/U=" + str(Ustr) + "/Length=" + str(Lstr) +  "/Figures/"

        lCol        = ["red","black","seagreen","blue"]
        lMark       = ["","^","D","o"]
        lMarkSize   = [1,11,10,9]
        lMarkWidth  = [1,2,2,2]

        MarkPoints  = 30 ;

        lLineSize   = [3,1,1,1]
        lStyle      = ["-","","",""]
        lAlpha      = [1,0.7,0.7,0.7]

        xBins   = 6
        yBins   = 2

        xRange  = [0,0.25]

        xMargin = 0.
        yMargin = 0.15

        lXScale     = [1., Re_c * R_c, Re_c * R_c ,Re_c * R_c]
        pScale      = "linear"

        lXOffset    = [0.,0.,0.,0.]

        lHline      = []
        lHlineColor = ["black","black"]
        lHlineStyle = ["--","--"]
        lHlineWidth = [2,2]

        lVline      = []
        lVlineColor = []
        lVlineStyle = []
        lVlineWidth = []

        lAffline        = []
        lAfflineColor   = ["black"]
        lAfflineStyle   = ["--"]
        lAfflineWidth   = [2]

        LegLoc      = 1
        LegPos      = [1.,1.]
        LegCol      = 1
        LegSize     = 25

        lTextPos    = [[0.15,0.91],[0.5,0.05]]
        lText       = [r"$R_{e,R}$="+str(Restr),r"$K$="+str(K_c)]
        lTextAlign  = ["center","center"]
        lTextColor  = ["black","black"]

        xLabel=r"$x \times \left[ R_{e,R} R\rvert_{x=0} \right]^{-1}$"


        liX     = [0,ix,ix,ix]
        lLabel  = [
                  r"$Steady$",
                  r"$N_x$="+str(J1)+r", $N_r$="+str(L1),
                  r"$N_x$="+str(J2)+r", $N_r$="+str(L2),
                  r"$N_x$="+str(J3)+r", $N_r$="+str(L3)
                  ]


        lFileSep    = [",",",",",",","]
        lFile       = [ANA , Pois_1, Pois_2, Pois_3 ]

        #####
        # Tw
        #####
        yLabel      = r"$\tau_w  \times \left[ \mu \frac{u_{x}\rvert_{x=0}}{R\rvert_{x=0}} \right]^{-1}$"
        liY         = [5,iTw,iTw,iTw]
        lYScale     = [1., mu_c * U_c / R_c, mu_c * U_c / R_c, mu_c * U_c / R_c]
        lYOffset    = [0.,0.,0.,0.]
        yRange      = [-50,400]
        lHline      = [4.]
        title       = "Tw_Pois_K_"+str(Kstr)+".pdf"
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
        LegPos      = [1.,0.8]
        yLabel      = r"$\left[p-p\rvert_{x=0} \right] \times \left[ \rho u_{x}\rvert_{x=0}^2 \right]^{-1}$"
        liY         = [2,iP,iP,iP]
        lYScale     = [1., U_c * U_c, U_c * U_c, U_c * U_c]
        lYOffset    = ["first","first","first","first"]
        yRange      = [-2.5,0]
        lHline      = [0.]
        lAffline    = [[-8,[0.25,-2.6176750366156298]]]
        title = "P_Pois_K_"+str(Kstr)+".pdf"
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
        LegPos      = [1.,0.8]
        yLabel      = r"$u_{x}\rvert_{r=0} \times \left[u_{x}\rvert_{x=0}\right]^{-1}$"
        liY         = [6,iU0,iU0,iU0]
        lYScale     = [1., U_c, U_c, U_c]
        lYOffset    = [0.,0.,0.,0.]
        yRange      = [0.99,2]
        lHline      = [1.,2.]
        title = "U0_Pois_K_"+str(Kstr)+".pdf"
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
