#!/usr/bin/python3
import sys, getopt
from csv_libPlot_Sensitivity import *

def main(argv) :

    # PATHS
    ###########

    HOME = "/Users/Arthur/"
    PATH = HOME + "Documents/UPMC/These/Codes/multilayer/example/Well-Balance/Asymptotic/Womersley/"

    PATHWOM_20 = HOME + "Documents/UPMC/These/Codes/multilayer/example/Well-Balance/Asymptotic/Womersley/Womersley/a=20/"
    PATHWOM_15 = HOME + "Documents/UPMC/These/Codes/multilayer/example/Well-Balance/Asymptotic/Womersley/Womersley/a=15/"
    PATHWOM_10 = HOME + "Documents/UPMC/These/Codes/multilayer/example/Well-Balance/Asymptotic/Womersley/Womersley/a=10/"
    PATHWOM_5 = HOME + "Documents/UPMC/These/Codes/multilayer/example/Well-Balance/Asymptotic/Womersley/Womersley/a=5/"

    # FILE :
    ###########
    dataName = "Artery_0_t_r_Ux.csv"

    nfig = 1 ;

    for Wom in["20"] :

        #Choose Womersley number
        if (Wom == "5") :
            PATHWOM = PATHWOM_5
        elif (Wom == "10") :
            PATHWOM = PATHWOM_10
        elif (Wom == "15") :
            PATHWOM = PATHWOM_15
        elif (Wom == "20") :
            PATHWOM = PATHWOM_20

        Wom_L4_J50   = PATH + "T_12/" +"a="+str(Wom) + "/"   + "K=1.e4/"   + "L=4/Raf=0/J=50/"   + "HRQ/Order=1/KIN_HAT/Figures/" + dataName
        Wom_L4_J100  = PATH + "T_12/" +"a="+str(Wom) + "/"   + "K=1.e4/"   + "L=4/Raf=0/J=100/"  + "HRQ/Order=1/KIN_HAT/Figures/" + dataName
        Wom_L4_J200  = PATH + "T_12/" +"a="+str(Wom) + "/"   + "K=1.e4/"   + "L=4/Raf=0/J=200/"  + "HRQ/Order=1/KIN_HAT/Figures/" + dataName
        Wom_L4_J400  = PATH + "T_12/" +"a="+str(Wom) + "/"   + "K=1.e4/"   + "L=4/Raf=0/J=400/"  + "HRQ/Order=1/KIN_HAT/Figures/" + dataName
        Wom_L4_J800  = PATH + "T_12/" +"a="+str(Wom) + "/"   + "K=1.e4/"   + "L=4/Raf=0/J=800/"  + "HRQ/Order=1/KIN_HAT/Figures/" + dataName
        Wom_L4_J1600 = PATH + "T_12/" +"a="+str(Wom) + "/"   + "K=1.e4/"   + "L=4/Raf=0/J=1600/" + "HRQ/Order=1/KIN_HAT/Figures/" + dataName
        Wom_L4_J3200 = PATH + "T_12/" +"a="+str(Wom) + "/"   + "K=1.e4/"   + "L=4/Raf=0/J=3200/" + "HRQ/Order=1/KIN_HAT/Figures/" + dataName

        Wom_L8_J50   = PATH + "T_12/" +"a="+str(Wom) + "/"   + "K=1.e4/"   + "L=8/Raf=0/J=50/"   + "HRQ/Order=1/KIN_HAT/Figures/" + dataName
        Wom_L8_J100  = PATH + "T_12/" +"a="+str(Wom) + "/"   + "K=1.e4/"   + "L=8/Raf=0/J=100/"  + "HRQ/Order=1/KIN_HAT/Figures/" + dataName
        Wom_L8_J200  = PATH + "T_12/" +"a="+str(Wom) + "/"   + "K=1.e4/"   + "L=8/Raf=0/J=200/"  + "HRQ/Order=1/KIN_HAT/Figures/" + dataName
        Wom_L8_J400  = PATH + "T_12/" +"a="+str(Wom) + "/"   + "K=1.e4/"   + "L=8/Raf=0/J=400/"  + "HRQ/Order=1/KIN_HAT/Figures/" + dataName
        Wom_L8_J800  = PATH + "T_12/" +"a="+str(Wom) + "/"   + "K=1.e4/"   + "L=8/Raf=0/J=800/"  + "HRQ/Order=1/KIN_HAT/Figures/" + dataName
        Wom_L8_J1600 = PATH + "T_12/" +"a="+str(Wom) + "/"   + "K=1.e4/"   + "L=8/Raf=0/J=1600/" + "HRQ/Order=1/KIN_HAT/Figures/" + dataName
        Wom_L8_J3200 = PATH + "T_12/" +"a="+str(Wom) + "/"   + "K=1.e4/"   + "L=8/Raf=0/J=3200/" + "HRQ/Order=1/KIN_HAT/Figures/" + dataName

        Wom_L16_J50   = PATH + "T_12/" +"a="+str(Wom) + "/"   + "K=1.e4/"   + "L=16/Raf=0/J=50/"   + "HRQ/Order=1/KIN_HAT/Figures/" + dataName
        Wom_L16_J100  = PATH + "T_12/" +"a="+str(Wom) + "/"   + "K=1.e4/"   + "L=16/Raf=0/J=100/"  + "HRQ/Order=1/KIN_HAT/Figures/" + dataName
        Wom_L16_J200  = PATH + "T_12/" +"a="+str(Wom) + "/"   + "K=1.e4/"   + "L=16/Raf=0/J=200/"  + "HRQ/Order=1/KIN_HAT/Figures/" + dataName
        Wom_L16_J400  = PATH + "T_12/" +"a="+str(Wom) + "/"   + "K=1.e4/"   + "L=16/Raf=0/J=400/"  + "HRQ/Order=1/KIN_HAT/Figures/" + dataName
        Wom_L16_J800  = PATH + "T_12/" +"a="+str(Wom) + "/"   + "K=1.e4/"   + "L=16/Raf=0/J=800/"  + "HRQ/Order=1/KIN_HAT/Figures/" + dataName
        Wom_L16_J1600 = PATH + "T_12/" +"a="+str(Wom) + "/"   + "K=1.e4/"   + "L=16/Raf=0/J=1600/" + "HRQ/Order=1/KIN_HAT/Figures/" + dataName
        Wom_L16_J3200 = PATH + "T_12/" +"a="+str(Wom) + "/"   + "K=1.e4/"   + "L=16/Raf=0/J=3200/" + "HRQ/Order=1/KIN_HAT/Figures/" + dataName

        Wom_L32_J50   = PATH + "T_12/" +"a="+str(Wom) + "/"   + "K=1.e4/"   + "L=32/Raf=0/J=50/"   + "HRQ/Order=1/KIN_HAT/Figures/" + dataName
        Wom_L32_J100  = PATH + "T_12/" +"a="+str(Wom) + "/"   + "K=1.e4/"   + "L=32/Raf=0/J=100/"  + "HRQ/Order=1/KIN_HAT/Figures/" + dataName
        Wom_L32_J200  = PATH + "T_12/" +"a="+str(Wom) + "/"   + "K=1.e4/"   + "L=32/Raf=0/J=200/"  + "HRQ/Order=1/KIN_HAT/Figures/" + dataName
        Wom_L32_J400  = PATH + "T_12/" +"a="+str(Wom) + "/"   + "K=1.e4/"   + "L=32/Raf=0/J=400/"  + "HRQ/Order=1/KIN_HAT/Figures/" + dataName
        Wom_L32_J800  = PATH + "T_12/" +"a="+str(Wom) + "/"   + "K=1.e4/"   + "L=32/Raf=0/J=800/"  + "HRQ/Order=1/KIN_HAT/Figures/" + dataName
        Wom_L32_J1600 = PATH + "T_12/" +"a="+str(Wom) + "/"   + "K=1.e4/"   + "L=32/Raf=0/J=1600/" + "HRQ/Order=1/KIN_HAT/Figures/" + dataName
        Wom_L32_J3200 = PATH + "T_12/" +"a="+str(Wom) + "/"   + "K=1.e4/"   + "L=32/Raf=0/J=3200/" + "HRQ/Order=1/KIN_HAT/Figures/" + dataName

        Wom_L64_J50   = PATH + "T_12/" +"a="+str(Wom) + "/"   + "K=1.e4/"   + "L=64/Raf=0/J=50/"   + "HRQ/Order=1/KIN_HAT/Figures/" + dataName
        Wom_L64_J100  = PATH + "T_12/" +"a="+str(Wom) + "/"   + "K=1.e4/"   + "L=64/Raf=0/J=100/"  + "HRQ/Order=1/KIN_HAT/Figures/" + dataName
        Wom_L64_J200  = PATH + "T_12/" +"a="+str(Wom) + "/"   + "K=1.e4/"   + "L=64/Raf=0/J=200/"  + "HRQ/Order=1/KIN_HAT/Figures/" + dataName
        Wom_L64_J400  = PATH + "T_12/" +"a="+str(Wom) + "/"   + "K=1.e4/"   + "L=64/Raf=0/J=400/"  + "HRQ/Order=1/KIN_HAT/Figures/" + dataName
        Wom_L64_J800  = PATH + "T_12/" +"a="+str(Wom) + "/"   + "K=1.e4/"   + "L=64/Raf=0/J=800/"  + "HRQ/Order=1/KIN_HAT/Figures/" + dataName
        Wom_L64_J1600 = PATH + "T_12/" +"a="+str(Wom) + "/"   + "K=1.e4/"   + "L=64/Raf=0/J=1600/" + "HRQ/Order=1/KIN_HAT/Figures/" + dataName
        Wom_L64_J3200 = PATH + "T_12/" +"a="+str(Wom) + "/"   + "K=1.e4/"   + "L=64/Raf=0/J=3200/" + "HRQ/Order=1/KIN_HAT/Figures/" + dataName

        Wom_L128_J50   = PATH + "T_12/" +"a="+str(Wom) + "/"   + "K=1.e4/"   + "L=128/Raf=0/J=50/"   + "HRQ/Order=1/KIN_HAT/Figures/" + dataName
        Wom_L128_J100  = PATH + "T_12/" +"a="+str(Wom) + "/"   + "K=1.e4/"   + "L=128/Raf=0/J=100/"  + "HRQ/Order=1/KIN_HAT/Figures/" + dataName
        Wom_L128_J200  = PATH + "T_12/" +"a="+str(Wom) + "/"   + "K=1.e4/"   + "L=128/Raf=0/J=200/"  + "HRQ/Order=1/KIN_HAT/Figures/" + dataName
        Wom_L128_J400  = PATH + "T_12/" +"a="+str(Wom) + "/"   + "K=1.e4/"   + "L=128/Raf=0/J=400/"  + "HRQ/Order=1/KIN_HAT/Figures/" + dataName
        Wom_L128_J800  = PATH + "T_12/" +"a="+str(Wom) + "/"   + "K=1.e4/"   + "L=128/Raf=0/J=800/"  + "HRQ/Order=1/KIN_HAT/Figures/" + dataName
        Wom_L128_J1600 = PATH + "T_12/" +"a="+str(Wom) + "/"   + "K=1.e4/"   + "L=128/Raf=0/J=1600/" + "HRQ/Order=1/KIN_HAT/Figures/" + dataName
        Wom_L128_J3200 = PATH + "T_12/" +"a="+str(Wom) + "/"   + "K=1.e4/"   + "L=128/Raf=0/J=3200/" + "HRQ/Order=1/KIN_HAT/Figures/" + dataName

        # ANALYTIC
        ###########
        ANA_Ux  = PATHWOM+"womProfil.csv"

        # PLOTING :
        ###########
        it = 0 ; ix = 1 ; iR0 = 2 ; iA0 = 3 ; iK = 4 ;
        iR = 5 ; iRmR0 = 6 ; iA = 7 ;
        iQ = 8 ; iU = 9 ; iU0 = 10 ;
        iP = 11 ; igradxP = 12 ; iE = 13 ;
        iTw = 14 ; iCf = 15 ; ia = 16 ;

        Store = PATH + "T_12/" +"a=" + str(Wom) + "/Figures/" + "KIN_HAT/"

        xLabel = r'$\frac{\lambda}{\Delta x}$'
        yLabel = r'$\frac{L_a}{\alpha}$'

        Length = 200.
        Alpha = float(Wom)
        Lambda = 80.

        lX = [50,100,200,400,800,1600,3200]
        lX = [x * Lambda / Length for x in lX]
        lY = [4,8,16,32,64,128]
        lY = [y / Alpha for y in lY]

        llFile = [
                    [Wom_L4_J50,Wom_L8_J50,Wom_L16_J50,Wom_L32_J50,Wom_L64_J50,Wom_L128_J50],
                    [Wom_L4_J100,Wom_L8_J100,Wom_L16_J100,Wom_L32_J100,Wom_L64_J100,Wom_L128_J100],
                    [Wom_L4_J200,Wom_L8_J200,Wom_L16_J200,Wom_L32_J200,Wom_L64_J200,Wom_L128_J200],
                    [Wom_L4_J400,Wom_L8_J400,Wom_L16_J400,Wom_L32_J400,Wom_L64_J400,Wom_L128_J400],
                    [Wom_L4_J800,Wom_L8_J800,Wom_L16_J800,Wom_L32_J800,Wom_L64_J800,Wom_L128_J800],
                    [Wom_L4_J1600,Wom_L8_J1600,Wom_L16_J1600,Wom_L32_J1600,Wom_L64_J1600,Wom_L128_J1600],
                    [Wom_L4_J3200,Wom_L8_J3200,Wom_L16_J3200,Wom_L32_J3200,Wom_L64_J3200,Wom_L128_J3200]
                 ]

        lliX = [
                    [0,0,0,0,0,0],
                    [0,0,0,0,0,0],
                    [0,0,0,0,0,0],
                    [0,0,0,0,0,0],
                    [0,0,0,0,0,0],
                    [0,0,0,0,0,0],
                    [0,0,0,0,0,0]
               ]

        xAna = 0 ;

        LegPos = 1
        textPos = [[0.05,0.94],[0.5,0.05]]
        text = ["",""]

        for iProf in [1,2,3,4] :

            ################
            # UX
            ################

            yAna = iProf ;
            lliY = [
                        [iProf,iProf,iProf,iProf,iProf,iProf],
                        [iProf,iProf,iProf,iProf,iProf,iProf],
                        [iProf,iProf,iProf,iProf,iProf,iProf],
                        [iProf,iProf,iProf,iProf,iProf,iProf],
                        [iProf,iProf,iProf,iProf,iProf,iProf],
                        [iProf,iProf,iProf,iProf,iProf,iProf],
                        [iProf,iProf,iProf,iProf,iProf,iProf]
                   ]
            FileAna = ANA_Ux

            cbLabel = r"$\mathrm{Err}\left[Q\right]$"
            title = "Map_J_La_err_Ux_O1_iProf_"+str(iProf)+".eps"

            nfig = plot_csv_Sensitivity_Map_Profile(pathStore=Store,title=title,llFile=llFile,lliX=lliX,lliY=lliY,lX=lX,lY=lY,FileAna=FileAna,xAna=xAna,yAna=yAna,xLabel=xLabel,yLabel=yLabel,cbLabel=cbLabel,LegPos=LegPos,text=text,textPos=textPos,nf=nfig)

if __name__ == "__main__":
   main(sys.argv[1:])
