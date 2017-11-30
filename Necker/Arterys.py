#example.py
import numpy as np
import math
# import matplotlib.pyplot as plt
from pylab import *
import matplotlib
from mpl_toolkits.mplot3d import Axes3D
import pickle

data = np.load("velocity-download-595f881f278f6a562e020a3d-678dd80d2456e8ab.npy")
# print("data shape: ", data.shape)
# data shape: (20, 3, 160, 128, 224)
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
# print ("v_rl_0 shape: ", v_rl_0.shape)
#v_rl_0 shape:  (160, 128, 224)

# AP component of velocity at the first time point for all pixels
v_ap_0 = data[0][1]
# print ("v_ap_0 shape: ", v_rl_0.shape)
#v_ap_0 shape:  (160, 128, 224)

# IS component of velocity at the first time point for all pixels
v_is_0 = data[0][2]
# print ("v_is_0 shape: ", v_rl_0.shape)
#v_is_0 shape:  (160, 128, 224)

# velocity at pixel location (20, 30, 40) at the last time point
v = np.zeros(3)
# print ("v shape: ", v.shape)
v[0] = data[19][0][40][30][20]
v[1] = data[19][1][40][30][20]
v[2] = data[19][2][40][30][20]
# print ("v = ", v)
# magnitude of v
# print( "v magnitude (speed): ", math.sqrt(v.dot(v)))

x = np.linspace(0,128,128)
y = np.linspace(0,224,224)

x,y = np.meshgrid(x,y)

x=np.transpose(x)
y=np.transpose(y)

mag= np.zeros((128,224))

# line, = plt.plot(y,mag)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
for t in range(0,20):
	Vmag0 = data[t][0][40]
	Vmag1 = data[t][1][40]
	Vmag2 = data[t][2][40]

	for i in range(35,100):
		for j in range(45,180):
			if (i>0 and i<55 and j>170 and j<224) or (i<45 and j<57):
				mag[i,j] = 0.
			else :
				mag[i,j] = math.sqrt(Vmag0[i,j]**2 + Vmag1[i,j]**2 + Vmag2[i,j]**2)
	# 		# datamin = np.min(mag)
	# 		# datamax = np.max(mag)
			# col = ax.scatter(i,j,mag[i,j], color='r', marker='o')

	surf = ax.plot_surface(x,y,mag,rstride=1,cstride=1,cmap=cm.coolwarm,linewidth=0,antialiased=False)
	# fig.colorbar(surf, shrink=0.5, aspect=5)
	draw()
	pause(0.5)
	plt.figure(2)
	y = np.linspace(0,224,224)	
	plt.plot(y,mag[64,:])
	draw()
	pause(0.5)
	clf()
# matplotlib.animation.Animation.save('movie.mp4')
show()

