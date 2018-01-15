#!/usr/bin/python3
import sys, getopt
from csv_libPlot_Profile import *

def main(argv) :

    # PATHS
    ###########

    HOME = "/Users/Arthur/"
    PATH = HOME + "Documents/UPMC/These/Codes/multilayerSingle/example/Well-Balance/Asymptotic/Womersley/"
    PATHWB = HOME + "Documents/UPMC/These/Codes/multilayer/example/Well-Balance/Asymptotic/Womersley/"


    PATHWOM_20 = HOME + "Documents/UPMC/These/Codes/multilayer/example/Well-Balance/Asymptotic/Womersley/Womersley/a=20/"
    PATHWOM_15 = HOME + "Documents/UPMC/These/Codes/multilayer/example/Well-Balance/Asymptotic/Womersley/Womersley/a=15/"
    PATHWOM_10 = HOME + "Documents/UPMC/These/Codes/multilayer/example/Well-Balance/Asymptotic/Womersley/Womersley/a=10/"
    PATHWOM_5 = HOME + "Documents/UPMC/These/Codes/multilayer/example/Well-Balance/Asymptotic/Womersley/Womersley/a=5/"

    # FILE :
    ###########
    dataName = "Artery_0_t_r_Ux.csv"

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
            La = "128"

            Wom     = PATH + "T_12/" +"a="+str(Womstr) + "/" + "K=1.e4/" + "dR=" + dRstr + "/L=" + str(La) + "/Raf=0/J=" +str(J) + "/" + "HRQ/Order=1/KIN_HAT/Figures/" + dataName
            WomWB   = PATHWB + "T_12/" +"a="+str(Womstr) + "/" + "K=1.e4/" + "dR=" + dRstr + "/L=" + str(La) + "/Raf=0/J=" +str(J) + "/" + "HRQ/Order=1/KIN_HAT/Figures/" + dataName

            # ANALYTIC
            ##########

            ANA = PATHWOM+"womProfil.csv"

            # PLOTING :
            ###########

            Store = PATH + "T_12/" +"a="+str(Womstr)+"/Figures/"


            lCol = [
                    "black","green","blue","red",
                    "black","green","blue","red",
                    "black","green","blue","red"
                    ]
            lMark = [
                        "","","","",
                        "o","o","o","o",
                        "^","^","^","^"
                    ]
            lMarkSize = [
                            1,1,1,1,
                            7,7,7,7,
                            7,7,7,7
                        ]
            lMarkWidth = [
                            1,1,1,1,
                            1,1,1,1,
                            1,1,1,1
                        ]
            MarkPoints = 45
            lLineSize = [
                        2,2,2,2,
                        1,1,1,1,
                        1,1,1,1
                        ]
            lStyle = [
                    "-","-","-","-",
                    "","","","",
                    "","","",""
                    ]

            lAlpha = [
                        1,1,1,1,
                        0.7,0.7,0.7,0.7,
                        0.7,0.7,0.7,0.7
                    ]

            liX = [
                    1,2,3,4,
                    1,2,3,4,
                    1,2,3,4
                    ]

            liY= [
                    0,0,0,0,
                    0,0,0,0,
                    0,0,0,0
                    ]

            xLabel=r"$U_x$ ($\frac{cm}{s}$)"
            yLabel = r"$\frac{r}{R}$"

            lTextPos = [[0.02,0.05],[0.53,0.05],[0.64,0.05],[0.72,0.05],[0.8,0.05],[0.88,0.05],[0.96,0.05]]
            lText = [r"$N$=$1600$, $L$=$128$",r"$t$=[",r"0.2,",r"0.4,",r"0.5,","0.7",r"]$T$"]
            lTextAlign = ["left","left","center","center","center","center","right"]
            lTextColor = ["black","black","black","green","blue","red","black"]
            LegPos = 12
            lLabel = [
                        r"$Analylic$","","","",
                        r"$Single$","","","",
                        r"$WB$","","",""
                        ]

            title = "Prof_Ux_Wom_"+str(Womstr) + "_O1_x_25_J_"+str(J)+".pdf"
            lFile = [
                    ANA,ANA,ANA,ANA,
                    Wom,Wom,Wom,Wom,
                    WomWB,WomWB,WomWB,WomWB
                    ]

            nfig = plot_csv_Profile(
                    pathStore=Store,title=title,lFile=lFile,
                    liX=liX,liY=liY,
                    xLabel=xLabel,yLabel=yLabel,lLabel=lLabel,LegPos=LegPos,
                    lText=lText,lTextPos=lTextPos,lTextAlign=lTextAlign,lTextColor=lTextColor,
                    lCol=lCol,lMark=lMark,
                    lMarkSize=lMarkSize,lMarkWidth=lMarkWidth,MarkPoints=MarkPoints,
                    lLineSize=lLineSize,lStyle=lStyle,lAlpha=lAlpha,nf=nfig)


if __name__ == "__main__":
   main(sys.argv[1:])
