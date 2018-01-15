#!/usr/bin/python3
import sys, getopt
from multiS_libData import *
from multiS_libWrite import *

def main(argv) :
    PATH = ""
    # COMMAND LINE ARGUMENTS
    #############################
    try :
        opts, args = getopt.getopt(argv,"hp:",["path="])
    except getopt.GetoptError:
          print ('plot.py -p <PATH> ')
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

    # PLOTING :
    ###########
    nfig = 1

    Le = 10.
    te = 20.

    lTime = [0.99 * te]

    write_x_R0_A0_K_R_RmR0_A_Q_U_U0_P_gradP_E_Tw_Cf_a(cls=wb,numArt=0,lTime=lTime)

    lX = [0, 0.1*Le, 0.2*Le, 0.3*Le, 0.4*Le, 0.5*Le,
          0.6*Le, 0.7*Le, 0.8*Le, 0.9*Le, 0.99*Le]

    write_x_Ux(cls=wb,numArt=0,lX=lX,Time=lTime[0])


if __name__ == "__main__":
   main(sys.argv[1:])
