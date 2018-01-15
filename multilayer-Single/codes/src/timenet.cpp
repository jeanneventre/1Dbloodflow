#include "timenet.h"

time_c::time_c () {
  ts = ZERO;
  te = ZERO;
  dt = ZERO;
  nt = 0;
  nstore = 0;
  n = 0 ;
  cfl = ONE;
  dtcfl = ZERO;
  order = 1 ;
}
