#ifndef STRINGMANAGE_H_INCLUDED
#define STRINGMANAGE_H_INCLUDED

#include <lib.h>

using namespace std;
namespace stringManage
{
    int findPosition_inTable(const vector<string>&, const string&);
    vector<string> split(const string& s, const string& delim, const bool keep_empty = true);

};

#endif // STRINGMANAGE_H_INCLUDED
