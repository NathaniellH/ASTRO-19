import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 1, 100)

def sine(x):
    return np.sin(x)

def cosine(x):
    return np.cos(x)

y_sin = sine(x)
y_cos = cosine(x)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))

ax1.plot(x, y_sin, color="blue")
ax1.set_title("sin(x)")
ax1.set_xlabel("x")
ax1.set_ylabel("sin(x)")

ax2.plot(x, y_cos, color="green")
ax2.set_title("cos(x)")
ax2.set_xlabel("x")
ax2.set_ylabel("cos(x)")

plt.tight_layout()
plt.savefig("sine_cosine_multipanel_plot.pdf")
plt.show()