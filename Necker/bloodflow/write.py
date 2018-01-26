#!/usr/bin/python3
import  sys, getopt

from    bfS_libData     import *
from    bfS_libWrite    import *

def main(argv) :
    PATH = "";
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

    wb = dataS_Opt(folderPath,folderPath_store,logo="Sane")

    # PLOTING :
    ###########
    nfig = 1

    L_c = 10.; 

    T_c = 0.98 ; 

    lTime = [1.*T_c,2.*T_c,3.*T_c,4.*T_c ]
    
    lX = [0. , L_c/2., L_c]

    for pType in ["Q", "U", "A", "P", "R"] :
        write_Opt_x(cls=wb,numArt=0,lTime=lTime,pType=pType)
        write_Opt_t(cls=wb,numArt=0,lX=lX,pType=pType)

if __name__ == "__main__":
   main(sys.argv[1:])
