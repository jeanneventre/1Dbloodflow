#!/usr/bin/python3
import sys, getopt
from csv_libPlot import *

def main(argv) :

    # PATHS
    ###########

    HOME = "/Users/Arthur/"
    PATH    = HOME + "Documents/UPMC/These/Codes/multilayerSingle/example/Well-Balance/Asymptotic/Stenose/Established/Cos/Rvar/"
    PATH1D  = HOME + "Documents/UPMC/These/Codes/bloodflowSingle/example/Well-Balance/Asymptotic/Stenose/Established/Cos/Rvar/"

    PATH_Steady = HOME + "Dropbox/These/Codes/SOURCES_RNSPaxi/Stenosis/"

    # FILE :
    ###########
    dataName = "Artery_0_x_R0_A0_K_R_RmR0_A_Q_U_U0_P_gradP_E_Tw_Cf_a.csv"
    dataName1D = "Artery_0_x_R0_A0_K_R_RmR0_A_Q_U_P_gradxP_E_Hrbc_Nrbc_G_fst_Twst_Tw_Fr.csv"

    nfig = 1

    Kstr        = "1e7"
    Restr       = "100"
    Ustr        = "100"
    Lstr        = "25"
    Lststr      = "10"

    K_c     = r"$10^7$"
    Re_c    = float(Restr) ;
    U_c     = float(Ustr) ;
    R_c     = 1. ;
    mu_c    = U_c * R_c / Re_c ;

    #Choose number of layers & Choose number of cells
    J = "1600" ;
    La = "32"

    for dRstr in ["-0.4","+0.4"] :

        Sten  = PATH + "K=" + str(Kstr) + "/Re=" + str(Restr) + "/U=" + str(Ustr) + "/Length=" + str(Lstr) + "/dR=" + str(dRstr) + "/Lst=" + str(Lststr) + "/L=" + str(La) + "/Raf=0/J=" +str(J) + "/" + "HRQ/Order=1/KIN_HAT/Figures/" + dataName

        phi1 = "-4"
        Sten1_1D   = PATH1D + "K=" + str(Kstr) + "/Re=" + str(Restr) + "/U=" + str(Ustr) + "/Length=" + str(Lstr) + "/dR=" + str(dRstr) + "/Lst=" + str(Lststr) + "/Newtonian" + "/phi=" + str(phi1) + "/J=" +str(J) + "/" + "HRQ/Order=1/KIN_HAT/Figures/" + dataName1D

        if (dRstr == "-0.4") :
            Steady = PATH_Steady + "Established_Stenose_dR_0p4/T.OUT"
        if (dRstr == "+0.4") :
            Steady = PATH_Steady + "Established_Aneurysm_dR_0p4/T.OUT"

        # PLOTING :
        ###########

        Store = PATH + "K=" + str(Kstr) + "/Re=" + str(Restr) + "/U=" + str(Ustr) + "/Length=" + str(Lstr) + "/dR=" + str(dRstr) + "/Lst=" + str(Lststr) +  "/Figures/"

        lCol        =   [   "black", "red",
                            "blue",
                            "green"
                        ]
        lMark       =   [   "", "",
                            "^",
                            "D"
                        ]
        lMarkSize   =   [   9, 9,
                            9,
                            9
                        ]
        lMarkWidth  =   [   2, 2,
                            2,
                            2
                        ]

        MarkPoints = 60 ;

        lLineSize   =   [   2, 2,
                            2,
                            2
                        ]
        lStyle      =   [   "--", "-",
                            "",
                            ""
                        ]
        lAlpha      =   [   1, 1,
                            0.7,
                            0.7
                        ]

        LegLoc = 1
        if (dRstr == "+0.4") :
            LegPos = [0.,0.36]
        else :
            LegPos = [1,0.8]
        LegCol = 1

        lLabel      =   [   "", r"$Steady$",
                            r"$Multiring$, $N_r$="+str(La),
                            r"$1D$, $C_f$=$8\pi\nu$"
                        ]

        # lTextPos =   [[0.15,0.905],[0.25,0.04],[0.5,0.05],[0.75,0.05]]
        # lText =      [r"$R_{e,R}$="+str(Restr),r"$N_x$="+str(J),
        #               r"$K$="+str(K_c),r"$\Delta R$="+str(dRstr)]
        # lTextAlign = ["center","center","center","center"]
        # lTextColor = ["black","black","black","black"]

        lTextPos =   [[0.15,0.905],[0.25,0.04]]
        lText =      [r"$R_{e,R}$="+str(Restr),r"$N_x$="+str(J)]
        lTextAlign = ["center","center"]
        lTextColor = ["black","black"]

        # lTextPos =   [[0.15,0.905]]
        # lText =      [r"$R_{e,R}$="+str(Restr)]
        # lTextAlign = ["center"]
        # lTextColor = ["black"]

        xRange = []
        yRange = []

        lHline      = [0]
        lHlineColor = ["black"]
        lHlineWidth = [2]
        lHlineStyle = ["-"]

        lVline      = [0.10]
        lVlineColor = ["black"]
        lVlineWidth = [2]
        lVlineStyle = ["--"]

        xLabel=r"$x \times \left[R_{e,R} R_{|x=0}\right]^{-1}$"


        liX         =   [   1, 0,
                            1,
                            1
                        ]
        lXScale     =   [   Re_c*R_c, 1.,
                            Re_c*R_c,
                            Re_c*R_c
                        ]
        lXOffset    =   [   0., 0.,
                            0.,
                            0.
                        ]

        for pType in ["Tw","P"] :

            if (pType == "Tw") :
                yLabel=r"$\tau_w \times \left[  \mu \frac{U_{|x=0}}{R_{|x=0}} \right]^{-1}$"
                iYRef       = 5
                iY          = 14
                iY1D        = 18
                YScaleRef   = 1.
                YScale      = mu_c * U_c / R_c
                YScale1D    = - mu_c * U_c / R_c
                YOffsetRef  = 0.
                YOffset     = 0.
                YOffset1D   = 0.

                if (dRstr == "-0.4") :
                    R0Scale     = 4./100.*R_c
                    R0Offset    = -1
                if (dRstr == "+0.4") :
                    R0Scale     = 4./20.*R_c
                    R0Offset    = -0.5

            if (pType == "P") :
                yLabel = r"$\left[p-p_{|x=0}\right] \times \left[ \rho u_{x_{|x=0}}^2 \right]^{-1}$"
                iYRef       = 2
                iY          = 11
                iY1D        = 10
                YScaleRef   = 1.
                YScale      = U_c * U_c
                YScale1D    = U_c * U_c
                YOffsetRef  = "first"
                YOffset     = "first"
                YOffset1D   = "first"

                if (dRstr == "-0.4") :
                    R0Scale     = 4./10.*R_c
                    R0Offset    = -1
                if (dRstr == "+0.4") :
                    R0Scale     = 4./2.*R_c
                    R0Offset    = -0.5

            liY         =   [   2, iYRef,
                                iY,
                                iY1D
                            ]

            lYScale     =   [   R0Scale, YScaleRef,
                                YScale,
                                YScale1D
                            ]
            lYOffset    =   [   R0Offset, YOffsetRef,
                                YOffset,
                                YOffset1D
                            ]

            lFileSep    =   [ ",",",",
                              ",",
                              ","
                            ]
            lFile       =   [   Sten1_1D, Steady,
                                Sten,
                                Sten1_1D
                            ]

            title = "Conf_" + pType + "_dR_" + str(dRstr) + ".pdf"

            nfig = plot_csv_adim(
                    pathStore=Store,title=title,lFile=lFile,lFileSep=lFileSep,
                    liX=liX,liY=liY,
                    xLabel=xLabel,yLabel=yLabel,lLabel=lLabel,
                    lXScale=lXScale,lYScale=lYScale,lXOffset=lXOffset,lYOffset=lYOffset,
                    xRange=xRange,yRange=yRange,
                    lHline=lHline,lHlineColor=lHlineColor,lHlineWidth=lHlineWidth,lHlineStyle=lHlineStyle,
                    lVline=lVline,lVlineColor=lVlineColor,lVlineWidth=lVlineWidth,lVlineStyle=lVlineStyle,
                    LegLoc=LegLoc,LegPos=LegPos,LegCol=LegCol,
                    lText=lText,lTextPos=lTextPos,lTextAlign=lTextAlign,lTextColor=lTextColor,
                    lCol=lCol,lMark=lMark,
                    lMarkSize=lMarkSize,lMarkWidth=lMarkWidth,MarkPoints=MarkPoints,
                    lLineSize=lLineSize,lStyle=lStyle,lAlpha=lAlpha,nf=nfig)

if __name__ == "__main__":
   main(sys.argv[1:])
