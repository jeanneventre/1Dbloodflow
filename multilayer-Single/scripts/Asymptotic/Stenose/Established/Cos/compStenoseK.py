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

    for dRstr in ["-0.4","+0.4"] :

        #Choose number of layers & Choose number of cells
        J = "1600" ;
        La = "32"

        K1str = "1e6"
        Sten_K1  = PATH + "K=" + str(K1str) + "/Re=" + str(Restr) + "/U=" + str(Ustr) + "/Length=" + str(Lstr) + "/dR=" + str(dRstr) + "/Lst=" + str(Lstenstr) + "/L=" + str(La) + "/Raf=0/J=" +str(J) + "/" + "HRQ/Order=1/KIN_HAT/Figures/" + dataName

        K2str = "1e7"
        Sten_K2  = PATH + "K=" + str(K2str) + "/Re=" + str(Restr) + "/U=" + str(Ustr) + "/Length=" + str(Lstr) + "/dR=" + str(dRstr) + "/Lst=" + str(Lstenstr) + "/L=" + str(La) + "/Raf=0/J=" +str(J) + "/" + "HRQ/Order=1/KIN_HAT/Figures/" + dataName

        K3str = "1e8"
        Sten_K3  = PATH + "K=" + str(K3str) + "/Re=" + str(Restr) + "/U=" + str(Ustr) + "/Length=" + str(Lstr) + "/dR=" + str(dRstr) + "/Lst=" + str(Lstenstr) + "/L=" + str(La) + "/Raf=0/J=" +str(J) + "/" + "HRQ/Order=1/KIN_HAT/Figures/" + dataName

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

        Store = PATH + "/Figures/"

        lCol = ["red","blue","green","indigo"]
        lMark = ["","o","^","s"]
        lMarkSize = [1,7,7,7]
        lMarkWidth = [1,2,2,2]

        MarkPoints = 60 ;

        lLineSize = [2.5,1,1,1]
        lStyle = ["-","","",""]
        lAlpha = [1,0.7,0.7,0.7]
        liX = [0,ix,ix,ix]

        xLabel=r"$\frac{x}{R_{e,R} R}$"

        lXScale = [1.,Re_c * R_c,Re_c * R_c,Re_c * R_c]
        lXOffset = [0.,0.,0.,0.]

        LegPos = 1
        lLabel = [r"$Steady$",r"$Multiring$, $K$=$10^6$",r"$Multiring$, $K$=$10^7$",r"$Multiring$, $K$=$10^8$"]

        lTextPos = [[0.15,0.91],[0.25,0.04],[0.75,0.05]]
        lText = [r"$R_{e,R}$="+str(Restr),r"$N_x$="+str(J)+r", $N_r$="+str(La),r"$\Delta R$="+str(dRstr)]
        lTextAlign = ["center","center","center"]
        lTextColor = ["black","black","black"]

        lFile = [ANA , Sten_K1, Sten_K2, Sten_K3 ]

        #####
        # Tw
        #####
        yLabel = r"$\frac{\tau_w}{\mu \frac{u_{x_{|x=0}}}{R_{|x=0}}}$"
        liY = [5,iTw,iTw,iTw]
        lYScale = [1., mu_c * U_c / R_c, mu_c * U_c / R_c, mu_c * U_c / R_c]
        lYOffset = [0.,0.,0.,0.]
        title = "Tw_Sten_dR_"+str(dRstr)+".pdf"
        nfig = plot_csv_adim(
                pathStore=Store,title=title,lFile=lFile,
                liX=liX,liY=liY,
                xLabel=xLabel,yLabel=yLabel,lLabel=lLabel,
                lXScale=lXScale,lYScale=lYScale,lXOffset=lXOffset,lYOffset=lYOffset,
                LegPos=LegPos,
                lText=lText,lTextPos=lTextPos,lTextAlign=lTextAlign,lTextColor=lTextColor,
                lCol=lCol,lMark=lMark,
                lMarkSize=lMarkSize,lMarkWidth=lMarkWidth,MarkPoints=MarkPoints,
                lLineSize=lLineSize,lStyle=lStyle,lAlpha=lAlpha,nf=nfig)

        # #####
        # # P
        # #####
        yLabel = r"$\frac{p-p_{|x=0}}{\rho u_{x_{|x=0}}^2}$"
        liY = [2,iP,iP,iP]
        lYScale = [1., U_c * U_c, U_c * U_c, U_c * U_c]
        lYOffset = ["first","first","first","first"]
        title = "P_Sten_dR_"+str(dRstr)+".pdf"
        nfig = plot_csv_adim(
                pathStore=Store,title=title,lFile=lFile,
                liX=liX,liY=liY,
                xLabel=xLabel,yLabel=yLabel,lLabel=lLabel,
                lXScale=lXScale,lYScale=lYScale,lXOffset=lXOffset,lYOffset=lYOffset,
                LegPos=LegPos,
                lText=lText,lTextPos=lTextPos,lTextAlign=lTextAlign,lTextColor=lTextColor,
                lCol=lCol,lMark=lMark,
                lMarkSize=lMarkSize,lMarkWidth=lMarkWidth,MarkPoints=MarkPoints,
                lLineSize=lLineSize,lStyle=lStyle,lAlpha=lAlpha,nf=nfig)


        # #####
        # # U0
        # #####
        yLabel = r"$\frac{u_{x_{|r=0}}}{u_{x_{|x=0}}}$"
        liY = [6,iU0,iU0,iU0]
        lYScale = [1., U_c, U_c, U_c]
        lYOffset = [0.,0.,0.,0.]
        title = "U0_Sten_dR_"+str(dRstr)+".pdf"
        nfig = plot_csv_adim(
                pathStore=Store,title=title,lFile=lFile,
                liX=liX,liY=liY,
                xLabel=xLabel,yLabel=yLabel,lLabel=lLabel,
                lXScale=lXScale,lYScale=lYScale,lXOffset=lXOffset,lYOffset=lYOffset,
                LegPos=LegPos,
                lText=lText,lTextPos=lTextPos,lTextAlign=lTextAlign,lTextColor=lTextColor,
                lCol=lCol,lMark=lMark,
                lMarkSize=lMarkSize,lMarkWidth=lMarkWidth,MarkPoints=MarkPoints,
                lLineSize=lLineSize,lStyle=lStyle,lAlpha=lAlpha,nf=nfig)


if __name__ == "__main__":
   main(sys.argv[1:])
