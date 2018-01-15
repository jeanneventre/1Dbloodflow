#!/usr/bin/python3
import sys, getopt
from csv_libPlot import *

def main(argv) :

    # PATHS
    ###########

    HOME = "/Users/Arthur/"
    PATH = HOME + "Documents/UPMC/These/Codes/multilayerSingle/example/Well-Balance/Asymptotic/Womersley/"

    PATHWOM_20 = HOME + "Documents/UPMC/These/Codes/multilayerSingle/example/Well-Balance/Asymptotic/Womersley/Womersley/a=20/"
    PATHWOM_15 = HOME + "Documents/UPMC/These/Codes/multilayerSingle/example/Well-Balance/Asymptotic/Womersley/Womersley/a=15/"
    PATHWOM_10 = HOME + "Documents/UPMC/These/Codes/multilayerSingle/example/Well-Balance/Asymptotic/Womersley/Womersley/a=10/"
    PATHWOM_5 = HOME + "Documents/UPMC/These/Codes/multilayerSingle/example/Well-Balance/Asymptotic/Womersley/Womersley/a=5/"

    # FILE :
    ###########
    dataName = "Artery_0_x_R0_A0_K_R_RmR0_A_Q_U_U0_P_gradP_E_Tw_Cf_a.csv"

    nfig = 1

    dRstr = "1e-3"

    for Womstr in ["5", "20"] :

            #Choose Womersley number
            if (Womstr == "5") :
                PATHWOM = PATHWOM_5
            elif (Womstr == "10") :
                PATHWOM = PATHWOM_10
            elif (Womstr == "15") :
                PATHWOM = PATHWOM_15
            elif (Womstr == "20") :
                PATHWOM = PATHWOM_20

            J = "1600"
            L = "128"

            #Choose number of cells

            Wom    = PATH + "T_12/" +"a="+str(Womstr) + "/" + "K=1.e4/" + "dR=" + dRstr + "/L=" + str(L) + "/Raf=0/J=" +str(J) + "/" + "HRQ/Order=1/KIN_HAT/Figures/" + dataName

            # PLOTING :
            ###########
            it = 0 ; ix = 1 ; iR0 = 2 ; iA0 = 3 ; iK = 4 ;
            iR = 5 ; iRmR0 = 6 ; iA = 7 ;
            iQ = 8 ; iU = 9 ; iU0 = 10 ;
            iP = 11 ; igradxP = 12 ; iE = 13 ;
            iTw = 14 ; iCf = 15 ; ia = 16 ;

            Store = PATH + "T_12/" +"a=" + str(Womstr) + "/Figures/"

            lCol = ["red","blue"]
            lMark = ["","o"]
            lMarkSize = [1,9]
            lMarkWidth = [1,2]

            if (Womstr == "5") :
                MarkPoints = 100 ;
            elif (Womstr == "20") :
                MarkPoints = 130 ;

            lLineSize = [2.5,1]
            lStyle = ["-",""]
            lAlpha = [1,0.7]
            liX = [0,ix]

            xLabel=r"$x \times L^{-1}$"

            LegLoc = 1
            LegPos = [1.,0.97]
            LegCol = 2

            lLabel = [r"$Analytic$",r"$Multiring$"]

            lTextPos = [[0.15,0.91],[0.25,0.04],[0.75,0.04]]
            lText = [r"$\alpha$="+str(Womstr),r"$N_x$=$1600$, $N_r=128$",r"$t=0.3 T_c + 11 T_c$"]
            lTextAlign = ["center","center","center"]
            lTextColor = ["black","black","black"]

            #####
            # Q
            #####
            yLabel = r"$Q$ $\left[ \frac{cm^3}{s} \right] $"
            liY = [1,iQ]

            # WOM = 20
            title = "Q_Wom_"+str(Womstr) + "_O1_t_1p8_J_"+str(J)+".pdf"
            lFile = [PATHWOM+"womQx.csv" , Wom ]

            nfig = plot_csv(
                    pathStore=Store,title=title,lFile=lFile,
                    liX=liX,liY=liY,
                    xLabel=xLabel,yLabel=yLabel,lLabel=lLabel,
                    LegLoc=LegLoc,LegPos=LegPos,LegCol=LegCol,
                    lText=lText,lTextPos=lTextPos,lTextAlign=lTextAlign,lTextColor=lTextColor,
                    lCol=lCol,lMark=lMark,
                    lMarkSize=lMarkSize,lMarkWidth=lMarkWidth,MarkPoints=MarkPoints,
                    lLineSize=lLineSize,lStyle=lStyle,lAlpha=lAlpha,nf=nfig)

            #####
            # Tw
            #####
            yLabel = r"$\tau_w$ $\left[ \frac{g}{cm.s^2} \right] $"
            liY = [1,iTw]

            title = "Tw_Wom_"+str(Womstr) + "_O1_t_1p8_J_"+str(J)+".pdf"
            lFile = [PATHWOM+"womTwx.csv" , Wom ]

            nfig = plot_csv(
                    pathStore=Store,title=title,lFile=lFile,
                    liX=liX,liY=liY,
                    xLabel=xLabel,yLabel=yLabel,lLabel=lLabel,
                    LegLoc=LegLoc,LegPos=LegPos,LegCol=LegCol,
                    lText=lText,lTextPos=lTextPos,lTextAlign=lTextAlign,lTextColor=lTextColor,
                    lCol=lCol,lMark=lMark,
                    lMarkSize=lMarkSize,lMarkWidth=lMarkWidth,MarkPoints=MarkPoints,
                    lLineSize=lLineSize,lStyle=lStyle,lAlpha=lAlpha,nf=nfig)
            #####
            # P
            #####
            yLabel = r"$Q$ $\left[ \frac{cm^3}{s} \right] $"
            liY = [1,iP]

            title = "P_Wom_"+str(Womstr) + "_O1_t_1p8_J_"+str(J)+".pdf"
            lFile = [PATHWOM+"womPx.csv" , Wom ]

            nfig = plot_csv(
                    pathStore=Store,title=title,lFile=lFile,
                    liX=liX,liY=liY,
                    xLabel=xLabel,yLabel=yLabel,lLabel=lLabel,
                    LegLoc=LegLoc,LegPos=LegPos,LegCol=LegCol,
                    lText=lText,lTextPos=lTextPos,lTextAlign=lTextAlign,lTextColor=lTextColor,
                    lCol=lCol,lMark=lMark,
                    lMarkSize=lMarkSize,lMarkWidth=lMarkWidth,MarkPoints=MarkPoints,
                    lLineSize=lLineSize,lStyle=lStyle,lAlpha=lAlpha,nf=nfig)

if __name__ == "__main__":
   main(sys.argv[1:])
