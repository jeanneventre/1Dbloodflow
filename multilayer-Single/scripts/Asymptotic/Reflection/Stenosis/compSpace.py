#! /usr/bin/python2.7
import sys, getopt
import os
import numpy        as np
import math         as mt

from csv_libPlot    import *

from help_Wave      import *

def main(argv) :

    # PATHS
    ###########

    HOME = "/Users/Arthur/"
    PATH2D = HOME + "/Documents/UPMC/These/Codes/multilayerSingle/example/Well-Balance/Asymptotic/Reflection/Stenosis/"

    nfig = 1

    drCoarsestr = "0.25"
    drFinestr   = "0.01"
    Nxstr       = "800"
    xOrderstr   = "2"

    HRstr       = "HRQ"
    Solverstr   = "KIN_HAT"

    dtstr       = "1e-5"
    tOrderstr   = "3"

    Kstr        = "1e4"
    Knlstr      = "0"

    Shstr       = "1e-3"
    dRststr     = "-0.5"
    dKststr     = "0"

    PATH    = PATH2D + "Sh=" + Shstr + "/K=" + str(Kstr) + "/Knl=" + Knlstr + "/dRst=" + dRststr + "/dKst=" + dKststr

    Store   = PATH2D + "Figures/"

    for pType in ["Q","P","U","A","RmR0","Tw"] :

        # FILE :
        ###########
        dName = "Artery_0_x_"

        if (pType == "Q") :
            pName = "Q.csv"
            pLabel = r"$Q$ $\left[\frac{cm^3}{s}\right]$"
        if (pType == "U") :
            pName = "U.csv"
            pLabel = r"$U$ $\left[\frac{cm}{s}\right]$"
        if (pType == "P") :
            pName = "P.csv"
            pLabel = r"$p$ $\left[\frac{g}{cm.s^{2}}\right]$"
        if (pType == "A") :
            pName = "A.csv"
            pLabel = r"$A$ $\left[cm^{2}\right]$"
        if (pType == "RmR0") :
            pName = "RmR0.csv"
            pLabel = r"$R-R_0$ $\left[cm\right]$"
        if (pType == "Tw") :
            pName = "Tw.csv"
            pLabel = r"$\tau_w$ $\left[\frac{g}{cm.s^{2}}\right]$"

        P1 =  "0"
        PATH  = PATH2D + "Sh=" + Shstr + "/K=" + str(Kstr) + "/Knl=" + P1 + "/dRst=" + dRststr + "/dKst=" + dKststr
        Data1 = PATH + "/drCoarse=" + drCoarsestr + "-drFine=" + drFinestr + "/Nx=" + str(Nxstr) + "/xOrder=" + str(xOrderstr) + "/dt=" + str(dtstr) + "/tOrder=" + str(tOrderstr) + "/" + str(Solverstr) + "/" + str(HRstr) +  "/Figures/" + dName + pName

        P2 =  "1e1"
        PATH  = PATH2D + "Sh=" + Shstr + "/K=" + str(Kstr) + "/Knl=" + P2 + "/dRst=" + dRststr + "/dKst=" + dKststr
        Data2 = PATH + "/drCoarse=" + drCoarsestr + "-drFine=" + drFinestr + "/Nx=" + str(Nxstr) + "/xOrder=" + str(xOrderstr) + "/dt=" + str(dtstr) + "/tOrder=" + str(tOrderstr) + "/" + str(Solverstr) + "/" + str(HRstr) +  "/Figures/" + dName + pName

        P3 =  "1e2"
        PATH  = PATH2D + "Sh=" + Shstr + "/K=" + str(Kstr) + "/Knl=" + P3 + "/dRst=" + dRststr + "/dKst=" + dKststr
        Data3 = PATH + "/drCoarse=" + drCoarsestr + "-drFine=" + drFinestr + "/Nx=" + str(Nxstr) + "/xOrder=" + str(xOrderstr) + "/dt=" + str(dtstr) + "/tOrder=" + str(tOrderstr) + "/" + str(Solverstr) + "/" + str(HRstr) +  "/Figures/" + dName + pName

        P4 =  "1e3"
        PATH  = PATH2D + "Sh=" + Shstr + "/K=" + str(Kstr) + "/Knl=" + P4 + "/dRst=" + dRststr + "/dKst=" + dKststr
        Data4 = PATH + "/drCoarse=" + drCoarsestr + "-drFine=" + drFinestr + "/Nx=" + str(Nxstr) + "/xOrder=" + str(xOrderstr) + "/dt=" + str(dtstr) + "/tOrder=" + str(tOrderstr) + "/" + str(Solverstr) + "/" + str(HRstr) +  "/Figures/" + dName + pName


        iX = 0;

        ######################################
        ######################################

        lCol        = [ "blue","red","green",
                        "blue","red","green",
                        "blue","red","green",
                        "blue","red","green"]
        lMark       = [ "","","",
                        "","","",
                        "","","",
                        "","",""]
        lMarkSize   = [ 5,5,5,
                        5,5,5,
                        5,5,5,
                        5,5,5]
        lMarkWidth  = [ 2,2,2,
                        2,2,2,
                        2,2,2,
                        2,2,2]
        MarkPoints  = 40

        lLineSize   = [ 2,2,2,
                        2,2,2,
                        2,2,2,
                        2,2,2]
        lStyle      = [ "-","-","-",
                        "--","--","--",
                        "-.","-.","-.",
                        ":",":",":"]
        lAlpha      = [ 1,1,1,
                        1,1,1,
                        1,1,1,
                        1,1,1]

        LegLoc      = 1
        LegPos      = [1.,1.]
        LegCol      = 1

        xRange      = []
        yRange      = []

        # Refine reflection coefficients
        AP = np.pi*(1.)**2. ; AD = np.pi * (0.5)**2.
        KP = float(Kstr)    ; KD = float(Kstr)
        Y1 = Admittance(1,KP,AP) ; Y2 = Admittance(1,KD,AD)
        Rt, Tt = Reflection_2Arteries(RHO=1,AP=AP,AD=AD,KP=KP,KD=KD)

        if (pType == "Q") :
            Qmax = float(Shstr) * celerity(1,KP,AP) * AP
            lHline = [Qmax,-Rt*Qmax,Y2/Y1*Tt*Qmax]
        elif (pType == "P") :
            Pmax = float(Kstr) * float(Shstr)
            lHline = [Pmax,Rt*Pmax,Tt*Pmax]
        elif (pType == "RmR0") :
            RmR0max = float(Shstr) / np.sqrt(np.pi)
            lHline = [RmR0max,Rt*RmR0max,Tt*RmR0max]
        else :
            lHline      = [0,0,0]

        lHlineColor = [ "black","blue","red"]
        lHlineWidth = [ 1,1,1]
        lHlineStyle = [ "--","--","--"]

        lVline      = []
        lVlineColor = []
        lVlineWidth = []
        lVlineStyle = []

        lXScale     = [ 1.,1.,1.,
                        1.,1.,1.,
                        1.,1.,1.,
                        1.,1.,1.]
        lYScale     = [ 1.,1.,1.,
                        1.,1.,1.,
                        1.,1.,1.,
                        1.,1.,1.]

        lXOffset    = [ 0.,0.,0.,
                        0.,0.,0.,
                        0.,0.,0.,
                        0.,0.,0.]
        lYOffset    = [ 0.,0.,0.,
                        0.,0.,0.,
                        0.,0.,0.,
                        0.,0.,0.]

        lText       = [ r"$S_h$=" + Shstr,
                        r"$K$="+str(Kstr), r"$K_{nl}$="+str(Knlstr),
                        r"$\Delta R_{st}$=" + dRststr, r"$\Delta K_{st}$=" + dKststr]
        lTextAlign  = [ "center",
                        "center", "center",
                        "center", "center"]
        lTextPos    = [ [0.25,0.925],
                        [0.5,0.935], [0.75,0.925],
                        [0.25,0.04], [0.75,0.04] ]
        lTextColor  = [ "black",
                        "black", "black",
                        "black", "black"]

        xLabel      =r"$x$ $\left[cm\right]$"
        yLabel      = pLabel
        lLabel      = [ P1, "", "",
                        P2, "", "",
                        P3, "", "",
                        P4, "", ""]

        liX         = [ 0,0,0,
                        0,0,0,
                        0,0,0,
                        0,0,0]
        liY         = [ 1,2,3,
                        1,2,3,
                        1,2,3,
                        1,2,3]
        lFileSep    = [ ",",",",",",
                        ",",",",",",
                        ",",",",",",
                        ",",",",","]
        lFile       = [ Data1,Data1,Data1,
                        Data2,Data2,Data2,
                        Data3,Data3,Data3,
                        Data4,Data4,Data4]

        title = "Comp_" + pType + "_2D_x.pdf"

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
