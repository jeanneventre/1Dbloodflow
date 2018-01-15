#!/usr/bin/python3
import sys, getopt
from csv_libPlot_Profile import *

def main(argv) :

    # PATHS
    ###########

    HOME = "/Users/Arthur/"
    PATH = HOME + "Documents/UPMC/These/Codes/multilayerSingle/example/Well-Balance/Asymptotic/Poiseuille/Elastic/"

    # FILE :
    ###########
    dataName_Profile = "Artery_0_x_r_Ux.csv"
    dataName_Properties = "Artery_0_x_R0_A0_K_R_RmR0_A_Q_U_U0_P_gradP_E_Tw_Cf_a.csv"

    nfig = 1

    Kstr = "1e2"

    Shstr   = "1e-1"
    Lstr    = "10"

    if (Shstr == "1e-1") :
        Sh_p = r"$10^{-1}$"

    K_c     = float(Kstr)
    Sh_c    = float(Shstr) ;
    L_c     = float(Lstr) ;
    R0_c    = 1. ;
    mu_c    = 1. ;
    rho_c   = 1. ;
    Rs_c    = R0_c * (1. + Sh_c)
    Re_c    = R0_c * (1. - Sh_c)
    Q_c     = np.pi * K_c / (40.*mu_c/rho_c*L_c) * ((Rs_c**5.)-(Re_c**5.))
    Us_c    = Q_c / (np.pi * Rs_c * Rs_c)
    #Choose number of layers & Choose number of cells
    J = "800"
    La = "64"

    ProFile  = PATH + "K=" + str(Kstr) + "/Sh=" + str(Shstr) + "/Length=" + str(Lstr) +  "/L=" + str(La) + "/Raf=0/J=" +str(J) + "/" + "HRQ/Order=1/KIN_HAT/Figures/" + dataName_Profile
    PropFile = PATH + "K=" + str(Kstr) + "/Sh=" + str(Shstr) + "/Length=" + str(Lstr) +  "/L=" + str(La) + "/Raf=0/J=" +str(J) + "/" + "HRQ/Order=1/KIN_HAT/Figures/" + dataName_Properties

    # PLOTING :
    ###########
    Store = PATH + "K=" + str(Kstr) + "/Sh=" + str(Shstr) + "/Length=" + str(Lstr) +  "/Figures/"

    it = 0 ; ix = 1 ; iR0 = 2 ; iA0 = 3 ; iK = 4 ;
    iR = 5 ; iRmR0 = 6 ; iA = 7 ;
    iQ = 8 ; iU = 9 ; iU0 = 10 ;
    iP = 11 ; igradxP = 12 ; iE = 13 ;
    iTw = 14 ; iCf = 15 ; ia = 16 ;

    lPropX  = [it,ix,iR0,iR]

    xScale  = L_c
    yScale  = Rs_c
    cbScale = Us_c

    lTextPos    = [[0.15,0.905],[0.5,0.05],[0.97,0.92]]
    lText       = [r"$S_h$="+str(Sh_p), r"$N$="+str(J) +r", $L$=" +str(La),r"$Steady$ $multiring$"]
    lTextAlign  = ["center","center","right"]
    lTextColor  = ["black","black","black"]

    nArrow  = 100 ;
    scArrow = 1. ;

    Colormap    = 'BlueRed'
    Umid        = 1.

    liY = [1,2,3,4,5,6,7,8,9,10]

    xLabel=r"$x \times L^{-1}$"
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
