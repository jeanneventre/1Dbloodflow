#!/usr/bin/python3
import sys, getopt
from csv_libPlot_Profile import *

import numpy as np

def main(argv) :

    # PATHS
    ###########

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

        for dRstr in [ "0","-0.4" ] :

            # for label in [ "2p0T", "2p1T", "2p2T", "2p3T", "2p4T", "2p5T", "2p6T", "2p7T", "2p8T", "2p9T", "3p0T", "3p1T", "3p2T", "3p3T", "3p4T", "3p5T", "3p6T", "3p7T", "3p8T", "3p9T", "4p0T", "4p1T", "4p2T", "4p3T", "4p4T", "4p5T", "4p6T", "4p7T", "4p8T", "4p9T" ] :
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
                dataName_Properties = "Artery_0_" + str(label) + "_x_R0_A0_K_R_RmR0_A_Q_U_U0_P_gradP_E_Tw_Cf_a_Sh.csv"

                #Choose number of layers & Choose number of cells
                J = "3200"
                La = "32"

                ProFile  = PATH + "K=" + str(Kstr) + "/Re=" + str(Restr) + "/a=" + str(Womstr) + "/Sh=" + str(Shstr) + "/Length=" + str(Lstr) + "/dR=" + str(dRstr) + "/Lst=" + str(Lstenstr) + "/Rt=" + str(Rtstr) + "/L=" + str(La) + "/Raf=0/J=" +str(J) + "/" + "HRQ/Order=1/KIN_HAT/Figures/" + dataName_Profile
                PropFile = PATH + "K=" + str(Kstr) + "/Re=" + str(Restr) + "/a=" + str(Womstr) + "/Sh=" + str(Shstr) + "/Length=" + str(Lstr) + "/dR=" + str(dRstr) + "/Lst=" + str(Lstenstr) + "/Rt=" + str(Rtstr) + "/L=" + str(La) + "/Raf=0/J=" +str(J) + "/" + "HRQ/Order=1/KIN_HAT/Figures/" + dataName_Properties

                # PLOTING :
                ###########
                Store = PATH + "K=" + str(Kstr) + "/Re=" + str(Restr) + "/a=" + str(Womstr) + "/Sh=" + str(Shstr) + "/Length=" + str(Lstr) + "/dR=" + str(dRstr) + "/Lst=" + str(Lstenstr) + "/Rt=" + str(Rtstr) + "/Figures/"

                it = 0 ; ix = 1 ; iR0 = 2 ; iA0 = 3 ; iK = 4 ;
                iR = 5 ; iRmR0 = 6 ; iA = 7 ;
                iQ = 8 ; iU = 9 ; iU0 = 10 ;
                iP = 11 ; igradxP = 12 ; iE = 13 ;
                iTw = 14 ; iCf = 15 ; ia = 16 ; iSh = 17 ;

                lPropX      = [it,ix,iR0,iR]

                xScale      = Re_c * R_c
                yScale      = R_c
                cbScale     = U_c

                cbRange = [-0.5,3.75] ;

                lTextPos = [[0.15,0.905],[0.38,0.915],[0.6,0.905],[0.76,0.905],
                            [0.25,0.04],[0.6,0.05],[0.85,0.05]]
                lText =     [
                            r"$R_{e,R}$="+str(Restr),r"$\alpha$="+str(Womstr),r"$S_h$="+str(Sh),str(label_c),
                            r"$N_x$="+str(J)+r", $N_r$="+str(La),
                            r"$K$="+str(K),r"$\Delta R$=" + str(dRstr)
                            ]
                lTextAlign = ["center","center","center","left",
                              "center","center","center"]
                lTextColor = ["black","black","black","black","black","black","black"]

                nArrow = 100;
                scArrow = 0.9 ;

                Colormap = 'BlueRed'

                Umid = 1.01

                liY = [1,2,3,4,5,6,7,8,9,10,11]

                if (dRstr == "0") :
                    preTitle = "Ux_Arrow_Straight_K_"
                else :
                    preTitle = "Ux_Arrow_Sten_K_"
                title = preTitle + str(Kstr) + "_" + str(label) + ".pdf"

                xLabel=r"$x \times \left[ R_{e,R} R\rvert_{x=0} \right]^{-1}$"
                yLabel=r"$r \times \left[R\rvert_{x=0}\right]^{-1}$"
                cbLabel=r"$u_x \times \left[ u_{x}\rvert_{x=0} \right]^{-1}$"

                nfig = plot_csv_Streamlines_Ux_adim(
                    pathStore=Store,title=title,PropFile=PropFile,ProFile=ProFile,
                    lPropX=lPropX,liY=liY,
                    xLabel = xLabel, yLabel = yLabel, cbLabel = cbLabel,
                    xScale = xScale, yScale = yScale, cbScale = cbScale, cbRange = cbRange,
                    nArrow=nArrow,scArrow=scArrow,  Colormap=Colormap,Umid=Umid,
                    lText=lText,lTextPos=lTextPos,lTextAlign=lTextAlign,lTextColor=lTextColor,
                    nf=nfig) ;

if __name__ == "__main__":
   main(sys.argv[1:])
