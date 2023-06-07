import numpy as np
import matplotlib.pyplot as plt

# Define the signal x[n] = delta[n] + delta[n - 2]
n = np.arange(-10, 10)  # Range of values for n
x = np.zeros_like(n)
x[np.where(n == 0)] = 1
x[np.where(n == 2)] = 1

# Compute the DTFT of x[n]
w = np.linspace(-np.pi, np.pi, 1000)  # Frequency range
X = 1 + np.exp(-1j * 2 * w)  # DTFT of x[n]

# Plot x[n]
plt.subplot(2, 1, 1)
plt.stem(n, x, use_line_collection=True)
plt.xlabel('n')
plt.ylabel('x[n]')
plt.title('Signal x[n] = delta[n] + delta[n - 2]')

# Plot |X(e^jω)|
plt.subplot(2, 1, 2)
plt.plot(w, np.abs(X))
plt.xlabel('ω')
plt.ylabel('|X(e^jω)|')
plt.title('Magnitude of Fourier Transform')

plt.tight_layout()
plt.show()
