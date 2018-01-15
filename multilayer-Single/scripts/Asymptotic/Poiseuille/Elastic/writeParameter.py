#! /usr/bin/python2.7
import sys, getopt
import os
import numpy as np
import math as mt
from multiS_libDef import *

def Rx(nu,Rs,K,Q,x) :
    return ( (Rs**5.) -40. * nu * Q / (np.pi*K) * x )**(1./5.)

def main(argv) :
    PATH = "" ; logo = "" ;
    Solver = '' ; HR = '' ; Cells = '' ; Order = '' ;
    Layer = "" ; Raf = '' ;
    Kstr = "" ;

    Shstr = "" ; Lstr = ""

    # COMMAND LINE ARGUMENTS
    #############################
    try :
        opts, args = getopt.getopt(argv,"hp:l:s:y:c:r:j:o:k:f:d:",["path=","logo=","Solver","HR","Layer=","Raffinement=","Cells=","Order=","K=","Sh=","Length="])
    except getopt.GetoptError:
          print ('writeParameter-55.py -p <PATH> -l <logo> -s <Solver> -y <HR> -c <Layer> -r <Raf> -j <Cells> -o <Order> -k <K> -f <Sh> -d <Length>')
          sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print ('writeParameter-55.py -p <PATH> -l <logo> -s <Solver> -y <HR> -c <Layer> -r <Raf> -j <Cells> -o <Order> -k <K> -f <Sh> -d <Length>')
            sys.exit()
        if opt in ("-p", "--PATH"):
            PATH = arg
        if opt in ("-l", "--logo"):
            logo = arg

        if opt in ("-j", "--Cells"):
            Cells = arg
        if opt in ("-o", "--Order"):
            Order = arg
        if opt in ("-s", "--Sol"):
            Solver = arg
        if opt in ("-y", "--HR"):
            HR = arg
        if opt in ("-c", "--Layer"):
            Layer = arg
        if opt in ("-r", "--Raf"):
            Raf = arg

        if opt in ("-k", "--K"):
            Kstr = arg
        if opt in ("-f", "--Sh"):
            Shstr = arg
        if opt in ("-d", "--Length"):
            Lstr = arg

    if (PATH == "" ) :
        print("Empty PATH -----> EXIT")
        sys.exit()
    if (Solver == "" ) :
        print("Empty Solver -----> EXIT")
        sys.exit()
    if (HR == '' ) :
        print("Empty HR -----> EXIT")
        sys.exit()
    if (Cells == '' ) :
        print("Empty Cells -----> EXIT")
        sys.exit()
    if (Order == '' ) :
        print("Empty Order -----> EXIT")
        sys.exit()
    if (Layer == '' ) :
        print("Empty Layer -----> EXIT")
        sys.exit()
    if (Raf == '' ) :
        print("Empty Raf -----> EXIT")
        sys.exit()
    if (Kstr == '' ) :
        print("Empty Kstr -----> EXIT")
        sys.exit()
    if (Shstr == '' ) :
        print("Empty Shstr -----> EXIT")
        sys.exit()
    if (Lstr == '' ) :
        print("Empty Length -----> EXIT")
        sys.exit()

    print("---------------------")
    print("UNITS : cm, g, s")
    print("---------------------")
    print

    Sh_c    = double(Shstr)
    K_c     = double(Kstr)
    L_c     = double(Lstr)
    R0_c    = 1.
    rho_c   = 1.
    mu_c    = 1.

    Rs_c    = R0_c * (1. + Sh_c)
    Re_c    = R0_c * (1. - Sh_c)

    ps_c    = K_c * (Rs_c - R0_c)
    pe_c    = K_c * (Re_c - R0_c)

    Q_c     = np.pi * K_c / (40.*mu_c/rho_c*L_c) * ((Rs_c**5.)-(Re_c**5.))

    te_c    = 20.

    print("Sh=",Sh_c)
    print("Rs=",Rs_c)
    print("Re=",Re_c)
    print("ps=",ps_c)
    print("pe=",pe_c)
    print("Q=",Q_c)

    ###################################
    # NETWORK
    #############################
    N_art_tot = 1

    # LAYERS
    #############################
    layer = [int(Layer)]

    #############################
    # GEOMETRICAL PARAMETERS

    # Length of the vessels (cm)
    L = array( [ L_c ] )
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
        print ('Dimension error in geometric parameters A or L')
        sys.exit()

    #####################
    # MECHANICAL PARAMETERS

    # Density (g/cm^3)
    rho = rho_c # rho of water
    # Viscosity (g/cm/s ~ Pa.s = 10 * g/cm/s)
    mu  = mu_c # Dynamic viscosity (g/cm/s)
    nu  = mu/rho                 # (cm^2/s) Cinematic viscosity : Water at 25 C = 0,887012e-6

    # Stiffness coefficient beta (g/cm^2/s^2 ~ Pa/m = 0.1 g/(cm*s)^2)
    K = ones(NbrArt) * K_c / np.sqrt(np.pi)

    # Viscoelasticity coefficient C_v (cm^2/s)
    Cv = zeros(NbrArt)

    # Moens-Korteweg celerity (cm/s)
    c = sqrt( 0.5 * K / rho * sqrt(A))

    # Check length of array
    if len(L) != len(K) or len(L) != len(c):
        print ('Dimension error in geometric parameters K or c')
        sys.exit()

    ######################
    # NUMBER OF MESH POINTS

    N =  array( [  float(Cells) ] )
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

    ###################
    # ARTERY

    arts = [artery(i) for i in range(NbrArt)]

    # Define the properties of each artery

    for i in range(NbrArt):

        arts[i].solver      =str(Solver)
        arts[i].solverOrder =int(Order)
        arts[i].HR          =str(HR)
        arts[i].N           =int(N[i])

        arts[i].nLayer      = layer[i]
        arts[i].layProp     = layer_Refinement(int(Raf),nLayer=int(layer[i]))

        arts[i].rho         = rho
        arts[i].mu          = mu
        arts[i].L           = L[i]
        arts[i].Profile     = str("Poiseuille")

        #Create the mesh
        arts[i].dx          = mesh(arts[i].L,arts[i].N)
        arts[i].x           = space(arts[i].dx)
        arts[i].R           = R[i] * shape_R(arts[i].x)
        arts[i].K           = K[i] * shape_K(arts[i].x)
        arts[i].Cv          = Cv[i]* shape_Cv(arts[i].x)

        #Initial condition
        arts[i].InitProfile = str("Poiseuille")
        arts[i].initA       = np.pi * Rx(nu,Rs_c,K_c,Q_c,arts[i].x)* Rx(nu,Rs_c,K_c,Q_c,arts[i].x)
        arts[i].initQ       = Q_c * np.ones(arts[i].N)

        #Output points
        arts[i].outPut=[0]	# Mesh points for which data will be stored
        num_measpt = int(arts[i].N)
        L_measpt=[float(n)*L[i]/float(num_measpt-1) for n in range(1,num_measpt-1)] # (m)
        for k in range(len(L_measpt)) :
            arts[i].outPut.append(int(L_measpt[k]/arts[i].dx[0]))
        arts[i].outPut.append( arts[i].N-1 )

    #####################
    # Time setup

    t_start = 0.99*te_c # (s)
    t_end   = 1.0*te_c # (s)

    # CFL
    Ct      = 1.
    dt_CFL  = Ct * min(dx/(Q_c/Rs_c+c))

    # Time step
    power   = float(floor(mt.log10(dt_CFL)))
    fact    = floor(dt_CFL / (10. ** power))
    dt      = min(float(fact) * 10. ** (power),1.e-4)
    # Store step
    dt_store    = 1.e-2 * (t_end-t_start)
    storeStep   = max(1,int(dt_store / dt))

    print ("---->Time step dt = ", dt)
    print ("---->CFL Time step dt_CFL = ",dt_CFL)

    timeSteps = int(t_end/dt)
    tt = ones(timeSteps)
    for it in range(timeSteps) :
        tt[it] = float(it) * dt

    tS              = timeSetup()
    tS.tt           = tt
    tS.dt           = dt
    tS.t_start      = t_start
    tS.t_end        = t_end
    tS.Nt           = timeSteps
    tS.storeStep    = storeStep
    tS.CFL          = Ct
    tS.timeOrder    = 3

    ###################
    # Boundary condition

    #Boundary conditions for Poiseuille solution
    p_Input     = ones(timeSteps) * ps_c
    p_Output    = ones(timeSteps) * pe_c

    Q_Input     = Q_c * ones(timeSteps)

    Rt_Output   = np.zeros(timeSteps)

    ###################
    # daugher arteries, headPt and tailPt  :
    arts[0].daughterArts = [] ;

    arts[0].headPt.append(point(0))     ;
    arts[0].tailPt.append(point(1))     ;
    arts[0].headPt[0].type = "inP"      ; arts[0].headPt[0].data = p_Input ;
    arts[0].tailPt[0].type = "outP"     ; arts[0].tailPt[0].data = p_Output ;

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
