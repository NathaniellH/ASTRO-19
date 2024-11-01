import numpy as np
import matplotlib.pyplot as plt

data = np.random.uniform(low=0.0, high=1.0, size=1000)

fig, ax = plt.subplots(figsize=(8, 6))
ax.hist(data, bins=100, color='orange', edgecolor='black', alpha=0.7)

ax.set_xlabel("Random Value")
ax.set_ylabel("Frequency")
ax.set_title("Histogram of Uniformly Distributed Random Numbers")

plt.savefig("uniform_random_histogram.pdf")
plt.show()