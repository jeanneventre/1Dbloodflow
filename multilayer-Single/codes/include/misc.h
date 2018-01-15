#ifndef MISC_H_INCLUDED
#define MISC_H_INCLUDED

#include <lib.h>
#include <matrix.h>
#include <error.h>
#include <omp.h>

#define MAX(a,b) (a>=b?a:b)
#define MIN(a,b) (a<=b?a:b)

#define ZERO        0.L
#define ONEsTWELVE  1.L/12.L
#define ONEsEIGHT   1.L/8.L
#define ONEsSIX     1.L/6.L
#define ONEsFIVE    0.2L
#define ONEsFOUR    0.25L
#define ONEsTHREE   1.L/3.L
#define TWOsFIVE    0.4L
#define ONEsTWO     0.5L
#define TWOsTHREE   2.L/3.L
#define THREEsFOUR  0.75L
#define ONE         1.L
#define FIVEsFOUR   1.25L
#define THREEsTWO   1.5L
#define TWO         2.L
#define FIVEsTWO    2.5L
#define THREE       3.L
#define FOUR        4.L
#define FIVE        5.L
#define EIGHT       8.L
#define TEN         10.L
#define PI 3.1415926535897932384626433832795028841971L

#define HEPS 1.e-6L

#define EPSILON 1.e-14L
#define EPSILON_X 1.e-13L
#define EPSILON_BC 1.e-12L
#define EPSILON_G 1.e-12L

#define EPSILON_CV 2.e-15L
#define maxIt 40

#define VERSION "bloodflow_1D version 3.0, 2016-05"

using namespace std;

typedef long double SCALAR;
typedef unsigned int uint;
typedef matrix<long double> MATR;

#endif // MISC_H_INCLUDED
