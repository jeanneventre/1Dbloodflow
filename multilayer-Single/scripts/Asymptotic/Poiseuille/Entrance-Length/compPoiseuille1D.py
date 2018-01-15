#!/usr/bin/python3
import sys, getopt
from csv_libPlot import *

def main(argv) :

    # PATHS
    ###########

    HOME = "/Users/Arthur/"
    PATH = HOME + "Documents/UPMC/These/Codes/multilayerSingle/example/Well-Balance/Asymptotic/Poiseuille/Entrance-Length/"

    PATH1D = HOME + "Documents/UPMC/These/Codes/bloodflowSingle/example/Well-Balance/Asymptotic/Poiseuille/"


    PATHPOIS = HOME + "Dropbox/These/Codes/SOURCES_RNSPaxi/Entrance_Poiseuille/"

    # FILE :
    ###########
    dataName = "Artery_0_x_R0_A0_K_R_RmR0_A_Q_U_U0_P_gradP_E_Tw_Cf_a.csv"
    dataName1D = "Artery_0_x_R0_A0_K_R_RmR0_A_Q_U_P_E_Tw_Cf_Fr.csv"

    nfig = 1

    Kstr = "1e8"
    Restr = "1000"
    Ustr = "100"
    Lstr = "250"

    #Choose number of layers & Choose number of cells
    J = "1600" ; J1D = "1600"
    La = "32"

    Pois    = PATH + "K=" + str(Kstr) + "/Re=" + str(Restr) + "/U=" + str(Ustr) + "/Length=" + str(Lstr) +  "/L=" + str(La) + "/Raf=0/J=" +str(J) + "/" + "HRQ/Order=1/KIN_HAT/Figures/" + dataName

    Pois_1D_8   = PATH1D + "K=" + str(Kstr) + "/Re=" + str(Restr) + "/U=" + str(Ustr) + "/Length=" + str(Lstr) +  "/phi=8"  + "/J=" +str(J1D) + "/" + "HRQ/Order=1/KIN_HAT/Figures/" + dataName1D
    Pois_1D_40  = PATH1D + "K=" + str(Kstr) + "/Re=" + str(Restr) + "/U=" + str(Ustr) + "/Length=" + str(Lstr) +  "/phi=40" + "/J=" +str(J1D) + "/" + "HRQ/Order=1/KIN_HAT/Figures/" + dataName1D


    # PLOTING :
    ###########
    it = 0 ; ix = 1 ; iR0 = 2 ; iA0 = 3 ; iK = 4 ;
    iR = 5 ; iRmR0 = 6 ; iA = 7 ;
    iQ = 8 ; iU = 9 ; iU0 = 10 ;
    iP = 11 ; igradxP = 12 ; iE = 13 ;
    iTw = 14 ; iCf = 15 ; ia = 16 ;

    iQ1D = 8 ; iTw1D = 12 ; iP1D = 10 ;

    Store = PATH + "K=" + str(Kstr) + "/Re=" + str(Restr) + "/U=" + str(Ustr) + "/Length=" + str(Lstr) +  "/Figures/"

    lCol = ["red",
                "black","blue","green"]
    lMark = ["",
                "o","",""]
    lMarkSize = [1,
                    7,1,1]
    lMarkWidth = [1,
                    2,1,1]

    MarkPoints = 60 ;

    lLineSize = [2,
                    1,2,2]
    lStyle = ["-",
                "","-","-"]
    lAlpha = [1,
                0.7,1,1]
    liX = [0,
            ix,ix,ix]

    xLabel=r"$\frac{x}{R_{e,R} R}$"

    lXScale = [1.,1000.,1000.,1000.]
    lXOffset = [0.,0.,0.,0.]

    LegPos = 1
    lLabel = [r"$Steady$",r"$Multiring$, $L$="+str(La),r"$1D$, $\gamma$=$8$",r"$1D$, $\gamma$=$40$",""]

    lTextPos = [[0.25,0.05],[0.75,0.05]]
    lText = [r"$N$="+str(J),r"$t=1.8$ s"]
    lTextAlign = ["center","center"]
    lTextColor = ["black","black"]

    lFile = [PATHPOIS+"T.OUT", Pois, Pois_1D_8, Pois_1D_40]

    #####
    # Tw
    #####
    yLabel = r"$\frac{\tau_w}{\mu \frac{U_{x=0}}{R_{x=0}}}$"
    liY = [5,
            iTw,iTw1D,iTw1D]
    lYScale = [1.,10.,10.,10.]
    lYOffset = [0.,0.,0.,0.]
    title = "Tw_Pois.pdf"
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
    yLabel = r"$\frac{P-P_{x=L}}{\rho U_{x=0}^2}$"
    liY = [2,
            iP,iP1D,iP1D]
    lYScale = [1.,10000.,10000.,10000.]
    lYOffset = ["first","first","first","first"]
    title = "P_Pois.pdf"
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
