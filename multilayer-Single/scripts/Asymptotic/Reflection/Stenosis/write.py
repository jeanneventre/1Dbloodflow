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

    T_c = 0.1
    lTime = [0.55*T_c,1.05*T_c,1.1*T_c]

    write_x(cls=wb,numArt=0,lTime=lTime,pType='Q')
    write_x(cls=wb,numArt=0,lTime=lTime,pType='A')
    write_x(cls=wb,numArt=0,lTime=lTime,pType='U')
    write_x(cls=wb,numArt=0,lTime=lTime,pType='P')
    write_x(cls=wb,numArt=0,lTime=lTime,pType='RmR0')
    write_x(cls=wb,numArt=0,lTime=lTime,pType='Tw')

if __name__ == "__main__":
   main(sys.argv[1:])
