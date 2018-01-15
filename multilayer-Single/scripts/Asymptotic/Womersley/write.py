#!/usr/bin/python3
import sys, getopt
from multiS_libData import *
from multiS_libWrite import *

def main(argv) :
    PATH = "" ;
    # COMMAND LINE ARGUMENTS
    #############################
    try :
        opts, args = getopt.getopt(argv,"hp:",["path="])
    except getopt.GetoptError:
          print ('plotWom.py -p <PATH>')
          sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print ('plotWom.py -p <PATH>')
            sys.exit()
        elif opt in ("-p", "--PATH"):
            PATH = arg


	if not os.path.exists(str(PATH)+"Figures"):
		os.makedirs(str(PATH)+"Figures")
	folderPath_store = str(PATH) + "Figures/"

    print("Path to file :",str(PATH))

    folderPath_Ref = str(PATH)

    # DATA CLASS :
    ##############
    ref = dataS(folderPath_Ref,folderPath_store,logo="Sane")

    # PLOTING :
    ###########
    nfig = 1

    T = 0.5

    t = 11. * T + 0.3

    write_x_R0_A0_K_R_RmR0_A_Q_U_U0_P_gradP_E_Tw_Cf_a(cls=ref,numArt=0,lTime=[t])

    # lX = [0]
    # write_t_R0_A0_K_R_RmR0_A_Q_U_U0_P_gradP_E_Tw_Cf(cls=ref,numArt=0,lX=lX)
    #
    # tp = 11. * T ;
    # lTime = [tp + 0.2*T, tp + 0.4*T, tp + 0.5*T, tp + 0.7*T]
    # xPos = 25
    #
    # write_t_Ux(cls=ref,numArt=0,xPos=xPos,lTime=lTime)

    L_c = 200.
    lX = [  0,  0.1*L_c, 0.2*L_c, 0.3*L_c, 0.4*L_c, 0.5*L_c,
            0.6*L_c, 0.7*L_c, 0.8*L_c, 0.9*L_c, 0.99*L_c]

    write_x_Ux(cls=ref,numArt=0,lX=lX,Time=[t])

if __name__ == "__main__":
   main(sys.argv[1:])
