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

	x = np.linspace(0,224,224) # RL
	y = np.linspace(0,128,128) # AP
	z = np.linspace(0,160,160) # IS 

	y,z = np.meshgrid(y,z)

	y=np.transpose(y)
	z=np.transpose(z)

	mag= np.zeros((160,128))

	mean_d = np.zeros(20)
	mean_f = np.zeros(20)

	D1 = np.array([RLp(33.48), APp(-18.79), ISp(101.11)])
	D2 = np.array([RLp(33.48), APp(-15.65), ISp(114.15)])

	F1 = np.array([RLp(33.48), APp(4.73), ISp(42.71)])
	F2 = np.array([RLp(33.48), APp(17.28), ISp(42.71)])

	for t in range(0,20):
		# t=10

		Vmag0 = data[t][0]
		Vmag1 = data[t][1]
		Vmag2 = data[t][2]

		V0 = Vmag0[:,:,121]
		V1 = Vmag1[:,:,121]
		V2 = Vmag2[:,:,121]

		for i in range(0,160):
			for j in range(0,128): 
				mag[i,j] = math.sqrt(V0[i,j]**2 + V1[i,j]**2 + V2[i,j]**2)
		
		mean_d[t] = np.mean(mag[F1[1]:F2[1], F1[2]])
		mean_f[t] = np.mean(mag[D1[1], D1[2]:D2[2]])

		# plot(mag[F1[1]:F2[1], F1[2]])
		# plot(mag[D1[1], D1[2]:D2[2]])

	md = np.mean(mean_d)
	mf = np.mean(mean_f)
	plot(np.linspace(0,0.98,20),mean_d,'r', label= 'entrée')
	plot(np.linspace(0,0.98,20),mean_f,'k', label= 'sortie')

	xlabel('t')
	ylabel('Umoy')
	title('Moyenne de la magnitude de la vitesse en fonction du temps')
	legend()

	plot(np.linspace(0,0.98,20),md*np.ones(20), 'r--', label = 'moyenne entrée')
	plot(np.linspace(0,0.98,20),mf*np.ones(20), 'k--', label = 'moyenne sortie')
	
	# Te = 6.97*2*0.98/20
	# tt =  np.linspace(0,0.98,1000)
	# figure()
	# a = 70+ 589*np.sin(2*np.pi/Te * tt)* (tt<Te/2)
	# plot( tt, a)

	# Ts = Te
	# b = 176+246* np.sin(2*np.pi/Ts * tt)* (tt<Ts/2)

	# plot(tt,b)
	# figure()

	# mag = transpose(mag)

	# CS = contourf(y,z,mag,50,cmap=cm.coolwarm)

	# title('coupe AP/IS')
	# xlabel('AP')
	# ylabel('IS')

	# plot(D1[1], D1[2], 'r*')
	# plot(D2[1], D2[2], 'r*')

	# plot(F1[1], F1[2], 'r*')
	# plot(F2[1], F2[2], 'r*')


	# Vv0 = Vmag0[ISp(42.71), : ,: ]
	# Vv1 = Vmag1[ISp(42.71), : ,: ]
	# Vv2 = Vmag2[ISp(42.71), : ,: ]

	# y = np.linspace(0,128,128)

	# x,y = np.meshgrid(x,y)
	# mag = np.zeros((128,224))

	# for i in range(0,128):
	# 		for j in range(0,224): 
	# 			mag[i,j] = math.sqrt(Vv0[i,j]**2 + Vv1[i,j]**2 + Vv2[i,j]**2)

	# figure()
	# contourf(x,y,mag, 100,cmap=cm.coolwarm)
	# plot(F1[0], F1[1], 'r*')
	# plot(F2[0], F2[1], 'r*')
	# title('coupe RL/AP')
	# xlabel('RL')
	# ylabel('AP')

	# figure ()

	# Vv0 = Vmag0[:,61 ,: ]
	# Vv1 = Vmag1[:,61 ,: ]
	# Vv2 = Vmag2[:,61 ,: ]

	# mag = np.zeros((160,224))

	# for i in range(0,160):
	# 	for j in range(0,224):
	# 		mag[i,j] = math.sqrt(Vv0[i,j]**2 + Vv1[i,j]**2 + Vv2[i,j]**2)

	# x = np.linspace(0,224,224) # RL
	# y = np.linspace(0,128,128) # AP
	# z = np.linspace(0,160,160) # IS 			

	# x,z = np.meshgrid(x,z)

	# contourf(z,x,mag, 100,cmap=cm.coolwarm)
	# plot(D1[2], D1[0], 'r*')
	# plot(D2[2], D2[0], 'r*')
	# title('coupe RL/IS')
	# ylabel('RL')
	# xlabel('IS')

	show()