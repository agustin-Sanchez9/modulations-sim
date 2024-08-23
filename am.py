import numpy as np
import matplotlib.pyplot as plt

# definicion de variables
t = np.linspace(0,5,500)
n = len(t)
Fs = 1 / (t[1] - t[0])

# formula para el mensaje (un tono) 
msj = 1 + np.cos(2*np.pi*1*t)

# carrier
carrier = np.cos(2*np.pi*5*t)

# modulacion del mensaje
am = msj * carrier

# espectro de frecuencias del mensaje
msj_fft = np.fft.fft(msj)

# espectro de frecuencias de la carrier
carrier_fft =np.fft.fft(carrier)

# espectro de frecuencias del mensaje modulado
am_fft = np.fft.fft(am)

# defino var f para frecuencias
f = np.fft.fftfreq(n,1/Fs)

# graficos con matplot
plt.subplot(3,2,1)
plt.plot(t,msj)
plt.title("tiempo")
plt.grid(True)

plt.subplot(3,2,2)
plt.plot(f,msj_fft)
plt.axis([-10,10,0,500])
plt.title("frecuencia")
plt.grid(True)

plt.subplot(3,2,3)
plt.plot(t,carrier)
plt.grid(True)

plt.subplot(3,2,4)
plt.plot(f,carrier_fft)
plt.axis([-10,10,0,500])
plt.grid(True)

plt.subplot(3,2,5)
plt.plot(t,am)
plt.grid(True)

plt.subplot(3,2,6)
plt.plot(f,am_fft)
plt.axis([-10,10,0,500])
plt.grid(True)

plt.show()