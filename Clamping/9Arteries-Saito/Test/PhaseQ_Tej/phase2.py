import sys, getopt
import os
import numpy    as np
import math     as mt
import scipy    as sp

from bfS_libDef import *
from help_Input     import *
from help_Sum       import *
import  help_Output as out
import csv

from sklearn import metrics
import pathlib
import matplotlib.pyplot as plt


def main(argv) :

	# -----------------------------------------------------
    # ---- PATH 
    hd = header()
    hd.headerInput(argv) ; 

    HOME    = "/home/ventre/"
    PATH1D  = "Documents/Boulot/Thèse/code/bloodflow/bloodflow/Examples/Clamping/9Arteries-Saito/"
    PATHs   = "Documents/Boulot/Thèse/code/bloodflow/bloodflow/scripts/Clamping/9Arteries-Saito/"
    # # MAC 
    # HOME    = "/Users/jeanneventre/"
    # PATH1D  = "Documents/Boulot/Thèse/code/bloodflow/Examples/Clamping/9Arteries-Saito/"
    # PATHs   = "Documents/Boulot/Thèse/code/bloodflow/scripts/Clamping/9Arteries-Saito/"

    Nx       = hd.Nxstr

    xOrder   = hd.xOrderstr

    dt       = hd.dtstr
    tOrder   = hd.tOrderstr

    NN       = hd.NNstr

    HR       = "HRQ"
    Solver   = "KIN_HAT"

    Conj     = "jS"

    nuv      = hd.Cvstr
    Rt       = hd.Rtstr
    C        = hd.Cstr
    Q        = hd.Qstr
    P1       = hd.P1
    Rt2      = hd.P2   

    State = "Test/PhaseQ_Tej"

    PATH = HOME + PATH1D + State + "/" + NN + "/" + Conj + "/nuv=" + nuv +  "/Q=" + Q + "/P1=" + P1 + "/R2=" + Rt2 + "/C=" + C + "/Nx=" + Nx + "/xOrder=" + xOrder + "/dt=" + dt + "/tOrder=" + tOrder + "/" + Solver + "/" + HR + "/"

    os.chdir(HOME)
    integ = PATHs + State
    os.chdir(integ)
    fileName = 'mat.csv' 

    fh = open(fileName, 'a')
    fh.write("\n")
   
if __name__ == "__main__":
	main(sys.argv[1:])
