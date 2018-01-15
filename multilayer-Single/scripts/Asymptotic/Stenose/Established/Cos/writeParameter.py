#! /usr/bin/python3
#units  cm kg s (pas for E, beta pas/cm, beta kg/(s*cm^2) )
import sys, getopt
import os
from numpy import *
import math as mt

from multiS_libDef import *

def main(argv) :

    PATH = "" ; logo = "" ;
    Solver = '' ; HR = '' ; Cells = '' ; Order = '' ;
    Layer = "" ; Raf = '' ;
    Kstr = "" ;

    Ustr = "" ; Restr = "" ; Length = ""
    dRstr = "" ; Lstr = ""

    # COMMAND LINE ARGUMENTS
    #############################
    try :
        opts, args = getopt.getopt(argv,"hp:l:s:y:c:r:j:o:k:u:e:d:t:w:",["path=","logo=","Solver","HR","Layer=","Raffinement=","Cells=","Order=","K=","U=","Re=","Length=","Rst=","Lst=","verbose="])
    except getopt.GetoptError:
          print ('writeParameter-55.py -p <PATH> -l <logo> -s <Solver> -y <HR> -c <Layer> -r <Raf> -j <Cells> -o <Order> -k <K> -u <U> -e <Re> -d <Length> -t <Rst> -w <Lst> -v <verbose>')
          sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print ('writeParameter-55.py -p <PATH> -l <logo> -s <Solver> -y <HR> -c <Layer> -r <Raf> -j <Cells> -o <Order> -k <K> -u <U> -e <Re> -d <Length> -t <Rst> -w <Lst> -v <verbose>')
            sys.exit()
        if opt in ("-p", "--PATH"):
            PATH = arg
        if opt in ("-l", "--logo"):
            logo = arg
        if opt in ("-s", "--Sol"):
            Solver = arg
        if opt in ("-y", "--HR"):
            HR = arg
        if opt in ("-c", "--Layer"):
            Layer = arg
        if opt in ("-r", "--Raf"):
            Raf = arg
        if opt in ("-j", "--Cells"):
            Cells = arg
        if opt in ("-o", "--Order"):
            Order = arg
        if opt in ("-k", "--K"):
            Kstr = arg
        if opt in ("-u", "--U"):
            Ustr = arg
        if opt in ("-e", "--Re"):
            Restr = arg
        if opt in ("-d", "--Length"):
            Length = arg
        if opt in ("-t", "--Rst"):
            dRstr = arg
        if opt in ("-w", "--Lst"):
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
    if (Ustr == '' ) :
        print("Empty Ustr -----> EXIT")
        sys.exit()
    if (Restr == '' ) :
        print("Empty Restr -----> EXIT")
        sys.exit()
    if (Length == '' ) :
        print("Empty Length -----> EXIT")
        sys.exit()
    if (dRstr == '' ) :
        print("Empty dRstr -----> EXIT")
        sys.exit()
    if (Lstr == '' ) :
        print("Empty Lstr -----> EXIT")
        sys.exit()

    print("---------------------")
    print("UNITS : cm, g, s")
    print("---------------------")
    print

    Re_c = double(Restr)
    K_c = double(Kstr)
    U_c = double(Ustr)
    R_c = 1.
    dR_c = double(dRstr)
    L_c = double(Lstr)
    te_c =  Re_c * R_c / U_c

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
    L = array( [ float(Length) ] )
    # Radius of the artery (cm)
    R = array( [ float(R_c) ] )
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
    rho = 1. # rho of water
    # Viscosity (g/cm/s ~ Pa.s = 10 * g/cm/s)
    mu = U_c * R_c * rho / Re_c #3.5e-2		# Dynamic viscosity (g/cm/s)
    nu = mu/rho # (cm^2/s) Cinematic viscosity : Water at 25 C = 0,887012e-6

    # Stiffness coefficient beta (g/cm^2/s^2 ~ Pa/m = 0.1 g/(cm*s)^2)
    K = ones(NbrArt) * K_c

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
        #Position the stenosis in the middle of the artery
        LS = 5. ; LE = LS + L_c
        for i in range (N) :
            if (x[i] >= LS and x[i] <= LE ) :
                shape[i] = shape[i] + dR_c * 0.5 *( 1. + cos( pi + 2. * pi * float( x[i]-LS )/float(LE-LS) ) )
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
        arts[i].Profile = str("Poiseuille")

        #Create the mesh
        arts[i].dx      = mesh(arts[i].L,arts[i].N)
        arts[i].x       = space(arts[i].dx)
        arts[i].R       = R[i] * shape_R(arts[i].x)
        arts[i].K       = K[i] * shape_K(arts[i].x)
        arts[i].Cv      = Cv[i]* shape_Cv(arts[i].x)

        #Initial condition
        arts[i].InitProfile = str("Poiseuille")
        arts[i].initA   = pi * arts[i].R * arts[i].R
        arts[i].initQ   = arts[i].initA * U_c

        #Output points
        arts[i].outPut=[0]	# Mesh points for which data will be stored
        num_measpt = int(arts[i].N)
        L_measpt=[float(n)*L[i]/float(num_measpt-1) for n in range(1,num_measpt-1)] # (m)
        for k in range(len(L_measpt)) :
            arts[i].outPut.append(int(L_measpt[k]/arts[i].dx[0]))
        arts[i].outPut.append( arts[i].N-1 )

    #####################
    # Time setup

    t_start = 0.45  * te_c # (s)
    t_end   = 0.5   * te_c # (s)

    # CFL
    Ct      = 1.
    dt_CFL  = Ct * min(dx/(U_c+c))

    # Time step
    power   = float(floor(mt.log10(dt_CFL)))
    fact    = floor(dt_CFL / (10. ** power))
    dt      = min(float(fact) * 10. ** (power),2.e-6)
    # Store step
    dt_store    = 1.e-3 * te_c
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

    #Boundary conditions for Poiseuille solution
    U_Input = ones(timeSteps) * U_c
    Rt = zeros(timeSteps);

    ###################
    # daugher arteries, headPt and tailPt  :
    arts[0].daughterArts = [] ;

    arts[0].headPt.append(point(0))     ;
    arts[0].tailPt.append(point(1))     ;
    arts[0].headPt[0].type = "inU"      ; arts[0].headPt[0].data = U_Input ;
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
