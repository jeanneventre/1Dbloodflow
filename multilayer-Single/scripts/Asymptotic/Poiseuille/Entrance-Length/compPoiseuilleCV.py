#!/usr/bin/python3
import sys, getopt
from csv_libPlot import *

def main(argv) :

    # PATHS
    ###########

    HOME = "/Users/Arthur/"
    PATH = HOME + "Documents/UPMC/These/Codes/multilayerSingle/example/Well-Balance/Asymptotic/Poiseuille/Entrance-Length/"

    # FILE :
    ###########
    dataName = "Artery_0_x_R0_A0_K_R_RmR0_A_Q_U_U0_P_gradP_E_Tw_Cf_a.csv"

    nfig = 1

    Restr = "100"
    Ustr = "100"
    Lstr = "25"

    Re_c = float(Restr) ;
    U_c = float(Ustr) ;
    R_c = 1. ;
    mu_c = U_c * R_c / Re_c ;

    K1 = "1e6" ; L1 = "32" ;
    K1_1 = PATH + "K=" + str(K1) + "/Re=" + str(Restr) + "/U=" + str(Ustr) + "/Length=" + str(Lstr) +  "/L=" + str(L1) + "/Raf=0/J=" +str("800")    + "/" + "HRQ/Order=1/KIN_HAT/Figures/" + dataName
    K1_2 = PATH + "K=" + str(K1) + "/Re=" + str(Restr) + "/U=" + str(Ustr) + "/Length=" + str(Lstr) +  "/L=" + str(L1) + "/Raf=0/J=" +str("1600")   + "/" + "HRQ/Order=1/KIN_HAT/Figures/" + dataName
    K1_3 = PATH + "K=" + str(K1) + "/Re=" + str(Restr) + "/U=" + str(Ustr) + "/Length=" + str(Lstr) +  "/L=" + str(L1) + "/Raf=0/J=" +str("3200")   + "/" + "HRQ/Order=1/KIN_HAT/Figures/" + dataName

    K2 = "1e7" ; L2 = "32" ;
    K2_1 = PATH + "K=" + str(K2) + "/Re=" + str(Restr) + "/U=" + str(Ustr) + "/Length=" + str(Lstr) +  "/L=" + str(L2) + "/Raf=0/J=" +str("800")    + "/" + "HRQ/Order=1/KIN_HAT/Figures/" + dataName
    K2_2 = PATH + "K=" + str(K2) + "/Re=" + str(Restr) + "/U=" + str(Ustr) + "/Length=" + str(Lstr) +  "/L=" + str(L2) + "/Raf=0/J=" +str("1600")   + "/" + "HRQ/Order=1/KIN_HAT/Figures/" + dataName
    K2_3 = PATH + "K=" + str(K2) + "/Re=" + str(Restr) + "/U=" + str(Ustr) + "/Length=" + str(Lstr) +  "/L=" + str(L2) + "/Raf=0/J=" +str("3200")   + "/" + "HRQ/Order=1/KIN_HAT/Figures/" + dataName

    K3 = "1e8" ; L3 = "32" ;
    K3_1 = PATH + "K=" + str(K3) + "/Re=" + str(Restr) + "/U=" + str(Ustr) + "/Length=" + str(Lstr) +  "/L=" + str(L3) + "/Raf=0/J=" +str("800")    + "/" + "HRQ/Order=1/KIN_HAT/Figures/" + dataName
    K3_2 = PATH + "K=" + str(K3) + "/Re=" + str(Restr) + "/U=" + str(Ustr) + "/Length=" + str(Lstr) +  "/L=" + str(L3) + "/Raf=0/J=" +str("1600")   + "/" + "HRQ/Order=1/KIN_HAT/Figures/" + dataName
    K3_3 = PATH + "K=" + str(K3) + "/Re=" + str(Restr) + "/U=" + str(Ustr) + "/Length=" + str(Lstr) +  "/L=" + str(L3) + "/Raf=0/J=" +str("3200")   + "/" + "HRQ/Order=1/KIN_HAT/Figures/" + dataName

    # PLOTING :
    ###########
    it = 0 ; ix = 1 ; iR0 = 2 ; iA0 = 3 ; iK = 4 ;
    iR = 5 ; iRmR0 = 6 ; iA = 7 ;
    iQ = 8 ; iU = 9 ; iU0 = 10 ;
    iP = 11 ; igradxP = 12 ; iE = 13 ;
    iTw = 14 ; iCf = 15 ; ia = 16 ;

    Store = PATH + "/Figures/"

    lCol        = ["black","blue"]
    lMark       = ["o","s"]
    lMarkSize   = [7,7]
    lMarkWidth  = [1,1]

    MarkPoints  = 50 ;

    lLineSize   = [1,1]
    lStyle      = ["-","-"]
    lAlpha      = [1,1]
    liX         = [ix,ix]

    xLabel      =r"$N_x$"

    lLabel      = [ "","" ]

    LegPos      = 1
    lTextPos    = [[0.5,0.05]]
    lText       = [""]
    lTextAlign  = ["center"]
    lTextColor  = ["black"]

    lllFile     =   [
                        [ [K1_2,K1_1],  [K2_2,K2_1],    [K3_2,K3_1] ],
                        [ [K1_3,K1_2],  [K2_3,K2_2],    [K3_3,K3_2] ]
                    ]
    llliX       =   [
                        [ [ix,ix],      [ix,ix],        [ix,ix]     ],
                        [ [ix,ix],      [ix,ix],        [ix,ix]     ]
                    ]

    llX          =   [
                        [float(K1),float(K2),float(K3)],
                        [float(K1),float(K2),float(K3)]
                     ]

    errType     = 'L2'
    LinLog      = 'lin'

    lPower      = [ 1./3., 1./3. ]

    #####
    # Tw
    #####
    yLabel      = errType  + r"$\left( \tau_w \right)$"
    llliY       =   [
                        [ [iTw,iTw],    [iTw,iTw],  [iTw,iTw] ],
                        [ [iTw,iTw],    [iTw,iTw],  [iTw,iTw] ]
                    ]

    title = "Cv_K_Tw_Pois.pdf"
    nfig = plot_csv_Convergence(
            pathStore=Store,title=title,
            lllFile=lllFile,llliX=llliX,llliY=llliY,
            llX = llX, lPower = lPower,
            errType = errType, LinLog = LinLog,
            xLabel=xLabel,yLabel=yLabel,lLabel=lLabel,
            LegPos=LegPos,
            lText=lText,lTextPos=lTextPos,lTextAlign=lTextAlign,lTextColor=lTextColor,
            lCol=lCol,lMark=lMark,
            lMarkSize=lMarkSize,lMarkWidth=lMarkWidth,MarkPoints=MarkPoints,
            lLineSize=lLineSize,lStyle=lStyle,lAlpha=lAlpha,nf=nfig)

    #####
    # U0
    #####
    yLabel      = errType  + r"$\left( u_{x_{|x=0}} \right)$"
    llliY       =   [
                        [ [iU0,iU0],    [iU0,iU0],  [iU0,iU0] ],
                        [ [iU0,iU0],    [iU0,iU0],  [iU0,iU0] ]
                    ]

    title = "Cv_K_U0_Pois.pdf"
    nfig = plot_csv_Convergence(
            pathStore=Store,title=title,
            lllFile=lllFile,llliX=llliX,llliY=llliY,
            llX = llX, lPower = lPower,
            errType = errType, LinLog = LinLog,
            xLabel=xLabel,yLabel=yLabel,lLabel=lLabel,
            LegPos=LegPos,
            lText=lText,lTextPos=lTextPos,lTextAlign=lTextAlign,lTextColor=lTextColor,
            lCol=lCol,lMark=lMark,
            lMarkSize=lMarkSize,lMarkWidth=lMarkWidth,MarkPoints=MarkPoints,
            lLineSize=lLineSize,lStyle=lStyle,lAlpha=lAlpha,nf=nfig)

    #####
    # P
    #####
    yLabel      = errType  + r"$\left( P \right)$"
    llliY       =   [
                        [ [iP,iP],    [iP,iP],  [iP,iP] ],
                        [ [iP,iP],    [iP,iP],  [iP,iP] ]
                    ]

    title = "Cv_K_P_Pois.pdf"
    nfig = plot_csv_Convergence(
            pathStore=Store,title=title,
            lllFile=lllFile,llliX=llliX,llliY=llliY,
            llX = llX, lPower = lPower,
            errType = errType, LinLog = LinLog,
            xLabel=xLabel,yLabel=yLabel,lLabel=lLabel,
            LegPos=LegPos,
            lText=lText,lTextPos=lTextPos,lTextAlign=lTextAlign,lTextColor=lTextColor,
            lCol=lCol,lMark=lMark,
            lMarkSize=lMarkSize,lMarkWidth=lMarkWidth,MarkPoints=MarkPoints,
            lLineSize=lLineSize,lStyle=lStyle,lAlpha=lAlpha,nf=nfig)

    #####
    # Q
    #####
    yLabel      = errType  + r"$\left( Q \right)$"
    llliY       =   [
                        [ [iQ,iQ],    [iQ,iQ],  [iQ,iQ] ],
                        [ [iQ,iQ],    [iQ,iQ],  [iQ,iQ] ]
                    ]

    title = "Cv_K_Q_Pois.pdf"
    nfig = plot_csv_Convergence(
            pathStore=Store,title=title,
            lllFile=lllFile,llliX=llliX,llliY=llliY,
            llX = llX, lPower = lPower,
            errType = errType, LinLog = LinLog,
            xLabel=xLabel,yLabel=yLabel,lLabel=lLabel,
            LegPos=LegPos,
            lText=lText,lTextPos=lTextPos,lTextAlign=lTextAlign,lTextColor=lTextColor,
            lCol=lCol,lMark=lMark,
            lMarkSize=lMarkSize,lMarkWidth=lMarkWidth,MarkPoints=MarkPoints,
            lLineSize=lLineSize,lStyle=lStyle,lAlpha=lAlpha,nf=nfig)


if __name__ == "__main__":
   main(sys.argv[1:])
