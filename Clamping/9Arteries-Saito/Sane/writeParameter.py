#! /usr/bin/python2.7
import sys, getopt
import os
import numpy    as np
import math     as mt

from bfS_libDef import *

from help_Input     import *
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
    rho_c   = 1. ;

    if      (hd.NNstr == "Newtonian") :
        phi_c   = -4. ;
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

    # Mechanical properties
    nuv_c   = float(hd.Cvstr)
    Knl_c   = 0.

    # Numerical properties
    Nx_c        = float (hd.Nxstr)
    xOrder_c    = int   (hd.xOrderstr)
    dt_c        = float (hd.dtstr)
    tOrder_c    = int   (hd.tOrderstr)
    hd.Nxmax    = 200

    # Time properties
    T_c     = 0.57 ;
    ts_c    = 10. * T_c ;
    te_c    = 12. * T_c ; 

    # Boundary properties
    # Inlet
    Q_c = 400
    # Outlet
    Pout_c  = 0. ; # Capillary pressure (used in RLC outflow bc)
    Rt_c    = float(hd.Rtstr) ;
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
    # dR_c    = 0.
    # dK_c    = 0.

    ############################################################################
    ############################################################################
    # Network
    ############################################################################
    ###########################################################################
    #############################
    # Geometrical parameters
    #############################

    # Length of the vessels (cm)
    L = np.array( [ 4.0, 72.5, 2.0, 38.5, 3.9, 69.1, 34.5, 96.9, 96.9 ] )
    # Radius of the artery (cm)
    R = np.array( [ 1.5, 0.5, 1.3, 0.4, 1.2, 0.4, 0.8, 0.5, 0.5] )
    # R = D / 2.
    D = 2. * R
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
    # Width of the wall (cm)
    h = np.array( [ 0.16, 0.06, 0.12, 0.06, 0.1, 0.06, 0.1, 0.5, 0.5] )
    # E = np.array( [ 0.4, 0.4, 0.4, 0.6, 0.4, 0.4,0.4, 0.8,0.8 ]) * 1e7

    E = float (hd.Kstr)
    # dE = np.array([0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2])*1e7
    # E = E+dE

    # Stiffness coefficient beta (g/cm^2/s^2 ~ Pa/m = 0.1 g/(cm*s)^2)
    K = rigidity(E,h,R)
    # Viscoelasticity coefficient C_v (cm^2/s)
    nuv = nuv_c
    Cv  = viscoelasticity(rho,nuv,h,R)
    # Nonlinear stiffness coefficient beta (g/cm^3/s^2)
    Knl = Knl_c * np.ones(NArt)
    # Moens-Korteweg celerity (cm/s)
    c = celerity(rho,K,A)

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
    hd.headerBC     (arts,fact_c,Pout_c)

    hd.headerOutput (arts)
    # Set specific output points
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

    Q_Input = Q_c * PulseSin(T_c, tt)
    V_c         = integrate(tt,Q_Input) / ( te_c / T_c)
    print ("---->Ejection period (s)                : ", T_c)
    print ("---->Stroke Volume (cm^3)               : ", V_c)
    print ("---->Cardiac Output (L/min)             : ", V_c / T_c * 60./1000.)
    print ("---->Maximum Input Flow Rate (cm^3/s)   : ", Q_c)
    print ("---->Maximum Input Speed (cm/s)         : ", Q_c / A[0] )

    # Q_Input     =   (   2.8e6 *   (   3.1199 +  7.7982 * np.sin( 2  * np.pi / T_c * tt + 0.5769)
    #                                         +   4.1228 * np.sin( 4  * np.pi / (T_c) * tt - 0.8738)
    #                                         -   1.0611 * np.sin( 6  * np.pi / (T_c)* tt + 0.7240)
    #                                         +   0.7605 * np.sin( 8  * np.pi / (T_c) * tt -0.6387)
    #                                         -   0.9148 * np.sin( 10 * np.pi / T_c * tt +1.1598)
    #                                         +   0.4924 * np.sin( 12 * np.pi / T_c * tt -1.0905)
    #                                         -   0.5580 * np.sin( 14 * np.pi / T_c * tt +1.042)
    #                                         +   0.3280 * np.sin( 16 * np.pi / T_c * tt -0.5570)
    #                                         -   0.3941 * np.sin( 18 * np.pi / T_c * tt +1.2685)
    #                                         +   0.2833 * np.sin( 20 * np.pi / T_c * tt +0.6702)
    #                                         +   0.2272 * np.sin( 22 * np.pi / T_c * tt -1.4983)
    #                                         +   0.2249 * np.sin( 24 * np.pi / T_c * tt +0.9924)
    #                                         +   0.2589 * np.sin( 26 * np.pi / T_c * tt -1.5616)
    #                                         -   0.1460 * np.sin( 28 * np.pi / T_c * tt -1.3106)
    #                                         +   0.2141 * np.sin( 30 * np.pi / T_c * tt -1.1306)
    #                                         -   0.1253 * np.sin( 32 * np.pi / T_c * tt +0.1552)
    #                                         +   0.1321 * np.sin( 34 * np.pi / T_c * tt -1.5595)
    #                                         -   0.1399 * np.sin( 36 * np.pi / T_c * tt +0.4223)
    #                                         -   0.0324 * np.sin( 38 * np.pi / T_c * tt +0.7811)
    #                                         -   0.1211 * np.sin( 40 * np.pi / T_c * tt +1.0729)
    #                             ) /1000./60./2.5
    #                 )

    # Q_Input = 3e6/1000./60/2.5 * (2.5+ 7*( np.sin(2*np.pi /T_c * (tt-0.5)) + 0.5*np.sin(4*np.pi /T_c * (tt-0.5))) )#+ 0.5*np.sin(12*np.pi/T_c * tt))

    # x = np.array([ 139263.08977103  , 30633.91621266,   -3343.23891143,  -11180.43854173,
    # 673.36107665 ,  -2908.83686411,    1646.90656992  ,  -416.15620448,
    # -1330.41989531])

    # P_Input = x[0] + x[1] * np.sin(2 * np.pi/T_c * tt + x[2]) + x[3] * np.sin(4*np.pi/T_c * tt + x[4]) + x[5] * np.sin(6 * np.pi/T_c *tt + x[6])- x[7] * np.sin(14*np.pi/T_c * tt +x[8])

    # a               = 217.801         
    # b               = 299.778          
    # c               = -68.602         
    # d               = -291.923         
    # e               = 39.217           
    # f               = 42.4621     
    # g               = 53.7485  


    # Q_Input = a+ b * np.sin(2*np.pi/T_c * tt +c) + d * np.sin(4*np.pi/T_c * tt + e) + f*np.sin(6*np.pi/T_c *tt+g)


    # Q_Input = 3e6/1000./60. * (np.sin(2*np.pi*tt/(T_c-0.1) * (tt< ts_c + T_c)))

    # P_Input = 180000 + 30000 * PulseSin(T_c,tt)  

    # P_Input = 95000 + 25000 * np.sin(2*np.pi /T_c * tt - 1.2)

    # Oulet

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

    arts[0].iDAG(   hConj=0,        dArts=[arts[1], arts[2]],
                    xType="inQ",    xData=Q_Input,
                    FData=F_Input,  HData=H_Input,          tConj=hd.CONJ,nt=timeSteps)

    arts[1].RtDAG( hConj=1,     Rt=Rt_c,                    tConj=hd.CONJ,nt=timeSteps)

    arts[2].jDAG(  hConj=1,     dArts=[arts[3],arts[4]],    tConj=hd.CONJ,nt=timeSteps)
    
    arts[3].RtDAG( hConj=3,     Rt=0.784,                    tConj=hd.CONJ,nt=timeSteps)

    arts[4].jDAG(  hConj=3,     dArts=[arts[5],arts[6]],    tConj=hd.CONJ,nt=timeSteps)

    arts[5].RtDAG( hConj=5,     Rt=Rt_c,                    tConj=hd.CONJ,nt=timeSteps)

    arts[6].jDAG( hConj=5,      dArts=[arts[7], arts[8]],   tConj=hd.CONJ,nt=timeSteps) 
    arts[7].RtDAG( hConj=7,     Rt= 0.724,                    tConj=hd.CONJ,nt=timeSteps)
    arts[8].RtDAG( hConj=7,     Rt= 0.724,                    tConj=hd.CONJ,nt=timeSteps)

    # clamp here -------
    # arts[6].RtDAG( hConj=5,      Rt=1.,                      tConj=hd.CONJ,nt=timeSteps)
    # arts[7].RtDAG( hConj=10,     Rt=0.724,                    tConj=hd.CONJ,nt=timeSteps)
    # arts[8].RtDAG( hConj=10,     Rt=0.724,                    tConj=hd.CONJ,nt=timeSteps)


    # iart = 0 ; ihconj = 0 ; itconj = iart + 1 ;
    # arts[iart].daughterArts = [arts[1],arts[2]] ;
    # # Head point
    # arts[iart].headPt.append(point(ihconj));
    # arts[iart].headPt[0].type  = "inP"              ; arts[iart].headPt[0].data  = P_Input ;
    # # Tail point
    # arts[iart].tailPt.append(point(itconj));
    # arts[iart].tailPt[0].type = hd.CONJ                ; arts[iart].tailPt[0].data  = np.zeros(timeSteps);

    # iart = 1 ; ihconj = 1 ; itconj = iart + 1 ;
    # # Head point
    # arts[iart].headPt.append(point(ihconj));
    # arts[iart].headPt[0].type  = hd.CONJ               ; arts[iart].headPt[0].data  = np.zeros(timeSteps);
    # # Tail point
    # arts[iart].tailPt.append(point(itconj));
    # arts[iart].tailPt[0].type = "outRt"             ; arts[iart].tailPt[0].data  = Rt_Output;

    # iart = 2 ; ihconj = 1 ; itconj = iart + 1 ;
    # arts[iart].daughterArts = [arts[3],arts[4]] ;
    # # Head point
    # arts[iart].headPt.append(point(ihconj));
    # arts[iart].headPt[0].type  = hd.CONJ               ; arts[iart].headPt[0].data  = np.zeros(timeSteps);
    # # Tail point
    # arts[iart].tailPt.append(point(itconj));
    # arts[iart].tailPt[0].type = hd.CONJ                ; arts[iart].tailPt[0].data  = np.zeros(timeSteps);

    # iart = 3 ; ihconj = 3 ; itconj = iart + 1 ;
    # # Head point
    # arts[iart].headPt.append(point(ihconj));
    # arts[iart].headPt[0].type  = hd.CONJ               ; arts[iart].headPt[0].data  = np.zeros(timeSteps);
    # # Tail point
    # arts[iart].tailPt.append(point(itconj));
    # arts[iart].tailPt[0].type = "outRt"             ; arts[iart].tailPt[0].data  = Rt_Output ;

    # iart = 4 ; ihconj = 3 ; itconj = iart + 1 ;
    # arts[iart].daughterArts = [arts[5],arts[6]] ;
    # # Head point
    # arts[iart].headPt.append(point(ihconj));
    # arts[iart].headPt[0].type  = hd.CONJ               ; arts[iart].headPt[0].data  = np.zeros(timeSteps);
    # # Tail point
    # arts[iart].tailPt.append(point(itconj));
    # arts[iart].tailPt[0].type = hd.CONJ                ; arts[iart].tailPt[0].data  = np.zeros(timeSteps) ;

    # iart = 5 ; ihconj = 5 ; itconj = iart + 1 ;
    # # Head point
    # arts[iart].headPt.append(point(ihconj));
    # arts[iart].headPt[0].type  = hd.CONJ               ; arts[iart].headPt[0].data  = np.zeros(timeSteps);
    # # Tail point
    # arts[iart].tailPt.append(point(itconj));
    # arts[iart].tailPt[0].type = "outRt"             ; arts[iart].tailPt[0].data  = Rt_Output ;

    # iart = 6 ; ihconj = 5 ; itconj = iart + 1 ;
    # arts[iart].daughterArts = [arts[7],arts[8]] ;
    # # Head point
    # arts[iart].headPt.append(point(ihconj));
    # arts[iart].headPt[0].type  = hd.CONJ               ; arts[iart].headPt[0].data  = np.zeros(timeSteps);
    # # Tail point
    # arts[iart].tailPt.append(point(itconj));
    # arts[iart].tailPt[0].type = hd.CONJ                ; arts[iart].tailPt[0].data  = np.zeros(timeSteps);

    # iart = 7 ; ihconj = 7 ; itconj = iart + 1 ;
    # # Head point
    # arts[iart].headPt.append(point(ihconj));
    # arts[iart].headPt[0].type  = hd.CONJ               ; arts[iart].headPt[0].data  = np.zeros(timeSteps);
    # # Tail point
    # arts[iart].tailPt.append(point(itconj));
    # arts[iart].tailPt[0].type = "outRt"             ; arts[iart].tailPt[0].data  = Rt_Output ;

    # iart = 8 ; ihconj = 7 ; itconj = iart + 1 ;
    # # Head point
    # arts[iart].headPt.append(point(ihconj));
    # arts[iart].headPt[0].type  = hd.CONJ               ; arts[iart].headPt[0].data  = np.zeros(timeSteps);
    # # Tail point
    # arts[iart].tailPt.append(point(itconj));
    # arts[iart].tailPt[0].type = "outRt"             ; arts[iart].tailPt[0].data  = Rt_Output ;


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
