import numpy as np
import matplotlib.pyplot as plt
from math import pi


# create time axis
Fs = 1000
n = np.arange(start=0, stop=2, step=1 / Fs)


# generate the carrier wave
Fc = 100
Ac = 1
c = Ac*np.cos(2*pi*Fc*n)  # carrier signal


# generate the message

Fm = 2                 #Fm must be less than Fc
Am = 0.5               #this case is under-modulated and if M > 1 will be over-modulated  note; m = Am/Ac
m = Am*np.cos(2*pi*Fm*n)      #message signal


#AM(Amplitude Modulated) signal
s = c*(1+m/Ac)


#plot
plt.plot(n, s)
plt.title("Normal AM")
plt.xlabel("t(s)")
plt.ylabel("Amp")
plt.show()
