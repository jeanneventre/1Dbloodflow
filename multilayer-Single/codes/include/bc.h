#ifndef BC_H
#define BC_H

#include <misc.h>
#include <VECT.h>

class bc {

  // Private variables can only be accessed by the base class
  private:

    string type;
    VECT data;

  // Protected variables can be accessed by any derived class
  protected:

  // Public variables, accessible from outside the class
  public:

    // Constructor
    //############
    bc() ;
    bc(string _type, VECT _data);

    // Getters
    //########
    string  get_type()              const   {return type    ;}
    VECT    get_data()              const   {return data    ;}
    SCALAR  get_data(const int nt)  const   {return data[nt];}

  };

#endif // BC_H
