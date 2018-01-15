import numpy as np
import matplotlib.pyplot as plt

T_c = 0.62
tt = np.linspace(0,12*T_c,5000)

# Q = np.sin(2*np.pi/T_c*tt)
# print(T_c)
# Q_Input = (np.maximum(0, np.sin(2*np.pi* tt/(0.8*T_c) ))*(tt < 0.8*T_c)
# 	 + np.maximum(0, np.sin(2*np.pi* tt/(0.8*T_c)+2*np.pi/T_c))*(tt<2*0.85*T_c)*(tt>0.8*T_c)
	# + np.maximum(0, np.sin(2*np.pi* tt/(0.8*T_c)+ 4*np.pi/T_c))*(tt<3*T_c)*(tt>2*T_c)
	# + np.maximum(0, np.sin(2*np.pi* tt/(0.8*T_c)+ 6*np.pi/T_c))*(tt<4*0.97*T_c)*(tt>3*T_c)
	# + np.maximum(0, np.sin(2*np.pi* tt/(0.8*T_c)+ 8*np.pi/T_c))*(tt<5*T_c)*(tt>4*1.1*T_c)
	# + np.maximum(0, np.sin(2*np.pi* tt/(0.8*T_c)+ 10*np.pi/T_c))*(tt<6*T_c)*(tt>5*1.1*T_c)
	# + np.maximum(0, np.sin(2*np.pi* tt/(0.8*T_c)+ 12*np.pi/T_c))*(tt<7*1.05*T_c)*(tt>6*1.1*T_c)
	# + np.maximum(0, np.sin(2*np.pi* tt/(0.8*T_c)+ 14*np.pi/T_c))*(tt<8*1.05*T_c)*(tt>7*1.1*T_c)
	# + np.maximum(0, np.sin(2*np.pi* tt/(0.8*T_c)+ 16*np.pi/T_c))*(tt<9*1.05*T_c)*(tt>8*1.1*T_c)
	# + np.maximum(0, np.sin(2*np.pi* tt/(0.8*T_c)+ 18*np.pi/T_c))*(tt<10*1.05*T_c)*(tt>9*1.1*T_c)
	# + np.maximum(0, np.sin(2*np.pi* tt/(0.8*T_c)+ 20*np.pi/T_c))*(tt<11*1.05*T_c)*(tt>10*1.1*T_c)
	# + np.maximum(0, np.sin(2*np.pi* tt/(0.8*T_c)+ 22*np.pi/T_c))*(tt<12*1.08*T_c)*(tt>11*1.1*T_c)
 	# )
# B = np.maximum(0, np.sin(2*np.pi* tt/(0.8*T_c)-6.2831853071795862))*(tt>=T_c)


# plt.plot(tt, B)
# plt.plot(tt, Q)
# T_c = 0.57
# tt = np.linspace(0,12*T_c,5000)

# Q = np.sin(2*np.pi/T_c*tt)
# Q_Input = ( np.maximum(0, np.sin(2*np.pi* tt/(0.8*T_c) ))*(tt <= 0.8*T_c)
# + np.maximum(0, np.sin(2*np.pi* tt/(0.8*T_c)+ 2*np.pi/T_c))*(tt<2*0.85*T_c)*(tt>0.8*T_c)
# + np.maximum(0, np.sin(2*np.pi* tt/(0.8*T_c)+ 4*np.pi/T_c))*(tt<3*0.9*T_c)*(tt>2*0.8*T_c)
# + np.maximum(0, np.sin(2*np.pi* tt/(0.8*T_c)+ 6*np.pi/T_c))*(tt<4*0.9*T_c)*(tt>3*0.9*T_c)
# + np.maximum(0, np.sin(2*np.pi* tt/(0.8*T_c)+ 8*np.pi/T_c))*(tt<5*0.9*T_c)*(tt>4*0.92*T_c)
# + np.maximum(0, np.sin(2*np.pi* tt/(0.8*T_c)+ 10*np.pi/T_c))*(tt<6*0.9*T_c)*(tt>5*0.92*T_c)
# + np.maximum(0, np.sin(2*np.pi* tt/(0.8*T_c)+ 12*np.pi/T_c))*(tt<7*0.92*T_c)*(tt>6*0.93*T_c)
# + np.maximum(0, np.sin(2*np.pi* tt/(0.8*T_c)+ 14*np.pi/T_c))*(tt<8*0.95*T_c)*(tt>7*0.94*T_c)
# + np.maximum(0, np.sin(2*np.pi* tt/(0.8*T_c)+ 16*np.pi/T_c))*(tt<9*0.97*T_c)*(tt>8*0.95*T_c)
# + np.maximum(0, np.sin(2*np.pi* tt/(0.8*T_c)+ 18*np.pi/T_c))*(tt<10*0.97*T_c)*(tt>9*0.97*T_c)
# + np.maximum(0, np.sin(2*np.pi* tt/(0.8*T_c)+ 20*np.pi/T_c))*(tt<11*0.97*T_c)*(tt>10*0.97*T_c)
# + np.maximum(0, np.sin(2*np.pi* tt/(0.8*T_c)+ 22*np.pi/T_c))*(tt<12*0.98*T_c)*(tt>11*0.97*T_c)
# )

def Q(t,alpha):
	return np.sin(np.pi * t/alpha)*(t<alpha)

# plt.plot(tt,Q)

Qq = np.zeros(5000)
for i in range(0,5000):
	Qq[i] = Q(tt[i]/T_c - int(tt[i]/T_c),0.4)

plt.plot(tt, Qq,'.')
# plt.plot(tt,Q)

plt.show()