from windkessel import * 

def cost(x,Pexp,Qinput, dt,timeSteps):

	Pnum = np.zeros(timeSteps)
	Pnum[0] = Pexp[0]
	for i in range(0,timeSteps - 1): 
		Pnum[i+1] = Pnum[i] + dt / (x[1]*x[2]) * ( (x[0]+x[1]) * Qinput[i] - Pnum[i] + x[0]*x[1]*x[2]/ dt * (Qinput[i+1] - Qinput[i])) 

	return np.sqrt(integrate.trapz((Pexp - Pnum)**2, dx=dt))

def data(direc,nArt,pName):
	liX         = []
	liY         = []
	lFileSep    = []
	lFile       = []
	os.chdir(direc)
	liX.append(0)
	liY.append([1,2,3])
	lFileSep.append(",")
	lFile.append("Artery_" + str(round(nArt)) + "_t_" + pName + ".csv")
	nplot = len(lFile)
	for j in range(0,nplot):
		P = np.genfromtxt(lFile[j], delimiter = str(lFileSep[j]))
	return P

def main(argv):

	HOME      = "/home/ventre/Documents/Boulot/Thèse/"
	PATH1D    = "code/bloodflow/bloodflow/Examples/"
	Clamping  = "Clamping/9Arteries-Saito/Test/Resistance/"
	State     = "PostClamp/"
	Fig       = "Newtonian/jS/nuv=5e4/Nx=10/xOrder=2/dt=1e-4/tOrder=2/KIN_HAT/HRQ/Figures"

	direc = HOME + PATH1D + Clamping + State + Fig 
	nArt = 0
	S = 'post'

	Arg     = "Argentine/"
	Code    = "Codes/"
	Data    = "Patient2015/Data/"
	Res     = "Resultats"
	Fig     = "Figures"

	direc_fig = HOME + Arg + Code + Fig + "/1D"
	direc_res = HOME + Arg + Code + Res + "/1D"
	
	x0 = x_init('1D_' + S, nArt) 
	pName = 'P'
	Data = data(direc,nArt,pName)

	T_c = 0.62
	ts = 9 * T_c
	te = 10 * T_c
	t = np.linspace(0,te,len(Data))
	t = t-ts
	dt = t[10]-t[9]
	length = 1
	Pexp = Data[:,length]
	timeSteps = int(len(Pexp)/(te/T_c))


	Pexp = Pexp[int(timeSteps*(ts/T_c)):int(timeSteps*(te/T_c))]
	tt = t[int(timeSteps*(ts/T_c)):int(timeSteps*(te/T_c))]
	xQ = x0[1:3]

	# Qinput = Q_entree(xQ,t+ts,T_c)
	# Qinput = Qinput[int(timeSteps*(ts/T_c)):int(timeSteps*(te/T_c))]


	pName = 'Q'
	Q = data(direc,nArt,pName)
	Qin = Q[:,length]
	Qinput = Qin[int(timeSteps*(ts/T_c)):int(timeSteps*(te/T_c))]
	plot(tt,Qinput)
	figure()

	V_c = Stroke_vol(Qinput,tt)	

	x0 = np.delete(x0,0) 
	xinit = x0[2:5]
	j0 = cost(xinit,Pexp,Qinput,dt,timeSteps)

	xx = optimisation(cost,xinit,Pexp,Qinput,dt,timeSteps)
	jf = cost(xx,Pexp,Qinput,dt,timeSteps)

	Pnum = res_ode(xx,Pexp,Qinput,dt,timeSteps)

	ecriture_P(Pnum,'1D_' + S,nArt,direc_res)
	ecriture_res('1D_' + S,nArt,direc_res,x0,xx,j0,jf,V_c)

	Pnum = lecture_P('1D_' + S,nArt,direc_res)

	n = 2
	titre = 'Artery'

	plot(tt[0:timeSteps:n],Pa_to_mmHg(CGS_to_Pa(Pnum[0:timeSteps:n])),'k^-',ms=7, lw=1, label = 'windkessel model')
	plot(tt,Pa_to_mmHg(CGS_to_Pa(Pexp)),'r',label = '1D numerical simulation', lw = 2)
	xlabel('Time (s)', fontsize = 12)
	ylabel('Pressure (mmHg)', fontsize=12)
	title('Fitting of the pressure wave against time for post clamp', fontsize=14)
	legend(fontsize=12,loc='upper right')
	savefig('postclamp0.eps')
	show()

	# affichage(Pexp,Pnum,tt,tt,timeSteps,titre, '1D ' + S ,nArt,n)
	# show()
	# enregistrement_fig(Pexp,Pnum,tt,tt,timeSteps,titre,'_1D' + S ,nArt,n,direc_fig)

	# pts = np.zeros(len(T_c)+1, dtype = int)
	# pts[1]= T_c[0]*100
	# for i in range(1,len(T_c)+1):
	# 	pts[i] = pts[i-1] + T_c[i-1] *100

	# 	# T = np.array([0.725,1.895,3.24,4.63,5.99,7.39,8.79,10.147,11.5,12.95,14.33,15.74,17.23,18.7,20])


if __name__ == "__main__":
	main(sys.argv[1:])

