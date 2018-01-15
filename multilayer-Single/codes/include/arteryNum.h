#ifndef ARTERYNUM_H
#define ARTERYNUM_H

#include <misc.h>
#include <VECT.h>
#include <bc.h>
#include <timenet.h>
#include <artery.h>
#include <triDiagMatrix.h>
#include <vesselProperties.h>
#include <helpFunctions.h>
#include <arteryBC.h>
#include <alger.h>

using namespace alger;

// Inherited class artery
class arteryNum : public artery {

  // Private variables can only be accessed by the base class
  private:

    // Helpfull variables
    VECT Q;
    VECT Tw, gradxP;
    VECT alpha, phi;

    MATR Ul, Ulr ;
    MATR Ul_d, Ul_u;
    MATR G1s2, u1s2;

    // First and second order variables
    //#################################
    VECT A_l,A_r;
    MATR Ql_l,Ql_r;
    VECT K_l,K_r;
    VECT Z_l,Z_r;
    VECT H_l,H_r;
    VECT HmZ_l,HmZ_r;
    VECT A0_l,A0_r;

    VECT Knl_l,Knl_r;
    VECT Znl_l,Znl_r;

    // Hydrostatic reconstruction variables
    //#####################################
    VECT Kst,Zst,A0st;
    VECT Knlst,Znlst;
    VECT Kc,Zc,A0c;
    VECT A_ll,A_rr;
    MATR Ql_ll,Ql_rr;
    VECT Ac_ll,Ac_rr;

    // Flux variables
    //###############
    VECT fluxA;
    MATR fluxAl, fluxQl;

    VECT RHS1, RHS1_Star, RHS1_StarStar;
    MATR RHS2, RHS2_Star, RHS2_StarStar;

    // Tridiagonal matrix
    //###################
    triDiagMatrix Amatrix , Bmatrix;
    triDiagMatrix Afmatrix ;

    // Boundary conditions
    //####################
    VECT Ainlet_r , Aoutlet_l;
    VECT Qinlet_r , Qoutlet_l;
    SCALAR inData1  , inData2;
    SCALAR outData1 , outData2;
    int nInBC       , nOutBC;

    void inBC(const time_c& timenet , const bc inbc) ;
    void outBC(const time_c& timenet, const bc outbc) ;

    // Update
    void update_Q() ;
    void update_gradxP() ;
    void update_Tw() ;
    void update_alpha() ;
    void update_phi() ;
    void update_Ul() ;
    void update_Ulr() ;
    void update_Data();

    // High order reconstruction
    void reconstruct_1order();
    void reconstruct_2order();
    //Hydrostatic Reconstruction
    void reconstruct_K();
    void reconstruct_K_HR();
    void reconstruct_Geometry_HR();
    void reconstruct_HRQ();
    void reconstruct_Ul();
    // Flux
    void fluxKinetic_Hat();
    // Mass exchanges
    void G1s2_u1s2();
    // Evaluate Right Hand Side
    void eval_RHS_HR(int i, SCALAR& RHS);
    void eval_RHS(VECT& RHS1, MATR& RHS2);

    void stepFlux(VECT& RHS1, MATR& RHS2);

    // Temporal schemes
    void Euler(const time_c& timenet);
    void RungeKutta_2order(const time_c& timenet);
    void RungeKutta_3order(const time_c& timenet);
    void AdamBashforth_2order(const time_c& timenet);
    void AdamBashforth_3order(const time_c& timenet);

    // Viscoelastic solver
    void set_diffusionMatrix(const time_c& timenet);
    void stepParabolic();
    // Friction solver
    void set_frictionMatrix(const time_c& timenet, const int i);
    void stepFriction(const time_c& timenet);

  // Protected variables can be accessed by any derived class
  protected:

  // Public variables, accessible from outside the class
  public:

    // Constructor
    //############
    arteryNum(const vesselProperties& vP, const time_c& timenet);

    // Initialization
    void initialization(const time_c& timenet) ;

    // Time advance
    void stepBC(const time_c& timenet) ;
    void stepReconstruct();
    void step(const time_c& timenet);

    // Getters
    //########
    SCALAR get_G1s2 (int j, int i)  const { return G1s2(j,i)           ;};

    // Readers
    //########
    double  read_Q      (int pos)   const { return double(Q[pos])      ;};
    double  read_gradxP (int pos)   const { return double(gradxP[pos]) ;};
    double  read_Tw     (int pos)   const { return double(Tw[pos])     ;};
    double  read_U0     (int pos)   const { return double(Ul(0,pos))   ;};
    double  read_alpha  (int pos)   const { return double(alpha[pos])  ;};
    double  read_phi    (int pos)   const { return double(phi[pos])    ;};

    double  read_Ul (int j, int i)  const { return double(Ul(j,i))     ;};
    double  read_Ulr(int j, int i)  const { return double(Ulr(j,i))    ;};

};

#endif // ARTERYNUM_H
