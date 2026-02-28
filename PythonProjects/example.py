# # x = 3
# # y = 5
# # z = x + y
# # print(z)
# import numpy as np
# import matplotlib.pyplot as plt
# from sklearn import svm
# from sklearn.datasets import make_blobs
#
# # 1. Generate synthetic data
# X, y = make_blobs(n_samples=100, centers=2, random_state=0, cluster_std=1.0)
#
# # 2. Train an SVM classifier
# clf = svm.SVC(kernel='linear', C=1.0)
# clf.fit(X, y)
#
# # 3. Plot the data points
# plt.scatter(X[:, 0], X[:, 1], c=y, s=30)
#
# # 4. Plot the decision boundary
# ax = plt.gca()
# xlim = ax.get_xlim()
# ylim = ax.get_ylim()
#
# # Create grid to evaluate model
# xx = np.linspace(xlim[0], xlim[1], 30)
# yy = np.linspace(ylim[0], ylim[1], 30)
# YY, XX = np.meshgrid(yy, xx)
# xy = np.vstack([XX.ravel(), YY.ravel()]).T
# Z = clf.decision_function(xy).reshape(XX.shape)
#
# # Plot decision boundary and margins
# ax.contour(XX, YY, Z, levels=[0], colors='k', linewidths=2)
# ax.contour(XX, YY, Z, levels=[-1, 1], colors='k', linestyles=['--'])
#
# plt.title("Linear SVM Example")
# plt.show()


import numpy as np
import matplotlib.pyplot as plt

# Sampling parameters
fs = 1000        # Sampling frequency (Hz)
t = np.linspace(0, 1, fs, endpoint=False)

# Example signal: 50 Hz sine wave
signal = np.sin(2 * np.pi * 50 * t)

# Compute FFT
fft_vals = np.fft.fft(signal)
freqs = np.fft.fftfreq(len(fft_vals), 1/fs)

# Magnitude spectrum (only positive frequencies)
magnitude = np.abs(fft_vals)

# Plot
plt.plot(freqs[:len(freqs)//2], magnitude[:len(magnitude)//2])
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.title("FFT of the Signal")
plt.show()

