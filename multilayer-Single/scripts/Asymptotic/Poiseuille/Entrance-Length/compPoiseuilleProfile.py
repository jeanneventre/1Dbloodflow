#!/usr/bin/python3
import sys, getopt
from csv_libPlot_Profile import *

def main(argv) :

    # PATHS
    ###########

    HOME = "/Users/Arthur/"
    PATH = HOME + "Documents/UPMC/These/Codes/multilayerSingle/example/Well-Balance/Asymptotic/Poiseuille/Entrance-Length/"

    PATHPOIS = HOME + "Dropbox/These/Codes/SOURCES_RNSPaxi/Entrance_Poiseuille/"

    # FILE :
    ###########
    dataName = "Artery_0_x_r_Ux.csv"

    nfig = 1

    Restr = "100"
    Ustr = "100"
    Lstr = "25"

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

        #Choose number of layers & Choose number of cells
        for J in ["800","3200"] :

            La = "32"

            Pois    = PATH + "K=" + str(Kstr) + "/Re=" + str(Restr) + "/U=" + str(Ustr) + "/Length=" + str(Lstr) +  "/L=" + str(La) + "/Raf=0/J=" +str(J) + "/" + "HRQ/Order=1/KIN_HAT/Figures/" + dataName

            ANA = PATHPOIS + "USpe.OUT"

            # PLOTING :
            ###########
            it = 0 ; ix = 1 ; iR0 = 2 ; iA0 = 3 ; iK = 4 ;
            iR = 5 ; iRmR0 = 6 ; iA = 7 ;
            iQ = 8 ; iU = 9 ; iU0 = 10 ;
            iP = 11 ; igradxP = 12 ; iE = 13 ;
            iTw = 14 ; iCf = 15 ; ia = 16 ;

            Store = PATH + "K=" + str(Kstr) + "/Re=" + str(Restr) + "/U=" + str(Ustr) + "/Length=" + str(Lstr) +  "/Figures/"

            lCol = [
                    "black","darkgreen","darkblue","darkred","orangered","indigo",
                    "black","seagreen","blue","red","orange","darkviolet"
                    ]
            lMark = [
                        "","","","","","",
                        "^","D","o",">","s","+"
                    ]
            lMarkSize = [
                            1,1,1,1,1,1,
                            9,9,9,9,9,9
                        ]
            lMarkWidth = [
                            1,1,1,1,1,1,
                            2,2,2,2,2,2
                        ]
            MarkPoints = 32
            lLineSize = [
                        2,2,2,2,2,2,
                        2,2,2,2,2,2
                        ]
            lStyle = [
                    "-","-","-","-","-","-",
                    "","","","","",""
                    ]

            lAlpha = [
                        1,1,1,1,1,1,
                        0.7,0.7,0.7,0.7,0.7,0.7
                    ]

            liX = [
                    1,2,3,4,5,6,
                    1,2,3,4,5,6
                    ]

            lXScale = [ 1.,1.,1.,1.,1.,1.,
                        U_c,U_c,U_c,U_c,U_c,U_c
                      ]
            lXOffset = [ 0., 0., 0., 0., 0., 0.,
                         0., 0., 0., 0., 0., 0.
                       ]

            liY= [
                    0,0,0,0,0,0,
                    0,0,0,0,0,0
                    ]

            lYScale = [ 1.,1.,1.,1.,1.,1.,
                        1.,1.,1.,1.,1.,1.
                      ]
            lYOffset = [ 0., 0., 0., 0., 0., 0.,
                         0., 0., 0., 0., 0., 0.
                       ]

            xLabel=r"$u_x \times \left[u_{x}\rvert_{x=0}\right]^{-1}$"
            yLabel = r"$r \times \left[R\rvert_{x=0}\right]^{-1}$"

            lTextPos =   [[0.15,0.905],[0.25,0.04],[0.75,0.05],
                          [0.01,0.51],[0.217,0.54],[0.42,0.54],[0.195,0.44],[0.39,0.44],[0.195,0.34],[0.355,0.34],[0.49,0.34]]
            lText =      [r"$R_{e,R}$="+str(Restr),r"$N_x$="+str(J)+r", $N_r$="+str(La),r"$K=$"+str(K_c),
                         r"$\frac{x}{R_{e,R}R\rvert_{x=0}}$=$\left[ \right.$", r"0.005$\left( \vartriangle \right)$,",
                         r"0.01$\left( \diamond \right)$,",r"0.025$\left( \circ \right)$,",
                         r"0.05$\left( \vartriangleright \right)$,",r"0.1$\left( \square \right)$,",
                         r"0.2$\left( + \right)$",r"$\left.\right]$"]
            lTextAlign = ["center","center","center",
                          "left","left","left","left","left","left","left","left"]
            lTextColor = ["black","black","black",
                         "black","black","seagreen","blue","red","orange","darkviolet","black"]

            LegLoc = 1
            LegPos = [0.98,0.98]
            LegCol = 2

            lLabel = [
                        r"$Steady$","","","","","",
                        r"$Multiring$","","","","",""
                        ]

            title = "Prof_Ux_Pois_"+str(Restr) + "K_"+ str(Kstr) + "_J_" + str(J) + ".pdf"
            lFile = [
                    ANA,ANA,ANA,ANA,ANA,ANA,
                    Pois,Pois,Pois,Pois,Pois,Pois
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
