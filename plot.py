import numpy as np
import matplotlib.pyplot as plt
from read_write import quadrature_and_phase


#create Numpy arrays from binary files quadrature and phase 
Ex_mod, Ex_phase = quadrature_and_phase("./dados/realEx.datab", "./dados/imagEx.datab")

# create array x from -10000 to 10000 with spacing 250
x = np.arange(-10000, 10250, 250)

freq = []
for i in range(0, 4):
    freq += [np.log10(Ex_mod[i*81:(i+1)*81], dtype=np.float64)]

def cm_to_inche(value):
    return value/2.54

plt.style.use('default')

plt.figure(figsize=(cm_to_inche(26),cm_to_inche(13)))
plt.plot(x, freq[0], 'o', color='red', label='0.25 Hz')
plt.plot(x, freq[1], 'o', color='blue', label='0.75 Hz')
plt.plot(x, freq[2], 'o', color='orange', label='1.25 Hz')
plt.plot(x, freq[3], 'o', color='green', label='3.00 Hz')
plt.legend()
plt.grid(True)
plt.xlabel("$x$ (m)")
plt.ylabel("$\log |E_x|$ (V/m)")
plt.show()