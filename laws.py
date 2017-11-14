import numpy as np 
import matplotlib.pyplot as plt


l1 = np.linspace(1,5, 500)

S1 = (l1-1);
S2 = (l1 - 1/l1);
S3 = (l1**2 - 1/l1**2)/2;

plt.plot(l1,S1,label='Elastic: $\sigma_1 = 2 \mu (\lambda_1 -1)$')
plt.plot(l1,S2, label='Varga: $\sigma_1 = 2 \mu (\lambda_1 - \lambda_1^{-1}$')
plt.plot(l1,S3,label = 'Neo-Hooke: $\sigma_1 = \mu (\lambda_1^2 - \lambda_1^{-2})$'  )
plt.legend()
plt.xlabel("$\lambda_1$")
plt.ylabel("$\sigma$")
plt.axis([1,5, 0,10])
plt.savefig('sigma.eps')
A = np.linspace(1.,10, 500)

# plt.figure()
# p1 = (np.sqrt(A)-1)
# p2 = 1/np.sqrt(A) - 1/(A*np.sqrt(A))
# p3 = 1/2 - 1/A**2/2


# plt.plot(A, p1, label ="Elastic")

# plt.plot(A, p2,label = "Varga")

# plt.plot(A, p3,label="Neo-Hooke")
# plt.axis([1,10, 0,1])
# plt.xlabel('Area')
# plt.ylabel('Pressure')
# plt.legend()
# plt.savefig('p_A.eps')
plt.show()