#! /usr/bin/python3
#units  cm kg s (pas for E, beta pas/cm, beta kg/(s*cm^2) )
import sys, getopt
import os
from numpy import *
import math as mt
import matplotlib.pyplot as plt
from multiS_libDef  import *
from help_Raff      import *

def main(argv) :

    PATH = "" ; logo = "" ;
    Solver = '' ; HR = '' ; Cells = '' ; Order = '' ;
    Layer = "" ; Raf = '' ;
    Kstr = "" ;
    Rtstr = "" ;
    Restr = "" ; Womstr = "" ; Shstr = "" ; Length = ""
    dRstr = "" ; Lstr = ""

    # COMMAND LINE ARGUMENTS
    #############################
    try :
        opts, args = getopt.getopt(argv,"hp:l:s:y:c:r:j:o:k:e:a:f:d:t:w:b:",["path=","logo=","Solver","HR","Layer=","Raffinement=","Cells=","Order=","K=","Re=","Wom=","Sh=","Length=","Rst=","Lst=","Rt=","verbose="])
    except getopt.GetoptError:
          print ('writeParameter-55.py -p <PATH> -l <logo> -s <Solver> -y <HR> -c <Layer> -r <Raf> -j <Cells> -o <Order> -k <K> -e <Re> -a <Wom> -f <Sh> -d <Length> -t <Rst> -w <Lst> -b <Rt> -v <verbose>')
          sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print ('writeParameter-55.py -p <PATH> -l <logo> -s <Solver> -y <HR> -c <Layer> -r <Raf> -j <Cells> -o <Order> -k <K> -e <Re> -a <Wom> -f <Sh> -d <Length> -t <Rst> -w <Lst> -b <Rt> -v <verbose>')
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
        if opt in ("-e", "--Re"):
            Restr = arg
        if opt in ("-a", "--Wom"):
            Womstr = arg
        if opt in ("-f", "--Sh"):
            Shstr = arg
        if opt in ("-d", "--Length"):
            Length = arg
        if opt in ("-t", "--Rst"):
            dRstr = arg
        if opt in ("-w", "--Lst"):
            Lstr = arg
        if opt in ("-b", "--Rt"):
            Rtstr = arg

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
    if (Restr == '' ) :
        print("Empty Restr -----> EXIT")
        sys.exit()
    if (Womstr == '' ) :
        print("Empty Womstr -----> EXIT")
        sys.exit()
    if (Shstr == '' ) :
        print("Empty Shstr -----> EXIT")
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
    if (Rtstr == '' ) :
        print("Empty Rtstr -----> EXIT")
        sys.exit()

    print("---------------------")
    print("UNITS : cm, g, s")
    print("---------------------")
    print

    Re_c = double(Restr)
    Wom_c = double(Womstr)
    Sh_c = double(Shstr)

    K_c = double(Kstr)
    Knl_c = 0.
    R_c = 1.
    dR_c = double(dRstr)
    L_c = double(Lstr)
    rho_c = 1.

    c_c = sqrt( K_c / 2. / rho_c * sqrt(pi)*R_c )
    U_c = Sh_c * c_c
    Q_c = 550.;

    print("---->Reynolds Re_c = ", Re_c)
    print("---->Womserley Wom_c = ", Wom_c)
    print("---->Shapiro Sh_c = ", Sh_c)
    print("---->Velocity U_c = ", U_c)


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
    rho = rho_c # rho of water
    # Viscosity (g/cm/s ~ Pa.s = 10 * g/cm/s)
    mu = U_c * R_c * rho / Re_c #3.5e-2		# Dynamic viscosity (g/cm/s)
    nu = mu/rho # (cm^2/s) Cinematic viscosity : Water at 25 C = 0,887012e-6

    # Stiffness coefficient beta (g/cm^2/s^2 ~ Pa/m = 0.1 g/(cm*s)^2)
    K = ones(NbrArt) * K_c

    # Nonlinear stiffness coefficient beta (g/cm^3/s^2)
    Knl = np.ones(NbrArt) * Knl_c

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
        arts[i].solverOrder =int(Order)
        arts[i].HR          =str(HR)
        arts[i].N           =int(N[i])

        arts[i].nLayer = layer[i]
        # arts[i].layProp = layer_Refinement(int(Raf),nLayer=int(layer[i]))
        arts[i].layProp = geometricRaffinement_Radial(Lmax=1./float(layer[i]),Lmin=1./float(layer[i]))
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
        arts[i].Knl     = Knl[i]* shape_Knl(arts[i].x)

        #Initial condition
        arts[i].InitProfile = str("Polhausen")
        arts[i].initA   = pi * arts[i].R * arts[i].R
        arts[i].initQ   = zeros(arts[i].N)

        #Output points
        arts[i].outPut=[0]	# Mesh points for which data will be stored
        arts[i].outPutProfile=[0]	# Mesh points for which data will be stored
        num_measpt = int(arts[i].N)
        L_measpt=[float(n)*L[i]/float(num_measpt-1) for n in range(1,num_measpt-1)] # (m)
        for k in range(len(L_measpt)) :
            arts[i].outPut.append(int(L_measpt[k]/arts[i].dx[0]))
            arts[i].outPutProfile.append(int(L_measpt[k]/arts[i].dx[0]))
        arts[i].outPut.append( arts[i].N-1 )
        arts[i].outPutProfile.append( arts[i].N-1 )

    #####################
    # Time setup
    T_c = 2. * pi / nu * ( (R_c / Wom_c )**2. )

    print("---->Period T_c = ", T_c)

    t_start = 4.  * T_c # (s)
    t_end   = 5.  * T_c # (s)

    # CFL
    Ct      = 1.
    dt_CFL  = Ct * min(dx/(U_c+c))

    # Time step
    power   = float(floor(mt.log10(dt_CFL)))
    fact    = floor(dt_CFL / (10. ** power))
    dt      = min(float(fact) * 10. ** (power),1.e-5)
    # Store step
    dt_store    = 1.e-3 * T_c
    storeStep   = max(1,int(dt_store / dt))

    # Store Profile
    dt_storeProfile = 1.e-1 * (t_end-t_start)
    storeStepProfile= max(1,int(dt_storeProfile / dt))

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
    tS.storeStepProfile     = storeStepProfile
    tS.CFL          = Ct
    tS.timeOrder    = 1

    ###################
    # Boundary condition

    #Boundary conditions for Poiseuille solution
    U_Input = maximum( 0., sin(2.*pi/T_c * tt) ) * U_c
    Rt = float(Rtstr) * ones(timeSteps);


    # def Q(t,alpha):
    #     return np.sin(np.pi * t/alpha)*(t<alpha)

    # Q_Input = np.zeros(timeSteps)
    # for i in range(0,timeSteps):
    #     Q_Input[i] = Q_c * Q(tt[i]/T_c - int(tt[i]/T_c), 0.35)

    # V_c         = integrate(tt,Q_Input) / ( t_end / T_c)
    ###################
    # daugher arteries, headPt and tailPt  :
    arts[0].daughterArts = [] ;

    arts[0].headPt.append(point(0))     ;
    arts[0].tailPt.append(point(1))     ;
    arts[0].headPt[0].type = "inQ"      ; arts[0].headPt[0].data = U_Input ;
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
