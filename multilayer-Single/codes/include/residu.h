#ifndef RESIDU_H
#define RESIDU_H

#include <misc.h>

class residu {

  // Private variables can only be accessed by the base class
  private:

    SCALAR resA, resAmax;
    SCALAR resQ, resQmax;

  // Protected variables can be accessed by any derived class
  protected:

  // Public variables, accessible from outside the class
  public:

    // Constructor
    //############
    residu() ;

    // Setters
    //########
    void set_resA     (SCALAR _res) { resA    = _res ;}
    void set_resAmax  (SCALAR _res) { resAmax = _res ;}
    void set_resQ     (SCALAR _res) { resQ    = _res ;}
    void set_resQmax  (SCALAR _res) { resQmax = _res ;}

    // Getters
    //########
    SCALAR get_resA     () const { return resA   ;}
    SCALAR get_resAmax  () const { return resAmax;}
    SCALAR get_resQ     () const { return resQ   ;}
    SCALAR get_resQmax  () const { return resQmax;}


};

#endif // RESIDU_H
