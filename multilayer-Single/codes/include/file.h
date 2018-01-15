#ifndef FILE_H
#define FILE_H

#include "misc.h"

class file {

  // Private variables can only be accessed by the base class
  private:

    string dagFile;
    string inoutFile;

    string propertiesFile;
    string dxFile, dlFile;
    string a0File, kFile, cvFile, knlFile;

    string initaFile, initqFile;

    string outputFile, outputProFile;
    string timeFile;

  // Protected variables can be accessed by any derived class
  protected:

  // Public variables, accessible from outside the class
  public:

    // Default constructor
    //####################
    file();

    // Setters
    //########
    string get_dagFile()        const   {return dagFile;}
    string get_inoutFile()      const   {return inoutFile;}
    string get_propertiesFile() const   {return propertiesFile;}
    string get_dxFile()         const   {return dxFile;}
    string get_dlFile()         const   {return dlFile;}
    string get_a0File()         const   {return a0File;}
    string get_kFile()          const   {return kFile;}
    string get_cvFile()         const   {return cvFile;}
    string get_knlFile()        const   {return knlFile;}
    string get_initaFile()      const   {return initaFile;}
    string get_initqFile()      const   {return initqFile;}
    string get_outputFile()     const   {return outputFile;}
    string get_outputProFile()  const   {return outputProFile;}
    string get_timeFile()       const   {return timeFile;}


    // Getters
    //########
    void set_dagFile        (const string & _dagFile)         {dagFile=_dagFile;}
    void set_inoutFile      (const string & _inoutFile)       {inoutFile=_inoutFile;}
    void set_propertiesFile (const string & _propertiesFile)  {propertiesFile=_propertiesFile;}
    void set_dxFile         (const string & _dxFile)          {dxFile=_dxFile;}
    void set_dlFile         (const string & _dlFile)          {dlFile=_dlFile;}
    void set_a0File         (const string & _a0File)          {a0File=_a0File;}
    void set_kFile          (const string & _kFile)           {kFile=_kFile;}
    void set_cvFile         (const string & _cvFile)          {cvFile=_cvFile;}
    void set_knlFile        (const string & _knlFile)         {knlFile=_knlFile;}
    void set_initaFile      (const string & _initaFile)       {initaFile=_initaFile;}
    void set_initqFile      (const string & _initqFile)       {initqFile=_initqFile;}
    void set_outputFile     (const string & _outputFile)      {outputFile=_outputFile;}
    void set_outputProFile  (const string & _outputProFile)   {outputProFile=_outputProFile;}
    void set_timeFile       (const string & _timeFile)        {timeFile=_timeFile;}

  };

#endif // FILE_H
