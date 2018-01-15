#!/usr/bin/python3
import sys, getopt
from multiS_libData import *
from multiS_libMovie import *

import numpy as np

def main(argv) :
    PATH = "";
    Restr = "" ;
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

    nfig = 1

    # MOVIING
    #########

    numArt      = 0

    nArrowX     = 20
    nArrowY     = 100
    scArrow     = 1

    nStore      = 60

    Umid        = 0
    Colormap    = "BlueRed"

    TextPos     = [0.5,1.05]
    TextAlign   = "center"
    TextColor   = "black"

    speedUp     = 1
    slowDownfps = 10

    nfig = animate_x(   cls=wb,numArt=numArt,pType='Tw',
                        TextPos=TextPos,TextAlign=TextAlign,TextColor=TextColor,
                        speedUp=speedUp,slowDownfps=slowDownfps,
                        nf=nfig)

    nfig = animate_Arrow_UUr(   cls=wb,numArt=numArt,
                                nArrowX=nArrowX,nArrowY=nArrowY,scArrow=scArrow,
                                nStore=nStore,
                                Umid=Umid,Colormap=Colormap,
                                TextPos=TextPos,TextAlign=TextAlign,TextColor=TextColor,
                                speedUp=speedUp,slowDownfps=slowDownfps,
                                nf=nfig)

if __name__ == "__main__":
   main(sys.argv[1:])
