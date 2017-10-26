##! /usr/bin/python2.7
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

def main(argv) :

    # Read input parameters and store them in hd
    hd = header()
    hd.headerInput(argv) ;

    # Fluid properties
    rho_c   = 1. ;

    if (hd.NNstr == "NonNewtonian") :
        phi_c   = -1. ;
        mu0_c   = 1.3    ;
        mu1_c   = 0.05 ;
        kmu_c   = 0.2 ;
        amu_c   = 1.5  ;

    # Geometrical properties
    L_c     = 10. ;
    R0_c    = 1. ;
    xm_c    = L_c / 2.

    # Mechanical properties
    K_c     = float(hd.Kstr)
    Cv_c    = 0.
    Knl_c   = 0.

    # Numerical properties
    Nx_c        = float (hd.Nxstr)
    xOrder_c    = float (hd.xOrderstr)
    dt_c        = float (hd.dtstr)
    tOrder_c    = int   (hd.tOrderstr)

    # Time properties

    ts_c    = 0. ;
    te_c    = 5. ;

    # Inlet & Outlet
    Rt_c    = 0. ;
    Pout_c  = 0. ; # Capillary pressure (used in RLC outflow bc)
    # Junction
    fact_c  = 1 ;

    # Rheology
    if (hd.NNstr == "NonNewtonian") :
        F_c     = 1.
        H_c     = 0.45
    else :
        F_c     = 0.
        H_c     = 0.

    # Passive Transport
    C_c    = 1. ;
    O_c    = 1. ;

    # Step
    dR_c    = float(hd.dRstr)

    ############################################################################
    ############################################################################
    # Network
    ############################################################################
    ############################################################################

    # Angle of bifurcation
    # Angle = np.array( [ [0.*np.pi,np.pi] ] )

    #############################
    # Geometrical parameters
    #############################

    # Length of the vessels (cm)
    L = np.array( [ L_c ] )
    # Radius of the artery (cm)
    R = np.array( [ R0_c ] )
    D = R * 2.
    A = np.pi * R * R

    NArt = len(L)

    # Check length of array
    if NArt != len(A) :
        print ('Dimension error in geometric parameters A_ref or L')
        sys.exit()

    #############################
    # Mechanical parameters
    #############################

    # Density (g/cm^3)
    rho = rho_c
    # Stiffness coefficient beta (g/cm^2/s^2 ~ Pa/m = 0.1 g/(cm*s)^2)
    K   = np.array( [ K_c ] )
    # Viscoelasticity coefficient C_v (cm^2/s)
    Cv  = Cv_c  * np.ones(NArt)
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
    phi = phi_c * np.ones(NArt)
    # Newtonian viscosities
    mu0 = mu0_c * np.ones(NArt)
    mu1 = mu1_c * np.ones(NArt)
    # Aggregation coefficient
    kmu = kmu_c * np.ones(NArt)
    # Desaggregation coefficient
    amu = amu_c * np.ones(NArt)

    #############################
    # Artery
    #############################

    arts = [artery(i) for i in range(NArt)]

    # Define default arterial properties
    hd.headerNum    (arts,L,c)
    hd.headerProp   (arts,rho,L,R,K,Cv,Knl)
    hd.headerRheo   (arts,phi,mu0,mu1,kmu,amu)

    hd.headerInit   (arts,F_c,H_c,C_c,O_c)
    # Set specific initial properties
    for i in range(NArt) :
        for ix in range(arts[i].N) :
            arts[i].initA[ix] = np.pi * R[i]*R[i] * decreasingStep(dR_c,xm_c,arts[i].x[ix]) * decreasingStep(dR_c,xm_c,arts[i].x[ix])

    hd.headerBC     (arts,fact_c,Pout_c)
    hd.headerOutput (arts)

    #############################
    # Time setup
    #############################

    # CFL
    Ct      = 1.
    dt_CFL  = hd.headerCFL(arts,Ct)

    # Analytic input signal
    #######################

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
    Rt_Input    = Rt_c * np.ones(timeSteps);
    #Q_Input     = PulseSin(1., tt)
    
    Pulse_Input             = PulseCos(1.,tt)
    Pulse_Input[tt > 1.]    = 0.
    Q_Input                 = Pulse_Input ;
    
    # Oulet
    Rt_Output   = Rt_c * np.ones(timeSteps);

    # Rheology
    H_Input     = np.zeros(timeSteps)
    F_Input     = np.zeros(timeSteps)
    H_Output    = np.zeros(timeSteps)
    F_Output    = np.zeros(timeSteps)

    # Passive transport
    C_Input   = np.zeros(timeSteps)
    O_Input   = np.zeros(timeSteps)
    C_Output  = np.zeros(timeSteps)
    O_Output  = np.zeros(timeSteps)

    #############################
    # Construct network
    #############################

    iart = 0 ; ihconj = 0 ; itconj = iart + 1 ;
    arts[iart].daughterArts = [] ;
    # Head point
    arts[iart].headPt.append(point(ihconj));
    arts[iart].headPt[0].type   = "inQ"    ; arts[iart].headPt[0].data = Q_Input ;
    # Tail point
    arts[iart].tailPt.append(point(itconj));
    arts[iart].tailPt[0].type   = "outRt"   ; arts[iart].tailPt[0].data = Rt_Output ;

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
