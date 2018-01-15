#!/usr/bin/python3
import sys, getopt
from csv_libPlot_Profile import *

def main(argv) :

    # PATHS
    ###########

    HOME = "/Users/Arthur/"
    PATH = HOME + "Documents/UPMC/These/Codes/multilayerSingle/example/Well-Balance/Asymptotic/Poiseuille/Entrance-Length/"

    # FILE :
    ###########
    dataName_Profile = "Artery_0_x_r_Ux.csv"
    dataName_Properties = "Artery_0_x_R0_A0_K_R_RmR0_A_Q_U_U0_P_gradP_E_Tw_Cf_a.csv"

    nfig = 1

    Kstr = "1e7"

    Restr = "100"
    Ustr = "100"
    Lstr = "25"

    Re_c = float(Restr) ;
    U_c = float(Ustr) ;
    R_c = 1. ;
    mu_c = U_c * R_c / Re_c ;

    #Choose number of layers & Choose number of cells
    J = "3200"
    La = "32"

    ProFile  = PATH + "K=" + str(Kstr) + "/Re=" + str(Restr) + "/U=" + str(Ustr) + "/Length=" + str(Lstr) +  "/L=" + str(La) + "/Raf=0/J=" +str(J) + "/" + "HRQ/Order=1/KIN_HAT/Figures/" + dataName_Profile
    PropFile = PATH + "K=" + str(Kstr) + "/Re=" + str(Restr) + "/U=" + str(Ustr) + "/Length=" + str(Lstr) +  "/L=" + str(La) + "/Raf=0/J=" +str(J) + "/" + "HRQ/Order=1/KIN_HAT/Figures/" + dataName_Properties

    # PLOTING :
    ###########
    Store = PATH + "K=" + str(Kstr) + "/Re=" + str(Restr) + "/U=" + str(Ustr) + "/Length=" + str(Lstr) +  "/Figures/"

    it = 0 ; ix = 1 ; iR0 = 2 ; iA0 = 3 ; iK = 4 ;
    iR = 5 ; iRmR0 = 6 ; iA = 7 ;
    iQ = 8 ; iU = 9 ; iU0 = 10 ;
    iP = 11 ; igradxP = 12 ; iE = 13 ;
    iTw = 14 ; iCf = 15 ; ia = 16 ;

    lPropX = [it,ix,iR0,iR]

    xScale = Re_c * R_c
    yScale = R_c
    cbScale = U_c

    lTextPos = [[0.5,0.05],[0.97,0.92]]
    lText = [r"$N$="+str(J) +r", $L$=" +str(La),r"$t$=$1.8$ $s$"]
    lTextAlign = ["center","right"]
    lTextColor = ["black","black"]

    nArrow = 100 ;
    scArrow = 2. ;

    Colormap = 'BlueRed'
    Umid = 1.
    liY = [1,2,3,4,5,6]

    xLabel=r"$x \times \left[ R_{e,R} R_{|x=0} \right]^{-1}$"
    yLabel=r"$ r \times R_{|x=0}^{-1}$"
    cbLabel=r"$u_x \times u_{x_{|x=0}}^{-1}$"

    title = "Ux_Arrow.pdf"

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
