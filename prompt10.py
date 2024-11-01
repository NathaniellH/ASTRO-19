import numpy as np
import matplotlib.pyplot as plt

data = np.random.exponential(scale=1.0, size=1000)

plt.figure(figsize=(8, 6))
plt.hist(data, bins=100, color='teal', edgecolor='black', alpha=0.6)

plt.xlabel("Random Value")
plt.ylabel("Frequency")
plt.title("Histogram of Exponentially Distributed Random Numbers")

plt.savefig("exponential_distribution_histogram.pdf")
plt.show()