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
    dataName = "Artery_0_x_r_Ux.csv"

    Kstr    = "1e2"
    Shstr   = "1e-1"
    Lstr    = "10"

    PATH =  PATH2D + "K=" + str(Kstr) + "/Sh=" + str(Shstr) + "/Length=" + str(Lstr)

    J100_L8     = PATH + "/L=" + str(8)  + "/Raf=0/J=" + str(100)    + "/" + "HRQ/Order=1/KIN_HAT/Figures/" + dataName
    J200_L16    = PATH + "/L=" + str(16) + "/Raf=0/J=" + str(200)    + "/" + "HRQ/Order=1/KIN_HAT/Figures/" + dataName
    J400_L32    = PATH + "/L=" + str(32) + "/Raf=0/J=" + str(400)    + "/" + "HRQ/Order=1/KIN_HAT/Figures/" + dataName
    J800_L64    = PATH + "/L=" + str(64) + "/Raf=0/J=" + str(800)    + "/" + "HRQ/Order=1/KIN_HAT/Figures/" + dataName

    ANA = PATHANA + "ux.csv"

    # GET ERROR
    ###########
    iX  = 0;
    iY1 = 1; iY2 = 2; iY3 = 3; iY4 = 4; iY5 = 5;
    iY6 = 6; iY7 = 7; iY8 = 8; iY9 = 9; iY10 = 10; iY11 = 11 ;

    STORE = PATH + "/Figures/"

    llX     =   [
                    [ [0,iX], [0,iX], [0,iX], [0,iX], [0,iX], [0,iX], [0,iX], [0,iX], [0,iX], [0,iX], [0,iX] ],
                    [ [0,iX], [0,iX], [0,iX], [0,iX], [0,iX], [0,iX], [0,iX], [0,iX], [0,iX], [0,iX], [0,iX] ],
                    [ [0,iX], [0,iX], [0,iX], [0,iX], [0,iX], [0,iX], [0,iX], [0,iX], [0,iX], [0,iX], [0,iX] ],
                    [ [0,iX], [0,iX], [0,iX], [0,iX], [0,iX], [0,iX], [0,iX], [0,iX], [0,iX], [0,iX], [0,iX] ]
                ]
    llY     =   [
                    [ [1,iY1], [1,iY2], [1,iY3], [1,iY4], [1,iY5], [1,iY6], [1,iY7], [1,iY8], [1,iY9], [1,iY10], [1,iY11] ],
                    [ [1,iY1], [1,iY2], [1,iY3], [1,iY4], [1,iY5], [1,iY6], [1,iY7], [1,iY8], [1,iY9], [1,iY10], [1,iY11] ],
                    [ [1,iY1], [1,iY2], [1,iY3], [1,iY4], [1,iY5], [1,iY6], [1,iY7], [1,iY8], [1,iY9], [1,iY10], [1,iY11] ],
                    [ [1,iY1], [1,iY2], [1,iY3], [1,iY4], [1,iY5], [1,iY6], [1,iY7], [1,iY8], [1,iY9], [1,iY10], [1,iY11] ]
                ]

    llFile  =   [
                    [ANA,J100_L8]   ,
                    [ANA,J200_L16]  ,
                    [ANA,J400_L32]  ,
                    [ANA,J800_L64]
                ]
    lFact   =   [
                    [float(Lstr)/100., float(Lstr)/100., float(Lstr)/100., float(Lstr)/100., float(Lstr)/100., float(Lstr)/100., float(Lstr)/100., float(Lstr)/100., float(Lstr)/100., float(Lstr)/100., float(Lstr)/100.] ,
                    [float(Lstr)/200., float(Lstr)/200., float(Lstr)/200., float(Lstr)/200., float(Lstr)/200., float(Lstr)/200., float(Lstr)/200., float(Lstr)/200., float(Lstr)/200., float(Lstr)/200., float(Lstr)/200.] ,
                    [float(Lstr)/400., float(Lstr)/400., float(Lstr)/400., float(Lstr)/400., float(Lstr)/400., float(Lstr)/400., float(Lstr)/400., float(Lstr)/400., float(Lstr)/400., float(Lstr)/400., float(Lstr)/400.] ,
                    [float(Lstr)/800., float(Lstr)/800., float(Lstr)/800., float(Lstr)/800., float(Lstr)/800., float(Lstr)/800., float(Lstr)/800., float(Lstr)/800., float(Lstr)/800., float(Lstr)/800., float(Lstr)/800.]
                ]
    # lFact   =   [
    #                 [2., 2., 2., 2., 2., 2., 2. ,2., 2., 2., 2.] ,
    #                 [2., 2., 2., 2., 2., 2., 2. ,2., 2., 2., 2.] ,
    #                 [2., 2., 2., 2., 2., 2., 2. ,2., 2., 2., 2.] ,
    #                 [2., 2., 2., 2., 2., 2., 2. ,2., 2., 2., 2.]
    #             ]

    lFactOrder=   [
                    100.,
                    200.,
                    400.,
                    800.
                  ]

    xrType = "r"

    for Ltype in ["L1"] :

        title = Ltype + "_Ux.csv"

        write_csv_Err_Cv(   pathStore=STORE,title=title,
                            llFile=llFile,
                            llX=llX,llY=llY,
                            lFact=lFact,lFactOrder=lFactOrder,
                            xrType=xrType,Ltype=Ltype)

if __name__ == "__main__":
   main(sys.argv[1:])
