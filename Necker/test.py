#example.py
import numpy as np
import math
from pylab import *
from mpl_toolkits.mplot3d import Axes3D
import imageio

# conversion mm --> pix
def RLp(x): 
	return int((204.78 + x) * 224/440) 
def APp(x): 
	return int((186.87 + x) * 128/352)
def ISp(x):
	return int((26.38 + x) * 160/208)

# conversion pix --> mm 
def RLm(x): 
	return -204.78 + x * 440/224
def APm(x):
	return -186.87 + x * 352/128
def ISm(x):
	return -26.38 + x * 208/160

if __name__ == '__main__':
	data = np.load("velocity-download-595f881f278f6a562e020a3d-678dd80d2456e8ab.npy")

	x = np.linspace(0,128,128)
	y = np.linspace(0,160,160)

	x,y = np.meshgrid(x,y)

	x=np.transpose(x)
	y=np.transpose(y)

	mag= np.zeros((160,128))

	t=10

	Vmag0 = data[t][0]
	Vmag1 = data[t][1]
	Vmag2 = data[t][2]

	V0 = Vmag0[:,:,121]
	V1 = Vmag1[:,:,121]
	V2 = Vmag2[:,:,121]

	for i in range(0,160):
		for j in range(0,128): 
			mag[i,j] = math.sqrt(V0[i,j]**2 + V1[i,j]**2 + V2[i,j]**2)

	mag = transpose(mag)

	CS = contourf(x,y,mag,50,cmap=cm.coolwarm)

	D1 = np.array([RLp(33.48), APp(-18.79), ISp(101.11)])
	D2 = np.array([RLp(33.48), APp(-15.65), ISp(114.15)])

	F1 = np.array([RLp(33.48), APp(4.73), ISp(42.71)])
	F2 = np.array([RLp(33.48), APp(17.28), ISp(42.71)])

	plot(D1[1], D1[2], 'r*')
	plot(D2[1], D2[2], 'r*')

	plot(F1[1], F1[2], 'r*')
	plot(F2[1], F2[2], 'r*')

	figure()

	plot(mag[F1[1]:F2[1], F1[2]])
	plot(mag[D1[1], D1[2]:D2[2]])


	show()