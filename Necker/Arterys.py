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

# for t in range(0,20):
mid_x = 68
mid_y = 110

# for k in range(0,160):
k=70
t = 10	
Vmag0 = data[t][0][k]
Vmag1 = data[t][1][k]
Vmag2 = data[t][2][k]

for i in range(0,128):
	for j in range(0,224):
		mag[i,j] = math.sqrt(Vmag0[i,j]**2 + Vmag1[i,j]**2 + Vmag2[i,j]**2)
	# 		# datamin = np.min(mag)
	# 		# datamax = np.max(mag)
			# ax.scatter(i,j,mag[i,j], color='r', marker='o')
fig = figure()
ax = fig.add_subplot(321, projection='3d')
surf = ax.plot_surface(x,y,mag,rstride=1,cstride=1,cmap=cm.coolwarm,linewidth=0,antialiased=False)
xlabel('x')
ylabel('y')

pts_x = np.array([34,103,68,68])
pts_y = np.array([110,110,187,42])

pts_x2 = np.array([43,94,68,68])
pts_y2 = np.array([110,110,169,53])

a = 34 
b = 73

ax = fig.add_subplot(322)
CS = ax.contourf(x,y,mag,50,cmap=cm.coolwarm)
plot(pts_x,pts_y, 'r*')
plot(pts_x2,pts_y2, 'k*')
xlabel('x')
ylabel('y')

for i in range(0,128):
	for j in range(0,224):
		if (((x[i,j]-68.5)/a)**2 + ((y[i,j]-115)/b)**2 )<=1 :
			mag[i,j] = math.sqrt(Vmag0[i,j]**2 + Vmag1[i,j]**2 + Vmag2[i,j]**2)
		else : 
			mag[i,j] = 0.

ax = fig.add_subplot(323)
# CS = plt.contour(x,y,mag,25,linewidths=0.5, colors='k')
CS = ax.contourf(x,y,mag,50,cmap=cm.coolwarm)

plot(pts_x,pts_y, 'r*')
plot(pts_x2,pts_y2, 'k*')
xlabel('x')
ylabel('y')

a = 25.5
b = 58

for i in range(0,128):
	for j in range(0,224):
		if (((x[i,j]-68.5)/a)**2 + ((y[i,j]-115)/b)**2 )<=1 :
			mag[i,j] = math.sqrt(Vmag0[i,j]**2 + Vmag1[i,j]**2 + Vmag2[i,j]**2)
		else : 
			mag[i,j] = 0.

ax = fig.add_subplot(324)
CS = ax.contourf(x,y,mag,50,cmap=cm.coolwarm)
plot(pts_x2,pts_y2, 'k*')
text(pts_x2[0]-10,pts_y2[0]-10, 'A')
text(pts_x2[1]+5, pts_y2[1]+5, 'B')
text(pts_x2[2], pts_y2[2]+7, 'C')
text(pts_x2[3], pts_y2[3]+8, 'D')
xlabel('x')
ylabel('y')

ax = fig.add_subplot(325)
xx = np.linspace(0,128,128)
plot(xx, mag[:,mid_y])
# ylabel('magnitude of velocity in y = L/2')
xlabel('x direction')
title('coupe suivant AB ')
mean_x = np.mean(mag[:,mid_y])	 # moyenne dans la direction x en y = 112 
plot(xx, mean_x * np.ones(128))

ax = fig.add_subplot(326)
yy = np.linspace(0,224,224)	
plot(yy,mag[mid_x,:])
# ylabel('magnitude of velocity in x = l/2')
xlabel('y direction')
title('coupe suivant CD')
mean_y = np.mean(mag[mid_x,:]) 	 # moyenne dans la direction y en x = 64
plot(yy,mean_y * np.ones(224))


mean = np.mean(mag)				 # moyenne dans l'ellipse 
print(mean_x, mean_y,mean)

# draw()
# pause(0.5)
# clf()	

# # plt.cla()
# # draw()
# show()

show()

figure()
for k in range(0,160):
	Vmag0 = data[t][0][k]
	Vmag1 = data[t][1][k]
	Vmag2 = data[t][2][k]

	for i in range(0,128):
		for j in range(0,224):
			mag[i,j] = math.sqrt(Vmag0[i,j]**2 + Vmag1[i,j]**2 + Vmag2[i,j]**2)

	contourf(x,y,mag,50,cmap=cm.coolwarm)
	plot(pts_x,pts_y, 'r*')
	plot(pts_x2,pts_y2, 'k*')
	title('coupe ' + str(k))
	pause(0.01)
	draw()


