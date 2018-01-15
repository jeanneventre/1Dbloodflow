#!/usr/bin/python3
import sys, getopt
from csv_libPlot_Sensitivity import *

def main(argv) :

    # PATHS
    ###########

    HOME = "/Users/Arthur/"
    PATH = HOME + "Documents/UPMC/These/Codes/multilayerSingle/example/Well-Balance/Asymptotic/Womersley/"

    PATHWOM_20 = HOME + "Documents/UPMC/These/Codes/multilayer/example/Well-Balance/Asymptotic/Womersley/Womersley/a=20/"
    PATHWOM_15 = HOME + "Documents/UPMC/These/Codes/multilayer/example/Well-Balance/Asymptotic/Womersley/Womersley/a=15/"
    PATHWOM_10 = HOME + "Documents/UPMC/These/Codes/multilayer/example/Well-Balance/Asymptotic/Womersley/Womersley/a=10/"
    PATHWOM_5 = HOME + "Documents/UPMC/These/Codes/multilayer/example/Well-Balance/Asymptotic/Womersley/Womersley/a=5/"

    # FILE :
    ###########
    dataName = "Artery_0_x_R0_A0_K_R_RmR0_A_Q_U_U0_P_gradP_E_Tw_Cf_a.csv"

    nfig = 1 ;

    dRstr = "1e-3"

    for Womstr in["5", "20"] :

        #Choose Womersley number
        if (Womstr == "5") :
            PATHWOM = PATHWOM_5
        elif (Womstr == "10") :
            PATHWOM = PATHWOM_10
        elif (Womstr == "15") :
            PATHWOM = PATHWOM_15
        elif (Womstr == "20") :
            PATHWOM = PATHWOM_20

        Wom_L4_J25   = PATH + "T_12/" +"a="+str(Womstr) + "/"   + "K=1.e4/" + "dR=" + dRstr + "/L=4/Raf=0/J=25/"   + "HRQ/Order=1/KIN_HAT/Figures/" + dataName
        Wom_L4_J50   = PATH + "T_12/" +"a="+str(Womstr) + "/"   + "K=1.e4/" + "dR=" + dRstr + "/L=4/Raf=0/J=50/"   + "HRQ/Order=1/KIN_HAT/Figures/" + dataName
        Wom_L4_J100  = PATH + "T_12/" +"a="+str(Womstr) + "/"   + "K=1.e4/" + "dR=" + dRstr + "/L=4/Raf=0/J=100/"  + "HRQ/Order=1/KIN_HAT/Figures/" + dataName
        Wom_L4_J200  = PATH + "T_12/" +"a="+str(Womstr) + "/"   + "K=1.e4/" + "dR=" + dRstr + "/L=4/Raf=0/J=200/"  + "HRQ/Order=1/KIN_HAT/Figures/" + dataName
        Wom_L4_J400  = PATH + "T_12/" +"a="+str(Womstr) + "/"   + "K=1.e4/" + "dR=" + dRstr + "/L=4/Raf=0/J=400/"  + "HRQ/Order=1/KIN_HAT/Figures/" + dataName
        Wom_L4_J800  = PATH + "T_12/" +"a="+str(Womstr) + "/"   + "K=1.e4/" + "dR=" + dRstr + "/L=4/Raf=0/J=800/"  + "HRQ/Order=1/KIN_HAT/Figures/" + dataName
        Wom_L4_J1600 = PATH + "T_12/" +"a="+str(Womstr) + "/"   + "K=1.e4/" + "dR=" + dRstr + "/L=4/Raf=0/J=1600/" + "HRQ/Order=1/KIN_HAT/Figures/" + dataName
        Wom_L4_J3200 = PATH + "T_12/" +"a="+str(Womstr) + "/"   + "K=1.e4/" + "dR=" + dRstr + "/L=4/Raf=0/J=3200/" + "HRQ/Order=1/KIN_HAT/Figures/" + dataName

        Wom_L8_J25   = PATH + "T_12/" +"a="+str(Womstr) + "/"   + "K=1.e4/" + "dR=" + dRstr + "/L=8/Raf=0/J=25/"   + "HRQ/Order=1/KIN_HAT/Figures/" + dataName
        Wom_L8_J50   = PATH + "T_12/" +"a="+str(Womstr) + "/"   + "K=1.e4/" + "dR=" + dRstr + "/L=8/Raf=0/J=50/"   + "HRQ/Order=1/KIN_HAT/Figures/" + dataName
        Wom_L8_J100  = PATH + "T_12/" +"a="+str(Womstr) + "/"   + "K=1.e4/" + "dR=" + dRstr + "/L=8/Raf=0/J=100/"  + "HRQ/Order=1/KIN_HAT/Figures/" + dataName
        Wom_L8_J200  = PATH + "T_12/" +"a="+str(Womstr) + "/"   + "K=1.e4/" + "dR=" + dRstr + "/L=8/Raf=0/J=200/"  + "HRQ/Order=1/KIN_HAT/Figures/" + dataName
        Wom_L8_J400  = PATH + "T_12/" +"a="+str(Womstr) + "/"   + "K=1.e4/" + "dR=" + dRstr + "/L=8/Raf=0/J=400/"  + "HRQ/Order=1/KIN_HAT/Figures/" + dataName
        Wom_L8_J800  = PATH + "T_12/" +"a="+str(Womstr) + "/"   + "K=1.e4/" + "dR=" + dRstr + "/L=8/Raf=0/J=800/"  + "HRQ/Order=1/KIN_HAT/Figures/" + dataName
        Wom_L8_J1600 = PATH + "T_12/" +"a="+str(Womstr) + "/"   + "K=1.e4/" + "dR=" + dRstr + "/L=8/Raf=0/J=1600/" + "HRQ/Order=1/KIN_HAT/Figures/" + dataName
        Wom_L8_J3200 = PATH + "T_12/" +"a="+str(Womstr) + "/"   + "K=1.e4/" + "dR=" + dRstr + "/L=8/Raf=0/J=3200/" + "HRQ/Order=1/KIN_HAT/Figures/" + dataName

        Wom_L16_J25   = PATH + "T_12/" +"a="+str(Womstr) + "/"   + "K=1.e4/" + "dR=" + dRstr + "/L=16/Raf=0/J=25/"   + "HRQ/Order=1/KIN_HAT/Figures/" + dataName
        Wom_L16_J50   = PATH + "T_12/" +"a="+str(Womstr) + "/"   + "K=1.e4/" + "dR=" + dRstr + "/L=16/Raf=0/J=50/"   + "HRQ/Order=1/KIN_HAT/Figures/" + dataName
        Wom_L16_J100  = PATH + "T_12/" +"a="+str(Womstr) + "/"   + "K=1.e4/" + "dR=" + dRstr + "/L=16/Raf=0/J=100/"  + "HRQ/Order=1/KIN_HAT/Figures/" + dataName
        Wom_L16_J200  = PATH + "T_12/" +"a="+str(Womstr) + "/"   + "K=1.e4/" + "dR=" + dRstr + "/L=16/Raf=0/J=200/"  + "HRQ/Order=1/KIN_HAT/Figures/" + dataName
        Wom_L16_J400  = PATH + "T_12/" +"a="+str(Womstr) + "/"   + "K=1.e4/" + "dR=" + dRstr + "/L=16/Raf=0/J=400/"  + "HRQ/Order=1/KIN_HAT/Figures/" + dataName
        Wom_L16_J800  = PATH + "T_12/" +"a="+str(Womstr) + "/"   + "K=1.e4/" + "dR=" + dRstr + "/L=16/Raf=0/J=800/"  + "HRQ/Order=1/KIN_HAT/Figures/" + dataName
        Wom_L16_J1600 = PATH + "T_12/" +"a="+str(Womstr) + "/"   + "K=1.e4/" + "dR=" + dRstr + "/L=16/Raf=0/J=1600/" + "HRQ/Order=1/KIN_HAT/Figures/" + dataName
        Wom_L16_J3200 = PATH + "T_12/" +"a="+str(Womstr) + "/"   + "K=1.e4/" + "dR=" + dRstr + "/L=16/Raf=0/J=3200/" + "HRQ/Order=1/KIN_HAT/Figures/" + dataName

        Wom_L32_J25   = PATH + "T_12/" +"a="+str(Womstr) + "/"   + "K=1.e4/" + "dR=" + dRstr + "/L=32/Raf=0/J=25/"   + "HRQ/Order=1/KIN_HAT/Figures/" + dataName
        Wom_L32_J50   = PATH + "T_12/" +"a="+str(Womstr) + "/"   + "K=1.e4/" + "dR=" + dRstr + "/L=32/Raf=0/J=50/"   + "HRQ/Order=1/KIN_HAT/Figures/" + dataName
        Wom_L32_J100  = PATH + "T_12/" +"a="+str(Womstr) + "/"   + "K=1.e4/" + "dR=" + dRstr + "/L=32/Raf=0/J=100/"  + "HRQ/Order=1/KIN_HAT/Figures/" + dataName
        Wom_L32_J200  = PATH + "T_12/" +"a="+str(Womstr) + "/"   + "K=1.e4/" + "dR=" + dRstr + "/L=32/Raf=0/J=200/"  + "HRQ/Order=1/KIN_HAT/Figures/" + dataName
        Wom_L32_J400  = PATH + "T_12/" +"a="+str(Womstr) + "/"   + "K=1.e4/" + "dR=" + dRstr + "/L=32/Raf=0/J=400/"  + "HRQ/Order=1/KIN_HAT/Figures/" + dataName
        Wom_L32_J800  = PATH + "T_12/" +"a="+str(Womstr) + "/"   + "K=1.e4/" + "dR=" + dRstr + "/L=32/Raf=0/J=800/"  + "HRQ/Order=1/KIN_HAT/Figures/" + dataName
        Wom_L32_J1600 = PATH + "T_12/" +"a="+str(Womstr) + "/"   + "K=1.e4/" + "dR=" + dRstr + "/L=32/Raf=0/J=1600/" + "HRQ/Order=1/KIN_HAT/Figures/" + dataName
        Wom_L32_J3200 = PATH + "T_12/" +"a="+str(Womstr) + "/"   + "K=1.e4/" + "dR=" + dRstr + "/L=32/Raf=0/J=3200/" + "HRQ/Order=1/KIN_HAT/Figures/" + dataName

        Wom_L64_J25   = PATH + "T_12/" +"a="+str(Womstr) + "/"   + "K=1.e4/" + "dR=" + dRstr + "/L=64/Raf=0/J=25/"   + "HRQ/Order=1/KIN_HAT/Figures/" + dataName
        Wom_L64_J50   = PATH + "T_12/" +"a="+str(Womstr) + "/"   + "K=1.e4/" + "dR=" + dRstr + "/L=64/Raf=0/J=50/"   + "HRQ/Order=1/KIN_HAT/Figures/" + dataName
        Wom_L64_J100  = PATH + "T_12/" +"a="+str(Womstr) + "/"   + "K=1.e4/" + "dR=" + dRstr + "/L=64/Raf=0/J=100/"  + "HRQ/Order=1/KIN_HAT/Figures/" + dataName
        Wom_L64_J200  = PATH + "T_12/" +"a="+str(Womstr) + "/"   + "K=1.e4/" + "dR=" + dRstr + "/L=64/Raf=0/J=200/"  + "HRQ/Order=1/KIN_HAT/Figures/" + dataName
        Wom_L64_J400  = PATH + "T_12/" +"a="+str(Womstr) + "/"   + "K=1.e4/" + "dR=" + dRstr + "/L=64/Raf=0/J=400/"  + "HRQ/Order=1/KIN_HAT/Figures/" + dataName
        Wom_L64_J800  = PATH + "T_12/" +"a="+str(Womstr) + "/"   + "K=1.e4/" + "dR=" + dRstr + "/L=64/Raf=0/J=800/"  + "HRQ/Order=1/KIN_HAT/Figures/" + dataName
        Wom_L64_J1600 = PATH + "T_12/" +"a="+str(Womstr) + "/"   + "K=1.e4/" + "dR=" + dRstr + "/L=64/Raf=0/J=1600/" + "HRQ/Order=1/KIN_HAT/Figures/" + dataName
        Wom_L64_J3200 = PATH + "T_12/" +"a="+str(Womstr) + "/"   + "K=1.e4/" + "dR=" + dRstr + "/L=64/Raf=0/J=3200/" + "HRQ/Order=1/KIN_HAT/Figures/" + dataName

        Wom_L128_J25   = PATH + "T_12/" +"a="+str(Womstr) + "/"   + "K=1.e4/" + "dR=" + dRstr + "/L=128/Raf=0/J=25/"   + "HRQ/Order=1/KIN_HAT/Figures/" + dataName
        Wom_L128_J50   = PATH + "T_12/" +"a="+str(Womstr) + "/"   + "K=1.e4/" + "dR=" + dRstr + "/L=128/Raf=0/J=50/"   + "HRQ/Order=1/KIN_HAT/Figures/" + dataName
        Wom_L128_J100  = PATH + "T_12/" +"a="+str(Womstr) + "/"   + "K=1.e4/" + "dR=" + dRstr + "/L=128/Raf=0/J=100/"  + "HRQ/Order=1/KIN_HAT/Figures/" + dataName
        Wom_L128_J200  = PATH + "T_12/" +"a="+str(Womstr) + "/"   + "K=1.e4/" + "dR=" + dRstr + "/L=128/Raf=0/J=200/"  + "HRQ/Order=1/KIN_HAT/Figures/" + dataName
        Wom_L128_J400  = PATH + "T_12/" +"a="+str(Womstr) + "/"   + "K=1.e4/" + "dR=" + dRstr + "/L=128/Raf=0/J=400/"  + "HRQ/Order=1/KIN_HAT/Figures/" + dataName
        Wom_L128_J800  = PATH + "T_12/" +"a="+str(Womstr) + "/"   + "K=1.e4/" + "dR=" + dRstr + "/L=128/Raf=0/J=800/"  + "HRQ/Order=1/KIN_HAT/Figures/" + dataName
        Wom_L128_J1600 = PATH + "T_12/" +"a="+str(Womstr) + "/"   + "K=1.e4/" + "dR=" + dRstr + "/L=128/Raf=0/J=1600/" + "HRQ/Order=1/KIN_HAT/Figures/" + dataName
        Wom_L128_J3200 = PATH + "T_12/" +"a="+str(Womstr) + "/"   + "K=1.e4/" + "dR=" + dRstr + "/L=128/Raf=0/J=3200/" + "HRQ/Order=1/KIN_HAT/Figures/" + dataName

        # ANALYTIC
        ###########
        ANA_Q   = PATHWOM + "womQx.csv"
        ANA_P   = PATHWOM + "womPx.csv"
        ANA_Tw  = PATHWOM + "womTwx.csv"

        # PLOTING :
        ###########
        it = 0 ; ix = 1 ; iR0 = 2 ; iA0 = 3 ; iK = 4 ;
        iR = 5 ; iRmR0 = 6 ; iA = 7 ;
        iQ = 8 ; iU = 9 ; iU0 = 10 ;
        iP = 11 ; igradxP = 12 ; iE = 13 ;
        iTw = 14 ; iCf = 15 ; ia = 16 ;

        Store = PATH + "T_12/" + "a=" + str(Womstr) + "/Figures/"

        xLabel = r'$N_x \times \lambda \times L^{-1}$'
        yLabel = r'$N_r \times \alpha^{-1}$'

        Length = 200.
        Alpha = float(Womstr)
        Lambda = 80.

        lX = [25,50,100,200,400,800,1600,3200]
        lX = [x * Lambda / Length for x in lX]
        lY = [4,8,16,32,64,128]
        lY = [y / Alpha for y in lY]

        llFile = [
                    [Wom_L4_J25,Wom_L8_J25,Wom_L16_J25,Wom_L32_J25,Wom_L64_J25,Wom_L128_J25],
                    [Wom_L4_J50,Wom_L8_J50,Wom_L16_J50,Wom_L32_J50,Wom_L64_J50,Wom_L128_J50],
                    [Wom_L4_J100,Wom_L8_J100,Wom_L16_J100,Wom_L32_J100,Wom_L64_J100,Wom_L128_J100],
                    [Wom_L4_J200,Wom_L8_J200,Wom_L16_J200,Wom_L32_J200,Wom_L64_J200,Wom_L128_J200],
                    [Wom_L4_J400,Wom_L8_J400,Wom_L16_J400,Wom_L32_J400,Wom_L64_J400,Wom_L128_J400],
                    [Wom_L4_J800,Wom_L8_J800,Wom_L16_J800,Wom_L32_J800,Wom_L64_J800,Wom_L128_J800],
                    [Wom_L4_J1600,Wom_L8_J1600,Wom_L16_J1600,Wom_L32_J1600,Wom_L64_J1600,Wom_L128_J1600],
                    [Wom_L4_J3200,Wom_L8_J3200,Wom_L16_J3200,Wom_L32_J3200,Wom_L64_J3200,Wom_L128_J3200]
                 ]

        lliX = [
                    [ix,ix,ix,ix,ix,ix],
                    [ix,ix,ix,ix,ix,ix],
                    [ix,ix,ix,ix,ix,ix],
                    [ix,ix,ix,ix,ix,ix],
                    [ix,ix,ix,ix,ix,ix],
                    [ix,ix,ix,ix,ix,ix],
                    [ix,ix,ix,ix,ix,ix],
                    [ix,ix,ix,ix,ix,ix]
               ]

        xAna = 0 ; yAna = 1 ;

        LegPos = 1

        lTextPos = [[1.175,0.95]]
        lText = [r"$\alpha$="+str(Womstr)]
        lTextAlign = ["center"]
        lTextColor = ["black"]

        Ltype = "L2"

        ################
        # Q
        ################
        lliY = [
                    [iQ,iQ,iQ,iQ,iQ,iQ],
                    [iQ,iQ,iQ,iQ,iQ,iQ],
                    [iQ,iQ,iQ,iQ,iQ,iQ],
                    [iQ,iQ,iQ,iQ,iQ,iQ],
                    [iQ,iQ,iQ,iQ,iQ,iQ],
                    [iQ,iQ,iQ,iQ,iQ,iQ],
                    [iQ,iQ,iQ,iQ,iQ,iQ],
                    [iQ,iQ,iQ,iQ,iQ,iQ]
               ]
        FileAna = ANA_Q

        cbLabel = r"$\mathrm{L_2}\left(Q\right)$"
        title = "Q_Map_J_La_O1.pdf"

        nfig = plot_csv_Sensitivity_Map_Wom(
                pathStore=Store,title=title,llFile=llFile,
                lliX=lliX,lliY=lliY,lX=lX,lY=lY,
                FileAna=FileAna,xAna=xAna,yAna=yAna,
                xLabel=xLabel,yLabel=yLabel,cbLabel=cbLabel,
                LegPos=LegPos,
                lText=lText,lTextPos=lTextPos,lTextAlign=lTextAlign,lTextColor=lTextColor,
                Ltype=Ltype,
                nf=nfig)

        ################
        # P
        ################
        lliY = [
                    [iP,iP,iP,iP,iP,iP],
                    [iP,iP,iP,iP,iP,iP],
                    [iP,iP,iP,iP,iP,iP],
                    [iP,iP,iP,iP,iP,iP],
                    [iP,iP,iP,iP,iP,iP],
                    [iP,iP,iP,iP,iP,iP],
                    [iP,iP,iP,iP,iP,iP],
                    [iP,iP,iP,iP,iP,iP]
               ]
        FileAna = ANA_P

        cbLabel = r"$\mathrm{L_2}\left(p\right)$"
        title = "P_Map_J_La_O1.pdf"

        nfig = plot_csv_Sensitivity_Map_Wom(
                pathStore=Store,title=title,llFile=llFile,
                lliX=lliX,lliY=lliY,lX=lX,lY=lY,
                FileAna=FileAna,xAna=xAna,yAna=yAna,
                xLabel=xLabel,yLabel=yLabel,cbLabel=cbLabel,
                LegPos=LegPos,
                lText=lText,lTextPos=lTextPos,lTextAlign=lTextAlign,lTextColor=lTextColor,
                Ltype=Ltype,
                nf=nfig)

        ################
        # Tw
        ################
        lliY = [
                    [iTw,iTw,iTw,iTw,iTw,iTw],
                    [iTw,iTw,iTw,iTw,iTw,iTw],
                    [iTw,iTw,iTw,iTw,iTw,iTw],
                    [iTw,iTw,iTw,iTw,iTw,iTw],
                    [iTw,iTw,iTw,iTw,iTw,iTw],
                    [iTw,iTw,iTw,iTw,iTw,iTw],
                    [iTw,iTw,iTw,iTw,iTw,iTw],
                    [iTw,iTw,iTw,iTw,iTw,iTw]
               ]
        FileAna = ANA_Tw

        cbLabel = r"$\mathrm{L_2}\left(\tau_w\right)$"
        title = "Tw_Map_J_La_O1.pdf"

        nfig = plot_csv_Sensitivity_Map_Wom(
                pathStore=Store,title=title,llFile=llFile,
                lliX=lliX,lliY=lliY,lX=lX,lY=lY,
                FileAna=FileAna,xAna=xAna,yAna=yAna,
                xLabel=xLabel,yLabel=yLabel,cbLabel=cbLabel,
                LegPos=LegPos,
                lText=lText,lTextPos=lTextPos,lTextAlign=lTextAlign,lTextColor=lTextColor,
                Ltype=Ltype,
                nf=nfig)

if __name__ == "__main__":
   main(sys.argv[1:])
