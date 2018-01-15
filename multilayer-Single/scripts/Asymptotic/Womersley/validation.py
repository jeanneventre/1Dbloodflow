#!/usr/bin/python3
import sys, getopt
from csv_libPlot import *

def main(argv) :

    # PATHS
    ###########

    HOME = "/Users/Arthur/"
    PATH = HOME + "Documents/UPMC/These/Codes/multilayerSingle/example/Well-Balance/Asymptotic/Womersley/"
    PATHWB = HOME + "Documents/UPMC/These/Codes/multilayer/example/Well-Balance/Asymptotic/Womersley/"

    PATH1D = HOME + "Documents/UPMC/These/Codes/bloodflow/example/Well-Balance/Asymptotic/Womersley/"

    PATHWOM_20 = HOME + "Documents/UPMC/These/Codes/multilayer/example/Well-Balance/Asymptotic/Womersley/Womersley/a=20/"
    PATHWOM_15 = HOME + "Documents/UPMC/These/Codes/multilayer/example/Well-Balance/Asymptotic/Womersley/Womersley/a=15/"
    PATHWOM_10 = HOME + "Documents/UPMC/These/Codes/multilayer/example/Well-Balance/Asymptotic/Womersley/Womersley/a=10/"
    PATHWOM_5 = HOME + "Documents/UPMC/These/Codes/multilayer/example/Well-Balance/Asymptotic/Womersley/Womersley/a=5/"

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
            WomWB  = PATHWB + "T_12/" +"a="+str(Womstr) + "/" + "K=1.e4/" + "dR=" + dRstr + "/L=" + str(L) + "/Raf=0/J=" +str(J) + "/" + "HRQ/Order=1/KIN_HAT/Figures/" + dataName

            # PLOTING :
            ###########
            it = 0 ; ix = 1 ; iR0 = 2 ; iA0 = 3 ; iK = 4 ;
            iR = 5 ; iRmR0 = 6 ; iA = 7 ;
            iQ = 8 ; iU = 9 ; iU0 = 10 ;
            iP = 11 ; igradxP = 12 ; iE = 13 ;
            iTw = 14 ; iCf = 15 ; ia = 16 ;

            Store = PATH + "T_12/" +"a=" + str(Womstr) + "/Figures/"

            lCol = ["red",
                        "blue","green"]
            lMark = ["",
                        "o","^"]
            lMarkSize = [1,
                            7,7]
            lMarkWidth = [1,
                            2,2]

            if (Womstr == "5") :
                MarkPoints = 120 ;
            elif (Womstr == "20") :
                MarkPoints = 150 ;

            lLineSize = [2,
                            1,2,2]
            lStyle = ["-",
                        "",""]
            lAlpha = [1,
                        0.7,0.7]
            liX = [0,
                    ix,ix]

            xLabel=r"$\frac{x}{L}$"

            LegPos = 12
            lLabel = [r"$Analytic$",r"$Single$", r"$WB$"]

            lTextPos = [[0.25,0.05],[0.75,0.05]]
            lText = [r"$N$=$1600$",r"$t=0.3T$"]
            lTextAlign = ["center","center"]
            lTextColor = ["black","black"]

            #####
            # Q
            #####
            yLabel = r"$Q$ ($\frac{cm^3}{s}$)"
            liY = [1,
                    iQ,iQ]

            # WOM = 20
            title = "Comp_Q_Wom_"+str(Womstr) + "_O1_t_1p8_J_"+str(J)+".pdf"
            lFile = [PATHWOM+"womQx.csv" ,Wom, WomWB ]

            nfig = plot_csv(
                    pathStore=Store,title=title,lFile=lFile,
                    liX=liX,liY=liY,
                    xLabel=xLabel,yLabel=yLabel,lLabel=lLabel,LegPos=LegPos,
                    lText=lText,lTextPos=lTextPos,lTextAlign=lTextAlign,lTextColor=lTextColor,
                    lCol=lCol,lMark=lMark,
                    lMarkSize=lMarkSize,lMarkWidth=lMarkWidth,MarkPoints=MarkPoints,
                    lLineSize=lLineSize,lStyle=lStyle,lAlpha=lAlpha,nf=nfig)

            #####
            # Tw
            #####
            yLabel = r"$\tau_w$ ($\frac{g}{cm.s^2}$)"
            liY = [1,
                    iTw,iTw]

            title = "Comp_Tw_Wom_"+str(Womstr) + "_O1_t_1p8_J_"+str(J)+".pdf"
            lFile = [PATHWOM+"womTwx.csv" , Wom, WomWB ]

            nfig = plot_csv(
                    pathStore=Store,title=title,lFile=lFile,
                    liX=liX,liY=liY,
                    xLabel=xLabel,yLabel=yLabel,lLabel=lLabel,LegPos=LegPos,
                    lText=lText,lTextPos=lTextPos,lTextAlign=lTextAlign,lTextColor=lTextColor,
                    lCol=lCol,lMark=lMark,
                    lMarkSize=lMarkSize,lMarkWidth=lMarkWidth,MarkPoints=MarkPoints,
                    lLineSize=lLineSize,lStyle=lStyle,lAlpha=lAlpha,nf=nfig)
            #####
            # P
            #####
            yLabel = r"$P$ ($\frac{g}{cm.s^2}$)"
            liY = [1,
                    iP,iP]

            title = "Comp_P_Wom_"+str(Womstr) + "_O1_t_1p8_J_"+str(J)+".pdf"
            lFile = [PATHWOM+"womPx.csv" , Wom, WomWB ]

            nfig = plot_csv(
                    pathStore=Store,title=title,lFile=lFile,
                    liX=liX,liY=liY,
                    xLabel=xLabel,yLabel=yLabel,lLabel=lLabel,LegPos=LegPos,
                    lText=lText,lTextPos=lTextPos,lTextAlign=lTextAlign,lTextColor=lTextColor,
                    lCol=lCol,lMark=lMark,
                    lMarkSize=lMarkSize,lMarkWidth=lMarkWidth,MarkPoints=MarkPoints,
                    lLineSize=lLineSize,lStyle=lStyle,lAlpha=lAlpha,nf=nfig)

if __name__ == "__main__":
   main(sys.argv[1:])
