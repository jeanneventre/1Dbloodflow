#!/usr/bin/python3
import sys, getopt
from csv_libPlot_Profile import *

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

            # ANALYTIC
            ##########

            ANA = PATHWOM + "womProfil.csv"

            # PLOTING :
            ###########

            Store = PATH + "T_12/" +"a="+str(Womstr)+"/Figures/"


            lCol = [
                    "black","darkgreen","darkblue","darkred",
                    "black","seagreen","blue","red"
                    ]
            lMark = [
                        "","","","",
                        "^","D","o",">"
                        # "^","^","^","^"
                    ]
            lMarkSize = [
                            1,1,1,1,
                            9,9,9,9
                        ]
            lMarkWidth = [
                            1,1,1,1,
                            2,2,2,2
                        ]
            MarkPoints = 30
            lLineSize = [
                        4,4,4,4,
                        2,2,2,2
                        ]
            lStyle = [
                    "-","-","-","-",
                    "","","",""
                    ]

            lAlpha = [
                        1,1,1,1,
                        0.7,0.7,0.7,0.7
                    ]

            liX = [
                    1,2,3,4,
                    1,2,3,4
                    ]

            liY= [
                    0,0,0,0,
                    0,0,0,0
                    ]

            lXScale     =   [   1.,1.,1.,1.,1.,1.,
                                1.,1.,1.,1.,1.,1.
                            ]
            lXOffset    =   [   0., 0., 0., 0., 0., 0.,
                                0., 0., 0., 0., 0., 0.
                            ]
            lYScale     =   [   1.,1.,1.,1.,1.,1.,
                                1.,1.,1.,1.,1.,1.
                            ]
            lYOffset    =   [   0., 0., 0., 0., 0., 0.,
                                0., 0., 0., 0., 0., 0.
                            ]

            xLabel=r"$u_x$ $\left[\frac{cm}{s}\right]$"
            yLabel = r"$r \times R^{-1}$"

            lTextPos = [[0.15,0.915],[0.5,0.04],[0.39,0.54],[0.46,0.54],[0.62,0.54],[0.39,0.44],[0.54,0.44],[0.68,0.43]]
            lText = [r"$\alpha$="+str(Womstr),r"$N_x$=$1600$, $N_r$=$128$",
                     r"$t$=[",r"0.2$\left( \vartriangle \right)$,",r"0.4$\left( \diamond \right)$,",
                     r"0.5$\left( \circ \right)$,",r"0.7$\left( \vartriangleright \right)$",r"]$T_c$+$11T_c$"]
            lTextAlign = ["center","center","left","left","left","left","left","left"]
            lTextColor = ["black","black","black","black","seagreen","blue","red","black"]

            # lTextPos = [[0.15,0.915],[0.5,0.04]]
            # lText = [r"$\alpha$="+str(Womstr),r"$N_x$=" + str(J) + r", $N_r$=" + str(La)]
            # lTextAlign = ["center","center"]
            # lTextColor = ["black","black"]


            LegLoc = 1
            LegPos = [0.98,0.98]
            LegCol = 2

            lLabel = [
                        r"$Analylic$","","","",
                        r"$Multiring$","","",""
                        ]

            # title = "Conf_Prof_Ux_Wom_"+str(Womstr) + ".pdf"
            title = "Prof_Ux_Wom_"+str(Womstr) + "_O1_x_25_J_" + str(J) + ".pdf"

            lFile = [
                    ANA,ANA,ANA,ANA,
                    Wom,Wom,Wom,Wom
                    ]

            nfig = plot_csv_Profile_adim(
                    pathStore=Store,title=title,lFile=lFile,
                    liX=liX,liY=liY,
                    xLabel=xLabel,yLabel=yLabel,lLabel=lLabel,
                    lXScale=lXScale,lYScale=lYScale,lXOffset=lXOffset,lYOffset=lYOffset,
                    LegLoc=LegLoc,LegPos=LegPos,LegCol=LegCol,
                    lText=lText,lTextPos=lTextPos,lTextAlign=lTextAlign,lTextColor=lTextColor,
                    lCol=lCol,lMark=lMark,
                    lMarkSize=lMarkSize,lMarkWidth=lMarkWidth,MarkPoints=MarkPoints,
                    lLineSize=lLineSize,lStyle=lStyle,lAlpha=lAlpha,nf=nfig)


if __name__ == "__main__":
   main(sys.argv[1:])
