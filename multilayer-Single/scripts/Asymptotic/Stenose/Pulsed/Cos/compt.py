#!/usr/bin/python3
import sys, getopt
from csv_libPlot import *

import numpy as np

def main(argv) :

    # PATHS
    ###########

    HOME = "/Users/Arthur/"
    PATH = HOME + "Documents/UPMC/These/Codes/multilayerSingle/example/Well-Balance/Asymptotic/Stenose/Pulsed/Cos/Rvar/"

    nfig = 1

    Restr   = "100"
    Womstr  = "15"
    Shstr   = "1e-2"

    Sh      = r"$10^{-2}$"

    Lstr    = "25"
    Lstenstr= "10"

    Rtstr   = "0"

    Re_c    = float(Restr) ;
    Wom_c   = float(Womstr) ;
    Sh_c    = float(Shstr) ;

    R_c     = 1. ;
    rho_c   = 1. ;

    for Kstr in [ "1e5" ] :

        c_c     = np.sqrt( float(Kstr)/2./rho_c * np.sqrt(np.pi)*R_c )
        U_c     = Sh_c * c_c ;
        mu_c    = U_c * R_c / Re_c ;
        nu_c    = mu_c/rho_c

        T_c = 2. * np.pi / nu_c * ( (R_c / Wom_c )**2. )


        if (Kstr == "1e5") :
            K_c = r"$10^5$"

        for dRstr in [ "-0.4" ] :

            #Choose number of layers & Choose number of cells

            for xPos in ["0p025Le","0p1Le","0p225Le"] :

                J = "3200" ; L = "32"; Label = xPos ; Label1_c = r"$\frac{x}{R_{e,R}R\rvert_{x=0}}$=$0.025$" ;

                dataName = "Artery_0_" + str(Label) + "_t_R0_A0_K_R_RmR0_A_Q_U_U0_P_gradP_E_Tw_Cf_Sh.csv"

                Sten    = PATH + "K=" + str(Kstr) + "/Re=" + str(Restr) + "/a=" + str(Womstr) + "/Sh=" + str(Shstr) + "/Length=" + str(Lstr) + "/dR=" + str(dRstr) + "/Lst=" + str(Lstenstr) + "/Rt=" + str(Rtstr) + "/L=" + str(L) + "/Raf=0/J=" +str(J) + "/" + "HRQ/Order=1/KIN_HAT/Figures/" + dataName
                Wom     = PATH + "K=" + str(Kstr) + "/Re=" + str(Restr) + "/a=" + str(Womstr) + "/Sh=" + str(Shstr) + "/Length=" + str(Lstr) + "/dR=" + str(0)     + "/Lst=" + str(Lstenstr) + "/Rt=" + str(Rtstr) + "/L=" + str(L) + "/Raf=0/J=" +str(J) + "/" + "HRQ/Order=1/KIN_HAT/Figures/" + dataName

                if (Label == "0p025Le") :
                    Label_c = r"$\frac{x}{R_{e,R}R\rvert_{x=0}}$=$0.025$" ;
                if (Label == "0p1Le") :
                    Label_c = r"$\frac{x}{R_{e,R}R\rvert_{x=0}}$=$0.1$" ;
                if (Label == "0p175Le") :
                    Label_c = r"$\frac{x}{R_{e,R}R\rvert_{x=0}}$=$0.175$" ;
                if (Label == "0p225Le") :
                    Label_c = r"$\frac{x}{R_{e,R}R\rvert_{x=0}}$=$0.225$" ;

                # PLOTING :
                ###########
                it = 0 ; ix = 1 ; iR0 = 2 ; iA0 = 3 ; iK = 4 ;
                iR = 5 ; iRmR0 = 6 ; iA = 7 ;
                iQ = 8 ; iU = 9 ; iU0 = 10 ;
                iP = 11 ; igradxP = 12 ; iE = 13 ;
                iTw = 14 ; iCf = 15 ; iSh = 16 ;

                Store = PATH + "K=" + str(Kstr) + "/Re=" + str(Restr) + "/a=" + str(Womstr) + "/Sh=" + str(Shstr) + "/Length=" + str(Lstr) + "/dR=" + str(dRstr) + "/Lst=" + str(Lstenstr) + "/Rt=" + str(Rtstr) +  "/Figures/"

                lCol        = ["red","blue"]
                lMark       = ["","o"]
                lMarkSize   = [1,9]
                lMarkWidth  = [1,2]

                MarkPoints  = 100 ;

                lLineSize   = [4,4]
                lStyle      = ["-",""]
                lAlpha      = [1,0.7]

                xBins       = 6
                yBins       = 2

                xRange      = [4,5]
                yRange      = []

                xMargin     = 0.
                yMargin     = 0.2

                lXScale     = [ T_c,T_c]
                pScale      = "linear"

                lXOffset    = [0.*T_c,0.*T_c]
                lYOffset    = [0.,0.]

                lHline          = [0]
                lHlineColor     = ["black"]
                lHlineWidth     = [2,2]
                lHlineStyle     = ["--"]

                lVline          = []
                lVlineColor     = []
                lVlineWidth     = []
                lVlineStyle     = []

                lAffline        = []
                lAfflineColor   = []
                lAfflineStyle   = []
                lAfflineWidth   = []

                LegLoc      = 3
                LegPos      = [0.72,0.023]
                LegCol      = 1
                LegSize     = 25

                lTextPos    = [ [0.15,0.905],[0.35,0.915],[0.54,0.905],[0.82,0.885],
                                [0.25,0.04],[0.6,0.05]]
                lText       = [ r"$R_{e,R}$="+str(Restr),r"$\alpha$="+str(Womstr),r"$S_h$="+str(Sh),Label_c,
                                r"$N_x$="+str(J)+r", $N_r$="+str(L),r"$K$="+str(K_c)]
                lTextAlign  = ["center","center","center","center","center","center"]
                lTextColor  = ["black","black","black","black","black","black"]

                xLabel      = r"$t \times T_c^{-1}$"

                lLabel      = [
                                r"$\Delta R$="+str(0),r"$\Delta R$="+str(dRstr)
                                ]

                liX         = [it,it]

                lFileSep    = [",",","]
                lFile       = [Wom,Sten]

                postTitle = "_Comp_t_x_" + Label +"_K_"+str(Kstr) + ".pdf"

                #####
                # Tw
                #####
                yLabel      = r"$ \tau_w \times \left[ \mu \frac{u_{x}\rvert_{x=0}}{R\rvert_{x=0}} \right]^{-1}$"
                liY         = [iTw,iTw]
                lYScale     = [mu_c * U_c / R_c,mu_c * U_c / R_c]
                yRange      = [-25,45]
                title       = "Tw" + postTitle
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
                yLabel      = r"$p \times \left[ \rho u_{x}\rvert_{x=0}^2 \right]^{-1}$"
                liY         = [iP,iP]
                lYScale     = [U_c * U_c,U_c * U_c]
                yRange      = [-25,125]
                title       = "P" + postTitle
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
                # # gradxP
                # #####
                yLabel      = r"$\nabla_x p \times \left[ \rho u_{x}\rvert_{x=0}^2 \times \left[R_{e,R}R\rvert_{x=0} \right]^{-1} \right]^{-1}$"
                liY         = [igradxP,igradxP]
                lYScale     = [U_c * U_c / (Re_c * R_c),U_c * U_c / (Re_c * R_c)]
                yRange      = [-800,800]
                title       = "gradxP" + postTitle
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
                yLabel      = r"$u_{x}\rvert_{r=0} \times \left[u_{x}\rvert_{x=0}\right]^{-1}$"
                liY         = [iU0,iU0]
                lYScale     = [U_c,U_c]
                yRange      = []
                title       = "U0" + postTitle
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
                # # Q
                # #####
                yLabel      = r"$Q \times \left[Q\rvert_{x=0}\right]^{-1}$"
                liY         = [iQ,iQ]
                lYScale     = [np.pi*R_c*R_c*U_c,np.pi*R_c*R_c*U_c]
                yRange      = [-0.1,1.1]
                title       = "Q" + postTitle
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
                # # Sh
                # #####
                yLabel      = r"$S_h$"
                liY         = [iSh,iSh]
                lYScale     = [1.,1.]
                yRange      = []
                title       = "Sh" + postTitle
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
