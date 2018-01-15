#!/usr/bin/python3
import sys, getopt
from csv_libPlot_Profile import *

def main(argv) :

    # PATHS
    ###########

    HOME = "/Users/Arthur/"
    PATH = HOME + "/Documents/UPMC/These/Codes/multilayerSingle/example/Well-Balance/Asymptotic/Womersley/"

    # FILE :
    ###########
    dataName_Profile = "Artery_0_x_r_Ux.csv"
    dataName_Properties = "Artery_0_x_R0_A0_K_R_RmR0_A_Q_U_U0_P_gradP_E_Tw_Cf_a.csv"

    nfig = 1

    Womstr = "20"
    Kstr = "1.e4"
    for dRstr in ["1e-3","1e-2","1e-1","3e-1"] :

        if (dRstr == "1e-3") :
            dR_p = r"$10^{-3}$"
        if (dRstr == "1e-2") :
            dR_p = r"$10^{-2}$"
        if (dRstr == "1e-1") :
            dR_p = r"$10^{-1}$"
        if (dRstr == "3e-1") :
            dR_p = r"$3 \times 10^{-1}$"

        #Choose number of layers & Choose number of cells
        J = "1600"
        La = "128"

        ProFile  = PATH + "T_12/a=" + str(Womstr) + "/K=" + str(Kstr) + "/dR=" + str(dRstr) + "/L=" + str(La) + "/Raf=0/J=" +str(J) + "/" + "HRQ/Order=1/KIN_HAT/Figures/" + dataName_Profile
        PropFile = PATH + "T_12/a=" + str(Womstr) + "/K=" + str(Kstr) + "/dR=" + str(dRstr) + "/L=" + str(La) + "/Raf=0/J=" +str(J) + "/" + "HRQ/Order=1/KIN_HAT/Figures/" + dataName_Properties

        # PLOTING :
        ###########
        Store = PATH + "T_12/a=" + str(Womstr) + "/Figures/"

        it = 0 ; ix = 1 ; iR0 = 2 ; iA0 = 3 ; iK = 4 ;
        iR = 5 ; iRmR0 = 6 ; iA = 7 ;
        iQ = 8 ; iU = 9 ; iU0 = 10 ;
        iP = 11 ; igradxP = 12 ; iE = 13 ;
        iTw = 14 ; iCf = 15 ; ia = 16 ;

        lPropX = [it,ix,iR0,iR]

        xScale = 200.
        yScale = 1.
        cbScale = 1.

        lTextPos = [[0.5,0.04],[0.15,0.915],[0.43,0.915],[0.97,0.905]]
        lText = [r"$N_x$="+str(J)+r", $N_r$="+str(La),r"$\alpha$="+str(Womstr),r"$\hat{R}$="+str(dR_p),r"$t$=$0.3 T_c+11T_c$"]
        lTextAlign = ["center","center","center","right"]
        lTextColor = ["black","black","black","black"]

        nArrow = 100;
        scArrow = 1.6 ;
        Colormap = 'BlueRed'
        Umid = 0.
        liY =   [1,2,3,4,5,6,7,8,9,10,11]

        title = "Ux_Arrow_a_" + str(Womstr) + "_dR_" + str(dRstr) + ".pdf"

        xLabel=r"$x \times L^{-1}$"
        yLabel=r"$r \times R^{-1}$"
        cbLabel=r"$u_x$ $\left[\frac{cm}{s}\right]$"

        nfig = plot_csv_Streamlines_Ux_adim(
                pathStore=Store,title=title,PropFile=PropFile,ProFile=ProFile,
                lPropX=lPropX,liY=liY,
                xLabel = xLabel, yLabel = yLabel, cbLabel = cbLabel,
                xScale = xScale, yScale = yScale, cbScale = cbScale,
                nArrow=nArrow,scArrow=scArrow,
                Colormap=Colormap,Umid=Umid,
                lText=lText,lTextPos=lTextPos,lTextAlign=lTextAlign,lTextColor=lTextColor,
                nf=nfig) ;

if __name__ == "__main__":
   main(sys.argv[1:])
