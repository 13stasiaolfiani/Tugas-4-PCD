import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft
from scipy.fftpack import ifft

data = np.loadtxt("profil.txt")
t = data[:,0]
x = data[:,1]

amplitudes = fft(x)
c = np.abs(amplitudes)
c_norm = 2 * c/len(t)
c[0] /= 2
c_half = c[0:len(amplitudes)//2]
f = np.fft.fftfreq(len(t), d = t[len(t)-1]/(len(t)-1))

p_t = np.zeros(len(amplitudes))
sigma = np.sqrt(np.log(0.5)/(-2.))/np.pi/10      #FIRST VERSION
s = 0.7                                           #SECOND VERSION
for i in range(len(c)):
    e = np.exp(-2*np.pi**2*sigma**2*f[i]**2)    #FIRST VERSION
    #e = np.e**(-f[i]**2/2/s**2)/s/np.sqrt(2*np.pi)    #SECOND VERSION
    if e > 0.1:
        #FIRST VERSION
        p_t[i] = np.exp(-2*np.pi**2*sigma**2*f[i]**2)
        p_t[-i] = np.exp(-2 * np.pi ** 2 * sigma ** 2 * f[i] ** 2)
        #SECOND VERSION:
        #p_t[i] = np.e**(-f[i]**2/2/s**2)/s/np.sqrt(2*np.pi)
        #p_t[-i] = np.e ** (-f[i] ** 2 / 2 / s ** 2)/s/np.sqrt(2*np.pi)
    else:
        pass

x_filtered = ifft(amplitudes * p_t)

fig = plt.figure(constrained_layout = True)
gs = fig.add_gridspec(2, 1)
a00 = fig.add_subplot(gs[0, 0])
a00.plot(t, x,color='blue', label="original")
a00.plot(t,x_filtered, color='red', label="filtered")
a00.legend(bbox_to_anchor=(0,1,1,0), loc="lower left", ncol = 1)
a01 = fig.add_subplot(gs[1, 0])
a01.plot(f,c, label="amplitudes")
a01.set_ylim([0,1000])
a01.legend()
a03 = a01.twinx()
a03.plot(f, p_t, color='red', label='filter characteristic')
plt.show()