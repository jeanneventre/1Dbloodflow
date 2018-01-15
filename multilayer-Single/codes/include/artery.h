#ifndef ARTERY_H
#define ARTERY_H

#include <misc.h>
#include <VECT.h>
#include <bc.h>
#include <timenet.h>
#include <vesselProperties.h>
#include <helpFunctions.h>
#include <profile.h>

// Base class artery
class artery {

  // Private variables can only be accessed by the base class
  private:

  // Protected variables can be accessed by any derived class
  protected:

    // Numerics
    //#########
    string solver;
    const int xorder;
    string hr;
    string profile;
    string initprofile;

    const int nx, nl;
    VECT x, dx, r, dl, dla, dlj ;
    SCALAR dxmin ;
    const SCALAR dt ;

    // Physics
    //#########
    const SCALAR rho, mu ;
    VECT k, cv, knl ;

    SCALAR deltaBL ;

    // Geometry
    //#########
    const SCALAR l;
    VECT a0 ;

    // Boundary conditions
    //####################
    vector<bc> artbc ;

    // Variables
    //##########
    VECT A, Am1, initA;
    VECT initQ;
    MATR initQl;
    MATR Ql, Qlm1;
    VECT Ainlet, Aoutlet;
    VECT Qinlet, Qoutlet;

  // Public variables, accessible from outside the class
  public:

    // Constructor
    //############
    artery(const vesselProperties& vP, const time_c& timenet);

    // Setters
    //########
    void set_x() ;
    void set_dxmin() ;
    void set_r() ;
    void set_dla() ;
    void set_dlj() ;

    void set_initQl() ;

    void set_Ainlet   (SCALAR _A) { Ainlet[0]   = _A ;}
    void set_Qinlet   (SCALAR _Q) { Qinlet[0]   = _Q ;}
    void set_Aoutlet  (SCALAR _A) { Aoutlet[0]  = _A ;}
    void set_Qoutlet  (SCALAR _Q) { Qoutlet[0]  = _Q ;}

    // Getters
    //########
    int    get_nl         () const  { return nl                ;}
    SCALAR get_Lambdamax  () const ;
    SCALAR get_dtmin      () const ;
    SCALAR get_dxmin      () const  { return double(dxmin)     ;}
    SCALAR get_resA       () const ;
    SCALAR get_resQl      () const ;
    // Other getters can be found in arteryNum.cpp
    virtual SCALAR get_G1s2 (int j, int i) const = 0 ;

    // Readers
    //########
    double read_x   (int pos) const { return double(x[pos])   ;}
    double read_a0  (int pos) const { return double(a0[pos])  ;}
    double read_k   (int pos) const { return double(k[pos])   ;}
    double read_cv  (int pos) const { return double(cv[pos])  ;}
    double read_knl (int pos) const { return double(knl[pos])  ;}
    double read_A   (int pos) const { return double(A[pos])   ;}
    // double read_P   (int pos) const { return pressure_invisc(k[pos],a0[pos],A[pos]);}
    double read_P   (int pos, const SCALAR dt) const    ;

    double read_Rl  (int j, int i) const { return double( sqrt(A[i] / PI) * r[j] ) ;  } ;
    // Other readers can be found in arteryNum.cpp
    virtual double read_Q     (int pos)      const = 0 ;
    virtual double read_gradxP(int pos)      const = 0 ;
    virtual double read_Tw    (int pos)      const = 0 ;
    virtual double read_U0    (int pos)      const = 0 ;

    virtual double read_alpha (int pos)      const = 0 ;
    virtual double read_phi   (int pos)      const = 0 ;

    virtual double read_Ul  (int j, int i) const = 0 ;
    virtual double read_Ulr (int j, int i) const = 0 ;

    // Help functions
    //###############
    void verbose(const time_c& timenet) ;

    // Virtual functions (members of arteryNum)
    //#########################################
    virtual void initialization(const time_c& timenet) =0 ;
    virtual void stepBC(const time_c& timenet) =0 ;
    virtual void stepReconstruct() =0 ;
    virtual void step(const time_c& timenet) =0 ;

};

#endif // ARTERY_H
