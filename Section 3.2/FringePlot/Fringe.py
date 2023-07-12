import numpy as np
import matplotlib.pyplot as plt

# read data
data1 = np.genfromtxt(r"Fringe1.txt", skip_header=3)
data2 = np.genfromtxt(r"Fringe2.txt", skip_header=3)
data3 = np.genfromtxt(r"Fringe3.txt", skip_header=3)
data4 = np.genfromtxt(r"Fringe4.txt", skip_header=3)

# plot data
plt.plot(data1[:,0], data1[:,1], label="x = 0 mm, y = 0 mm")
plt.plot(data1[:,0], data2[:,1], label="x = 45 mm, y = 0 mm")
plt.plot(data1[:,0], data3[:,1], label="x = 0 mm, y = 13.5 mm")
plt.plot(data1[:,0], data4[:,1], label="x = 45 mm, y = 13.5 mm")

# visual aid
plt.axvline(x=-75, color="black")
plt.axvline(x=75, color="black")

# show plot
plt.xlabel("z position [mm]")
plt.ylabel("Potential [V]")
plt.legend()
plt.show()