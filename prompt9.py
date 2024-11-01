import numpy as np
import matplotlib.pyplot as plt

random_numbers = np.random.uniform(0, 1, 1000)

plt.hist(random_numbers, bins=100, color='skyblue', edgecolor='black')
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.title("Histogram of Uniformly Distributed Random Numbers")

plt.savefig("uniform_distribution_histogram.pdf")
plt.show()