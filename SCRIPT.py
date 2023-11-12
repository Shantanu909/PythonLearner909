import matplotlib.pyplot as plt
import numpy as np


t = np.linspace(0, 1, 1000)
A = 2
f0 = 5

x = A*np.cos(2*np.pi*f0*t)

plt.plot(t, x, '-b')
plt.title(r'x(t) = 2\cos(2\pi 5t)')
plt.xlabel(r't (in s)')
plt.grid()

t = np.linspace(-8, 8, 1000)
x = np.sinc(t)
plt.plot(t, x, '-b')
plt.title(r'x(t) = sinc(t)')
plt.xlabel(r't (in s)')
plt.grid()

def p(t):
    """Basic rectangular pulse"""
    return 1 * (abs(t) < 0.5)

def pt(t):
    """ Basic triangular pulse"""
    return (1 - abs(t)) * (abs(t) < 1)

def sgn(t):
    """Sign function"""
    return 1 * (t >= 0) - 1 * (t < 0)

def u(t):
    """Unit step function"""
    return 1 * (t >= 0)

functions = [p, pt, sgn, u]

t = np.linspace(-2, 2, 1000)

plt.figure()
for i, function in enumerate(functions, start=1):
    plt.subplot(2, 2, i)
    plt.plot(t, function(t), '-b')
    plt.ylim((-1.1, 1.1))
    plt.title(function.__doc__)
plt.tight_layout()
plt.show()

F0 = 0.1
L = 100
n = np.arange(L)
x = np.cos(2*np.pi*F0*n)

plt.stem(x) 
plt.title('Discrete-time sinusoid of F0=0.1')
plt.xlabel('n')

from fractions import Fraction

n = np.arange(50)
frequencies = [0, 1/2, 1/4, 3/4, 1/16, 15/16]

for i, F0 in enumerate(frequencies, start=1):
    plt.subplot(3, 2, i)
    plt.stem(np.cos(2*np.pi*F0*n))
    plt.title(r'$\cos(2\pi {}n)$'.format(Fraction(F0)))

plt.tight_layout()

def x(t):
    return np.exp(-0.2 * t) * (t >= 0)

t = np.linspace(-10, 10, 1000)

f, (ax1, ax2, ax3, ax4) = plt.subplots(4, 1, sharex=True, sharey=True)
plt.subplots_adjust(hspace=1)
ax1.set_ylim([-0.2, 1.2])

ax1.plot(t, x(t))
ax1.set_title(r'x(t)')

ax2.plot(t, x(2-t))
ax2.set_title(r'x(2 - t)')

ax3.plot(t, x(4*t))
ax3.set_title(r'x(4t)')

ax4.plot(t, x(0.25*t))
ax4.set_title(r'x(\frac{1}{4}t)')
ax4.set_xlabel('t (in s)')

L = 20
n = np.arange(L)

x = np.exp(-0.2 * n) * (n >= 0)
x2 = x[::2]  # Decimation by 2: Remove one from every 2 points
v = np.zeros((2*L))
v[::2] = x   # v = x(n/2) for even n, 0 otherwise

f, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex=True, sharey=True)
plt.subplots_adjust(hspace=1)
ax1.set_ylim([-0.2, 1.2])

ax1.stem(x)
ax1.set_title(r'x[n]')

ax2.stem(x2)
ax2.set_title(r'x[2n]')

ax3.stem(v)
ax3.set_title(r'v[n]')

# The discrete signals are represented versus n, not versus t
ax3.set_xlabel('n')



import numpy as np
import matplotlib.pyplot as plt

import scipy
from scipy import signal

t = np.arange(0, 11)
x = (0.85) ** t
plt.figure(figsize = (10,8)) # set the size of figure

# 1. Plotting Analog Signal
plt.subplot(2, 2, 1)
plt.title('Analog Signal', fontsize=20)

plt.plot(t, x, linewidth=3, label='x(t) = (0.85)^t')
plt.xlabel('t' , fontsize=15)
plt.ylabel('amplitude', fontsize=15)
plt.legend(loc='upper right')

# 2. Sampling and Plotting of Sampled signal
plt.subplot(2, 2, 2)
plt.title('Sampling', fontsize=20)
plt.plot(t, x, linewidth=3, label='x(t) = (0.85)^t')
n = t

markerline, stemlines, baseline = plt.stem(n, x, label='x(n) = (0.85)^n')
plt.setp(stemlines, 'linewidth', 3)
plt.xlabel('n' , fontsize = 15)
plt.ylabel('amplitude', fontsize = 15)
plt.legend(loc='upper right')

# 3. Quantization
plt.subplot(2, 2, 3)
plt.title('Quantization', fontsize = 20)

plt.plot(t, x, linewidth =3)
markerline, stemlines, baseline=plt.stem(n,x)
plt.setp(stemlines, 'linewidth', 3)
plt.xlabel('n', fontsize = 15)
plt.ylabel('Range of Quantizer', fontsize=15)

plt.axhline(y = 0.1, xmin = 0, xmax = 10, color = 'r', linewidth = 3.0)
plt.axhline(y = 0.2, xmin = 0, xmax = 10, color = 'r', linewidth = 3.0)
plt.axhline(y = 0.3, xmin = 0, xmax = 10, color = 'r', linewidth = 3.0)
plt.axhline(y = 0.4, xmin = 0, xmax = 10, color = 'r', linewidth = 3.0)
plt.axhline(y = 0.5, xmin = 0, xmax = 10, color = 'r', linewidth = 3.0)
plt.axhline(y = 0.6, xmin = 0, xmax = 10, color = 'r', linewidth = 3.0)
plt.axhline(y = 0.7, xmin = 0, xmax = 10, color = 'r', linewidth = 3.0)
plt.axhline(y = 0.8, xmin = 0, xmax = 10, color = 'r', linewidth = 3.0)
plt.axhline(y = 0.9, xmin = 0, xmax = 10, color = 'r', linewidth = 3.0)
plt.axhline(y = 1.0, xmin = 0, xmax = 10, color = 'r', linewidth = 3.0)

plt.subplot(2, 2, 4)
plt.title('Quantized Signal', fontsize = 20)
xq = np.around(x,1)
markerline, stemlines, baseline = plt.stem(n,xq)
plt.setp(stemlines, 'linewidth', 3) 
plt.xlabel('n', fontsize = 15)
plt.ylabel('Range of Quantizer', fontsize=15)

plt.axhline(y = 0.1, xmin = 0, xmax = 10, color = 'r', linewidth = 3.0)
plt.axhline(y = 0.2, xmin = 0, xmax = 10, color = 'r', linewidth = 3.0)
plt.axhline(y = 0.3, xmin = 0, xmax = 10, color = 'r', linewidth = 3.0)
plt.axhline(y = 0.4, xmin = 0, xmax = 10, color = 'r', linewidth = 3.0)
plt.axhline(y = 0.5, xmin = 0, xmax = 10, color = 'r', linewidth = 3.0)
plt.axhline(y = 0.6, xmin = 0, xmax = 10, color = 'r', linewidth = 3.0)
plt.axhline(y = 0.7, xmin = 0, xmax = 10, color = 'r', linewidth = 3.0)
plt.axhline(y = 0.8, xmin = 0, xmax = 10, color = 'r', linewidth = 3.0)
plt.axhline(y = 0.9, xmin = 0, xmax = 10, color = 'r', linewidth = 3.0)
plt.axhline(y = 1.0, xmin = 0, xmax = 10, color = 'r', linewidth = 3.0)

plt.tight_layout()

impulse = signal.unit_impulse(10, 'mid')
shifted_impulse = signal.unit_impulse(7, 2)

# Sine wave
t = np.linspace(0, 10, 100)
amp = 5 # Amplitude
f = 50
x = amp * np.sin(2 * np.pi * f * t)

# Exponential Signal
x_ = amp * np.exp(-t)


plt.figure(figsize=(10, 8))

plt.subplot(2, 2, 1)
plt.plot(np.arange(-5, 5), impulse, linewidth=3, label='Unit impulse function')
plt.ylim(-0.01,1)
plt.xlabel('time.', fontsize=15)
plt.ylabel('Amplitude', fontsize=15)
plt.legend(fontsize=10, loc='upper right')

plt.subplot(2, 2, 2)
plt.plot(shifted_impulse, linewidth=3, label='Shifted Unit impulse function')

plt.xlabel('time.', fontsize=15)
plt.ylabel('Amplitude', fontsize=15)
plt.legend(fontsize=10, loc='upper right')

plt.subplot(2, 2, 3)
plt.plot(t, x, linewidth=3, label='Sine wave')

plt.xlabel('time.', fontsize=15)
plt.ylabel('Amplitude', fontsize=15)
plt.legend(fontsize=10, loc='upper right')

plt.subplot(2, 2, 4)
plt.plot(t, x_, linewidth=3, label='Exponential Signal')

plt.xlabel('time.', fontsize=15)
plt.ylabel('Amplitude', fontsize=15)
plt.legend(fontsize=10, loc='upper right')

plt.tight_layout()

plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.stem(n, x, 'yo', label='Sine wave')

plt.xlabel('time.', fontsize=15)
plt.ylabel('Amplitude', fontsize=15)
plt.legend(fontsize=10, loc='upper right')

plt.subplot(2, 2, 2)
plt.stem(n, x_, 'yo', label='Exponential Signal')

plt.xlabel('time.', fontsize=15)
plt.ylabel('Amplitude', fontsize=15)
plt.legend(fontsize=10, loc='upper right')


f = 20 # Hz
t = np.linspace(0, 0.5, 200)
x1 = np.sin(2 * np.pi * f * t)

s_rate = 35 # Hz. Here the sampling frequency is less than the requirement of sampling theorem

T = 1 / s_rate
n = np.arange(0, 0.5 / T)
nT = n * T
x2 = np.sin(2 * np.pi * f * nT) # Since for sampling t = nT.

print(len(t))
print(len(nT))
plt.figure(figsize=(10, 8))
plt.suptitle("Sampling a Sine Wave of Fmax=20Hz with fs=35Hz", fontsize=20)

plt.subplot(2, 2, 1)
plt.plot(t, x1, linewidth=3, label='SineWave of frequency 20 Hz')
plt.xlabel('time.', fontsize=15)
plt.ylabel('Amplitude', fontsize=15)
plt.legend(fontsize=10, loc='upper right')

plt.subplot(2, 2, 2)
plt.plot(nT, x2, 'ro', label='Sample marks after resampling at fs=35Hz')
plt.xlabel('time.', fontsize=15)
plt.ylabel('Amplitude', fontsize=15)
plt.legend(fontsize=10, loc='upper right')

plt.subplot(2, 2, 3)
plt.stem(nT, x2, 'm', label='Sample after resampling at fs=35Hz')
plt.xlabel('time.', fontsize=15)
plt.ylabel('Amplitude', fontsize=15)
plt.legend(fontsize=10, loc='upper right')

plt.subplot(2, 2, 4)
plt.plot(nT, x2, 'g-', label='Reconstructed Sine Wave')
plt.xlabel('time.', fontsize=15)
plt.ylabel('Amplitude', fontsize=15)
plt.legend(fontsize=10, loc='upper right')

plt.tight_layout()

f = 20 # Hz
t = np.linspace(0, 0.5, 200)
x1 = np.sin(2 * np.pi * f * t)

s_rate = 50 # Hz. Here the sampling frequency is less than the requirement of sampling theorem

T = 1 / s_rate
n = np.arange(0, 0.5 / T)
nT = n * T
x2 = np.sin(2 * np.pi * f * nT) # Since for sampling t = nT.

plt.figure(figsize=(10, 8))
plt.suptitle("Sampling a Sine Wave of Fmax=20Hz with fs=50Hz", fontsize=20)

plt.subplot(2, 2, 1)
plt.plot(t, x1, linewidth=3, label='SineWave of frequency 20 Hz')
plt.xlabel('time.', fontsize=15)
plt.ylabel('Amplitude', fontsize=15)
plt.legend(fontsize=10, loc='upper right')

plt.subplot(2, 2, 2)
plt.plot(nT, x2, 'ro', label='Sample marks after resampling at fs=50Hz')
plt.xlabel('time.', fontsize=15)
plt.ylabel('Amplitude', fontsize=15)
plt.legend(fontsize=10, loc='upper right')

plt.subplot(2, 2, 3)
plt.stem(nT, x2, 'm', label='Sample after resampling at fs=50Hz')
plt.xlabel('time.', fontsize=15)
plt.ylabel('Amplitude', fontsize=15)
plt.legend(fontsize=10, loc='upper right')

plt.subplot(2, 2, 4)
plt.plot(nT, x2, 'g-', label='Reconstructed Sine Wave')
plt.xlabel('time.', fontsize=15)
plt.ylabel('Amplitude', fontsize=15)
plt.legend(fontsize=10, loc='upper right')

plt.tight_layout()

f = 20 # Hz
t = np.linspace(0, 0.5, 200)
x1 = np.sin(2 * np.pi * f * t)

s_rate = 100 # Hz. Here the sampling frequency is less than the requirement of sampling theorem

T = 1 / s_rate
n = np.arange(0, 0.5 / T)
nT = n * T
x2 = np.sin(2 * np.pi * f * nT) # Since for sampling t = nT.
plt.figure(figsize=(10, 8))
plt.suptitle("Sampling a Sine Wave of Fmax=20Hz with fs=100Hz", fontsize=20)

plt.subplot(2, 2, 1)
plt.plot(t, x1, linewidth=3, label='SineWave of frequency 20 Hz')
plt.xlabel('time.', fontsize=15)
plt.ylabel('Amplitude', fontsize=15)
plt.legend(fontsize=10, loc='upper right')

plt.subplot(2, 2, 2)
plt.plot(nT, x2, 'ro', label='Sample marks after resampling at fs=100Hz')
plt.xlabel('time.', fontsize=15)
plt.ylabel('Amplitude', fontsize=15)
plt.legend(fontsize=10, loc='upper right')

plt.subplot(2, 2, 3)
plt.stem(nT, x2, 'm', label='Sample after resampling at fs=100Hz')
plt.xlabel('time.', fontsize=15)
plt.ylabel('Amplitude', fontsize=15)
plt.legend(fontsize=10, loc='upper right')

plt.subplot(2, 2, 4)
plt.plot(nT, x2, 'g-', label='Reconstructed Sine Wave')
plt.xlabel('time.', fontsize=15)
plt.ylabel('Amplitude', fontsize=15)
plt.legend(fontsize=10, loc='upper right')

plt.tight_layout()


t = np.linspace(0, 0.5, 200)
x1 = 2 * np.sin(2 * np.pi * 10 * t) + np.sin(2 * np.pi * 20 * t)

s_rate = 100 # Hz. Here the sampling frequency is less than the requirement of sampling theorem

T = 1 / s_rate
n = np.arange(0, 0.5 / T)
nT = n * T
x2 = 2 * np.sin(2 * np.pi * 10 * nT) + np.sin(2 * np.pi * 20 * nT) # Since for sampling t = nT.
plt.figure(figsize=(10, 8))
plt.suptitle("Sampling a Two Sine Wave of Fmax=20Hz with fs=100Hz", fontsize=20)

plt.subplot(2, 2, 1)
plt.plot(t, x1, linewidth=3, label='SineWave of frequency 20 Hz')
plt.xlabel('time.', fontsize=15)
plt.ylabel('Amplitude', fontsize=15)
plt.legend(fontsize=10, loc='upper right')

plt.subplot(2, 2, 2)
plt.plot(nT, x2, 'ro', label='Sample marks after resampling at fs=100Hz')
plt.xlabel('time.', fontsize=15)
plt.ylabel('Amplitude', fontsize=15)
plt.legend(fontsize=10, loc='upper right')

plt.subplot(2, 2, 3)
plt.stem(nT, x2, 'm', label='Sample after resampling at fs=100Hz')
plt.xlabel('time.', fontsize=15)
plt.ylabel('Amplitude', fontsize=15)
plt.legend(fontsize=10, loc='upper right')

plt.subplot(2, 2, 4)
plt.plot(nT, x2, 'g-', label='Reconstructed Sine Wave')
plt.xlabel('time.', fontsize=15)
plt.ylabel('Amplitude', fontsize=15)
plt.legend(fontsize=10, loc='upper right')

plt.tight_layout()

# Define domain
dx = 0.001
L = np.pi
x = L * np.arange(-1 + dx, 1 + dx, dx)
n = len(x)
nquart = int(np.floor(n / 4))
# Define hat function
f = np.zeros_like(x)
f[nquart:2*nquart] = (4 / n) * np.arange(1, nquart + 1)
f[2*nquart:3*nquart] = np.ones(nquart) - (4 / n) * np.arange(0, nquart)
fig, ax = plt.subplots()
ax.plot(x, f, '-', color='k', linewidth=2)



# # Define domain
# dx = 0.001
# L = np.pi
# x = L * np.arange(-1 + dx, 1 + dx, dx)
# n = len(x)
# nquart = int(np.floor(n / 4))

# # Define hat function
# f = np.zeros_like(x)
# f[nquart:2*nquart] = (4 / n) * np.arange(1, nquart + 1)
# f[2*nquart:3*nquart] = np.ones(nquart) - (4 / n) * np.arange(0, nquart)

# fig, ax = plt.subplots()
# ax.plot(x, f, '-', color='k', linewidth=2)

# # Compute Fourier Series

# A0 = np.sum(f * np.ones_like(x)) * dx
# fFS = A0 / 2

# A = np.zeros(20)
# B = np.zeros(20)
# for k in range(20):
#     A[k] = np.sum(f * np.cos(np.pi * (k + 1) * x/L)) * dx
#     B[k] = np.sum(f * np.sin(np.pi * (k + 1) * x/L)) * dx
#     fFs = fFS + A[k] * np.cos((k + 1) * np.pi * x / L) + B[k] * np.sin((k + 1) * np.pi * x / L)
#     ax.plot(x, fFS, '-')
#Gibbs Phenomena
dx = 0.01
L = 2 * np.pi
x = np.arange(0, L + dx, dx)
n = len(x)
nquart = int(np.floor(n / 4))

f = np.zeros_like(x)
f[nquart:3 * nquart] = 1

A0 = np.sum(f * np.ones_like(x)) * dx * 2 / L
fFS = A0 / 2 * np.ones_like(f)

for k in range(1, 101):
    Ak = np.sum(f * np.cos(2 * np.pi * k * x / L)) * dx * 2 / L
    Bk = np.sum(f * np.sin(2 * np.pi * k * x / L)) * dx * 2 / L    
    fFS = fFS + Ak * np.cos(2 * k * np.pi * x / L) + Bk * np.sin(2 * k * np.pi * x / L)
    
plt.plot(x, f, color='k', linewidth=2)
plt.plot(x, fFS, '-', color='r', linewidth=1.5)
plt.title('Gibbs Phenomena')
plt.show()


# Create synthetic signal
dt = 0.001
t = np.arange(0, 1, dt)
signal = np.sin(2 * np.pi * 50 * t) + np.sin(2 * np.pi * 120 * t) # Sum of 2 Sequencies
signal_clean = signal
signal = signal + 2.5 * np.random.randn(len(t)) # Add some noise
min_signal, max_signal = signal.min(), signal.max()

plt.plot(t, signal, color='c', linewidth=1.5, label='Noisy')
plt.plot(t, signal_clean, color='k', linewidth=2, label='Clean')
plt.xlim(t[0], t[-1])
plt.xlabel('t axis')
plt.ylabel('Vals')
plt.legend()

t = np.linspace(0, 1, 1000)
l = np.linspace(-2,2,1000)
plt.plot(t,l)
