#!/usr/bin/python3
import sys, getopt
from csv_libPlot_Profile import *

def main(argv) :

    # PATHS
    ###########

    HOME = "/Users/Arthur/"
    PATH = HOME + "Documents/UPMC/These/Codes/multilayerSingle/example/Well-Balance/Asymptotic/Stenose/Established/Cos/Rvar/"

    # FILE :
    ###########
    dataName_Profile = "Artery_0_x_r_Ux.csv"
    dataName_Properties = "Artery_0_x_R0_A0_K_R_RmR0_A_Q_U_U0_P_gradP_E_Tw_Cf_a.csv"
    # dataName_Properties = "Artery_0_x.csv"

    nfig = 1

    Restr       = "100"
    Ustr        = "100"
    Lstr        = "25"
    Lstenstr    = "10"

    Re_c        = float(Restr) ;
    U_c         = float(Ustr) ;
    R_c         = 1. ;
    mu_c        = U_c * R_c / Re_c ;

    for Kstr in [ "1e7" ] :

        if (Kstr == "1e6") :
            K_c = r"$10^6$"
        if (Kstr == "1e7") :
            K_c = r"$10^7$"
        if (Kstr == "1e8") :
            K_c = r"$10^8$"

        for dRstr in [ "-0.4","+0.4" ] :

            #Choose number of layers & Choose number of cells
            J = "3200"
            La = "32"

            ProFile  = PATH + "K=" + str(Kstr) + "/Re=" + str(Restr) + "/U=" + str(Ustr) + "/Length=" + str(Lstr) + "/dR=" + str(dRstr) + "/Lst=" + str(Lstenstr) + "/L=" + str(La) + "/Raf=0/J=" +str(J) + "/" + "HRQ/Order=1/KIN_HAT/Figures/" + dataName_Profile
            PropFile = PATH + "K=" + str(Kstr) + "/Re=" + str(Restr) + "/U=" + str(Ustr) + "/Length=" + str(Lstr) + "/dR=" + str(dRstr) + "/Lst=" + str(Lstenstr) + "/L=" + str(La) + "/Raf=0/J=" +str(J) + "/" + "HRQ/Order=1/KIN_HAT/Figures/" + dataName_Properties

            # PLOTING :
            ###########
            Store = PATH + "K=" + str(Kstr) + "/Re=" + str(Restr) + "/U=" + str(Ustr) + "/Length=" + str(Lstr) + "/dR=" + str(dRstr) + "/Lst=" + str(Lstenstr) + "/Figures/"

            it = 0 ; ix = 1 ; iR0 = 2 ; iA0 = 3 ; iK = 4 ;
            iR = 5 ; iRmR0 = 6 ; iA = 7 ;
            iQ = 8 ; iU = 9 ; iU0 = 10 ;
            iP = 11 ; igradxP = 12 ; iE = 13 ;
            iTw = 14 ; iCf = 15 ; ia = 16 ;

            lPropX = [it,ix,iR0,iR]

            xScale = Re_c * R_c
            yScale = R_c
            cbScale = U_c

            lTextPos = [[0.15,0.905],[0.25,0.04],[0.6,0.05],[0.85,0.05],[0.97,0.92]]
            lText = [r"$R_{e,R}$="+str(Restr),r"$N_x$="+str(J)+r", $N_r$="+str(La),
                     r"$K$="+str(K_c),r"$\Delta R$=" + str(dRstr),
                     r"$Steady$ $multiring$"]
            lTextAlign = ["center","center","center","center","right"]
            lTextColor = ["black","black","black","black","black"]

            # lTextPos    = []
            # lText       = []
            # lTextAlign  = []
            # lTextColor  = []

            nArrow = 100;
            scArrow = 1.

            Colormap = 'BlueRed'

            if (dRstr == "-0.4") :
                Umid = 2.01
            else :
                Umid = 1.01

            liY = [1,2,3,4,5,6,7,8,9,10,11]

            if (dRstr == "-0.4") :
                title = "Ux_Arrow_Sten_K_"+str(Kstr)+".pdf"
            else :
                title = "Ux_Arrow_Ane_K_"+str(Kstr)+".pdf"

            xLabel=r"$x \times \left[R_{e,R} R\rvert_{x=0} \right]^{-1}$"
            yLabel=r"$ r \times \left[R\rvert_{x=0}\right]^{-1}$"
            cbLabel=r"$u_x \times \left[u_{x}\rvert_{x=0}\right]^{-1}$"

            nfig = plot_csv_Streamlines_Ux_adim(
                pathStore=Store,title=title,PropFile=PropFile,ProFile=ProFile,
                lPropX=lPropX,liY=liY,
                xLabel = xLabel, yLabel = yLabel, cbLabel = cbLabel,
                xScale = xScale, yScale = yScale, cbScale = cbScale,
                nArrow=nArrow,scArrow=scArrow,Colormap=Colormap,Umid=Umid,
                lText=lText,lTextPos=lTextPos,lTextAlign=lTextAlign,lTextColor=lTextColor,
                nf=nfig) ;

if __name__ == "__main__":
   main(sys.argv[1:])
