#ifndef NETWORK_H
#define NETWORK_H

#include <misc.h>

#include <parser.h>
#include <timenet.h>
#include <output.h>
#include <residu.h>

#include <artery.h>
#include <arteryNum.h>


class network
{
  // Private variables can only be accessed by the base class
  private:

    // Network
    //########
    int nart, nconj, nbc ;
    vector<vesselProperties> vP ;
    vector<artery*> arts ;

    // Time
    //#####
    time_c timenet ;

    // Output
    //#######
    output outnet ;
    residu resnet ;
    FILE** file_record;
    FILE** profile_record;
    FILE*  file_residu;

    string dataFolder;
    string suffix;

  // Protected variables can be accessed by any derived class
  protected:

  // Public variables, accessible from outside the class
  public:

    // Constructor
	  //############
    network(const string&);

    // Run
    //####
    void run() ;

    // Network
    //########
    void appointSolver(artery*& art, vesselProperties& vP, time_c& timenet ) ;

    // Setters
    //########
    void set_dataFolder(const string& destiFolder) {dataFolder  = destiFolder ;}
    void set_suffix(const string& destiFolder)     {suffix      = destiFolder ;}

    // Writers
    //########
    void openFile() ;
    void closeFile() ;
    void writeToFile(const SCALAR _t) const;
    void writeToProfile(const SCALAR _t) const;

    // Checkers
    //#########
    void check_dt() ;
    void check_residu();

    // Functions
    //##########
    bool fileExist (const string&) ;

};

#endif // NETWORK_H
