#! /usr/bin/python2.7
import sys, getopt
import os
import numpy as np
import math as mt
from multiS_libDef import *

def main(argv) :
    PATH = "" ; logo = "" ;
    Solver = '' ; HR = '' ; Cells = '' ; Order = '' ;
    Layer = "" ; Raf = '' ;
    Kstr = "" ;

    dRstr = "" ; Womstr = "" ;

    # COMMAND LINE ARGUMENTS
    #############################
    try :
        opts, args = getopt.getopt(argv,"hp:l:s:y:c:r:j:o:k:d:w:",["path=","logo=","Solver","HR","Layer=","Raffinement=","Cells=","Order=","K=","dR=","Wom="])
    except getopt.GetoptError:
          print ('writeParameter-55.py -p <PATH> -l <logo> -s <Solver> -y <HR> -c <Layer> -r <Raf> -j <Cells> -o <Order> -k <K> -d <dR> -w <Wom>')
          sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print ('writeParameter-55.py -p <PATH> -l <logo> -s <Solver> -y <HR> -c <Layer> -r <Raf> -j <Cells> -o <Order> -k <K> -d <dR> -w <Wom>')
            sys.exit()
        if opt in ("-p", "--PATH"):
            PATH = arg
        if opt in ("-l", "--logo"):
            logo = arg

        if opt in ("-s", "--Sol"):
            Solver = arg
        if opt in ("-y", "--HR"):
            HR = arg
        if opt in ("-j", "--Cells"):
            Cells = arg
        if opt in ("-o", "--Order"):
            Order = arg
        if opt in ("-c", "--Layer"):
            Layer = arg
        if opt in ("-r", "--Raf"):
            Raf = arg

        if opt in ("-k", "--K"):
            Kstr = arg
        if opt in ("-d", "--dR"):
            dRstr = arg
        if opt in ("-w", "--Wom"):
            Womstr = arg

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
    if (dRstr == '' ) :
        print("Empty dRstr -----> EXIT")
        sys.exit()
    if (Womstr == '' ) :
        print("Empty Womstr -----> EXIT")
        sys.exit()

    print("---------------------")
    print("UNITS : cm, g, s")
    print("---------------------")
    print

    # Womersley
    #############################
    wom_c   = float(Womstr) ;
    T_c     = 0.5 ;
    R_c     = 1.
    nu_c    = 2. * pi / T_c / (wom_c/R_c)**2. # (cm^2/s)


    # NETWORK
    #############################
    N_art_tot = 1

    # LAYERS
    #############################
    layer = [int(Layer)]

    #####################
    # GEOMETRICAL PARAMETERS

    # Diameter of the artery (cm)
    R = array( [ R_c ] )
    D = R * 2.
    A = pi * R **2.
    # Length of the vessels (cm)
    L = array( [  200. ] )

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
    rho = 1.0 # rho of water

    # Viscosity (g/cm/s ~ Pa.s = 10 * g/cm/s)
    nu = nu_c # (cm^2/s) Cinematic viscosity : Water at 25 C = 0,887012e-6
    mu = nu * rho	# Dynamic viscosity (4 mPa.s ~ 4.e-2 g/cm/s)

    # Stiffness coefficient beta (g/cm^2/s^2 ~ Pa/m = 0.1 g/(cm*s)^2)
    K = ones(NbrArt) * float(Kstr)

    # Viscoelasticity coefficient C_v (cm^2/s)
    Cv = zeros(NbrArt)

    # Moens-Korteweg celerity (cm/s)
    c = sqrt(0.5 * K / rho * sqrt(A))

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

        arts[i].nLayer = layer[i]
        arts[i].layProp = layer_Refinement(int(Raf),nLayer=int(layer[i]))

        arts[i].rho     = rho
        arts[i].mu      = mu
        arts[i].L       = L[i]
        arts[i].Profile = str("Polhausen")

        #Create the mesh
        arts[i].dx      = mesh(arts[i].L,arts[i].N)
        arts[i].x       = space(arts[i].dx)
        arts[i].R       = R[i] * shape_R(arts[i].x)
        arts[i].K       = K[i] * shape_K(arts[i].x)
        arts[i].Cv      = Cv[i]* shape_Cv(arts[i].x)

        #Initial condition
        arts[i].InitProfile = str("Polhausen")
        arts[i].initA = np.pi * arts[i].R * arts[i].R
        arts[i].initQ = np.zeros(arts[i].N)

        #Output points
        arts[i].outPut=[0]	# Mesh points for which data will be stored
        num_measpt = int(arts[i].N)
        L_measpt=[float(n)*L[i]/float(num_measpt-1) for n in range(1,num_measpt-1)] # (m)
        for k in range(len(L_measpt)) :
            arts[i].outPut.append(int(L_measpt[k]/arts[i].dx[0]))
        arts[i].outPut.append( arts[i].N-1 )

    #####################
    # Time setup

    t_start = 11. * T_c # (s)
    t_end   = 12. * T_c # (s)

    # CFL
    Ct      = 0.2
    dt_CFL  = Ct * min(dx/c)

    # Time step
    power   = float(floor(mt.log10(dt_CFL)))
    fact    = floor(dt_CFL / (10. ** power))
    dt      = min(float(fact) * 10. ** (power),1.e-4)
    # Store step
    dt_store    = 1.e-2
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
    tS.timeOrder    = 1

    ###################
    # Boundary condition

    #Boundary conditions for Womersley solution

    dR_c = float(dRstr) ;
    P_c = np.sqrt(np.pi)*K[0]*dR_c

    P_Input = P_c * sin(2.*pi/T_c*tt)
    Rt = zeros(timeSteps);

    ###################
    # daugher arteries, headPt and tailPt  :
    arts[0].daughterArts = [] ;

    arts[0].headPt.append(point(0))     ;
    arts[0].tailPt.append(point(1))     ;
    arts[0].headPt[0].type = "inP"      ; arts[0].headPt[0].data = P_Input ;
    arts[0].tailPt[0].type = "outRt"    ; arts[0].tailPt[0].data = Rt ;

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
