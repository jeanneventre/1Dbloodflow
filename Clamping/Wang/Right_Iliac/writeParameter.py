#! /usr/bin/python2.7
import sys, getopt
import os
import numpy    as np
import math     as mt

from bfS_libDef import *

from help_Input     import *

from help_Sum       import *
from help_Wave      import *
from help_Geometry  import *
from help_Inlet     import *
from help_Network   import *

from scipy.interpolate import interp1d

def main(argv) :

    # Read input parameters and store them in hd
    hd = header()
    hd.headerInput(argv) ;

    # Fluid properties
    ##################
    rho_c   = 1. ;

    if      (hd.NNstr == "Newtonian") :
        phi_c   = -4. ;
        mu0_c   = 0. ;
        mu1_c   = 0.05 ;
        kmu_c   = 0. ;
        amu_c   = 0. ;
    elif    (hd.NNstr == "NonNewtonian") :
        phi_c   = -4. ;
        mu0_c   = 1.3    ;
        mu1_c   = 0.05 ;
        kmu_c   = 0.2 ;
        amu_c   = 1.5  ;
    elif    (hd.NNstr == "Inviscid") :
        phi_c   = 0. ;
        mu0_c   = 0. ;
        mu1_c   = 0. ;
        kmu_c   = 0. ;
        amu_c   = 0. ;

    # Mechanical properties
    # Cv_c    = 0.
    nuv_c   = float(hd.Cvstr)
    Knl_c   = 0.

    # Numerical properties
    Nx_c        = float (hd.Nxstr)
    xOrder_c    = int   (hd.xOrderstr)
    dt_c        = float (hd.dtstr)
    tOrder_c    = int   (hd.tOrderstr)
    hd.Nxmax    = 200

    # Time properties
    T_c     = 1. ;
    ts_c    = 9. * T_c
    te_c    = 10.* T_c

    # Boundary properties
    # Inlet
    Q_c = 300.
    # Outlet
    Pout_c  = 0. ; # Capillary pressure (used in RLC outflow bc)
    # Junction
    fact_c  = 1. ;

    # Rheology
    if (hd.NNstr == "NonNewtonian") :
        F_c     = 1.
        H_c     = 0.45
    else :
        F_c     = 0.
        H_c     = 0.

    # Passive Transport
    C_c    = 0. ;
    O_c    = 0. ;

    # Stenosis
    dR_c    = 0. ;

    ############################################################################
    ############################################################################
    # Network
    ############################################################################
    ############################################################################

    # Angle of bifurcation
    # Angle = np.array( [ [0.*np.pi,np.pi], [1./4.*np.pi,np.pi], [7./4.*np.pi,np.pi] ] )

    #############################
    # Geometrical parameters
    #############################

    # Length of the vessels (cm)
    L   = np.array([    4.0,  2.0,  3.4,  3.4,  17.7, 14.8, 42.2, 23.5, 6.7,  7.9,
                        17.1, 17.6, 17.7, 3.9,  20.8, 17.6, 17.7, 5.2,  3.4,  14.8,
                        42.2, 23.5, 6.7,  7.9,  17.1, 8.0,  10.4, 5.3,  2.0,  1.0,
                        6.6,  7.1,  6.3,  5.9,  1.0,  3.2,  1.0,  3.2,  10.6, 5.0,
                        1.0,  5.9,  5.8,  14.4, 5.0,  44.3, 12.6, 32.1, 34.3, 14.5,
                        5.0,  44.4, 12.7, 32.2, 34.4
                    ] )
    # Radius of the artery (cm)
    R   = np.array( [   1.470, 1.263, 0.699, 0.541, 0.473, 0.240, 0.515, 0.367, 0.454, 0.194,
                        0.433, 0.382, 0.382, 1.195, 0.413, 0.334, 0.334, 1.120, 0.474, 0.203,
                        0.455, 0.324, 0.401, 0.172, 0.383, 0.317, 1.071, 0.920, 0.588, 0.540,
                        0.458, 0.375, 0.386, 0.499, 0.843, 0.350, 0.794, 0.350, 0.665, 0.194,
                        0.631, 0.470, 0.470, 0.482, 0.301, 0.361, 0.356, 0.376, 0.198, 0.482,
                        0.301, 0.361, 0.356, 0.375, 0.197
                    ] )
    D   = 2. * R
    A   = np.pi * R * R

    NArt = len(L)

    # Check length of array
    if NArt != len(R) or NArt != len(A) :
        print ('Dimension error in geometric parameters A_ref or L')
        sys.exit()

    #############################
    # Mechanical parameters
    #############################

    # Density (g/cm^3)
    rho = rho_c
    # Stiffness coefficient beta (g/cm^2/s^2 ~ Pa/m = 0.1 g/(cm*s)^2)
    h   =   np.array( [ 0.163, 0.126, 0.080, 0.067, 0.063, 0.045, 0.067, 0.043, 0.046, 0.028,
                     0.046, 0.045, 0.042, 0.115, 0.063, 0.045, 0.042, 0.110, 0.066, 0.045,
                     0.067, 0.043, 0.046, 0.028, 0.046, 0.049, 0.100, 0.090, 0.064, 0.064,
                     0.049, 0.045, 0.054, 0.069, 0.080, 0.053, 0.080, 0.053, 0.075, 0.043,
                     0.065, 0.060, 0.060, 0.053, 0.040, 0.050, 0.047, 0.045, 0.039, 0.053,
                     0.040, 0.050, 0.047, 0.045, 0.039] );
    E   =   np.array( [ 0.4, 0.4, 0.4, 0.4, 0.4, 0.8, 0.4, 0.8, 0.8, 1.6,
                     0.8, 0.8, 0.8, 0.4, 0.4, 0.8, 0.8, 0.4, 0.4, 0.8,
                     0.4, 0.8, 0.8, 1.6, 0.8, 0.4, 0.4, 0.4, 0.4, 0.4,
                     0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4,
                     0.4, 0.4, 0.4, 0.8, 1.6, 0.8, 0.8, 1.6, 1.6, 0.8,
                     1.6, 0.8, 0.8, 1.6, 1.6] ) * 1e7
    K   = rigidity(E,h,R)
    # Viscoelasticity coefficient C_v (cm^2/s)
    nuv = nuv_c
    Cv  = viscoelasticity(rho,nuv,h,R)
    # Nonlinear stiffness coefficient beta (g/cm^3/s^2)
    Knl = Knl_c * np.ones(NArt)
    # Moens-Korteweg celerity (cm/s)
    c   = celerity(rho,K,A)

    # Check length of array
    if NArt != len(K) or NArt != len(Cv) or NArt != len(Knl) or NArt != len(c) :
        print ('Dimension error in geometric parameters K, Cv, Knl, c or L')
        sys.exit()

    #############################
    # Rheology
    #############################

    # Profile coefficient phi
    phi     = phi_c     * np.ones(NArt)
    # Newtonian viscosities
    mu0     = mu0_c     * np.ones(NArt)
    mu1     = mu1_c     * np.ones(NArt)
    # Aggregation coefficient
    kmu     = kmu_c     * np.ones(NArt)
    # Desaggregation coefficient
    amu     = amu_c     * np.ones(NArt)

    #############################
    # Artery
    #############################

    arts = [artery(i) for i in range(NArt)]

    # Define default arterial properties
    hd.headerNum    (arts,L,c)
    hd.headerProp   (arts,rho,L,R,K,Cv,Knl)
    hd.headerRheo   (arts,phi,mu0,mu1,kmu,amu)
    hd.headerInit   (arts,F_c,H_c,C_c,O_c)
    hd.headerBC     (arts,fact_c,Pout_c)

    hd.headerOutput (arts)
    # Specific output
    for i in range(NArt) :
        arts[i].outPut = []
        arts[i].outPut.append(0)
        arts[i].outPut.append(arts[i].N/2)
        arts[i].outPut.append(arts[i].N-1)

    #############################
    # Time setup
    #############################

    # CFL
    Ct      = 1.
    dt_CFL  = hd.headerCFL(arts,Ct)

    # Analytic input signal
    t_start = ts_c
    t_end   = te_c

    # Time step
    dt        = float(dt_c)
    if (dt > dt_CFL) :
        print("Error dt>dt_CFL", dt, dt_CFL)
        sys.exit()

    timeSteps = int(t_end/dt)
    tt = np.ones(timeSteps)
    for it in range(timeSteps) :
        tt[it] = float(it) * dt

    #######################

    dt_store    = 1.e-3 * (t_end-t_start)
    storeStep   = max(1,int(dt_store / dt))

    print ("---->Time step dt = ", dt)
    print ("---->CFL Time step dt_CFL = ",dt_CFL)

    tS              = timeSetup()
    tS.tt           = tt
    tS.dt           = dt
    tS.t_start      = t_start
    tS.t_end        = t_end
    tS.Nt           = timeSteps
    tS.storeStep    = storeStep
    tS.CFL          = Ct
    tS.timeOrder    = int(hd.tOrderstr)

    #############################
    # Boundary condition
    #############################

    # Inlet
    Q_Input = Q_c * PulseSin(T_c,tt)

    # Heart model
    V_c         = integrate(tt,Q_Input) / ( te_c / T_c)
    print ("---->Ejection period (s)                : ", T_c)
    print ("---->Stroke Volume (cm^3)               : ", V_c)
    print ("---->Cardiac Output (L/min)             : ", V_c / T_c * 60./1000.)
    print ("---->Maximum Input Flow Rate (cm^3/s)   : ", Q_c)
    print ("---->Maximum Input Speed (cm/s)         : ", Q_c / A[0] )
    print ("---->Reynolds number                    : ", Reynolds(rho_c,mu1_c,R[0],Q_c/A[0]))
    print ("---->Womersley number                   : ", Womersley(rho_c,mu1_c,R[0],T_c))

    # Rheology
    H_Input     = H_c * np.ones(timeSteps)
    F_Input     = np.zeros(timeSteps)

    # Passive transport
    C_Input   = np.zeros(timeSteps)
    O_Input   = np.zeros(timeSteps)
    C_Output  = np.zeros(timeSteps)
    O_Output  = np.zeros(timeSteps)

    #############################
    # Construct network
    #############################


    # Right cerebral
    arts[4].jDAG(   hConj=3,    dArts=[arts[11],arts[12]],  tConj=hd.CONJ,nt=timeSteps)

    arts[11].RtDAG( hConj=5,    Rt=0.784,                   tConj=hd.CONJ,nt=timeSteps)
    arts[12].RtDAG( hConj=5,    Rt=0.790,                   tConj=hd.CONJ,nt=timeSteps)

    # Left cerebral
    arts[14].jDAG(  hConj=2,    dArts=[arts[15],arts[16]],  tConj=hd.CONJ,nt=timeSteps)

    arts[15].RtDAG( hConj=15,   Rt=0.784,                   tConj=hd.CONJ,nt=timeSteps)
    arts[16].RtDAG( hConj=15,   Rt=0.791,                   tConj=hd.CONJ,nt=timeSteps)

    # Aorta
    arts[0].iDAG(   hConj=0,        dArts=[arts[1]],
                    xType="inQ",    xData=Q_Input,
                    FData=F_Input,  HData=H_Input,          tConj=hd.CONJ,nt=timeSteps)
    arts[1].jDAG(   hConj=1,    dArts=[arts[13],arts[14]],  tConj=hd.CONJ,nt=timeSteps)
    arts[13].jDAG(  hConj=2,    dArts=[arts[17],arts[18]],  tConj=hd.CONJ,nt=timeSteps)
    arts[17].jDAG(  hConj=14,   dArts=[arts[25],arts[26]],  tConj=hd.CONJ,nt=timeSteps)
    arts[26].jDAG(  hConj=18,   dArts=[arts[27],arts[28]],  tConj=hd.CONJ,nt=timeSteps)
    arts[27].jDAG(  hConj=27,   dArts=[arts[33],arts[34]],  tConj=hd.CONJ,nt=timeSteps)
    arts[34].jDAG(  hConj=28,   dArts=[arts[35],arts[36]],  tConj=hd.CONJ,nt=timeSteps)
    arts[36].jDAG(  hConj=35,   dArts=[arts[37],arts[38]],  tConj=hd.CONJ,nt=timeSteps)
    arts[38].jDAG(  hConj=37,   dArts=[arts[39],arts[40]],  tConj=hd.CONJ,nt=timeSteps)
    arts[40].jDAG(  hConj=39,   dArts=[arts[41],arts[42]],  tConj=hd.CONJ,nt=timeSteps)

    # Intercostals
    arts[25].RtDAG( hConj=18,   Rt=0.627,                   tConj=hd.CONJ,nt=timeSteps)

    # Celiac, Spleen, Gastric, Hepatic
    arts[28].jDAG(  hConj=27,   dArts=[arts[29],arts[30]],  tConj=hd.CONJ,nt=timeSteps)
    arts[29].jDAG(  hConj=29,   dArts=[arts[31],arts[32]],  tConj=hd.CONJ,nt=timeSteps)

    arts[30].RtDAG( hConj=29,   Rt=0.925,                   tConj=hd.CONJ,nt=timeSteps)
    arts[31].RtDAG( hConj=30,   Rt=0.921,                   tConj=hd.CONJ,nt=timeSteps)
    arts[32].RtDAG( hConj=30,   Rt=0.930,                   tConj=hd.CONJ,nt=timeSteps)

    # Renal
    arts[35].RtDAG( hConj=35,   Rt=0.861,                   tConj=hd.CONJ,nt=timeSteps)
    arts[37].RtDAG( hConj=37,   Rt=0.861,                   tConj=hd.CONJ,nt=timeSteps)

    # Mesentric
    arts[33].RtDAG( hConj=28,   Rt=0.934,                   tConj=hd.CONJ,nt=timeSteps)
    arts[39].RtDAG( hConj=39,   Rt=0.918,                   tConj=hd.CONJ,nt=timeSteps)

    # Right arm
    arts[2].jDAG(   hConj=1,    dArts=[arts[3],arts[4]],    tConj=hd.CONJ,nt=timeSteps)
    arts[3].jDAG(   hConj=3,    dArts=[arts[5],arts[6]],    tConj=hd.CONJ,nt=timeSteps)
    arts[6].jDAG(   hConj=4,    dArts=[arts[7],arts[8]],    tConj=hd.CONJ,nt=timeSteps)
    arts[8].jDAG(   hConj=7,    dArts=[arts[9],arts[10]],   tConj=hd.CONJ,nt=timeSteps)

    arts[5].RtDAG(  hConj=4,    Rt=0.906,                   tConj=hd.CONJ,nt=timeSteps)
    arts[7].RtDAG(  hConj=7,    Rt=0.820,                   tConj=hd.CONJ,nt=timeSteps)
    arts[9].RtDAG(  hConj=9,    Rt=0.956,                   tConj=hd.CONJ,nt=timeSteps)
    arts[10].RtDAG( hConj=9,    Rt=0.893,                   tConj=hd.CONJ,nt=timeSteps)

    # Left arm
    arts[18].jDAG(  hConj=14,   dArts=[arts[19],arts[20]],  tConj=hd.CONJ,nt=timeSteps)
    arts[20].jDAG(  hConj=19,   dArts=[arts[21],arts[22]],  tConj=hd.CONJ,nt=timeSteps)
    arts[22].jDAG(  hConj=21,   dArts=[arts[23],arts[24]],  tConj=hd.CONJ,nt=timeSteps)

    arts[19].RtDAG( hConj=19,   Rt=0.906,                   tConj=hd.CONJ,nt=timeSteps)
    arts[21].RtDAG( hConj=21,   Rt=0.821,                   tConj=hd.CONJ,nt=timeSteps)
    arts[23].RtDAG( hConj=23,   Rt=0.956,                   tConj=hd.CONJ,nt=timeSteps)
    arts[24].RtDAG( hConj=23,   Rt=0.893,                   tConj=hd.CONJ,nt=timeSteps)

    # Right leg
    arts[42].jDAG(  hConj=41,   dArts=[arts[49],arts[50]],  tConj=hd.CONJ,nt=timeSteps)
    #----Clamp here----
    # arts[49].jDAG(  hConj=43,   dArts=[arts[51],arts[52]],  tConj=hd.CONJ,nt=timeSteps)
    arts[49].RtDAG(  hConj=43,   Rt=1.,  tConj=hd.CONJ,nt=timeSteps)
    
    #----Not connected
    arts[51].iDAG(  hConj=56,       dArts=[arts[53],arts[54]],
                    xType="inQ",    xData=np.zeros(timeSteps),
                    FData=F_Input,  HData=H_Input,          tConj=hd.CONJ,nt=timeSteps)
    arts[52].RtDAG( hConj=56,   Rt=0.888,                   tConj=hd.CONJ,nt=timeSteps)
    # arts[51].jDAG(  hConj=50,   dArts=[arts[53],arts[54]],  tConj=hd.CONJ,nt=timeSteps)
    # arts[52].RtDAG( hConj=50,   Rt=0.888,                   tConj=hd.CONJ,nt=timeSteps)

    arts[50].RtDAG( hConj=43,   Rt=0.925,                   tConj=hd.CONJ,nt=timeSteps)
    arts[53].RtDAG( hConj=52,   Rt=0.724,                   tConj=hd.CONJ,nt=timeSteps)
    arts[54].RtDAG( hConj=52,   Rt=0.716,                   tConj=hd.CONJ,nt=timeSteps)

    # Left leg
    arts[41].jDAG(  hConj=41,   dArts=[arts[43],arts[44]],  tConj=hd.CONJ,nt=timeSteps)
    arts[43].jDAG(  hConj=42,   dArts=[arts[45],arts[46]],  tConj=hd.CONJ,nt=timeSteps)
    arts[45].jDAG(  hConj=44,   dArts=[arts[47],arts[48]],  tConj=hd.CONJ,nt=timeSteps)

    arts[44].RtDAG( hConj=42,   Rt=0.925,                   tConj=hd.CONJ,nt=timeSteps)
    arts[46].RtDAG( hConj=44,   Rt=0.885,                   tConj=hd.CONJ,nt=timeSteps)
    arts[47].RtDAG( hConj=46,   Rt=0.724,                   tConj=hd.CONJ,nt=timeSteps)
    arts[48].RtDAG( hConj=46,   Rt=0.716,                   tConj=hd.CONJ,nt=timeSteps)

    #############################
    # Network definition
    #############################

    net=network(ARTS=arts,tS=tS)

    #############################
    # Create necessary files
    #############################

    hd.headerFile() ;

    #############################
    # Write parameters
    #############################

    net.writeParam(str(hd.PATH)+"parameters_"+str(hd.LOGO))

if __name__ == "__main__":
   main(sys.argv[1:])
