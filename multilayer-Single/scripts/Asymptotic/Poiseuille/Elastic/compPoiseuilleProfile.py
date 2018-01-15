#!/usr/bin/python3
import sys, getopt
from csv_libPlot_Profile import *

def main(argv) :

    # PATHS
    ###########

    HOME = "/Users/Arthur/"
    PATH = HOME + "Documents/UPMC/These/Codes/multilayerSingle/example/Well-Balance/Asymptotic/Poiseuille/Elastic/"

    PATHPOIS = HOME + "Documents/UPMC/These/Codes/multilayerSingle/example/Well-Balance/Asymptotic/Poiseuille/Elastic/Analytic/"

    # FILE :
    ###########
    dataName = "Artery_0_x_r_Ux.csv"

    nfig = 1

    Shstr   = "1e-1"
    Lstr    = "10"

    Sh_c    = float(Shstr) ;
    L_c     = float(Lstr) ;

    if (Shstr == "1e-1") :
        Sh_p = r"$10^{-1}$"

    for Kstr in [ "1e2"] :

        if (Kstr == "1e2") :
            K_c = r"$10^2$"
        if (Kstr == "1e3") :
            K_c = r"$10^3$"
        if (Kstr == "1e4") :
            K_c = r"$10^4$"

        #Choose number of layers & Choose number of cells
        J = "800" ;
        La = "64"

        Pois    = PATH + "K=" + str(Kstr) + "/Sh=" + str(Shstr) + "/Length=" + str(Lstr) +  "/L=" + str(La) + "/Raf=0/J=" +str(J) + "/" + "HRQ/Order=1/KIN_HAT/Figures/" + dataName

        ANA     = PATHPOIS + "ux.csv"

        # PLOTING :
        ###########

        Store = PATH + "K=" + str(Kstr) + "/Sh=" + str(Shstr) + "/Length=" + str(Lstr) +  "/Figures/"

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
                1,3,5,7,9,11
                ]

        lXScale = [ 1.,1.,1.,1.,1.,1.,
                    1.,1.,1.,1.,1.,1.
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

        xLabel=r"$u_x$ $\left[\frac{cm}{s}\right]$"
        yLabel = r"$r \times R^{-1}$"

        lTextPos =   [[0.15,0.91],[0.5,0.04],
                      [0.05,0.605],
                      [0.13,0.63],[0.25,0.63],
                      [0.13,0.53],[0.275,0.53],
                      [0.13,0.43],[0.30,0.43],
                      [0.46,0.43]]
        lText =      [r"$\hat{R}$="+str(Sh_p),r"$N_x$="+str(J)+r", $N_r$="+str(La),
                     r"$\frac{x}{L}$=$\left[ \right.$",
                     r"0$\left( \vartriangle \right)$,", r"0.2$\left( \diamond \right)$,",
                     r"0.4$\left( \circ \right)$,", r"0.6$\left( \vartriangleright \right)$,",
                      r"0.8$\left( \square \right)$,", r"0.99$\left( + \right)$",r"$\left.\right]$"]
        lTextAlign = ["center","center",
                      "left","left","left","left","left","left","left","left"]
        lTextColor = ["black","black",
                     "black","black","seagreen","blue","red","orange","darkviolet","black"]

        LegLoc = 1
        LegPos = [1,0.97]
        LegCol = 2

        lLabel = [
                    r"$Steady$","","","","","",
                    r"$Multiring$","","","","",""
                    ]

        title = "Ux_Pois.pdf"
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
