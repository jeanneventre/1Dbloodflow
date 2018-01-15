#! /usr/bin/python3
#units  cm kg s (pas for E, beta pas/cm, beta kg/(s*cm^2) )
import sys, getopt
import os

import numpy as np
import math as mt
from multiS_libDef import *

def main(argv) :

    PATH = "" ; logo = "" ;
    Solver = "" ; HR = "" ;

    Nrstr = "" ; Rafstr = "" ;
    Nxstr = "" ; xOrderstr = "" ;

    dtstr = "" ; tOrderstr = "" ;

    Kstr    = "" ;
    Knlstr  = "" ;

    dRstr   = "" ;

    # COMMAND LINE ARGUMENTS
    #############################
    try :
        opts, args = getopt.getopt(argv,"hp:l:s:y:c:r:j:o:k:i:d:",["path=","logo=","Solver","HR","Nr=","Raf=","Nx=","xOrder=","K=","Knl=","dR="])
    except getopt.GetoptError:
          print ('writeParameter-55.py -p <PATH> -l <logo> -s <Solver> -y <HR> -c <Nr> -r <Raf> -j <Nx> -o <xOrder> -k <K> -i <Knl> -d <dR>')
          sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print ('writeParameter-55.py -p <PATH> -l <logo> -s <Solver> -y <HR> -c <Nr> -r <Raf> -j <Nx> -o <xOrder> -k <K> -i <Knl> -d <dR>')
            sys.exit()
        if opt in ("-p", "--PATH"):
            PATH = arg
        if opt in ("-l", "--logo"):
            logo = arg

        if opt in ("-s", "--Sol"):
            Solver = arg
        if opt in ("-y", "--HR"):
            HR = arg

        if opt in ("-c", "--Nr"):
            Nrstr = arg
        if opt in ("-r", "--Raf"):
            Rafstr = arg
        if opt in ("-j", "--Nx"):
            Nxstr = arg
        if opt in ("-o", "--xOrder"):
            xOrderstr = arg

        if opt in ("-k", "--K"):
            Kstr = arg
        if opt in ("-i", "--Knl"):
            Knlstr = arg

        if opt in ("-d", "--dR"):
            dRstr = arg

    if (PATH == "" ) :
        print("Empty PATH -----> EXIT")
        sys.exit()
    if (Solver == "" ) :
        print("Empty Solver -----> EXIT")
        sys.exit()
    if (HR == '' ) :
        print("Empty HR -----> EXIT")
        sys.exit()

    if (Nrstr == '' ) :
        print("Empty Nr -----> EXIT")
        sys.exit()
    if (Rafstr == '' ) :
        print("Empty Raf -----> EXIT")
        sys.exit()
    if (Nxstr == '' ) :
        print("Empty Nx -----> EXIT")
        sys.exit()
    if (xOrderstr == '' ) :
        print("Empty xOrder -----> EXIT")
        sys.exit()

    if (Kstr == '' ) :
        print("Empty Kstr -----> EXIT")
        sys.exit()
    if (Knlstr == '' ) :
        print("Empty Knlstr -----> EXIT")
        sys.exit()

    if (dRstr == '' ) :
        print("Empty dRstr -----> EXIT")
        sys.exit()

    print("---------------------")
    print("UNITS : cm, g, s")
    print("---------------------")
    print

    # Properties of water
    rho_c   = 1.

    mu_c    = 0.

    # Geometrical measured data
    R0_c    = 1.
    L_c     = 40.

    # Optimization data
    K_c     = double(Kstr)
    Knl_c   = double(Knlstr)
    Cv_c    = 0.

    # Pump model
    dR_c    = float(dRstr)
    T_c     = 0.4   # (s)
    P_c     = K_c * np.sqrt(np.pi) * dR_c   # (cm^3) Ejection volume of the pump

    # Simulation time
    te_c    = 0.6

    Nr_c        = float(Nrstr)
    Raf_c       = float(Rafstr)
    Nx_c        = float(Nxstr)
    xOrder_c    = int(xOrderstr)

    # NETWORK
    #############################
    N_art_tot = 1

    # LAYERS
    #############################
    layer = [int(Nr_c)]

    #############################
    # GEOMETRICAL PARAMETERS

    # Length of the vessels (cm)
    L =     array( [  L_c ] )

    # Radius of the artery (cm)
    R = array( [ R0_c ] )
    D = R * 2.
    A = pi * R **2.

    NbrArt=len(L)

    # Check for number of arteries :
    if NbrArt != N_art_tot :
        print ( "Wrong number of arteries" )
        sys.exit()

    # Check length of array
    if len(L) != len(A) :
        print ('Dimension error in geometric parameters A_ref or L')
        sys.exit()

    #####################
    # MECHANICAL PARAMETERS

    # Density (g/cm^3)
    rho = rho_c # rho of water

    # Viscosity (g/cm/s ~ Pa.s = 10 * g/cm/s)
    mu  = mu_c   # Dynamic viscosity (g/cm/s)
    nu  = mu/rho # (cm^2/s) Cinematic viscosity : Water at 25 C = 0,887012e-6

    # Stiffness coefficient beta (g/cm^2/s^2 ~ Pa/m = 0.1 g/(cm*s)^2)
    K =     ones(NbrArt) * K_c

    # Viscoelasticity coefficient C_v (cm^2/s)
    Cv =    ones(NbrArt) * Cv_c

    # Nonlinear stiffness coefficient beta (g/cm^3/s^2)
    Knl =   ones(NbrArt) * Knl_c

    # Moens-Korteweg celerity (cm/s)
    c = sqrt( 0.5* K / rho * sqrt(A)  )

        # Check length of array
    if len(L) != len(K) or len(L) != len(c):# or len(L) != len(C_v):
        print ('Dimension error in geometric parameters h, A_ref or L')
        sys.exit()

    ######################
    # NUMBER OF MESH POINTS

    N =  array( [ Nx_c ] )
    dx = L / N
    dx_min = min(dx)

    ###################
    # SHAPES (Well-balance)
    def mesh(L,N) :
        dx = float(L/N)
        shape = dx * ones(int(N))
        return shape ;

    def space(dx) :
        N = len(dx) ;
        shape = zeros(N) ;
        shape[0] = dx[0]/2.
        for i in range(1,N) :
            shape[i] = shape[i-1] + (dx[i-1]+dx[i])/2.
        return shape

    def shape_h(x) :
        N = len(x)
        shape = ones(N)
        return shape ;

    def shape_R(x) :
        N = len(x)
        shape = ones(N)
        return shape ;

    def shape_K(x) :
        N = len(x)
        shape = ones(N)
        return shape ;

    def shape_Cv(x) :
        N = len(x)
        shape = ones(N)
        return shape ;

    def shape_Knl(x) :
        N = len(x)
        shape = ones(N)
        return shape ;

    ###################
    # ARTERY

    arts = [artery(i) for i in range(NbrArt)]

    # Define the properties of each artery

    for i in range(NbrArt):

        arts[i].solver      =str(Solver)
        arts[i].HR          =str(HR)
        arts[i].solverOrder =int(xOrder_c)
        arts[i].N           =int(N[i])

        arts[i].nLayer      = layer[i]
        arts[i].layProp     = layer_Raffinement(levelRaf=int(Raf_c),posRaf=0.6,nLayer=int(layer[i]))

        arts[i].rho         = rho
        arts[i].mu          = mu
        arts[i].L           = L[i]
        arts[i].Profile     = str("Polhausen")

        #Create the mesh
        arts[i].dx      = mesh(arts[i].L,arts[i].N)
        arts[i].x       = space(arts[i].dx)
        arts[i].R       = R[i]  * shape_R(arts[i].x)
        arts[i].K       = K[i]  * shape_K(arts[i].x)
        arts[i].Cv      = Cv[i] * shape_Cv(arts[i].x)
        arts[i].Knl     = Knl[i]* shape_Knl(arts[i].x)

        #Initial condition
        arts[i].InitProfile = str("Polhausen")
        arts[i].initA       = pi * arts[i].R * arts[i].R
        arts[i].initQ       = zeros(arts[i].N)

        #Output points
        arts[i].outPut=[0]	# Mesh points for which data will be stored

        num_measpt = int(arts[i].N)
        L_measpt=[float(n)*L[i]/float(num_measpt-1) for n in range(1,num_measpt-1)] # (m)
        for k in range(len(L_measpt)) :
            arts[i].outPut.append(int(L_measpt[k]/dx[i]))

        arts[i].outPut.append( arts[i].N-1 )

        #Output Profile points
        arts[i].outPutProfile=[0]	# Mesh points for which data will be stored
        arts[i].outPutProfile.append( arts[i].N-1 )

    #####################
    # Time setup

    t_start = 0. # (s)
    t_end = te_c # (s)

    # CFL
    Ct = 0.2
    dt_CFL = Ct * min(dx/c)

    # Time step
    power = float(floor(mt.log10(dt_CFL)))
    fact = floor(dt_CFL / (10. ** power))
    dt = min(float(fact) * 10. ** (power),1.e-4)

    # Store step
    dt_store = 1.e-3
    storeStep = max(1,int(dt_store / dt))

    # Store Profile
    dt_storeProfile     = 1.e-1
    storeStepProfile    = max(1,int(dt_storeProfile / dt))

    print ("---->Time step dt = ", dt)
    print ("---->CFL Time step dt_CFL = ",dt_CFL)

    timeSteps = int(t_end/dt)
    tt = ones(timeSteps)
    for it in range(timeSteps) :
        tt[it] = float(it) * dt

    tS                      = timeSetup()
    tS.tt                   = tt
    tS.dt                   = dt
    tS.t_start              = t_start
    tS.t_end                = t_end
    tS.Nt                   = timeSteps
    tS.storeStep            = storeStep
    tS.storeStepProfile     = storeStepProfile
    tS.CFL                  = Ct
    tS.timeOrder            = 3

    ###################
    # Boundary condition

    #Inlet
    pulse_Input             = maximum( sin(2.*pi/T_c*tt), 0) ;
    pulse_Input[(tt > T_c)] = 0. ;

    P_Input     = P_c * pulse_Input

    #Oulet
    Rt_Output   = np.zeros(timeSteps);

    ###################
    # daugher arteries, headPt and tailPt  :
    arts[0].daughterArts = [] ;

    arts[0].headPt.append(point(0))  ;
    arts[0].headPt[0].type  = "inP"             ; arts[0].headPt[0].data    = P_Input ;

    arts[0].tailPt.append(point(1))  ;
    arts[0].tailPt[0].type  = "outRt"           ; arts[0].tailPt[0].data    = Rt_Output;

    ####################
    # Network definition :
    net=network(ARTS=arts,tS=tS)

    #####################
    # CREATE NECESSARY FILES
    if not os.path.exists(str(PATH)+"parameters_"+str(logo)) :
        os.makedirs(str(PATH)+"/parameters_"+str(logo))
    if not os.path.exists(str(PATH)+"parameters_"+str(logo)+"/Parameters") :
        os.makedirs(str(PATH)+"/parameters_"+str(logo)+"/Parameters")
    if not os.path.exists(str(PATH)+"/data"):
        os.makedirs(str(PATH)+"/data")
    if not os.path.exists(str(PATH)+"/Figures"):
        os.makedirs(str(PATH)+"/Figures")
    if not os.path.exists(str(PATH)+"/Movies"):
        os.makedirs(str(PATH)+"/Movies")

    #####################
    # WRITE PARAMETERS
    net.writeParam(str(PATH)+"parameters_"+str(logo))

if __name__ == "__main__":
   main(sys.argv[1:])
