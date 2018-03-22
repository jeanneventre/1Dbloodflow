import numpy as np

L = np.array( [ 4.0, 72.5, 2.0, 38.5, 3.9, 69.1, 34.5, 96.9, 96.9 ] ) # cm
R = np.array( [ 1.5, 0.5, 1.3, 0.4, 1.2, 0.4, 0.8, 0.5, 0.5] ) # cm
 
mu = 5e-2 # g cm^-1 s^-2 == 0.1 * Pa.s == 0.1* kg m^-1 s^-2 
rho = 1

R1    = 8 * mu * L[0] /(np.pi * R[0]**4)  # g cm^-4 s^-1 
R2    = 8 * mu * L[1] /(np.pi * R[1]**4) + 5.28e3
R3    = 8 * mu * L[2] /(np.pi * R[2]**4)
R4    = 8 * mu * L[3] /(np.pi * R[3]**4) + 5e3
R5    = 8 * mu * L[4] /(np.pi * R[4]**4)
R6    = 8 * mu * L[5] /(np.pi * R[5]**4) + 5.28e3
R7    = 8 * mu * L[6] /(np.pi * R[6]**4)
R8    = 8 * mu * L[7] /(np.pi * R[7]**4) + 5.18e3
R9    = 8 * mu * L[8] /(np.pi * R[8]**4) + 5.18e3

# print(R1,R2,R3,R4,R5,R6,R7,R8)

R = np.array([R1,R2,R3,R4,R5,R6,R7,R8])
print(R)
r1 = 1/(1/R8 + 1/R9)
r2 = R7 + r1
r3 = 1/(1/r2 + 1/R6)
r4 = R5 + r3
r5 = 1/(1/R4 + 1/r4)
r6 = R3 + r5
r7 = 1/(1/r6 + 1/R2)
r8 = R1 + r7

r8 =  r8 #* 0.0075006375541921
print(r8)

r1 = R5 + R6
r2 = 1/(1/R4 + 1/r1)
r3 = r2 + R3
r4 = 1/(1/R2 + 1/r3)
r5 = R1 + r4

r5 = r5 #* 0.0075006375541921

print(r5)
print(r8/r5)

# print('Pmoy avant', 89 * r8)
# print('Pmoy après', 89 * r5)