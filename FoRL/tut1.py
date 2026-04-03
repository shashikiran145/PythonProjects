import numpy as np
import matplotlib.pyplot as plt

def rand_softmax(z, N):
    z = np.array(z)

    # Softmax
    probs = np.exp(z - np.max(z))
    probs /= probs.sum()

    # Sample
    samples = np.random.choice(z, size=N, p=probs)

    return samples, probs

z = np.arange(1,11)
N = 10000

samples, true_probs = rand_softmax(z, N)

values, counts = np.unique(samples, return_counts=True)
real_freq = counts / N

plt.stem(values, real_freq, linefmt='b-')
plt.stem(z, true_probs, linefmt='r--')

plt.xlabel("Values")
plt.ylabel("Probabilities")
plt.legend(["Empirical", "True PMF"])
plt.grid()

plt.show()



