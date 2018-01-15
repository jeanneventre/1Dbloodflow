#!/usr/bin/python3
import sys, getopt
from csv_libWrite_Err import *

def main(argv) :

    # PATHS
    ###########

    HOME = "/Users/Arthur/"
    PATH2D = HOME + "Documents/UPMC/These/Codes/multilayerSingle/example/Well-Balance/Asymptotic/Womersley/"
    PATHANA= HOME + "Documents/UPMC/These/Codes/multilayerSingle/example/Well-Balance/Asymptotic/Womersley/Womersley/"

    # FILE :
    ###########
    dataName = "Artery_0_t_r_Ux.csv"

    Kstr    = "1.e4"
    dRstr   = "1e-3"
    Lstr    = "10"

    for a in ["5","20"] :

        PATH =  PATH2D + "T_12" + "/a=" + str(a) + "/K=" + str(Kstr) + "/dR=" + str(dRstr)

        STORE = PATH2D + "T_12" + "/a=" + str(a) + "/Figures/"

        J100_L8     = PATH + "/L=" + str(8)  + "/Raf=0/J=" + str(100)    + "/" + "HRQ/Order=1/KIN_HAT/Figures/" + dataName
        J200_L16    = PATH + "/L=" + str(16) + "/Raf=0/J=" + str(200)    + "/" + "HRQ/Order=1/KIN_HAT/Figures/" + dataName
        J400_L32    = PATH + "/L=" + str(32) + "/Raf=0/J=" + str(400)    + "/" + "HRQ/Order=1/KIN_HAT/Figures/" + dataName
        J800_L64    = PATH + "/L=" + str(64) + "/Raf=0/J=" + str(800)    + "/" + "HRQ/Order=1/KIN_HAT/Figures/" + dataName

        ANA = PATHANA + "a=" + str(a) + "/womProfil.csv"

        # GET ERROR
        ###########
        iX  = 0;
        iY1 = 1; iY2 = 2; iY3 = 3; iY4 = 4;

        llX     =   [
                        [ [0,iX], [0,iX], [0,iX], [0,iX] ],
                        [ [0,iX], [0,iX], [0,iX], [0,iX] ],
                        [ [0,iX], [0,iX], [0,iX], [0,iX] ],
                        [ [0,iX], [0,iX], [0,iX], [0,iX] ]
                    ]
        llY     =   [
                        [ [1,iY1], [1,iY2], [1,iY3], [1,iY4] ],
                        [ [1,iY1], [1,iY2], [1,iY3], [1,iY4] ],
                        [ [1,iY1], [1,iY2], [1,iY3], [1,iY4] ],
                        [ [1,iY1], [1,iY2], [1,iY3], [1,iY4] ]
                    ]

        llFile  =   [
                        [ANA,J100_L8]   ,
                        [ANA,J200_L16]  ,
                        [ANA,J400_L32]  ,
                        [ANA,J800_L64]
                    ]
        lFact   =   [
                        [ 1., 1., 1., 1. ] ,
                        [ 1., 1., 1., 1. ] ,
                        [ 1., 1., 1., 1. ] ,
                        [ 1., 1., 1., 1. ]
                    ]

        for Ltype in ["L1", "L2", "Linf"] :

            title = "a_"+ str(a) + "_" + Ltype + "_Ux.csv"

            write_csv_Err_Cv(   pathStore=STORE,title=title,
                                llFile=llFile,
                                llX=llX,llY=llY,
                                lFact=lFact,Ltype=Ltype)

if __name__ == "__main__":
   main(sys.argv[1:])
