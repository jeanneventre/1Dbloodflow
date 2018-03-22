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

    # L       =    np.array( [ 3.5, 80.0, 2.0, 67.5, 4.0, 71.0, 47.0, 36.5, 36.5 ] )
    L = np.array( [ 20] )
    # iArt = 3

    # lX = [  0., 0.1 * L[iArt], 0.2 * L[iArt], 0.3 * L[iArt], 0.4 * L[iArt], 0.5 * L[iArt],
    #         0.6 * L[iArt], 0.7 * L[iArt], 0.8 * L[iArt], 0.9 * L[iArt]]

    # write_Opt_t(cls=wb,numArt=iArt,lX=lX,pType='Q')
    # write_Opt_t(cls=wb,numArt=iArt,lX=lX,pType='P')
    # write_Opt_t(cls=wb,numArt=iArt,lX=lX,pType='U')
    # write_Opt_t(cls=wb,numArt=iArt,lX=lX,pType='T')

    lTime = [9.8]
    for iArt in [0.] :

        lX = [ 0., L[iArt]/2., L[iArt]]

        for pType in ["Q","P","R"] :
            write_Opt_t(cls=wb,numArt=int(iArt),lX=lX,pType=pType)
            # write_Opt_x(cls=wb,numArt=int(iArt),lTime=lTime,pType=pType)

        # lXmid = [L[iArt]/2.]
        # write_Opt_t_All(cls=wb,numArt=int(iArt),lX=lXmid)

if __name__ == "__main__":
   main(sys.argv[1:])
