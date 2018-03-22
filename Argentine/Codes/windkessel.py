import sys, getopt
import os
from scipy import integrate,optimize
import numpy    as np
import math     as mt
from pylab import *

def Q(t,alpha):
	return np.sin(np.pi * t/alpha)*(t<alpha)

def mmHg_to_Pa(P):
	return P * 133.322
def Pa_to_mmHg(P):
	return P * 0.0075006375541921
def  CGS_to_Pa(P):
	return 0.1*P
def Pa_to_CGS(P):
	return 10 * P

def J(x,Pexp,Qinput, dt,timeSteps):
	Pnum = np.zeros(timeSteps)
	Pnum[0] = Pexp[0]

	# Qinput = np.zeros(timeSteps)
	# for i in range(0,timeSteps):
	# 	Qinput[i] = x[3] * Q(t[i]/T_c - int(t[i]/T_c),x[4])

	for i in range(0,timeSteps - 1): 
		Pnum[i+1] = Pnum[i] + dt / (x[1]*x[2]) * ( (x[0]+x[1]) * Qinput[i] - Pnum[i] + x[0]*x[1]*x[2]/ dt * (Qinput[i+1] - Qinput[i])) 

	return np.sqrt(integrate.trapz((Pexp[0:len(Pexp)]-Pnum[0:timeSteps:10])**2,dx=dt))

def J_T(x,Pexp,Q0,t,T_c, dt,timeSteps):
	Qinput = np.zeros(timeSteps)

	for i in range(0,timeSteps):
		Qinput[i] = Q0 * Q(t[i]/T_c - int(t[i]/T_c),x[3])

	Pnum = np.zeros(timeSteps)
	Pnum[0] = Pexp[0]

	for i in range(0,timeSteps - 1): 
		Pnum[i+1] = Pnum[i] + dt / (x[1]*x[2]) * ( (x[0]+x[1]) * Qinput[i] - Pnum[i] + x[0]*x[1]*x[2]/ dt * (Qinput[i+1] - Qinput[i])) 

	# return np.sqrt(integrate.trapz((Pexp[0:len(Pexp)]-Pnum[0:timeSteps:10])**2,dx=dt))
	return np.sqrt(integrate.trapz((Pexp[0:len(Pexp)]-Pnum[0:timeSteps])**2,dx=dt))

def x_init(State, nPatient):
	liX         = []
	liY         = []
	lFileSep    = []
	lFile       = []
	liX.append(0)
	liY.append([1,2,3,4,5,6])
	lFileSep.append(",")
	lFile.append('x0_' + State + '.csv')
	nplot = len(lFile)
	for j in range(0,nplot):
		xentry = np.genfromtxt(lFile[j], delimiter = str(lFileSep[j]))
	x0 = np.zeros(6)
	for i in range(0,len(xentry)):
		if xentry[i,0] == nPatient :
			x0[:] = xentry[i,:]
	return x0

def data(direc,nArt):
	liX         = []
	liY         = []
	lFileSep    = []
	lFile       = []
	os.chdir(direc)
	liX.append(0)
	liY.append([1,2,3])
	lFileSep.append(",")
	lFile.append("Artery_" + str(round(nArt)) + "_t_P.csv")
	nplot = len(lFile)
	for j in range(0,nplot):
		P = np.genfromtxt(lFile[j], delimiter = str(lFileSep[j]))
	return P

def donnees_tot(State,nPatient, direc):
	liX         = []
	liY         = []
	lFileSep    = []
	lFile       = []
	os.chdir(direc)
	liX.append(1)
	liY.append([1,2,3,4,5,6,7])
	lFileSep.append(" ")
	lFile.append('all_' + str(nPatient) + "aorta_" + State + ".txt")
	nplot = len(lFile)
	for j in range(0,nplot):
		Pexp = np.genfromtxt(lFile[j], delimiter = str(lFileSep[j]))
	return Pexp

def donnees(State,nPatient, direc):
	liX         = []
	liY         = []
	lFileSep    = []
	lFile       = []
	os.chdir(direc)
	liX.append(1)
	liY.append([1,2,3,4,5,6,7])
	lFileSep.append(" ")
	lFile.append(str(nPatient) + "aorta_" + State + ".txt")
	nplot = len(lFile)
	for j in range(0,nplot):
		Pexp = np.genfromtxt(lFile[j], delimiter = str(lFileSep[j]))
	return Pexp

def Q_entree(x0,t,T_c):
	Q0 = x0[0]
	Tej = x0[1]
	Qinput = np.zeros(len(t))
	for i in range(0,int(len(t))):
		Qinput[i] = Q0 * Q(t[i]/T_c - int(t[i]/T_c),Tej)
	return Qinput

def Stroke_vol(Qinput, t):
	return integrate.simps(Qinput,t)

def optimisation(f,xinit,Pexp,Qinput,dt,timeSteps):
	minimizer_kwargs = {"args" : (Pexp,Qinput,dt,timeSteps), "bounds" : ((1e-8,None),(1e-8,None),(1e-6,1e-2)),"method": "L-BFGS-B"}
	b = optimize.basinhopping(f, xinit, minimizer_kwargs=minimizer_kwargs,niter=500,disp=True,niter_success = 20)
	xx = b.x 
	res = b.fun
	print('----> J initial   :',f(xinit,Pexp,Qinput,dt,timeSteps))
	print('----> J final     :',f(xx,Pexp,Qinput,dt,timeSteps))
	print('paramètres :',xx)
	return xx

def optimisation_T(f,xinit,Pexp,Q0,t,T_c,dt,timeSteps):
	minimizer_kwargs = {"args" : (Pexp,Q0,t,T_c,dt,timeSteps), "bounds" : ((1e-8,None),(1e-8,None),(1e-6,1e-2),(1e-8,1)),"method": "L-BFGS-B"}
	b = optimize.basinhopping(f, xinit, minimizer_kwargs=minimizer_kwargs,niter=500,disp=True,niter_success = 20)
	xx = b.x 
	res = b.fun
	print('----> J initial   :',f(xinit,Pexp,Q0,t,T_c,dt,timeSteps))
	print('----> J final     :',f(xx,Pexp,Q0,t,T_c,dt,timeSteps))
	print('paramètres :',xx)
	return xx

def res_ode(xx,Pexp,Qinput,dt,timeSteps):
	Pnum = np.zeros(timeSteps)
	Pnum[0] = Pexp[0]
	for i in range(0,timeSteps - 1): 
		Pnum[i+1] = Pnum[i] + dt / (xx[1]*xx[2]) * ( (xx[0]+xx[1]) * Qinput[i] - Pnum[i] + xx[0]*xx[1]*xx[2]/ dt * (Qinput[i+1] - Qinput[i])) 
	return Pnum

def ecriture_res_tot(State,nPatient,direc,xx):
	os.chdir(direc)
	fileName = 'all_' + State + 'clamp' + str(nPatient) + '.csv'
	fh = open(fileName, 'w')
	for i in range(xx.shape[0]):
		for j in range(xx.shape[1]):
			fh.write("%.20f, \t"%(xx[i,j]))
		fh.write("\n")

def ecriture_res(State,nPatient,direc,x0,xx,j0,jf,V_c):
	os.chdir(direc)
	fileName = State + 'clamp' + str(nPatient) + '.csv'
	fh = open(fileName, 'w')

	fh.write("%d, \t"%(0))
	for i in range(0,len(x0)):
		fh.write("%.20f, \t"%(x0[i]))
	fh.write("%.20f, \t %.20f"%(j0,V_c))
	fh.write("\n")

	fh.write("%d, \t"%(1))
	if len(xx) == 3 :
		fh.write("%.20f , \t %.20f, \t"%(x0[0], x0[1]))
	elif (len(xx)==4):
		fh.write("%.20f , \t %.20f, \t"%(x0[0], xx[3]))
	for i in range(0,len(xx)-1):
		fh.write("%.20f, \t"%(xx[i]))
	fh.write("%.20f, \t %.20f"%(jf,V_c))

	# fh.write("%d, \t %d, \t %.20f, \t %.20f, \t %.20f, \t %.20f, \t %.20f, \t %.20f"%(0,x0[0],x0[1], x0[2], x0[3],x0[4],j0,V_c) + "\n")  
	# fh.write("%d, \t %d, \t %.20f, \t %.20f, \t %.20f, \t %.20f, \t %.20f, \t %.20f"%(1,x0[0],xx[3], xx[0], xx[1],xx[2],jf,V_c) + "\n") 

def ecriture_P(Pnum,State,nPatient,direc):
	os.chdir(direc)
	fileName = 'P_' + State + 'clamp' + str(nPatient) + '.csv' 
	fh = open(fileName, 'w')
	for i in range(len(Pnum)):
		fh.write("%.20f \n"%(Pnum[i]))

def lecture_P(State,nPatient,direc):
	os.chdir(direc)
	liX         = []
	liY         = []
	lFileSep    = []
	lFile       = []
	liX.append(1)
	liY.append([1,2,3,4,5,6,7])
	lFileSep.append(" ")
	lFile.append('P_' + State + 'clamp' + str(nPatient) + '.csv')
	nplot = len(lFile)
	for j in range(0,nplot):
		Pnum = np.genfromtxt(lFile[j], delimiter = str(lFileSep[j]))
	return  Pnum

def lecture_x(State,nPatient,direc):
	os.chdir(direc)
	liX         = []
	liY         = []
	lFileSep    = []
	lFile       = []
	liX.append(1)
	liY.append([1,2,3,4,5,6,7])
	lFileSep.append(",")
	lFile.append('T_' + State + 'clamp' + str(nPatient) + '.csv')
	nplot = len(lFile)
	for j in range(0,nplot):
		x = np.genfromtxt(lFile[j], delimiter = str(lFileSep[j]))
	x = np.delete(x,0,axis=0)
	return x

def lecture_x_tot(State,nPatient,direc):
	os.chdir(direc)
	liX         = []
	liY         = []
	lFileSep    = []
	lFile       = []
	liX.append(1)
	liY.append([1,2,3,4,5,6,7])
	lFileSep.append(",")
	lFile.append('all_' + State + 'clamp' + str(nPatient) + '.csv')
	nplot = len(lFile)
	for j in range(0,nplot):
		x = np.genfromtxt(lFile[j], delimiter = str(lFileSep[j]))
	return x


def affichage(Pexp,Pnum,t,tt,timeSteps,titre,State,nPatient,n):
	figure()
	# xlim([-0.05,1.4])
	# ylim([50,152])
	plot(t[0:timeSteps:n],Pa_to_mmHg(CGS_to_Pa(Pnum[0:timeSteps:n])),'r^-',ms=7, lw=1, label = 'numerical')
	plot(tt,Pa_to_mmHg(CGS_to_Pa(Pexp)),'k',label = 'experimental', lw = 2)
	xlabel('Time (s)', fontsize = 12)
	ylabel('Pressure (mmHg)', fontsize=12)
	title(titre + ' ' + str(nPatient) + ', ' + State + 'clamp', fontsize=14)
	legend(fontsize=12)


def enregistrement_fig(Pexp,Pnum,t,tt,timeSteps,titre,State,nPatient,n,direc): 
	affichage(Pexp,Pnum,t,tt,timeSteps,titre,State,nPatient,n)
	os.chdir(direc)
	savefig(str(nPatient) + State + 'clamp.eps')

def plot_phase(x1,x2,posx1,posx2,xx,Pexp,Q0,t,T_c,dt,timeSteps):
	mag = np.zeros((len(x1), len(x2)))
	for i in range(len(x1)):
		for j in range(len(x2)):
			xm = xx
			xm[int(posx1)] = x1[i]
			xm[int(posx2)] = x2[j]
			mag[i,j] = J_T(xm,Pexp,Q0,t,T_c,dt,timeSteps)
	figure()
	levels = np.linspace(mag.min(), mag.max(), 150)
	Cs = contourf(x2,x1,mag,levels,cmap = cm.RdBu,
				color = ('r', 'g', 'b'),
				origin = 'lower',
				extend = 'both')
	Cs.cmap.set_under('red')
	Cs.cmap.set_over('black')
	CS4 = contour(x2,x1,mag, [2930],
				colors=('k',),
				linewidths=(3,),
				origin='upper')
	clabel(CS4, fmt='%2.1f', colors='w', fontsize=14)
	xlabel('x2',fontsize=12)
	ylabel('x1',fontsize=12)
	legend()
	colorbar(Cs)

def main(argv):

	HOME    = "/home/ventre/"
	PATH    = "Documents/Boulot/Thèse/Argentine/"
	Code    = "Codes/"
	Data    = "Patient2015/Data/"
	Res     = "Resultats"
	Fig     = "Figures"

	direc_c = HOME + PATH + Code
	direc_fig = HOME + PATH + Code + Fig
	direc_res = HOME + PATH + Code + Res
	direc_data = HOME + PATH + Code + Data

	State 	= 'post'
	nPatient = 6

	# x0 = x_init(State, nPatient)
	# Pexp = donnees(State, nPatient, direc_data)
	
	# timeSteps = len(Pexp) *10 
	# T_c = len(Pexp)/100 
	# dt = 1/timeSteps
	# t = np.linspace(0,T_c,num=timeSteps) 
	# tt = np.linspace(0,T_c,num=len(Pexp))

	# Pexp = Pa_to_CGS(mmHg_to_Pa(Pexp))

	# ########################################################################################
	# #### estimation sans Tej (rapide)

	# # x0 = np.delete(x0,0)
	# # Qinput = Q_entree(x0,t,T_c,timeSteps)
	# # V_c = Stroke_vol(Qinput,t)

	# # xinit = x0[2:5]
	# # j0 = J(xinit,Pexp,Qinput,dt,timeSteps)

	# # xx = optimisation(J,xinit,Pexp,Qinput,dt,timeSteps)
	# # jf = J(xx,Pexp,Qinput,dt,timeSteps)

	# # Pnum = res_ode(xx,Pexp,Qinput,dt,timeSteps)
	
	# # ecriture_P(Pnum,State,nPatient,direc_res)
	# # ecriture_res(State,nPatient,direc_res,x0,xx,j0,jf)

	# # n = 20
	# # titre  = 'Patient'
	# # Pnum = lecture_P(State,nPatient,direc_res)
	# # affichage(Pexp,Pnum,t,tt,timeSteps,titre,State,nPatient,n)
	# # show()

	# # enregistrement_fig(Pexp,Pnum,t,tt,timeSteps,titre,State,nPatient,n,direc_fig)
	
	# ########################################################################################

	# #### estimation avec Tej (lent)

	# x0 = np.delete(x0,0) 
	# xinit = x0[2:5]
	# xinit = append(xinit,x0[1])

	# Q0 = x0[0]
	# # j0 = J_T(xinit, Pexp,Q0,t,T_c,dt,timeSteps)
	
	# # xx = optimisation_T(J_T,xinit,Pexp,Q0,t,T_c,dt,timeSteps)
	# # jf = J_T(xx,Pexp,Q0,t,T_c,dt,timeSteps)
	
	# # xQ = np.array([Q0,xx[3]])
	# # Qinput = Q_entree(xQ,t,T_c)
	# # V_c = Stroke_vol(Qinput,t)	

	# # Pnum = res_ode(xx,Pexp,Qinput,dt,timeSteps)

	# # ecriture_P(Pnum,'T_' + State,nPatient,direc_res)
	# # ecriture_res('T_' + State,nPatient,direc_res,x0,xx,j0,jf,V_c)

	# # Pnum = lecture_P('T_' + State,nPatient,direc_res)
	# # n = 20
	# # titre  = 'Patient'
	# # affichage(Pexp,Pnum,t,tt,timeSteps,titre,State,nPatient,n)
	# # show()
	# # enregistrement_fig(Pexp,Pnum,t,tt,timeSteps,titre,State,nPatient,n,direc_fig)
	
	# ########################################################################################

	# ### plot phase 

	# X = lecture_x(State,nPatient,direc_res)
	# xx =[X[0,3], X[0,4], X[0,5], X[0,2]]
	# R1 = np.linspace(0.5*xx[0],1.5*xx[0],100)
	# R2 = np.linspace(0.5*xx[1],1.5*xx[1],200)
	# C1 = np.linspace(0.5*xx[2],1.5*xx[2],200)
	# pos_R1 = 0
	# pos_R2 = 1
	# pos_C1 = 2

	# plot_phase(R2,C1,pos_R2,pos_C1,xx,Pexp,Q0,t,T_c,dt,timeSteps) 

	# # figure()

	# # m = np.zeros(len(C1))
	# # for i in range(len(C1)):
	# # 	xm = np.array([xx[0], xx[1], C1[i], xx[3]])
	# # 	m[i] = J_T(xm,Pexp,Q0,t,T_c, dt,timeSteps)

	# # plot(C1,m)
	# # plot(xx[2], J_T(xx,Pexp,Q0,t,T_c,dt,timeSteps),'r*')

	# show()

	########################################################################################

	P = donnees_tot(State, nPatient, direc_data)

	# T = np.array([0.57, 1.71,2.83,3.96,5.22,6.47,7.71,8.93, 10.11, 11.26,12.49,13.62,14.76,15.88,16.98,18.14,19.26])
	T = np.array([0.725,1.895,3.24,4.63,5.99,7.39,8.79,10.147,11.5,12.95,14.33,15.74,17.23,18.7,20])
	T_end = 20

	T_c = np.zeros(len(T))
	for i in range(1,len(T)):
		T_c[i] = T[i] - T[i-1]

	T_c = np.delete(T_c, 0)

	tt = np.linspace(0,T_end,num=len(P))

	P_s = P[72:2000]
	t_s = tt[72:2000]-T[0]
	# plot(P_s)

	# pts=np.array([0,114,226,339,465,590,714,836,954,1069,1191,1305,1419,1531,1642,1757,1868])
	pts=np.array([0,108,236,368,497,630,763,892,1021,1158,1289,1424,1565,1705,1828])
	# pts = np.zeros(len(T_c)+1, dtype = int)
	# pts[1]= T_c[0]*100
	# for i in range(1,len(T_c)+1):
	# 	pts[i] = pts[i-1] + T_c[i-1] *100
	# print(pts)
	xx = np.zeros((len(pts)-1, 4))

	# for i in range(0,len(pts)-1):
	# 	os.chdir(direc_c)
	# 	Pp = P_s[pts[i]:pts[i+1]]
	# 	t = linspace(0,T_c[i],num=pts[i+1]-pts[i])
	# 	dt = t[2] - t[1]
	# 	plot(t,Pp)
	# 	x0 = x_init(State, nPatient)
	# 	Pexp = Pa_to_CGS(mmHg_to_Pa(Pp))

	# 	x0 = np.delete(x0,0) 
	# 	xinit = x0[2:5]
	# 	xinit = append(xinit,x0[1])

	# 	Q0 = x0[0]
	# 	j0 = J_T(xinit,Pexp,Q0,t,T_c[i],dt,pts[i+1]-pts[i])
		
	# 	xx[i,:] = optimisation_T(J_T,xinit,Pexp,Q0,t,T_c[i],dt,pts[i+1]-pts[i])
	# 	jf = J_T(xx[i,:],Pexp,Q0,t,T_c[i],dt,pts[i+1]-pts[i])
		
	# 	xQ = np.array([Q0,xx[i,3]])
	# 	Qinput = Q_entree(xQ,t,T_c[i])
	# 	V_c = Stroke_vol(Qinput,t)	

	# 	Pnum = res_ode(xx[i,:],Pexp,Qinput,dt,pts[i+1]-pts[i])
	# 	# plot(t,Pnum)
	# 	# plot(t,Pexp)

	# ecriture_res_tot(State,nPatient,direc_res,xx)

	xx = lecture_x_tot(State,nPatient,direc_res)
	xx = np.delete(xx,4,axis=1)

	tau = xx[:,1]*xx[:,2]
	print(np.median(tau))

	show()
if __name__ == "__main__":
	main(sys.argv[1:])

