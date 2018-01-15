#!/usr/bin/python3
import sys, getopt
from csv_libPlot_Sensitivity import *

def main(argv) :

    HOME = "/Users/Arthur/"
    PATH = HOME + "Documents/UPMC/These/Codes/multilayer/example/Well-Balance/Asymptotic/Poiseuille/Imposed_Velocity/Entrance-Length/Reflecting/"

    PATHPOIS = HOME + "Dropbox/These/Codes/SOURCES_RNSPaxi/Entrance_Poiseuille/"

    # FILE :
    ###########
    dataName = "Artery_0_x_R0_A0_K_R_RmR0_A_Q_U_U0_P_gradP_E_Tw_Cf_a.csv"

    nfig = 1

    Kstr = "1e8"
    Restr = "1000"
    Ustr = "100"
    Lstr = "75"

    rho = 1. ; mu = 0.1 ;

    Pois_L4_J50   = PATH + "K=" + str(Kstr) + "/Re=" + str(Restr) + "/U=" + str(Ustr) + "/Length=" + str(Lstr) +  "/L=4/Raf=0/J=50/"   + "HRQ/Order=1/KIN_HAT/Figures/" + dataName
    Pois_L4_J100  = PATH + "K=" + str(Kstr) + "/Re=" + str(Restr) + "/U=" + str(Ustr) + "/Length=" + str(Lstr) +  "/L=4/Raf=0/J=100/"  + "HRQ/Order=1/KIN_HAT/Figures/" + dataName
    Pois_L4_J200  = PATH + "K=" + str(Kstr) + "/Re=" + str(Restr) + "/U=" + str(Ustr) + "/Length=" + str(Lstr) +  "/L=4/Raf=0/J=200/"  + "HRQ/Order=1/KIN_HAT/Figures/" + dataName
    Pois_L4_J400  = PATH + "K=" + str(Kstr) + "/Re=" + str(Restr) + "/U=" + str(Ustr) + "/Length=" + str(Lstr) +  "/L=4/Raf=0/J=400/"  + "HRQ/Order=1/KIN_HAT/Figures/" + dataName
    Pois_L4_J800  = PATH + "K=" + str(Kstr) + "/Re=" + str(Restr) + "/U=" + str(Ustr) + "/Length=" + str(Lstr) +  "/L=4/Raf=0/J=800/"  + "HRQ/Order=1/KIN_HAT/Figures/" + dataName
    Pois_L4_J1600 = PATH + "K=" + str(Kstr) + "/Re=" + str(Restr) + "/U=" + str(Ustr) + "/Length=" + str(Lstr) +  "/L=4/Raf=0/J=1600/" + "HRQ/Order=1/KIN_HAT/Figures/" + dataName
    Pois_L4_J3200 = PATH + "K=" + str(Kstr) + "/Re=" + str(Restr) + "/U=" + str(Ustr) + "/Length=" + str(Lstr) +  "/L=4/Raf=0/J=3200/" + "HRQ/Order=1/KIN_HAT/Figures/" + dataName

    Pois_L8_J50   = PATH + "K=" + str(Kstr) + "/Re=" + str(Restr) + "/U=" + str(Ustr) + "/Length=" + str(Lstr) +  "/L=8/Raf=0/J=50/"   + "HRQ/Order=1/KIN_HAT/Figures/" + dataName
    Pois_L8_J100  = PATH + "K=" + str(Kstr) + "/Re=" + str(Restr) + "/U=" + str(Ustr) + "/Length=" + str(Lstr) +  "/L=8/Raf=0/J=100/"  + "HRQ/Order=1/KIN_HAT/Figures/" + dataName
    Pois_L8_J200  = PATH + "K=" + str(Kstr) + "/Re=" + str(Restr) + "/U=" + str(Ustr) + "/Length=" + str(Lstr) +  "/L=8/Raf=0/J=200/"  + "HRQ/Order=1/KIN_HAT/Figures/" + dataName
    Pois_L8_J400  = PATH + "K=" + str(Kstr) + "/Re=" + str(Restr) + "/U=" + str(Ustr) + "/Length=" + str(Lstr) +  "/L=8/Raf=0/J=400/"  + "HRQ/Order=1/KIN_HAT/Figures/" + dataName
    Pois_L8_J800  = PATH + "K=" + str(Kstr) + "/Re=" + str(Restr) + "/U=" + str(Ustr) + "/Length=" + str(Lstr) +  "/L=8/Raf=0/J=800/"  + "HRQ/Order=1/KIN_HAT/Figures/" + dataName
    Pois_L8_J1600 = PATH + "K=" + str(Kstr) + "/Re=" + str(Restr) + "/U=" + str(Ustr) + "/Length=" + str(Lstr) +  "/L=8/Raf=0/J=1600/" + "HRQ/Order=1/KIN_HAT/Figures/" + dataName
    Pois_L8_J3200 = PATH + "K=" + str(Kstr) + "/Re=" + str(Restr) + "/U=" + str(Ustr) + "/Length=" + str(Lstr) +  "/L=8/Raf=0/J=3200/" + "HRQ/Order=1/KIN_HAT/Figures/" + dataName

    Pois_L16_J50   = PATH + "K=" + str(Kstr) + "/Re=" + str(Restr) + "/U=" + str(Ustr) + "/Length=" + str(Lstr) +  "/L=16/Raf=0/J=50/"   + "HRQ/Order=1/KIN_HAT/Figures/" + dataName
    Pois_L16_J100  = PATH + "K=" + str(Kstr) + "/Re=" + str(Restr) + "/U=" + str(Ustr) + "/Length=" + str(Lstr) +  "/L=16/Raf=0/J=100/"  + "HRQ/Order=1/KIN_HAT/Figures/" + dataName
    Pois_L16_J200  = PATH + "K=" + str(Kstr) + "/Re=" + str(Restr) + "/U=" + str(Ustr) + "/Length=" + str(Lstr) +  "/L=16/Raf=0/J=200/"  + "HRQ/Order=1/KIN_HAT/Figures/" + dataName
    Pois_L16_J400  = PATH + "K=" + str(Kstr) + "/Re=" + str(Restr) + "/U=" + str(Ustr) + "/Length=" + str(Lstr) +  "/L=16/Raf=0/J=400/"  + "HRQ/Order=1/KIN_HAT/Figures/" + dataName
    Pois_L16_J800  = PATH + "K=" + str(Kstr) + "/Re=" + str(Restr) + "/U=" + str(Ustr) + "/Length=" + str(Lstr) +  "/L=16/Raf=0/J=800/"  + "HRQ/Order=1/KIN_HAT/Figures/" + dataName
    Pois_L16_J1600 = PATH + "K=" + str(Kstr) + "/Re=" + str(Restr) + "/U=" + str(Ustr) + "/Length=" + str(Lstr) +  "/L=16/Raf=0/J=1600/" + "HRQ/Order=1/KIN_HAT/Figures/" + dataName
    Pois_L16_J3200 = PATH + "K=" + str(Kstr) + "/Re=" + str(Restr) + "/U=" + str(Ustr) + "/Length=" + str(Lstr) +  "/L=16/Raf=0/J=3200/" + "HRQ/Order=1/KIN_HAT/Figures/" + dataName

    Pois_L32_J50   = PATH + "K=" + str(Kstr) + "/Re=" + str(Restr) + "/U=" + str(Ustr) + "/Length=" + str(Lstr) +  "/L=32/Raf=0/J=50/"   + "HRQ/Order=1/KIN_HAT/Figures/" + dataName
    Pois_L32_J100  = PATH + "K=" + str(Kstr) + "/Re=" + str(Restr) + "/U=" + str(Ustr) + "/Length=" + str(Lstr) +  "/L=32/Raf=0/J=100/"  + "HRQ/Order=1/KIN_HAT/Figures/" + dataName
    Pois_L32_J200  = PATH + "K=" + str(Kstr) + "/Re=" + str(Restr) + "/U=" + str(Ustr) + "/Length=" + str(Lstr) +  "/L=32/Raf=0/J=200/"  + "HRQ/Order=1/KIN_HAT/Figures/" + dataName
    Pois_L32_J400  = PATH + "K=" + str(Kstr) + "/Re=" + str(Restr) + "/U=" + str(Ustr) + "/Length=" + str(Lstr) +  "/L=32/Raf=0/J=400/"  + "HRQ/Order=1/KIN_HAT/Figures/" + dataName
    Pois_L32_J800  = PATH + "K=" + str(Kstr) + "/Re=" + str(Restr) + "/U=" + str(Ustr) + "/Length=" + str(Lstr) +  "/L=32/Raf=0/J=800/"  + "HRQ/Order=1/KIN_HAT/Figures/" + dataName
    Pois_L32_J1600 = PATH + "K=" + str(Kstr) + "/Re=" + str(Restr) + "/U=" + str(Ustr) + "/Length=" + str(Lstr) +  "/L=32/Raf=0/J=1600/" + "HRQ/Order=1/KIN_HAT/Figures/" + dataName
    Pois_L32_J3200 = PATH + "K=" + str(Kstr) + "/Re=" + str(Restr) + "/U=" + str(Ustr) + "/Length=" + str(Lstr) +  "/L=32/Raf=0/J=3200/" + "HRQ/Order=1/KIN_HAT/Figures/" + dataName

    Pois_L64_J50   = PATH + "K=" + str(Kstr) + "/Re=" + str(Restr) + "/U=" + str(Ustr) + "/Length=" + str(Lstr) +  "/L=64/Raf=0/J=50/"   + "HRQ/Order=1/KIN_HAT/Figures/" + dataName
    Pois_L64_J100  = PATH + "K=" + str(Kstr) + "/Re=" + str(Restr) + "/U=" + str(Ustr) + "/Length=" + str(Lstr) +  "/L=64/Raf=0/J=100/"  + "HRQ/Order=1/KIN_HAT/Figures/" + dataName
    Pois_L64_J200  = PATH + "K=" + str(Kstr) + "/Re=" + str(Restr) + "/U=" + str(Ustr) + "/Length=" + str(Lstr) +  "/L=64/Raf=0/J=200/"  + "HRQ/Order=1/KIN_HAT/Figures/" + dataName
    Pois_L64_J400  = PATH + "K=" + str(Kstr) + "/Re=" + str(Restr) + "/U=" + str(Ustr) + "/Length=" + str(Lstr) +  "/L=64/Raf=0/J=400/"  + "HRQ/Order=1/KIN_HAT/Figures/" + dataName
    Pois_L64_J800  = PATH + "K=" + str(Kstr) + "/Re=" + str(Restr) + "/U=" + str(Ustr) + "/Length=" + str(Lstr) +  "/L=64/Raf=0/J=800/"  + "HRQ/Order=1/KIN_HAT/Figures/" + dataName
    Pois_L64_J1600 = PATH + "K=" + str(Kstr) + "/Re=" + str(Restr) + "/U=" + str(Ustr) + "/Length=" + str(Lstr) +  "/L=64/Raf=0/J=1600/" + "HRQ/Order=1/KIN_HAT/Figures/" + dataName
    Pois_L64_J3200 = PATH + "K=" + str(Kstr) + "/Re=" + str(Restr) + "/U=" + str(Ustr) + "/Length=" + str(Lstr) +  "/L=64/Raf=0/J=3200/" + "HRQ/Order=1/KIN_HAT/Figures/" + dataName

    ANA = PATHPOIS+"T.OUT"

    # PLOTING :
    ###########
    it = 0 ; ix = 1 ; iR0 = 2 ; iA0 = 3 ; iK = 4 ;
    iR = 5 ; iRmR0 = 6 ; iA = 7 ;
    iQ = 8 ; iU = 9 ; iU0 = 10 ;
    iP = 11 ; igradxP = 12 ; iE = 13 ;
    iTw = 14 ; iCf = 15 ; ia = 16 ;

    Store = PATH + "K=" + str(Kstr) + "/Re=" + str(Restr) + "/U=" + str(Ustr) + "/Length=" + str(Lstr) +  "/Figures/" + "KIN_HAT/"


    xLabel = r'$\frac{R_{e,R} R}{\Delta x}$'
    yLabel = r'$L_a$'

    Re = 500.
    R = 0.5
    Length = 75

    lX = [50,100,200,400,800,1600,3200]
    # lX = [x * Re * R / Length for x in lX]
    lY = [4,8,16,32,64]

    llFile = [
                [Pois_L4_J50,Pois_L8_J50,Pois_L16_J50,Pois_L32_J50 ,Pois_L64_J50],
                [Pois_L4_J100,Pois_L8_J100,Pois_L16_J100,Pois_L32_J100 ,Pois_L64_J100],
                [Pois_L4_J200,Pois_L8_J200,Pois_L16_J200,Pois_L32_J200 ,Pois_L64_J200]
                [Pois_L4_J400,Pois_L8_J400,Pois_L16_J400,Pois_L32_J400 ,Pois_L64_J400],
                [Pois_L4_J800,Pois_L8_J800,Pois_L16_J800,Pois_L32_J800 ,Pois_L64_J800],
                [Pois_L4_J1600,Pois_L8_J1600,Pois_L16_J1600,Pois_L32_J1600,Pois_L64_J1600]
                # [Pois_L4_J3200,Pois_L8_J3200,Pois_L16_J3200,Pois_L32_J3200,Pois_L64_J3200]
             ]

    lliX = [
                [ix,ix,ix,ix,ix],
                [ix,ix,ix,ix,ix],
                [ix,ix,ix,ix,ix],
                [ix,ix,ix,ix,ix],
                [ix,ix,ix,ix,ix],
                [ix,ix,ix,ix,ix],
                [ix,ix,ix,ix,ix]
           ]

    xAna = 0 ; FileAna = ANA


    LegPos = 1
    textPos = [[0.05,0.94],[0.5,0.05]]
    text = ["",""]

    xLim = 1.

    ################
    # U0
    ################
    lliY = [
                [iU0,iU0,iU0,iU0,iU0],
                [iU0,iU0,iU0,iU0,iU0],
                [iU0,iU0,iU0,iU0,iU0],
                [iU0,iU0,iU0,iU0,iU0],
                [iU0,iU0,iU0,iU0,iU0],
                [iU0,iU0,iU0,iU0,iU0],
                [iU0,iU0,iU0,iU0,iU0]
           ]

    yAna = 6

    cbLabel = r"$\mathrm{Err}\left[U_{r=0}\right]$"
    title = "Map_J_La_err_U0_O1.eps"

    nfig = plot_csv_Sensitivity_Map_Poiseuille(pathStore=Store,title=title,llFile=llFile,lliX=lliX,lliY=lliY,lX=lX,lY=lY,FileAna=FileAna,xAna=xAna,yAna=yAna,rho=rho,mu=mu,xLabel=xLabel,yLabel=yLabel,cbLabel=cbLabel,LegPos=LegPos,text=text,textPos=textPos,nf=nfig)

    ################
    # P
    ################
    lliY = [
                [iP,iP,iP,iP,iP],
                [iP,iP,iP,iP,iP],
                [iP,iP,iP,iP,iP],
                [iP,iP,iP,iP,iP],
                [iP,iP,iP,iP,iP],
                [iP,iP,iP,iP,iP],
                [iP,iP,iP,iP,iP]
           ]

    yAna = 2

    cbLabel = r"$\mathrm{Err}\left[P\right]$"
    title = "Map_J_La_err_P_O1.eps"

    nfig = plot_csv_Sensitivity_Map_Poiseuille(pathStore=Store,title=title,llFile=llFile,lliX=lliX,lliY=lliY,lX=lX,lY=lY,FileAna=FileAna,xAna=xAna,yAna=yAna,rho=rho,mu=mu,xLabel=xLabel,yLabel=yLabel,cbLabel=cbLabel,LegPos=LegPos,text=text,textPos=textPos,nf=nfig)

    ################
    # Tw
    ################
    lliY = [
                [iTw,iTw,iTw,iTw,iTw],
                [iTw,iTw,iTw,iTw,iTw],
                [iTw,iTw,iTw,iTw,iTw],
                [iTw,iTw,iTw,iTw,iTw],
                [iTw,iTw,iTw,iTw,iTw],
                [iTw,iTw,iTw,iTw,iTw],
                [iTw,iTw,iTw,iTw,iTw]
           ]

    yAna = 5

    cbLabel = r"$\mathrm{Err}\left[\tau_w\right]$"
    title = "Map_J_La_err_Tw_O1.eps"

    nfig = plot_csv_Sensitivity_Map_Poiseuille(pathStore=Store,title=title,llFile=llFile,lliX=lliX,lliY=lliY,lX=lX,lY=lY,FileAna=FileAna,xAna=xAna,yAna=yAna,rho=rho,mu=mu,xLabel=xLabel,yLabel=yLabel,cbLabel=cbLabel,LegPos=LegPos,text=text,textPos=textPos,nf=nfig)


if __name__ == "__main__":
   main(sys.argv[1:])
