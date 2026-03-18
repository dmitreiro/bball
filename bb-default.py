import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# Parameters
# -----------------------------
m = 0.2          # mass [kg]
R = 0.05         # ball radius [m]
g = 9.81         # gravity [m/s^2]
k = 2000.0       # spring constant [N/m]
b = 5.0          # damping constant [N.s/m]

x0 = 1.0         # initial height of ball center [m]
v0 = 0.0         # initial velocity [m/s]

t_max = 3.0      # total simulation time [s]
dt = 0.0005      # time step [s]

# -----------------------------
# Time array
# -----------------------------
t = np.arange(0, t_max + dt, dt)

# Arrays to store solution
x = np.zeros_like(t)   # position
v = np.zeros_like(t)   # velocity
a = np.zeros_like(t)   # acceleration

# Initial conditions
x[0] = x0
v[0] = v0

# -----------------------------
# Time integration (Euler method)
# -----------------------------
for i in range(len(t) - 1):
    if x[i] > R:
        # Ball in the air
        acc = -g
    else:
        # Ball in contact with ground
        acc = (-b * v[i] + k * (R - x[i]) - m * g) / m

    a[i] = acc

    # Update velocity and position
    v[i + 1] = v[i] + acc * dt
    x[i + 1] = x[i] + v[i + 1] * dt

a[-1] = a[-2]

# -----------------------------
# Plot position over time
# -----------------------------
plt.figure(figsize=(8, 4))
plt.plot(t, x)
plt.xlabel("Time [s]")
plt.ylabel("Position [m]")
plt.title("Bouncing ball simulation")
plt.xlim(left=0)
plt.ylim(bottom=0)
plt.grid(True)
plt.tight_layout()
plt.show()