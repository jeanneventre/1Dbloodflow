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

    L =  [  4.0,  2.0,  3.4,  3.4,  17.7, 14.8, 42.2, 23.5, 6.7,  7.9,
            17.1, 17.6, 17.7, 3.9,  20.8, 17.6, 17.7, 5.2,  3.4,  14.8,
            42.2, 23.5, 6.7,  7.9,  17.1, 8.0,  10.4, 5.3,  2.0,  1.0,
            6.6,  7.1,  6.3,  5.9,  1.0,  3.2,  1.0,  3.2,  10.6, 5.0,
            1.0,  5.9,  5.8,  14.4, 5.0,  44.3, 12.6, 32.1, 34.3, 14.5,
            5.0,  44.4, 12.7, 32.2, 34.4 ]

    for iArt in [6,7,8,35,36,37,38,44,50] :

        lX = [ 0., L[iArt]/2., L[iArt]]

        for pType in ["Q","P"] :
            write_Opt_t(cls=wb,numArt=int(iArt),lX=lX,pType=pType)

        lXmid = [L[iArt]/2.]

        write_Opt_t_All(cls=wb,numArt=int(iArt),lX=lXmid)

if __name__ == "__main__":
   main(sys.argv[1:])
