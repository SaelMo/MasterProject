'''Back of the Envelope estimate of a potential given a rectangular boundary.
The code is written to be read as briefly as possible and to be easy to alter.
'''

import numpy as np
import matplotlib.pyplot as plt

Nx, Ny = 30*5, 120*5 # Meshgrid resolution
Vu, Vd, Vs = 1000, 0, -500 # Dirichlet Electrodes

# Meshgrid ambiguity at corners do not matter as they do not factor into the algorithm 
Potinit = (Vu+Vd+2*Vs)/4*np.ones((Nx, Ny)) # Initiate with mean of boundaries for faster convergence
Potinit[0, :], Potinit[-1, :] = Vu, Vd
Potinit[:, 0], Potinit[:, -1] = Vs, Vs
Pot = np.array(Potinit)

# The more runs the better although a convergence condition would be better
Runs = 5000
for n in range(Runs):
    PotBuffer = np.array(Potinit)
    
    # For every point on the interior the average of the nearest neighbours is taken
    PotBuffer[1:Nx-1,1:Ny-1] = ((np.roll(Pot, 1, axis = 1)+np.roll(Pot, -1, axis = 1) + 
    np.roll(Pot, 1, axis = 0)+np.roll(Pot, -1, axis = 0))/4)[1:Nx-1,1:Ny-1]
    Pot = PotBuffer

plt.imshow(Potinit)
plt.colorbar()
plt.show()
plt.imshow(Pot, interpolation='nearest', extent=[-6, 6, -1.5, 1.5])
cbar = plt.colorbar()
cbar.set_label('Potential [V]', rotation=270)
plt.xlabel("x [cm]")
plt.ylabel("y [cm]")
plt.show()
plt.plot(Pot[int(Nx/2),:])
plt.show()