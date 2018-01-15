#!/usr/bin/python3
import sys, getopt
from csv_libWrite_Err import *

def main(argv) :

    # PATHS
    ###########

    HOME = "/Users/Arthur/"
    PATH2D = HOME + "Documents/UPMC/These/Codes/multilayerSingle/example/Well-Balance/Asymptotic/Poiseuille/Elastic/"
    PATHANA= HOME + "Documents/UPMC/These/Codes/multilayerSingle/example/Well-Balance/Asymptotic/Poiseuille/Elastic/Analytic/"

    # FILE :
    ###########
    dataName = "Artery_0_x_R0_A0_K_R_RmR0_A_Q_U_U0_P_gradP_E_Tw_Cf_a.csv"

    Kstr    = "1e2"
    Shstr   = "1e-1"
    Lstr    = "10"

    PATH =  PATH2D + "K=" + str(Kstr) + "/Sh=" + str(Shstr) + "/Length=" + str(Lstr)

    J100_L8     = PATH + "/L=" + str(8)  + "/Raf=0/J=" + str(100)    + "/" + "HRQ/Order=1/KIN_HAT/Figures/" + dataName
    J200_L16    = PATH + "/L=" + str(16) + "/Raf=0/J=" + str(200)    + "/" + "HRQ/Order=1/KIN_HAT/Figures/" + dataName
    J400_L32    = PATH + "/L=" + str(32) + "/Raf=0/J=" + str(400)    + "/" + "HRQ/Order=1/KIN_HAT/Figures/" + dataName
    J800_L64    = PATH + "/L=" + str(64) + "/Raf=0/J=" + str(800)    + "/" + "HRQ/Order=1/KIN_HAT/Figures/" + dataName

    for pType in ["p","Q","R", "U0"] :

        if (pType == "p") :
            ANA = PATHANA + "px.csv"
            iY = 11 ;
        if (pType == "Q") :
            ANA = PATHANA + "Qx.csv"
            iY = 8 ;
        if (pType == "R") :
            ANA = PATHANA + "Rx.csv"
            iY = 5 ;
        if (pType == "U0") :
            ANA = PATHANA + "u0x.csv"
            iY = 10 ;

        # GET ERROR
        ###########
        iX = 1

        STORE = PATH + "/Figures/"

        llX     =   [
                        [ [0,iX] ],
                        [ [0,iX] ],
                        [ [0,iX] ],
                        [ [0,iX] ]
                    ]
        llY     =   [
                        [ [1,iY] ],
                        [ [1,iY] ],
                        [ [1,iY] ],
                        [ [1,iY] ]
                    ]
        llFile  =   [
                        [ANA,J100_L8]   ,
                        [ANA,J200_L16]  ,
                        [ANA,J400_L32]  ,
                        [ANA,J800_L64]
                    ]
        lFact   =   [
                        [ 1. ],
                        [ 1. ],
                        [ 1. ],
                        [ 1. ]
                    ]

        lFactOrder=   [
                        8.,
                        16.,
                        32.,
                        64.
                      ]

        xrType = "x"

        for Ltype in ["L1", "L2", "Linf"] :

            title = Ltype + "_" + str(pType) + ".csv"

            write_csv_Err_Cv(   pathStore=STORE,title=title,
                                llFile=llFile,
                                llX=llX,llY=llY,
                                lFact=lFact,lFactOrder=lFactOrder,
                                xrType=xrType,Ltype=Ltype)

if __name__ == "__main__":
   main(sys.argv[1:])
