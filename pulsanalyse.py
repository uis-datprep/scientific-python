import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt
from analyse import findpeaks


# Read data
x = np.genfromtxt('photopl.txt', dtype=None, delimiter=None, skip_header=4)
x = x.reshape(x.size, 1)
x = x / np.std(x)

# Generate time vector
fs = 40.0
N = np.size(x)
t = np.arange(0, N) / fs
t = t.reshape(t.size, 1)

# Detect peaks and plot
ind, peaks = findpeaks(x)
fig1 = plt.figure(1)
ax1 = plt.axes()
ax1.plot(t, x, 'b', t[ind, 0], x[ind, 0], 'go')
plt.xlabel('t [sek]')
plt.ylabel('x(t)')
plt.grid('on')
sz = fig1.get_size_inches()
# plt.figure(figsize=(8,5))
fig1.set_size_inches(8, 3)
sz2 = fig1.get_size_inches()
plt.axis([0, t[N - 1], -1.5, 4.5])
plt.savefig('photopl.png')
# print(sz)
# print(sz2)
# plt.show()

# Spectral analysis
whan = signal.get_window('hanning', 256)
f, Pxx = signal.welch(x.reshape(1, x.size), fs, nperseg=256,
                      nfft=1024, detrend=False, scaling='density')
Pxx = Pxx.reshape(Pxx.size, 1)
f = f.reshape(f.size, 1)
fig2 = plt.figure(2)
ax21 = fig2.add_subplot(211)
ax21.plot(f, 10 * np.log10(Pxx), 'b')
plt.xlabel('f [Hz]')
plt.ylabel('Magnitude [dB]')
plt.grid('on')
plt.axis([0, 20, -40, 20])


# Filter design
dt = 0.55
pb = np.array([0, 0.58 - dt, 0.58, 1.27, 1.27 + dt, 20]) / (40)
b = signal.remez(150, pb, [0, 1, 0], type='bandpass')
w, h = signal.freqz(b)
ax22 = fig2.add_subplot(212)
ax22.plot(w / (2 * np.pi) * 40, 20 * np.log10(np.abs(h)), 'b')
plt.xlabel('f [Hz]')
plt.ylabel('Magnitude [dB]')
plt.grid('on')
plt.axis([0, 20, -100, 20])
plt.savefig('specfilt.png')
# plt.show()

# Filter signal and detect peaks
y = signal.filtfilt(b, 1, x.reshape(1, x.size))
y = y.reshape(y.size, 1)
ind2, peaks2 = findpeaks(y)
fig3 = plt.figure(3)
ax3 = plt.axes()
# plt.plot(t,y,'r',t[ind2,0],y[ind2,0],'go')
ax3.plot(t, x + 1, 'b', t[ind, 0], x[ind, 0] + 1,
         'go', t, y, 'r', t[ind2, 0], y[ind2, 0], 'go')
plt.grid('on')
plt.savefig('filtered.png')


# Determine heart rate
#
# Time difference between beats
tp = t[ind2, 0]
d = np.diff(tp[1:-2], 1, 0)  # s/b
# Mean heart rate
hr = np.mean(d)  # s/b
bpm = 1/(hr/60)  # s/b/60s/min = 1/min/b
# Beats per minute
bpm = 1/(hr/60)  # s/b/60s/min = 1/min/b
# Heart rate variability
rrvar = np.std(d)
print('Heart rate '+str(round(bpm, 2))+' bpm')
print('Heart rate variability '+str(round(rrvar, 2))+' s')

plt.show()
