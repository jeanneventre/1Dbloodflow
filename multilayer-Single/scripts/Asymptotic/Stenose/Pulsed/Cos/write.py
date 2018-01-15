#!/usr/bin/python3
import sys, getopt
from multiS_libData import *
from multiS_libWrite import *

import numpy as np

def main(argv) :
    PATH = ""
    # COMMAND LINE ARGUMENTS
    #############################
    try :
        opts, args = getopt.getopt(argv,"hp:",["path="])
    except getopt.GetoptError:
          print ('plot.py -p <PATH>')
          sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print ('plot.py -p <PATH>')
            sys.exit()
        elif opt in ("-p", "--PATH"):
            PATH = arg

	if not os.path.exists(str(PATH)+"Figures"):
		os.makedirs(str(PATH)+"Figures")
	folderPath_store = str(PATH) + "Figures/"

    folderPath= str(PATH)

    # DATA CLASS :
    ##############

    wb = dataS(folderPath,folderPath_store,logo="Sane")

    # WRITING :
    ###########

    Re  = 100.
    Wom = 15.
    Sh  = 1.e-2

    K   = 1.e5
    R   = 1.
    rho = 1.

    U   = Sh * np.sqrt( K/2./rho * np.sqrt(np.pi)*R )
    nu  = U * R * rho / Re
    Le  = float(Re * R)
    T = 2. * np.pi / nu * ( (R / Wom )**2. )

    # lTime = [
    #             # 2.0*T, 2.1*T, 2.2*T, 2.25*T, 2.3*T, 2.4*T, 2.5*T, 2.6*T, 2.7*T, 2.75*T, 2.8*T, 2.9*T,
    #             # 3.0*T, 3.1*T, 3.2*T, 3.25*T, 3.3*T, 3.4*T, 3.5*T, 3.6*T, 3.7*T, 3.75*T, 3.8*T, 3.9*T,
    #             4.0*T, 4.1*T, 4.2*T, 4.25*T, 4.3*T, 4.4*T, 4.5*T, 4.6*T, 4.7*T, 4.75*T, 4.8*T, 4.9*T
    #
    #          ]
    # lLabel = [
    #             # "2p0T", "2p1T", "2p2T", "2p25T", "2p3T", "2p4T", "2p5T", "2p6T", "2p7T", "2p75T", "2p8T", "2p9T",
    #             # "3p0T", "3p1T", "3p2T", "3p25T", "3p3T", "3p4T", "3p5T", "3p6T", "3p7T", "3p75T", "3p8T", "3p9T",
    #             "4p0T", "4p1T", "4p2T", "4p25T", "4p3T", "4p4T", "4p5T", "4p6T", "4p7T", "4p75T", "4p8T", "4p9T"
    #          ]

    lTime = [
                4.0*T, 4.2*T, 4.6*T, 4.9*T
             ]
    lLabel = [
                "4p0T", "4p2T", "4p6T", "4p9T"
             ]

    # write_ChangeName_x_R0_A0_K_R_RmR0_A_Q_U_U0_P_gradP_E_Tw_Cf_a_Sh(cls=wb,numArt=0,lTime=lTime,lLabel=lLabel)
    write_ChangeName_x_All(cls=wb,numArt=0,lTime=lTime,lLabel=lLabel)
    #
    # lTime = [
    #             4.0*T, 4.2*T, 4.6*T, 4.9*T
    #          ]
    # lLabel = [
    #             "4p0T", "4p25T", "4p5T", "4p75T"
    #          ]
    #
    lX = [  0.*Le, 0.025*Le, 0.05*Le, 0.075*Le, 0.1*Le,
            0.125*Le, 0.15*Le, 0.175*Le, 0.2*Le,
            0.225*Le, 0.249*Le ]

    # # lX = [  0.*Le, 0.01*Le, 0.02*Le, 0.03*Le, 0.04*Le,
    # #         0.05*Le, 0.06*Le, 0.07*Le, 0.08*Le,
    # #         0.09*Le, 0.099*Le ]
    #
    # write_ChangeName_x_Ux(cls=wb,numArt=0,lX=lX,lTime=lTime,lLabel=lLabel)

    lLabel = [  "0p0Le", "0p025Le", "0p05Le", "0p075Le", "0p1Le",
                "0p125Le", "0p15Le", "0p175Le", "0p2Le",
                "0p225Le", "0p249Le"]

    # # lLabel = [  "0p0Le", "0p01Le", "0p02Le", "0p03Le", "0p04Le",
    # #             "0p05Le", "0p06Le", "0p06Le", "0p08Le",
    # #             "0p09Le", "0p099Le"]
    #
    # # write_ChangeName_t_R0_A0_K_R_RmR0_A_Q_U_U0_P_gradP_E_Tw_Cf_Sh(cls=wb,numArt=0,lX=lX,lLabel=lLabel)
    write_ChangeName_t_All(cls=wb,numArt=0,lX=lX,lLabel=lLabel)



if __name__ == "__main__":
   main(sys.argv[1:])
