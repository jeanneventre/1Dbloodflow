#ifndef VESSELPROPERTIES_H
#define VESSELPROPERTIES_H

#include <misc.h>
#include <VECT.h>
#include <bc.h>

class vesselProperties {

  // Private variables can only be accessed by the base class
  private:

    // Numerics
    //#########
    string  solver, hr, profile, initprofile;
    int     order;

    int     nx, nl ;
    VECT    dx, dl ;

    // Physics
    //#########
    SCALAR  rho, mu ;
    VECT    k, cv, knl ;

    // Geometry
    //#########
    SCALAR  l;
    VECT    a0 ;

    // Initial conditions
    //###################
    VECT inita, initq ;

    // Boundary conditions
    //####################
    vector<bc> artbc ;

  // Protected variables can be accessed by any derived class
  protected:

  // Public variables, accessible from outside the class
  public:

    // Default constructor
    //####################
    vesselProperties();

    // Setters
    //########
    string    get_solver() const      {return solver;}
    string    get_hr()     const      {return hr;}
    string    get_profile()const      {return profile;}
    string    get_initprofile()const  {return initprofile;}
    int       get_order()  const      {return order;}

    int       get_nx()     const   {return nx;}
    int       get_nl()     const   {return nl;}
    VECT      get_dx()     const   {return dx;}
    VECT      get_dl()     const   {return dl;}

    SCALAR    get_rho()    const   {return rho;}
    SCALAR    get_mu()     const   {return mu;}
    VECT      get_k()      const   {return k;}
    VECT      get_cv()     const   {return cv;}
    VECT      get_knl()    const   {return knl;}
    SCALAR    get_l()      const   {return l;}
    VECT      get_a0()     const   {return a0;}
    VECT      get_inita()  const   {return inita;}
    VECT      get_initq()  const   {return initq;}
    vector<bc>get_artbc()  const   {return artbc;}

    // Getters
    //########
    void set_solver     (const string & _solver)      {solver=_solver;}
    void set_hr         (const string & _hr)          {hr=_hr;}
    void set_profile    (const string & _profile)     {profile=_profile;}
    void set_initprofile(const string & _initprofile) {initprofile=_initprofile;}
    void set_order      (int _order)                  {order=_order;}

    void set_nx     (int _nx)                 {nx=_nx;}
    void set_nl     (int _nl)                 {nl=_nl;}
    void set_dx     (VECT _dx)                {dx=_dx;}
    void set_dl     (VECT _dl)                {dl=_dl;}

    void set_rho    (SCALAR _rho)             {rho=_rho;}
    void set_mu     (SCALAR _mu)              {mu=_mu;}
    void set_k      (VECT _k)                 {k=_k;}
    void set_cv     (VECT _cv)                {cv=_cv;}
    void set_knl    (VECT _knl)               {knl=_knl;}
    void set_l      (SCALAR _l)               {l=_l;}
    void set_a0     (VECT _a0)                {a0=_a0;}
    void set_inita  (VECT _inita)             {inita=_inita;}
    void set_initq  (VECT _initq)             {initq=_initq;}

    // Boundary condition
    //###################
    void    add_bc  (bc& _bc)                          { artbc.push_back(_bc)        ;}
    int     size_bc ()                          const { return artbc.size()         ;}
    string  type_bc (const int n)               const { return artbc[n].get_type()  ;}
    VECT    data_bc (const int n)               const { return artbc[n].get_data()  ;}
    SCALAR  data_bc (const int n, const int nt) const { return artbc[n].get_data(nt);}

  };

#endif // VESSELPROPERTIES_H
