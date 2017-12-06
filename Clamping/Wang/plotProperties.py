#!/usr/bin/python3
import  sys, getopt
import  numpy       as np

import  help_Output as out

from    csv_libPlot_Network import *

def main(argv) :

    # PATHS
    ###########

    HOME    = "/Users/Arthur/"
    PATH1D  = HOME + "Documents/UPMC/These/Codes/bloodflow/Examples/Clamping/Wang/"

    nfig    = 1

    Nxstr       = "3"
    xOrderstr   = "2"

    dtstr       = "1e-5"
    tOrderstr   = "2"

    NNstr       = "Newtonian"

    HRstr       = "HRQ"
    Solverstr   = "KIN_HAT"

    Conjstr     = "jS"

    nuvstr      = "0"

    for State in ["Sane"] :

        PATH    = PATH1D + State + "/" + NNstr + "/" + Conjstr + "/nuv=" + nuvstr + "/Nx=" + Nxstr + "/xOrder=" + xOrderstr + "/dt=" + dtstr + "/tOrder=" + tOrderstr + "/" + Solverstr + "/" + HRstr + "/"
        Store   = PATH1D + "Figures/"

        for pType in ["K","A0","Cv"] :

            pName,pLabel = out.getType(pType)

            # FILE :
            ###########

            lDag    = [
                        [0,1],[1,2],[1,3],[3,4],[3,5],[4,6],[4,7],[7,8],[7,9],[9,10],
                        [9,11],[5,12],[5,13],[2,14],[2,15],[15,16],[15,17],[14,18],[14,19],[19,20],
                        [19,21],[21,22],[21,23],[23,24],[23,25],[18,26],[18,27],[27,28],[27,29],[29,30],
                        [29,31],[30,32],[30,33],[28,34],[28,35],[35,36],[35,37],[37,38],[37,39],[39,40],
                        [39,41],[41,42],[41,43],[42,44],[42,45],[44,46],[44,47],[46,48],[46,49],[43,50],
                        [43,51],[50,52],[50,53],[52,54],[52,55]
                    ]

            # Length of the vessels (cm)
            lL  =   [
                        4.0,  2.0,  3.4,  3.4,  17.7, 14.8, 42.2, 23.5, 6.7,  7.9,
                        17.1, 17.6, 17.7, 3.9,  20.8, 17.6, 17.7, 5.2,  3.4,  14.8,
                        42.2, 23.5, 6.7,  7.9,  17.1, 8.0,  10.4, 5.3,  2.0,  1.0,
                        6.6,  7.1,  6.3,  5.9,  1.0,  3.2,  1.0,  3.2,  10.6, 5.0,
                        1.0,  5.9,  5.8,  14.4, 5.0,  44.3, 12.6, 32.1, 34.3, 14.5,
                        5.0,  44.4, 12.7, 32.2, 34.4
                    ]

            # Radius of the artery (cm)
            lR  =   [
                        1.470, 1.263, 0.699, 0.541, 0.473, 0.240, 0.515, 0.367, 0.454, 0.194,
                        0.433, 0.382, 0.382, 1.195, 0.413, 0.334, 0.334, 1.120, 0.474, 0.203,
                        0.455, 0.324, 0.401, 0.172, 0.383, 0.317, 1.071, 0.920, 0.588, 0.540,
                        0.458, 0.375, 0.386, 0.499, 0.843, 0.350, 0.794, 0.350, 0.665, 0.194,
                        0.631, 0.470, 0.470, 0.482, 0.301, 0.361, 0.356, 0.376, 0.198, 0.482,
                        0.301, 0.361, 0.356, 0.375, 0.197
                    ]
            lAngle  = [
                        np.pi*3./4.,    np.pi/2.,       -np.pi/2.,      -np.pi/2.,      np.pi*9./8.,    np.pi*5./4.,    -np.pi*1./4.,   np.pi*1./4.,    -np.pi*1./4.,   -np.pi/8.,
                        np.pi/8.,       np.pi*7./8.,    np.pi*9./8.,    np.pi/4.,       np.pi*7./8.,    np.pi*9./8.,    np.pi*7./8.,    0.,             np.pi/2.,       np.pi*3./4.,
                        np.pi*5./16.,   -np.pi*1./4.,   np.pi*1./4.,    np.pi*1./8.,    -np.pi*1./8.,   np.pi/2.,       0.,             0.,             -np.pi/2.,      -np.pi/2.,
                        -np.pi/4.,      -np.pi*3./4.,   -np.pi*3./8.,   np.pi/2.,       0.,             -np.pi/2.,      0.,             np.pi/2.,       0.,             np.pi/2.,
                        0.,             np.pi*3./8.,    -np.pi*3./8.,   np.pi*1./4.,    -np.pi*1./8.,   0.,             -np.pi/4.,      np.pi/8.,       -np.pi/8.,      -np.pi/4.,
                        np.pi/8.,       0.,             np.pi/4.,       np.pi/8.,       -np.pi/8.
                        ]

            xRange  = [-50.,60.]
            yRange  = [-135.,55.]

            xStart  = 0.
            yStart  = 0.

            if (pType == "K") :
                cbScale = 1.e7
                cbRange = [0,7]
                cbMid   = 0.5
                colorMap = "Segmented3"
            elif (pType == "A0") :
                cbScale = 1.
                cbRange = [0,8]
                cbMid   = 0.05
                colorMap = "Segmented"
            elif (pType == "Cv") :
                cbScale = 1.e3
                cbRange = [3.5,11.5]
                cbMid   = 0.5
                colorMap = "Segmented3"
            else :
                cbScale = 1.
                cbRange = []
                cbMid   = 0.5
                colorMap = "Segmented"

            if (pType == "K") :
                cbLabel = r"$K$ $10^{7} \left[ \frac{g}{cm^{2}.s^{2}} \right]$"
            elif (pType == "Cv") :
                cbLabel = r"$C_\nu$ $10^{3} \left[ \frac{cm^2}{s} \right]$"
            else :
                cbLabel = pLabel

            liX         = []
            liY         = []
            lFileSep    = []
            lFile       = []
            for i in range(55) :
                liX.append(0)
                liY.append([1,2,3])
                lFileSep.append(",")
                lFile.append( PATH + "Figures/" + "Artery_" + str(i) + "_t_"  + pName )

            T_c = 1.
            ts  = 9. * T_c

            for Time in [ ts ] :

                lText       = [r"$Wang$ $55$-$Artery$ $Network$"]
                lTextPos    = [[0.5,.01]]
                lTextAlign  = ["center"]
                lTextColor  = ["black"]

                title   = "Properties-Wang-" + State + "-" + pType + ".pdf"

                nfig = plot_csv_network(pathStore=Store,title=title,
                                        Time = Time,
                                        lFile=lFile,lFileSep=lFileSep,
                                        liX=liX,liY=liY,
                                        cbLabel=cbLabel,
                                        lDag=lDag,
                                        lL=lL,lR=lR,lAngle=lAngle,
                                        xStart=xStart,yStart=yStart,
                                        xRange=xRange,yRange=yRange,
                                        cbScale=cbScale,cbRange=cbRange,cbMid=cbMid,colorMap=colorMap,
                                        lText=lText,lTextPos=lTextPos,lTextAlign=lTextAlign,lTextColor=lTextColor,
                                        nf=nfig)

if __name__ == "__main__":
   main(sys.argv[1:])
