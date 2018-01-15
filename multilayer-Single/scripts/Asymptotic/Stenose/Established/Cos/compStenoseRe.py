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

    Restr = "100"
    Ustr = "100"
    Lstr = "25"
    Lstenstr = "10"

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

            J1 = "1600" ; L1 = "32"; R1 = "100"
            Sten_1  = PATH + "K=" + str(Kstr) + "/Re=" + str(R1) + "/U=" + str(Ustr) + "/Length=" + str(Lstr) + "/dR=" + str(dRstr) + "/Lst=" + str(Lstenstr) + "/L=" + str(L1) + "/Raf=0/J=" +str(J1) + "/" + "HRQ/Order=1/KIN_HAT/Figures/" + dataName

            J2 = "1600" ; L2 = "32"; R2 = "500"
            Sten_2  = PATH + "K=" + str(Kstr) + "/Re=" + str(R2) + "/U=" + str(Ustr) + "/Length=" + str(Lstr) + "/dR=" + str(dRstr) + "/Lst=" + str(Lstenstr) + "/L=" + str(L2) + "/Raf=0/J=" +str(J2) + "/" + "HRQ/Order=1/KIN_HAT/Figures/" + dataName

            J3 = "1600" ; L3 = "32"; R3 = "1000"
            Sten_3  = PATH + "K=" + str(Kstr) + "/Re=" + str(R3) + "/U=" + str(Ustr) + "/Length=" + str(Lstr) + "/dR=" + str(dRstr) + "/Lst=" + str(Lstenstr) + "/L=" + str(L3) + "/Raf=0/J=" +str(J3) + "/" + "HRQ/Order=1/KIN_HAT/Figures/" + dataName


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

            lCol = ["red","black","green","blue"]
            lMark = ["","^","D","o"]
            lMarkSize = [1,9,9,9]
            lMarkWidth = [1,2,2,2]

            MarkPoints = 40 ;

            lLineSize = [3,1,1,1]
            lStyle = ["-","","",""]
            lAlpha = [1,0.7,0.7,0.7]

            xRange = []
            yRange = []

            lHline      = [0]
            lHlineColor = ["black"]
            lHlineWidth = [2]
            lHlineStyle = ["-"]

            lVline      = [0.10]
            lVlineColor = ["black"]
            lVlineWidth = [2]
            lVlineStyle = ["--"]

            liX = [0,ix,ix,ix]

            xLabel=r"$x \times \left[ R_{e,R} R_{|x=0} \right]^{-1}$"

            lXScale = [1., Re_c * R_c, Re_c * R_c ,Re_c * R_c]
            lXOffset = [0.,0.,0.,0.]

            lLabel = [
                      r"$Steady$",
                      r"$Re$="+str(R1),
                       r"$Re$="+str(R2),
                       r"$Re$="+str(R3)
                      ]

            lTextPos = [[0.15,0.91],[0.25,0.05],[0.75,0.05]]
            lText = [r"$R_{e,R}$="+str(Restr),r"$K$="+str(K_c),r"$\Delta R$="+str(dRstr)]
            lTextAlign = ["center","center","center"]
            lTextColor = ["black","black","black"]

            lFileSep = [",",",",",",","]
            lFile = [ANA , Sten_1, Sten_2, Sten_3 ]

            if (dRstr == "-0.4") :
                postTitle = "_Sten_K_"+str(Kstr)+".pdf"
            else :
                postTitle = "_Ane_K_"+str(Kstr)+".pdf"

            #####
            # Tw
            #####
            LegLoc = 1
            LegPos = [1.,0.98]
            if (dRstr == "+0.4") :
                LegPos = [1.,0.6]
            LegCol = 1

            yLabel = r"$\tau_w \times \left[ \mu \frac{u_{x_{|x=0}}}{R_{|x=0}} \right]^{-1}$"
            liY = [5,iTw,iTw,iTw]
            lYScale = [1., U_c * R_c / float(R1) * U_c / R_c, U_c * R_c / float(R2) * U_c / R_c, U_c * R_c / float(R3) * U_c / R_c]
            lYOffset = [0.,0.,0.,0.]
            title = "Tw" + postTitle
            nfig = plot_csv_adim(
                    pathStore=Store,title=title,lFile=lFile,lFileSep=lFileSep,
                    liX=liX,liY=liY,
                    xLabel=xLabel,yLabel=yLabel,lLabel=lLabel,
                    lXScale=lXScale,lYScale=lYScale,lXOffset=lXOffset,lYOffset=lYOffset,
                    xRange=xRange,yRange=yRange,
                    lHline=lHline,lHlineColor=lHlineColor,lHlineWidth=lHlineWidth,lHlineStyle=lHlineStyle,
                    lVline=lVline,lVlineColor=lVlineColor,lVlineWidth=lVlineWidth,lVlineStyle=lVlineStyle,
                    LegLoc=LegLoc,LegPos=LegPos,LegCol=LegCol,
                    lText=lText,lTextPos=lTextPos,lTextAlign=lTextAlign,lTextColor=lTextColor,
                    lCol=lCol,lMark=lMark,
                    lMarkSize=lMarkSize,lMarkWidth=lMarkWidth,MarkPoints=MarkPoints,
                    lLineSize=lLineSize,lStyle=lStyle,lAlpha=lAlpha,nf=nfig)

            # #####
            # # P
            # #####
            LegLoc = 1
            LegPos = [1.,0.98]
            LegCol = 1

            yLabel = r"$\left[p-p_{|x=0}\right] \times \left[ \rho u_{x_{|x=0}}^2 \right]^{-1}$"
            liY = [2,iP,iP,iP]
            lYScale = [1., U_c * U_c, U_c * U_c, U_c * U_c]
            lYOffset = ["first","first","first","first"]
            title = "P" + postTitle
            nfig = plot_csv_adim(
                    pathStore=Store,title=title,lFile=lFile,lFileSep=lFileSep,
                    liX=liX,liY=liY,
                    xLabel=xLabel,yLabel=yLabel,lLabel=lLabel,
                    lXScale=lXScale,lYScale=lYScale,lXOffset=lXOffset,lYOffset=lYOffset,
                    xRange=xRange,yRange=yRange,
                    lHline=lHline,lHlineColor=lHlineColor,lHlineWidth=lHlineWidth,lHlineStyle=lHlineStyle,
                    lVline=lVline,lVlineColor=lVlineColor,lVlineWidth=lVlineWidth,lVlineStyle=lVlineStyle,
                    LegLoc=LegLoc,LegPos=LegPos,LegCol=LegCol,
                    lText=lText,lTextPos=lTextPos,lTextAlign=lTextAlign,lTextColor=lTextColor,
                    lCol=lCol,lMark=lMark,
                    lMarkSize=lMarkSize,lMarkWidth=lMarkWidth,MarkPoints=MarkPoints,
                    lLineSize=lLineSize,lStyle=lStyle,lAlpha=lAlpha,nf=nfig)


            # #####
            # # U0
            # #####
            LegLoc = 2
            LegPos = [0.35,0.5]
            if (dRstr == "+0.4") :
                LegLoc = 1
                LegPos = [0.9,0.955]
            LegCol = 1

            yLabel = r"$u_{x_{|r=0}} \times u_{x_{|x=0}}^{-1}$"
            liY = [6,iU0,iU0,iU0]
            lYScale = [1., U_c, U_c, U_c]
            lYOffset = [0.,0.,0.,0.]
            title = "U0" + postTitle
            nfig = plot_csv_adim(
                    pathStore=Store,title=title,lFile=lFile,lFileSep=lFileSep,
                    liX=liX,liY=liY,
                    xLabel=xLabel,yLabel=yLabel,lLabel=lLabel,
                    lXScale=lXScale,lYScale=lYScale,lXOffset=lXOffset,lYOffset=lYOffset,
                    xRange=xRange,yRange=yRange,
                    lHline=lHline,lHlineColor=lHlineColor,lHlineWidth=lHlineWidth,lHlineStyle=lHlineStyle,
                    lVline=lVline,lVlineColor=lVlineColor,lVlineWidth=lVlineWidth,lVlineStyle=lVlineStyle,
                    LegLoc=LegLoc,LegPos=LegPos,LegCol=LegCol,
                    lText=lText,lTextPos=lTextPos,lTextAlign=lTextAlign,lTextColor=lTextColor,
                    lCol=lCol,lMark=lMark,
                    lMarkSize=lMarkSize,lMarkWidth=lMarkWidth,MarkPoints=MarkPoints,
                    lLineSize=lLineSize,lStyle=lStyle,lAlpha=lAlpha,nf=nfig)

if __name__ == "__main__":
   main(sys.argv[1:])
