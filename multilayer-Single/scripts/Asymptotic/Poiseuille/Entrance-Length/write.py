#!/usr/bin/python3
import sys, getopt
from multiS_libData import *
from multiS_libWrite import *

def main(argv) :
    PATH = ""
    U = "" ; Re = "" ;
    # COMMAND LINE ARGUMENTS
    #############################
    try :
        opts, args = getopt.getopt(argv,"hp:u:r:",["path=",'U=','Re='])
    except getopt.GetoptError:
          print ('plot.py -p <PATH> -u <U> -r <Re>')
          sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print ('plot.py -p <PATH> -u <U> -r <Re>')
            sys.exit()
        elif opt in ("-p", "--PATH"):
            PATH = arg
        elif opt in ("-u", "--U"):
            U = float(arg)
        elif opt in ("-r", "--Re"):
            Re = float(arg)

	if not os.path.exists(str(PATH)+"Figures"):
		os.makedirs(str(PATH)+"Figures")
	folderPath_store = str(PATH) + "Figures/"

    folderPath= str(PATH)


    # DATA CLASS :
    ##############

    wb = dataS(folderPath,folderPath_store,logo="Sane")

    # PLOTING :
    ###########
    nfig = 1

    R = 1.
    L = 25.
    Le = float(Re * R)
    te = float(Le)/float(U)

    lTime = [te * 0.49]

    write_x_R0_A0_K_R_RmR0_A_Q_U_U0_P_gradP_E_Tw_Cf_a(cls=wb,numArt=0,lTime=lTime)

    lX = [0.005*Le, 0.01*Le, 0.025*Le, 0.05*Le, 0.1*Le, 0.2*Le, 0.24*Le]

    write_x_Ux(cls=wb,numArt=0,lX=lX,Time=lTime[0])


if __name__ == "__main__":
   main(sys.argv[1:])
