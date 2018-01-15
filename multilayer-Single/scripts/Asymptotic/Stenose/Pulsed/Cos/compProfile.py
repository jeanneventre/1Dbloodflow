#!/usr/bin/python3
import sys, getopt
from csv_libPlot_Profile import *

def main(argv) :

    HOME = "/Users/Arthur/"
    PATH = HOME + "Documents/UPMC/These/Codes/multilayerSingle/example/Well-Balance/Asymptotic/Stenose/Pulsed/Cos/Rvar/"

    nfig = 1

    Restr   = "100"
    Womstr  = "15"
    Shstr   = "1e-2"

    Sh      = r"$10^{-2}$"

    Lstr    = "25"
    Lstenstr= "10"

    Rtstr   = "0"

    Re_c    = float(Restr) ;
    Wom_c   = float(Womstr) ;
    Sh_c    = float(Shstr) ;

    R_c     = 1. ;
    rho_c   = 1. ;

    for Kstr in [ "1e5" ] :

        c_c     = np.sqrt( float(Kstr)/2./rho_c * np.sqrt(np.pi)*R_c )
        U_c     = Sh_c * c_c ;
        mu_c    = U_c * R_c / Re_c ;

        if (Kstr == "1e5") :
            K = r"$10^5$"

        for label in [ "4p2T", "4p6T", "4p9T" ] :

            if (label == "4p0T") :
                label_c = r"$t$=$4T_c$"
            elif (label == "4p2T") :
                label_c = r"$t$=$4.2T_c$"
            elif (label == "4p25T") :
                label_c = r"$t$=$4.25T_c$"
            elif (label == "4p5T") :
                label_c = r"$t$=$4.5T_c$"
            elif (label == "4p6T") :
                label_c = r"$t$=$4.6T_c$"
            elif (label == "4p75T") :
                label_c = r"$t$=$4.75T_c$"
            elif (label == "4p9T") :
                label_c = r"$t$=$4.9T_c$"
            else:
                label_c = r"$t$=" + str(label)
            # FILE :
            ###########
            dataName_Profile = "Artery_0_" + str(label) + "_x_r_Ux.csv"

            #Choose number of layers & Choose number of cells
            J = "3200"
            La = "32"

            Wom  = PATH + "K=" + str(Kstr) + "/Re=" + str(Restr) + "/a=" + str(Womstr) + "/Sh=" + str(Shstr) + "/Length=" + str(Lstr) + "/dR=" + str(0) + "/Lst=" + str(Lstenstr) + "/Rt=" + str(Rtstr) + "/L=" + str(La) + "/Raf=0/J=" +str(J) + "/" + "HRQ/Order=1/KIN_HAT/Figures/" + dataName_Profile
            Sten = PATH + "K=" + str(Kstr) + "/Re=" + str(Restr) + "/a=" + str(Womstr) + "/Sh=" + str(Shstr) + "/Length=" + str(Lstr) + "/dR=" + str(-0.4)    + "/Lst=" + str(Lstenstr) + "/Rt=" + str(Rtstr) + "/L=" + str(La) + "/Raf=0/J=" +str(J) + "/" + "HRQ/Order=1/KIN_HAT/Figures/" + dataName_Profile

            # PLOTING :
            ###########
            Store = PATH + "K=" + str(Kstr) + "/Re=" + str(Restr) + "/a=" + str(Womstr) + "/Sh=" + str(Shstr) + "/Length=" + str(Lstr) + "/dR=" + str(-0.4) + "/Lst=" + str(Lstenstr) + "/Rt=" + str(Rtstr) + "/Figures/"

            # PLOTING :
            ###########

            lCol        = [
                            "black","darkgreen","darkblue",
                            "black","seagreen","blue"
                          ]
            lMark       = [
                            "","","",
                            "^","D","o"
                            ]
            lMarkSize   = [
                            1,1,1,
                            9,9,9
                            ]
            lMarkWidth  = [
                            1,1,1,
                            2,2,2
                            ]

            MarkPoints  = 30

            lLineSize   = [
                            2,2,2,
                            2,2,2
                            ]
            lStyle      = [
                            "-","-","-",
                            "","",""
                            ]

            lAlpha      = [
                            1,1,1,
                            0.7,0.7,0.7
                            ]

            xRange      =   [-1,3.6]
            yRange      =   [-1,1]

            xMargin     = 0.
            yMargin     = 0.175

            lXScale     =   [   U_c,U_c,U_c,
                                U_c,U_c,U_c
                            ]
            lXOffset    =   [   0., 0., 0.,
                                0., 0., 0.
                            ]
            lYScale     =   [   R_c,R_c,R_c,
                                R_c,R_c,R_c
                                ]
            lYOffset    =   [   0., 0., 0.,
                                0., 0., 0.
                            ]

            xLabel      = r"$u_x \times \left[ u_{x}\rvert_{x=0} \right]^{-1}$"
            yLabel      = r"$r \times R^{-1}$"

            lTextPos = [[0.15,0.905],[0.38,0.915],[0.6,0.905],[0.76,0.905],
                        [0.25,0.04],[0.6,0.05],
                        [0.51,0.61],[0.51,0.53],[0.51,0.43],[0.51,0.34],[0.685,0.34]
                        ]
            lText =     [
                        r"$R_{e,R}$="+str(Restr),r"$\alpha$="+str(Womstr),r"$S_h$="+str(Sh),str(label_c),
                        r"$N_x$="+str(J)+r", $N_r$="+str(La),
                        r"$K$="+str(K),
                        r"$\frac{x}{R_{e,R} R\rvert_{x=0}}$=[",r"0.025$\left( \vartriangle \right)$,",r"0.1$\left( \diamond \right)$,",
                        r"0.225$\left( \circ \right)$",r"]"
                        ]
            lTextAlign = ["center","center","center","left",
                          "center","center",
                          "left","left","left","left","left"]
            lTextColor = ["black","black","black","black",
                          "black","black",
                          "black","black","seagreen","blue","black"]


            LegLoc      = 3
            LegPos      = [0.72,0.023]
            LegCol      = 1

            lLabel  = [
                        r"$\Delta R$=$0$","","",
                        r"$\Delta R$=-$0.4$","",""
                        ]

            title   = "Prof_Ux_t_" + label + ".pdf"

            liX         = [
                            2,5,10,
                            2,5,10
                          ]

            liY         = [
                            0,0,0,
                            0,0,0
                            ]

            lFile   = [
                        Wom,Wom,Wom,
                        Sten,Sten,Sten
                        ]

            nfig    = plot_csv_Profile_adim(
                        pathStore=Store,title=title,lFile=lFile,
                        liX=liX,liY=liY,
                        xLabel=xLabel,yLabel=yLabel,lLabel=lLabel,
                        lXScale=lXScale,lYScale=lYScale,xRange=xRange,yRange=yRange,xMargin=xMargin,yMargin=yMargin,lXOffset=lXOffset,lYOffset=lYOffset,
                        LegLoc=LegLoc,LegPos=LegPos,LegCol=LegCol,
                        lText=lText,lTextPos=lTextPos,lTextAlign=lTextAlign,lTextColor=lTextColor,
                        lCol=lCol,lMark=lMark,
                        lMarkSize=lMarkSize,lMarkWidth=lMarkWidth,MarkPoints=MarkPoints,
                        lLineSize=lLineSize,lStyle=lStyle,lAlpha=lAlpha,nf=nfig
                        )


if __name__ == "__main__":
   main(sys.argv[1:])
