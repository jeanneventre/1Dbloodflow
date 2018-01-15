#include <error.h>

void Error( std::string msg ) {
    Warning( msg ) ;
    std::cerr << "---EXIT---" << std::endl;
    exit(1);
}

void Warning( std::string msg ) {
    std::cerr << "Warning: " << msg << std::endl;
}
