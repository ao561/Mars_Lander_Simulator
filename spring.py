# Exercise 1
# %matplotlib inline
import numpy as np
import matplotlib.pyplot as plt

# mass, spring constant, initial position and velocity
m = 1
k = 1
x = 0
v = 1
# simulation time, timestep and time
t_max = 1000
dt = 1
t_array = np.arange(0, t_max, dt)

# initialise empty lists to record trajectories
x_list = []
v_list = []
x_verlet = []
v_verlet = []

x_verlet.append(x)
x_verlet.append(x + v * dt)  # Approximate using initial velocity
v_verlet.append(v)

# Euler integration
for t in t_array:

    # append current state to trajectories
    x_list.append(x)
    v_list.append(v)

    # calculate new position and velocity
    a = -k * x / m
    x = x + dt * v
    v = v + dt * a

    if len(x_verlet) >= 2:
      a_verlet = -k * x_verlet[-1] / m
      x_position = 2*x_verlet[-1] - x_verlet[-2] + dt**2 * a_verlet
      v_velocity = 1/dt * (x_position - x_verlet[-1])

      x_verlet.append(x_position)
      v_verlet.append(v_velocity)

# convert trajectory lists into arrays, so they can be sliced (useful for Assignment 2)
x_array = np.array(x_list)
v_array = np.array(v_list)
x_array_verlet = np.array(x_verlet[:len(t_array)])
v_array_verlet = np.array(v_verlet[:len(t_array)])



# plot the position-time graph
plt.figure(1)
plt.clf()
plt.xlabel('time (s)')
plt.grid()
plt.plot(t_array, x_array, label='x (m)')
plt.plot(t_array, v_array, label='v (m/s)')
plt.legend()
plt.show()

# plot for verlet
plt.figure(2)
plt.clf()
plt.xlabel('time (s)')
plt.grid()
plt.plot(t_array, x_array_verlet, label='x verlet(m)')
plt.plot(t_array, v_array_verlet, label='v verlet(m/s)')
plt.legend()
plt.show()
