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
from pylab import *

def main(argv) :

    # Read input parameters and store them in hd
    hd = header()
    hd.headerInput(argv) ;

    # Fluid properties
    rho_c   = 1. ;

    if      (hd.NNstr == "Newtonian") :
        phi_c   = -4 ;
        mu0_c   = 0. ;
        mu1_c   = 0.05 ;
        kmu_c   = 0. ;
        amu_c   = 0. ;
    elif    (hd.NNstr == "NonNewtonian") :
        phi_c   = float(hd.phistr) ;
        mu0_c   = 1.2 ;
        mu1_c   = 4.e-2 ;
        kmu_c   = 2.5e-1 ;
        amu_c   = 1.2 ;
    elif    (hd.NNstr == "Inviscid") :
        phi_c   = 0. ;
        mu0_c   = 0. ;
        mu1_c   = 0. ;
        kmu_c   = 0. ;
        amu_c   = 0. ;

    # Geometrical properties
    L_c     = 10. ;
    R0_c    = 1.4 ;
    h0_c    = 0.16 ;

    # Numerical properties
    Nx_c        = float (hd.Nxstr)
    xOrder_c    = int   (hd.xOrderstr)
    dt_c        = float (hd.dtstr)
    tOrder_c    = int   (hd.tOrderstr)

    # Mechanical properties
    nuv_c   = float(hd.Cvstr)
    Knl_c   = 0.

    # Time properties
    T_c     = 0.98 ;
    ts_c    = 0. * T_c ;
    te_c    = 5. * T_c;

    # Boundary properties

    # Inlet

    # Outlet
    P_c = float(hd.P1)
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
    C_c    = 0. ;
    O_c    = 0. ;

    # Stenosis
    dR_c    = -0.4;
    # dK_c    = 0.

    ############################################################################
    ############################################################################
    # Network
    ############################################################################
    ############################################################################

    #############################
    # Geometrical parameters
    #############################

    # Length of the vessels (cm)
    L = np.array( [ L_c ] )
    # Radius of the artery (cm)
    R = np.array( [ R0_c ] )
    D = R * 2.
    A = np.pi * R * R
    # thickness of the vessels (cm)
    h = np.array([ h0_c ])

    NArt = len(L)

    # Check length of array
    if NArt != len(A) :
        print ('Dimension error in geometric parameters A_ref or L')
        sys.exit()

    #############################
    # Specific shapes
    #############################

    def patho_R(x,xs,xe,dR) :
        N = len(x)
        shape = np.ones(N)
        for ix in range(N) :
            shape[ix] = cosStenosis(dr=dR,xs=xs,xe=xe,x=x[ix])
        return shape ;

    def patho_K(x,xs,xe,dK) :
        N = len(x)
        shape = np.ones(N)
        for ix in range(N) :
            shape[ix] = cosStenosis(dr=dK,xs=xs,xe=xe,x=x[ix])
        return shape ;

    #############################
    # Mechanical parameters
    #############################

    # Density (g/cm^3)
    rho = rho_c
    # Stiffness coefficient beta (g/cm^2/s^2 ~ Pa/m = 0.1 g/(cm*s)^2)
    E = 0.4e7
    K = rigidity(E,h,R)
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

    iPatho = 0 
    
    # arts[iPatho].K =  K[iPatho] * patho_K(x=arts[iPatho].x,xs=1./3.*arts[iPatho].L,xe=2./3.*arts[iPatho].L,dK=dK_c)

    # Define default arterial properties
    hd.headerNum    (arts,L,c)
    hd.headerProp   (arts,rho,L,R,K,Cv,Knl)
    arts[iPatho].R =  R[iPatho] * patho_R(x=arts[iPatho].x,xs=1./3.*arts[iPatho].L,xe=2./3.*arts[iPatho].L,dR=dR_c)
    hd.headerRheo   (arts,phi,mu0,mu1,kmu,amu)

    hd.headerInit   (arts,F_c,H_c,C_c,O_c)
    # Set specific initial conditions
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

    #Inlet

    # U_c = 30.;
    # U_Input = U_c * np.ones(timeSteps)
    
    def U(t,alpha):
        return np.sin(np.pi * t/alpha)*(t<alpha)

    U_Input = np.zeros(timeSteps)
    U_c = 58.9
    cc =  7.

    for i in range(0,timeSteps):
        U_Input[i] = cc + U_c * U(tt[i]/T_c - int(tt[i]/T_c),6.97/20)

    Q_in = U_Input * A ; 
    Q_c = cc * A 
    V_c         = integrate(tt,Q_in-Q_c) / ( te_c / T_c)

    P_Input  = np.zeros(timeSteps)

    #Outlet
    P_Output = P_c * np.ones(timeSteps)
    
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
    arts[iart].headPt[0].type       = "inU"         ; arts[iart].headPt[0].data     = U_Input   ;
    # Tail point
    arts[iart].tailPt.append(point(itconj));
    arts[iart].tailPt[0].type       = "outP"        ; arts[iart].tailPt[0].data     = P_Output      ;

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
