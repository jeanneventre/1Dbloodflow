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

    # WRITTING :
    ###########

    X = 235.; lR = [-0.3,-0.2,-0.1,0,0.1,0.2,0.3]
    write_t_r_Ux(cls=wb,Utype="UxUr",numArt=0,X=X,lR=lR)

    lX = [0., 28., 235., 252.]
    for pType in ["P","Q","U","U0","alpha","phi"] :
        write_t(cls=wb,numArt=0,lX=lX,pType=pType)

    lTime = [0.3, 0.6, 0.9]
    write_t_Ux(cls=wb,numArt=0,xPos=X,lTime=lTime)

if __name__ == "__main__":
   main(sys.argv[1:])
