#!/usr/bin/python3
import sys, getopt
from csv_libPlot_Profile import *

def main(argv) :

    # PATHS
    ###########

    HOME = "/Users/Arthur/"
    PATH = HOME + "Documents/UPMC/These/Codes/multilayerSingle/example/Well-Balance/Asymptotic/Stenose/Established/Cos/Rvar/"

    PATHSTEN = HOME + "Dropbox/These/Codes/SOURCES_RNSPaxi/Stenosis/"

    # FILE :
    ###########
    dataName = "Artery_0_x_r_Ux.csv"

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

        for dRstr in [ "-0.4", "+0.4" ] :

            #Choose number of layers & Choose number of cells
            J = "3200" ;
            La = "32"

            Sten  = PATH + "K=" + str(Kstr) + "/Re=" + str(Restr) + "/U=" + str(Ustr) + "/Length=" + str(Lstr) + "/dR=" + str(dRstr) + "/Lst=" + str(Lstenstr) + "/L=" + str(La) + "/Raf=0/J=" +str(J) + "/" + "HRQ/Order=1/KIN_HAT/Figures/" + dataName

            if (dRstr == "-0.4") :
                ANA = PATHSTEN + "Established_Stenose_dR_0p4/USpe.OUT"
            if (dRstr == "+0.4") :
                ANA = PATHSTEN + "Established_Aneurysm_dR_0p4/USpe.OUT"

            # PLOTING :
            ###########
            it = 0 ; ix = 1 ; iR0 = 2 ; iA0 = 3 ; iK = 4 ;
            iR = 5 ; iRmR0 = 6 ; iA = 7 ;
            iQ = 8 ; iU = 9 ; iU0 = 10 ;
            iP = 11 ; igradxP = 12 ; iE = 13 ;
            iTw = 14 ; iCf = 15 ; ia = 16 ;

            Store = PATH + "K=" + str(Kstr) + "/Re=" + str(Restr) + "/U=" + str(Ustr) + "/Length=" + str(Lstr) + "/dR=" + str(dRstr) + "/Lst=" + str(Lstenstr) +  "/Figures/"

            lCol = [
                    "black","darkgreen","darkblue","darkred","orangered","indigo",
                    "black","seagreen","blue","red","orange","darkviolet"
                    ]
            lMark = [
                        "","","","","","",
                        "^","D","o",">","s","+"
                        #"^","^","^","^","^","^"

                    ]
            lMarkSize = [
                            1,1,1,1,1,1,
                            9,9,9,9,9,9
                        ]
            lMarkWidth = [
                            1,1,1,1,1,1,
                            2,2,2,2,2,2
                        ]
            if (dRstr == "-0.4") :
                MarkPoints = 35
            else :
                MarkPoints = 35
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
                    2,3,4,5,6,7,
                    3,4,5,6,7,8
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
            yLabel = r"$ r \times \left[R\rvert_{x=0}\right]^{-1}$"

            lTextPos =   [[0.15,0.905],[0.25,0.04],[0.6,0.05],[0.85,0.05],
                          [0.02,0.62],[0.02,0.54],[0.207,0.54],[0.02,0.44],[0.165,0.44],[0.02,0.34],[0.2075,0.34],[0.02,0.24]]
            lText =      [r"$R_{e,R}$="+str(Restr),r"$N_x$="+str(J)+r", $N_r$="+str(La),
                          r"$K$="+str(K_c),r"$\Delta R$="+str(dRstr),
                         r"$\frac{x}{R_{e,R} R\rvert_{x=0}}$=$\left[ \right.$",
                         r"0.05$\left( \vartriangle \right)$,",r"0.075$\left( \diamond \right)$,",
                         r"0.1$\left( \circ \right)$,",r"0.125$\left( \vartriangleright \right)$,",
                         r"0.15$\left( \square \right)$,",r"0.175$\left( + \right)$",r"$\left.\right]$"]
            lTextAlign = ["center","center","center","center",
                          "left","left","left","left","left","left","left","left"]
            lTextColor = ["black","black","black","black",
                         "black","black","seagreen","blue","red","orange","darkviolet","black"]

            # lTextPos =   [[0.15,0.905],[0.25,0.04],[0.6,0.05],[0.85,0.05]]
            # lText =      [r"$R_{e,R}$="+str(Restr),r"$N_x$="+str(J)+r", $N_r$="+str(La),
            #               r"$K$="+str(K_c),r"$\Delta R$="+str(dRstr)]
            # lTextAlign = ["center","center","center","center"]
            # lTextColor = ["black","black","black","black"]

            LegLoc = 1
            LegPos = [0.98,0.98]
            LegCol = 2

            lLabel = [
                        r"$Steady$","","","","","",
                        r"$Multiring$","","","","",""
                        ]

            if (dRstr == "-0.4") :
                title = "Prof_Ux_Sten_K_"+ str(Kstr) + "_J_" + str(J) + ".pdf"
            else :
                title = "Prof_Ux_Ane_K_"+ str(Kstr) + "_J_" + str(J) + ".pdf"

            # title = "Conf_Prof_Ux_dR_" + str(dRstr) + ".pdf"

            lFile = [
                    ANA,ANA,ANA,ANA,ANA,ANA,
                    Sten,Sten,Sten,Sten,Sten,Sten
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
