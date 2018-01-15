#ifndef OUTPUT_H
#define OUTPUT_H

#include <misc.h>

class output {

  // Private variables can only be accessed by the base class
  private:

    vector <int> arteryRecord, arteryProfileRecord;
    vector <int> posRecord, posProfileRecord;
    vector <int> storeArt;

  // Protected variables can be accessed by any derived class
  protected:

  // Public variables, accessible from outside the class
  public:

    // Constructor
    //############
    output() ;

    // Setters
    //########

    // Getters
    //########
    int get_arteryRecord  (const int n) const { return arteryRecord[n]  ;}
    int get_posRecord     (const int n) const { return posRecord[n]     ;}

    int get_arteryProfileRecord  (const int n) const { return arteryProfileRecord[n]  ;}
    int get_posProfileRecord     (const int n) const { return posProfileRecord[n]     ;}

    int get_storeArt      (const int n) const { return storeArt[n]      ;}

    // Sizers
    //########
    int size_storeArt      () const { return storeArt.size()    ;}

    int size_posRecord     () const { return posRecord.size()   ;}
    int size_arteryRecord  () const { return arteryRecord.size();}

    int size_posProfileRecord     () const { return posProfileRecord.size()   ;}
    int size_arteryProfileRecord  () const { return arteryProfileRecord.size();}

    // Adders
    //#######
    void add_arteryRecord (const int nArt) { arteryRecord.push_back(nArt)  ;}
    void add_posRecord    (const int nPos) { posRecord.push_back(nPos)     ;}

    void add_arteryProfileRecord (const int nArt) { arteryProfileRecord.push_back(nArt)  ;}
    void add_posProfileRecord    (const int nPos) { posProfileRecord.push_back(nPos)     ;}

    void add_storeArt     (const int nArt) { storeArt.push_back(nArt)   ;}

};

#endif // OUTPUT_H
