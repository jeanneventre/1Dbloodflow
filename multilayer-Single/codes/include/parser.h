#ifndef PARSER_H
#define PARSER_H

#include <misc.h>
#include <vesselProperties.h>
#include <stringManage.h>
#include <file.h>
#include <bc.h>
#include <timenet.h>
#include <output.h>

using namespace std;
using namespace stringManage;

class parser {

	// Private variables can only be accessed by the base class
  private:

		string * propertiesData;
    string * inoutData ;
    string * timeData ;
    MATR dagData, outputData, outputProfileData;
		MATR dxData,dlData,a0Data,kData,cvData,knlData;
    MATR initaData,initqData;

  // Protected variables can be accessed by any derived class
  protected:

  // Public variables, accessible from outside the class
  public:

		// Constructor
	  //############
		parser(const file& dataFile);

		// Read all files
		void readtoString( const char* file, string*& data ) ;
    void readtoMatrix( const char* file, MATR& data ) ;

    // Setters
    //########
    int  nSet         ( const char* file) ;
	  void propertiesSet(vector<vesselProperties>&, int n);
    void bcSet        (vector<vesselProperties>&, int n);
    void tSet         (time_c& timenet) ;
    void outputSet    (output& outnet) ;

};


#endif // PARSER_H
