#!/usr/bin/python3
import sys, getopt
from csv_libPlot_Profile import *

def main(argv) :

    # PATHS
    ###########

    HOME = "/Users/Arthur/"
    PATH2D  = HOME + "Documents/UPMC/These/Codes/multilayerSingle/example/Well-Balance/Japan/Straight/"

    # FILE :
    ###########
    dataName_Profile = "Artery_0_x_r_Ux.csv"
    dataName_Properties = "Artery_0_x.csv"

    nfig = 1

    HRstr   = "HRQ"
    Orderstr= "1"

    Kstr    = "2e6"
    Cvstr   = "0"

    PATH    = PATH2D + "K=" + str(Kstr) + "/Cv=" + str(Cvstr)

    Store   = PATH2D + "/Figures/"

    #Choose number of layers & Choose number of cells
    J1 = "1600" ; L1 = "16"
    ProFile  = PATH + "/L=" + str(L1) + "/Raf=" + str("0") + "/J=" + str(J1) + "/" + str(HRstr) + "/Order=" + str(Orderstr) + "/KIN_HAT" +  "/Figures/" + dataName_Profile
    PropFile = PATH + "/L=" + str(L1) + "/Raf=" + str("0") + "/J=" + str(J1) + "/" + str(HRstr) + "/Order=" + str(Orderstr) + "/KIN_HAT" +  "/Figures/" + dataName_Properties

    # PLOTING :
    ###########

    it = 0 ; ix = 1 ; iR0 = 2 ; iA0 = 3 ; iK = 4 ;
    iR = 5 ; iRmR0 = 6 ; iA = 7 ;
    iQ = 8 ; iU = 9 ; iU0 = 10 ;
    iP = 11 ; igradxP = 12 ; iE = 13 ;
    iTw = 14 ; iCf = 15 ; ia = 16 ;

    lPropX = [it,ix,iR0,iR]

    xScale  = 1
    yScale  = 1
    cbScale = 1

    lText       = [r"$N_x$=" + str(J1) + r", $N_r$=" + str(L1), r"$Order$ " + str(Orderstr),
                   r"$K$="+str(Kstr),   r"$C_\nu$=" + str(Cvstr)]
    lTextAlign  = ["center", "center", "left", "left"]
    lTextPos    = [[0.25,0.04], [0.75,0.05], [0.05,0.935], [0.25,0.925] ]
    lTextColor  = ["black", "black", "black", "black" ]

    nArrow = 100;
    scArrow = 7.

    Colormap = 'BlueRed'

    Umid = 0.

    liY = [1,2,3,4,5,6,7,8,9,10,11]

    title = "Ux_Arrow.pdf"

    xLabel  =r"$x$ $\left[cm\right]$"
    yLabel  =r"$r$ $\left[cm\right]$"
    cbLabel =r"$u_x$ $\left[\frac{cm}{s}\right]$"

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
