'''Back of the Envelope estimate of a potential given a rectangular boundary.
The code is written to be read as briefly as possible and to be easy to alter.
'''
import numpy as np
import matplotlib.pyplot as plt

Nx, Ny = 60, 200 # Meshgrid resolution
Vu, Vd, Vs = 1000, 0, -2000 # Dirichlet Electrodes

# Meshgrid, ambiguity at corners do not matter as they're ignored by the algorithm
Potinit = np.zeros((Nx, Ny))
Potinit[0, :], Potinit[-1, :] = Vu, Vd
Potinit[:, 0], Potinit[:, -1] = Vs, Vs
plt.imshow(Potinit)
plt.colorbar()
plt.show()
Pot = np.array(Potinit)

# the more runs the better, the reader can decide on a more sophisticated conditions themselves
Runs = 100
for n in range(Runs):
    PotBuffer = np.array(Potinit)
    for i in range(1, Nx-1):
        for j in range(1, Ny-1):
            PotBuffer[i, j] = (Pot[i-1, j]+Pot[i+1, j]+Pot[i, j-1]+Pot[i, j+1])/4
    Pot = PotBuffer

plt.imshow(Pot)
plt.colorbar()
plt.show()