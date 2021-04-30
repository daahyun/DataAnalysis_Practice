import numpy as np
import math
import matplotlib.pyplot as plt
J = 5
n_iter = 2000
dt = 0.1

F0 = 1000
cf = [1, 2, 3]
n = len(cf)
colors = np.random.rand(n)
# phase of contours
ini_ph = np.random.rand(n,1) - 0.5
# Generate random vectors
r = np.random.rand(n,2) - 0.5
ini_r = r

iter = 1

plt.figure()
plt.scatter(ini_r[:,0],ini_r[:,1],c=colors)
while iter<n_iter:
    # Update vectors
    for i in range(n):
        att_force = r[i]*0
        repul_force = r[i]*0

        for j in range(n):
            if j != i:
                del_ph = F0*(cf[j] - cf[i])*(2*math.pi) + (ini_ph[j] - ini_ph[i])
                vec_ij = r[j] - r[i]
                norm_vec_ij = np.linalg.norm(vec_ij)

                att_force = att_force + (vec_ij/norm_vec_ij)*(1+J*np.cos(del_ph))
                repul_force = repul_force + (vec_ij/(norm_vec_ij*norm_vec_ij))

        r[i] = r[i] + (att_force-repul_force)/n*dt

    iter = iter+1
print(r)
plt.scatter(r[:,0],r[:,1],c=colors)
plt.show()

