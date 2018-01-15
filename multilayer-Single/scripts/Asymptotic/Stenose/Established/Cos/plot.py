#!/usr/bin/python3
import sys, getopt
from multiWB_libData_Opt import *
from multiWB_libMovie_Opt import *

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

    wb = dataWB_Opt(folderPath,folderPath_store,logo="Sane")

    nfig = 1

    # MOVIING
    #########

    # nfig = animate_Arrow_UUr(cls=wb,numArt=0,nX=20,speedUp=1,nf=nfig)

    nfig = animate_Stream_UUr(cls=wb,numArt=0,nX=100,nY=100,speedUp=1,nf=nfig)

    # nfig = animate_Opt_rsR_Profil(cls=wb,numArt=0,xPos=0.,speedUp=1,nf=nfig)
    # nfig = animate_Opt_rsR_Profil(cls=wb,numArt=0,xPos=2.,speedUp=1,nf=nfig)
    # nfig = animate_Opt_rsR_Profil(cls=wb,numArt=0,xPos=10.,speedUp=1,nf=nfig)
    # nfig = animate_Opt_rsR_Profil(cls=wb,numArt=0,xPos=15.,speedUp=1,nf=nfig)
    # nfig = animate_Opt_rsR_Profil(cls=wb,numArt=0,xPos=18.,speedUp=1,nf=nfig)

    # nfig = animate_Opt_x(cls=wb,numArt=0,pType='Tw',speedUp=1,nf=nfig)
    # nfig = animate_Opt_x(cls=wb,numArt=0,pType='Fr',speedUp=1,nf=nfig)
    # nfig = animate_Opt_x(cls=wb,numArt=0,pType='Q',speedUp=1,nf=nfig)
    # nfig = animate_Opt_x(cls=wb,numArt=0,pType='U0',speedUp=1,nf=nfig)

if __name__ == "__main__":
   main(sys.argv[1:])
