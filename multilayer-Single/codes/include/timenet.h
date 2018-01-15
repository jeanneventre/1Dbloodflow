#ifndef TIMENET_H
#define TIMENET_H

#include <misc.h>
#include <VECT.h>

class time_c {

  // Private variables can only be accessed by the base class
  private:

    SCALAR ts,te,dt;
    int nt,nstore,nstoreprofile,n;
    SCALAR cfl, dtcfl;
    int order;
    VECT t;

  // Protected variables can be accessed by any derived class
  protected:

  // Public variables, accessible from outside the class
  public:

    // Constructor
    //############
    time_c() ;

    // Setters
    //########
    void set_ts             (SCALAR _ts)          {ts=_ts;}
    void set_te             (SCALAR _te)          {te=_te;}
    void set_dt             (SCALAR _dt)          {dt=_dt;}
    void set_nt             (int _nt)             {nt=_nt;}
    void set_nstore         (int _nstore)         {nstore=_nstore;}
    void set_nstoreprofile  (int _nstoreprofile)  {nstoreprofile=_nstoreprofile;}
    void set_t              (VECT _t)             {t=_t;}
    void set_cfl            (SCALAR _cfl)         {cfl=_cfl;}
    void set_dtcfl          (SCALAR _dtcfl)       {dtcfl=_dtcfl;}
    void set_order          (int _order)          {order=_order;}

    void set_n              (int _n)              {n=_n;}

    // Getters
    //########
    SCALAR  get_ts()            const {return ts;}
    SCALAR  get_te()            const {return te;}
    SCALAR  get_dt()            const {return dt;}
    int     get_nt()            const {return nt;}
    int     get_nstore()        const {return nstore;}
    int     get_nstoreprofile() const {return nstoreprofile;}
    SCALAR  get_t(int i)        const {return t[i];}
    SCALAR  get_cfl()           const {return cfl;}
    SCALAR  get_dtcfl()         const {return dtcfl;}
    int     get_order()         const {return order;}

    int     get_n()             const {return n;}
};

#endif // TIMENET_H
