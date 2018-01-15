#!/usr/bin/python3
import sys, getopt
from multiS_libData import *
from multiS_libWrite import *

def main(argv) :
    PATH = ""
    Restr = ""
    # COMMAND LINE ARGUMENTS
    #############################
    try :
        opts, args = getopt.getopt(argv,"hp:r:",["path=","Re="])
    except getopt.GetoptError:
          print ('plot.py -p <PATH>')
          sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print ('plot.py -p <PATH>')
            sys.exit()
        elif opt in ("-p", "--PATH"):
            PATH = arg
        elif opt in ("-r", "--Re"):
            Restr = arg

	if not os.path.exists(str(PATH)+"Figures"):
		os.makedirs(str(PATH)+"Figures")
	folderPath_store = str(PATH) + "Figures/"

    folderPath= str(PATH)

    # DATA CLASS :
    ##############

    wb = dataS(folderPath,folderPath_store,logo="Sane")

    # WRITING :
    ###########

    R   = 1.
    L   = 25.
    Re  = float(Restr)
    U   = 100.
    Le  = 100.
    te  = float(Re) * float(R) /float(U)

    lTime = [te * 0.49]
    write_x_All(cls=wb,numArt=0,lTime=lTime)

    # lX = [0.025*Le, 0.05*Le, 0.075*Le, 0.1*Le, 0.125*Le, 0.15*Le, 0.2*Le]

    lX = [  0.*Le, 0.025*Le, 0.05*Le, 0.075*Le, 0.1*Le,
            0.125*Le, 0.15*Le, 0.175*Le, 0.2*Le,
            0.225*Le, 0.249*Le ]

    write_x_Ux(cls=wb,numArt=0,lX=lX,Time=lTime[0])


if __name__ == "__main__":
   main(sys.argv[1:])
