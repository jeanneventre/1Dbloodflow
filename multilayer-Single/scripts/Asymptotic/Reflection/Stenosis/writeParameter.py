#! /usr/bin/python2.7
import sys, getopt
import os
import numpy        as np
import math         as mt

from multiS_libDef  import *

from help_Sum       import *
from help_Raff      import *
from help_Wave      import *

def stenosisShape(x,Ls,Le,delta) :
    return 1. + delta * 0.5 * ( 1. + np.cos( np.pi + 2. * np.pi * float( x-Ls )/float(Le-Ls) ) )

def main(argv) :

    PATH = "" ; logo = "" ;
    Solver = '' ; HR = '' ;

    drCoarsestr = "" ; drFinestr = "" ;
    Nxstr = '' ; xOrderstr = '' ;

    dtstr = '' ; tOrderstr = '' ;

    Kstr    = "" ;
    Knlstr  = "" ;

    Shstr   = "" ;

    dRststr = "" ;
    dKststr = "" ;

    # COMMAND LINE ARGUMENTS
    #############################
    try :
        opts, args = getopt.getopt(argv,"hp:l:s:y:c:r:j:o:t:d:k:i:e:a:b:",["path=","logo=","Solver","HR","drCoarse=","drFine=","Nx=","xOrder=","dt=","tOrder=","K=","Knl=","dRstr","dRststr=","dKststr="])
    except getopt.GetoptError:
          print ('writeParameter-55.py -p <PATH> -l <logo> -s <Solver> -y <HR> -c <drCoarse> -r <drFine> -j <Nx> -o <xOrder> -t <dt> -d <tOrder> -k <K> -i <Knl> -e <dRstr> -a <dRststr> -b <dKststr>')
          sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print ('writeParameter-55.py -p <PATH> -l <logo> -s <Solver> -y <HR> -c <drCoarse> -r <drFine> -j <Nx> -o <xOrder> -t <dt> -d <tOrder> -k <K> -i <Knl> -e <dRstr> -a <dRststr> -b <dKststr>')
            sys.exit()
        if opt in ("-p", "--PATH"):
            PATH = arg
        if opt in ("-l", "--logo"):
            logo = arg

        if opt in ("-s", "--Sol"):
            Solver = arg
        if opt in ("-y", "--HR"):
            HR = arg

        if opt in ("-c", "--drCoarse"):
            drCoarsestr = arg
        if opt in ("-r", "--drFine"):
            drFinestr = arg
        if opt in ("-j", "--Nx"):
            Nxstr = arg
        if opt in ("-o", "--xOrder"):
            xOrderstr = arg

        if opt in ("-t", "--dt"):
            dtstr = arg
        if opt in ("-d", "--tOrder"):
            tOrderstr = arg

        if opt in ("-k", "--K"):
            Kstr = arg
        if opt in ("-i", "--Knl"):
            Knlstr = arg

        if opt in ("-e", "--Sh"):
            Shstr = arg
        if opt in ("-a", "--dRst"):
            dRststr = arg
        if opt in ("-b", "--dKst"):
            dKststr = arg

    if (PATH == "" ) :
        print("Empty PATH -----> EXIT")
        sys.exit()
    if (Solver == "" ) :
        print("Empty Solver -----> EXIT")
        sys.exit()
    if (HR == '' ) :
        print("Empty HR -----> EXIT")
        sys.exit()

    if (drCoarsestr == '' ) :
        print("Empty drCoarsestr -----> EXIT")
        sys.exit()
    if (drFinestr == '' ) :
        print("Empty drFinestr -----> EXIT")
        sys.exit()
    if (Nxstr == '' ) :
        print("Empty Nx -----> EXIT")
        sys.exit()
    if (xOrderstr == '' ) :
        print("Empty xOrder -----> EXIT")
        sys.exit()

    if (dtstr == '' ) :
        print("Empty dt -----> EXIT")
        sys.exit()
    if (tOrderstr == '' ) :
        print("Empty tOrder -----> EXIT")
        sys.exit()

    if (Kstr == '' ) :
        print("Empty Kstr -----> EXIT")
        sys.exit()
    if (Knlstr == '' ) :
        print("Empty Knlstr -----> EXIT")
        sys.exit()

    if (Shstr == '' ) :
        print("Empty dRstr -----> EXIT")
        sys.exit()

    if (dRststr == '' ) :
        print("Empty dRststr -----> EXIT")
        sys.exit()
    if (dKststr == '' ) :
        print("Empty dKststr -----> EXIT")
        sys.exit()

    print("---------------------")
    print("UNITS : cm, g, s")
    print("---------------------")
    print

    # Properties of water
    rho_c   = 1.
    mu_c    = 1.e-2

    # Geometrical measured data
    R0_c    = 1.
    L_c     = 10.

    # Propoerties of the stenosis
    dRst_c  = float(dRststr)
    dKst_c  = float(dKststr)
    Lst_s   = 4.5
    Lst_e   = 5.5

    # Optimization data
    K_c     = double(Kstr)
    Knl_c   = double(Knlstr)
    Cv_c    = 0.

    # Pump model
    T_c     = 0.1   # (s)
    Sh_c    = float(Shstr)
    Q_c     = Sh_c * celerity(rho_c,K_c,np.pi*R0_c*R0_c) * np.pi*R0_c*R0_c
    # Simulation time
    te_c    = 0.12

    drCoarse_c  = float(drCoarsestr)
    drFine_c    = float(drFinestr)
    Nx_c        = float(Nxstr)
    xOrder_c    = int(xOrderstr)
    dt_c        = float(dtstr)
    tOrder_c    = int(tOrderstr)

    # Define the coarse mesh size
    dxCoarse = float(L_c)/float(Nx_c)

    ###################################
    # NETWORK
    #############################
    N_art_tot = 1

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
    mu  = mu_c   # Dynamic viscosity (g/cm/s)

    # Stiffness coefficient beta (g/cm^2/s^2 ~ Pa/m = 0.1 g/(cm*s)^2)
    K   = ones(NbrArt) * K_c

    # Viscoelasticity coefficient C_v (cm^2/s)
    Cv  = ones(NbrArt) * Cv_c

    # Nonlinear stiffness coefficient beta (g/cm^3/s^2)
    Knl = np.ones(NbrArt) * Knl_c

    # Moens-Korteweg celerity (cm/s)
    c = celerity(rho,K,A)

        # Check length of array
    if len(L) != len(K) or len(L) != len(c) or len(L) != len(Cv) or len(L) != len(Knl) :
        print ('Dimension error in geometric parameters K, c, Cv, Knl or L')
        sys.exit()

    ###################
    # SHAPES (Well-balance)

    def space(dx) :
        N = len(dx) ;
        shape = zeros(N) ;
        shape[0] = dx[0]/2.
        for i in range(1,N) :
            shape[i] = shape[i-1] + (dx[i-1]+dx[i])/2.
        return shape

    def shape_R(x) :
        N = len(x)
        shape = ones(N)
        for i in range (N) :
            if (x[i] >= Lst_s and x[i] <= Lst_e ) :
                shape[i] = stenosisShape(x=x[i],Ls=Lst_s,Le=Lst_e,delta=dRst_c)
        return shape ;

    def shape_K(x) :
        N = len(x)
        shape = ones(N)
        for i in range (N) :
            if (x[i] >= Lst_s and x[i] <= Lst_e ) :
                shape[i] = stenosisShape(x=x[i],Ls=Lst_s,Le=Lst_e,delta=dKst_c)
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

        #Create the mesh
        arts[i].dx          = geometricRaffinement_Axial(  L=L_c,L1=0,L2=0,Lbuf=0, dxmax=dxCoarse, dxmin=dxCoarse )
        arts[i].x           = space(arts[i].dx)
        arts[i].N           = len(arts[i].dx)

        arts[i].layProp     = geometricRaffinement_Radial(  Lmax=drCoarse_c,Lmin=drFine_c)
        arts[i].nLayer      = len(arts[i].layProp)

        #Define numerical parameters
        arts[i].solver      =str(Solver)
        arts[i].HR          =str(HR)
        arts[i].solverOrder =int(xOrder_c)

        #Geometrical and mechanical parameters
        arts[i].rho         = rho
        arts[i].mu          = mu
        arts[i].L           = L[i]
        arts[i].R           = R[i]  * shape_R(arts[i].x)
        arts[i].K           = K[i]  * shape_K(arts[i].x)
        arts[i].Cv          = Cv[i] * shape_Cv(arts[i].x)
        arts[i].Knl         = Knl[i]* shape_Knl(arts[i].x)

        arts[i].Profile     = str("Polhausen")

        #Verification
        if( abs(arts[i].x[arts[i].N-1] + arts[i].dx[arts[i].N-1]/2. - arts[i].L) > 1.e-10) :
            print("Error in the geometrical parameters",arts[i].x[arts[i].N-1] + arts[i].dx[arts[i].N-1]/2., arts[i].L)
            sys.exit()

        #Initial condition
        arts[i].InitProfile = str("Polhausen")
        arts[i].initA       = pi * arts[i].R * arts[i].R
        arts[i].initQ       = zeros(arts[i].N)

        #Output points
        arts[i].outPut=[0]	# Mesh points for which data will be stored

        for ix in range(1,arts[i].N-1):
            arts[i].outPut.append( int(ix) )

        arts[i].outPut.append( arts[i].N-1 )

        #Output Profile points
        arts[i].outPutProfile=[0]	# Mesh points for which data will be stored

        arts[i].outPutProfile.append( arts[i].N-1 )

    #####################
    # Time setup

    # CFL
    Ct      = 1.
    dt_CFL  = Ct * min(arts[0].dx/c)

    # Analytic input signal
    #######################

    t_start = 0. # (s)
    t_end   = te_c # (s)

    # Time step
    # power   = float(floor(mt.log10(dt_CFL)))
    # fact    = floor(dt_CFL / (10. ** power))
    # dt      = min(float(fact) * 10. ** (power),1.e-5)

    dt        = float(dt_c)
    if (dt > dt_CFL) :
        print("Error dt>dt_CFL", dt, dt_CFL)
        sys.exit()

    print ("---->Time step dt = ", dt)
    print ("---->CFL Time step dt_CFL = ",dt_CFL)

    timeSteps = int(t_end/dt)
    tt        = ones(timeSteps)
    for it in range(timeSteps) :
        tt[it] = float(it) * dt

    # Store step
    dt_store        = 1.e-3 * (t_end-t_start)
    storeStep       = max(1,int(dt_store / dt))

    # Store Profile
    dt_storeProfile = 1.e-1 * (t_end-t_start)
    storeStepProfile= max(1,int(dt_storeProfile / dt))

    tS                      = timeSetup()
    tS.tt                   = tt
    tS.dt                   = dt
    tS.t_start              = t_start
    tS.t_end                = t_end
    tS.Nt                   = timeSteps
    tS.storeStep            = storeStep
    tS.storeStepProfile     = storeStepProfile
    tS.CFL                  = Ct
    tS.timeOrder            = int(tOrder_c)

    ###################
    # Boundary condition

    #Inlet
    pulse_Input             = maximum( sin(2.*pi/T_c*tt), 0) ;
    pulse_Input[(tt > T_c)] = 0. ;

    Q_Input     = Q_c * pulse_Input

    #Oulet
    Rt_Output   = np.zeros(timeSteps);

    ###################
    # daugher arteries, headPt and tailPt  :
    arts[0].daughterArts = [] ;

    arts[0].headPt.append(point(0))  ;
    arts[0].headPt[0].type  = "inQ"             ; arts[0].headPt[0].data    = Q_Input ;

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
