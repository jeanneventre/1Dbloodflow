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

    # PLOTING :
    ###########
    nfig = 1
    iArt = 0

    T_c = 0.1

    L = 10.
    lX = [ 0., L]
    lTime = [
            0.5 *T_c, 0.75 *T_c, 0.8 *T_c, 0.9 *T_c, 1. * T_c,
            1.1 * T_c , 1.2 * T_c, 1.5 * T_c, 1.8 * T_c
            ]

    for pType in ["Q", "P", "RmR0"] :

        write_x(cls=wb,numArt=0,lTime=lTime,pType=pType)
        write_t_All(cls=wb,numArt=int(iArt),lX=lX)


if __name__ == "__main__":
   main(sys.argv[1:])
