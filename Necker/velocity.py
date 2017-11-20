import numpy as np
from matplotlib import cm
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D

data=np.load('velocity-download-595f881f278f6a562e020a3d-678dd80d2456e8ab.npy')

N=20
v = np.zeros((N,3))

for i in range(0,N):
	v[i,:] = data[i,:,5,5,10] # for one position, 3D velocity vector for each time 

Nn=160
w = np.zeros((Nn,3))
for j in range(0,Nn):
	w[j,:] = data[10, :, j,5,10] # 3D velocity vector for each slice (depth)

Nnn = 128
x = np.zeros((Nnn,3))

for k in range(0,Nnn):
	x[k,:] = data[10, :, 5,k,10] # 3D velocity vector for each image row (height)

NNNN = 224
y = np.zeros((NNNN,3))
for k in range(0,NNNN):
	y[k,:] = data[10, :, 5,5,k] # 3D velocity vector for each image column (width)

# plt.plot(data[10,0,80, :,:])

U =data[10, 0,80,64,:]

V =data[10, 1,80,64,:]

W = data[10, 2,80,64,:]

plt.plot(V)

# fig = plt.figure()

# ax = fig.gca(projection='3d')

# ax = fig.add_subplot(111, projection='3d')
# ax.scatter(U,V,W,c='r', marker= 'o')
# ax.plot_trisurf(U,V,W,cmap=cm.coolwarm, linewidth=0, antialiased=False)
# Axes3D.scatter(data[10,0,:,10,10], data[10,1,:,10,10], data[10,2,:,10,10], zdir='z', s=20, c=None, depthshade=True, *args=None,**kwargs=None)

plt.show()