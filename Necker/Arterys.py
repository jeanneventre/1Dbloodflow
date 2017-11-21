#example.py
import numpy
import math
# import matplotlib.pyplot as plt
from pylab import *
from mpl_toolkits.mplot3d import Axes3D

data = numpy.load("velocity-download-595f881f278f6a562e020a3d-678dd80d2456e8ab.npy")
print("data shape: ", data.shape)
# data shape: (20, 3, 100, 152, 256)
# Data has 20 time points each of which is a volume of 100 slices.
# Each slice has 152 rows and 256 columns
#
# Velocity is a three vector (x, y, z) in patient space and has units of mm/s.
# That is, the x component is oriented in the Right->Left patient direction,
# the y component is oriented in the Anterior->Posterior patient direction
# and the z component is oriented in the Inferior->Superior patient direction. For axially
# acquired data these coordinate directions will align with the row, column, slice
# directions of the pixel data. For coronal, sagittal or oblique data sets
# they will be different.
# Variable data holds velocity at point (i, j, k) in space and at each time point (t).
#
# RL component of velocity at the first time point for all pixels
v_rl_0 = data[0][0]
print ("v_rl_0 shape: ", v_rl_0.shape)
#v_rl_0 shape:  (100, 152, 256)

# AP component of velocity at the first time point for all pixels
v_ap_0 = data[0][1]
print ("v_ap_0 shape: ", v_rl_0.shape)
#v_ap_0 shape:  (100, 152, 256)

# IS component of velocity at the first time point for all pixels
v_is_0 = data[0][2]
print ("v_is_0 shape: ", v_rl_0.shape)
#v_is_0 shape:  (100, 152, 256)
#
# velocity at pixel location (20, 30, 40) at the last time point
v = numpy.zeros(3)
print ("v shape: ", v.shape)
v[0] = data[19][0][40][30][20]
v[1] = data[19][1][40][30][20]
v[2] = data[19][2][40][30][20]
print ("v = ", v)
# magnitude of v
print( "v magnitude (speed): ", math.sqrt(v.dot(v)))

# fig = plt.figure()
# ax = fig.gca(projection='3d')


# ax.scatter(v[0],v[1],v[2],c='r', marker= 'o')		
# draw()
# pause(0.1)


# ax = fig.add_subplot(111, projection='3d')
# ax.scatter(v[0],v[1],v[2],c='r', marker= 'o')
# ax.plot_trisurf(U,V,W,cmap=cm.coolwarm, linewidth=0, antialiased=False)
# Axes3D.scatter(data[10,0,:,10,10], data[10,1,:,10,10], data[10,2,:,10,10], zdir='z', s=20, c=None, depthshade=True, *args=None,**kwargs=None)


# show()