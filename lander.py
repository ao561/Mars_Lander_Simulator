# Exercise 2
# %matplotlib inline
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# mass, spring constant, initial position and velocity
G = 6.67408e-11
mass_mars = 6.42e23
radius_mars = 3.39e6
position = np.array([0,0,9e6])
velocity = np.array([2181.3,0,0])
x_position = position
v_velocity = velocity


# simulation time, timestep and time
t_max = 100000
dt = 1
t_array = np.arange(0, t_max, dt)

# initialise empty lists to record trajectories
x_list = []
v_list = []
x_verlet = []
v_verlet = []


# Euler integration
for t in t_array:
    mag_position = np.linalg.norm(position)
    if mag_position < radius_mars:
      break
    # append current state to trajectories
    x_list.append(position)
    v_list.append(velocity)
    x_verlet.append(x_position)
    v_verlet.append(v_velocity)


    # calculate new position and velocity
    a = -G * mass_mars * position / mag_position**3
    position = position + dt * velocity
    velocity = velocity + dt * a

    if t >= t_array[1]:
      mag_position_verlet = np.linalg.norm(x_position)
      if mag_position_verlet < radius_mars:
        break
      a_verlet = -G * mass_mars * x_verlet[-1] / (np.linalg.norm(x_verlet[-1]))**3
      x_position = 2*x_verlet[-1] - x_verlet[-2] + dt**2 * a_verlet
      v_velocity = 1/dt * (x_position - x_verlet[-1])
    else:
      x_position = position
      v_velocity = velocity



# convert trajectory lists into arrays, so they can be sliced (useful for Assignment 2)
x_array = np.array(x_list)
v_array = np.array(v_list)
x_array_verlet = np.array(x_verlet)
v_array_verlet = np.array(v_verlet)

'''
# Scenario 1 Plot

plt.figure(1)
plt.clf()
plt.xlabel('time (s)')
plt.grid()
plt.plot(t_array[:len(x_array)], x_array[:,2], label='altitude euler (m)')
#plt.plot(t_array[:len(v_array)], v_array[:,2], label='v (m/s)')
plt.legend()
plt.show()

plt.figure(2)
plt.clf()
plt.xlabel('time (s)')
plt.grid()
plt.plot(t_array[:len(x_array)], x_array_verlet[:,2], label='altitude verlet (m)')
#plt.plot(t_array[:len(v_array_verlet)], v_array_verlet[:,2], label='v verlet (m/s)')
plt.legend()
plt.show()

'''

# Scenario 2-4

fig = plt.figure(3)
ax = fig.add_subplot(111, projection='3d')

u, v = np.mgrid[0:2*np.pi:100j, 0:np.pi:50j]
x_sphere = radius_mars * np.cos(u) * np.sin(v)
y_sphere = radius_mars * np.sin(u) * np.sin(v)
z_sphere = radius_mars * np.cos(v)
ax.plot_surface(x_sphere, y_sphere, z_sphere, color='r', alpha=0.5)

ax.plot(x_array[:,0], x_array[:,1], x_array[:,2], label='Euler Integration', color='b')
ax.set_xlabel('X Position')
ax.set_ylabel('Y Position')
ax.set_zlabel('Z Position')
ax.set_title('3D Trajectory of the Mars Lander')
ax.set_box_aspect([1,1,1])
ax.legend()
plt.show()

fig = plt.figure(4)
ax = fig.add_subplot(111, projection='3d')

u, v = np.mgrid[0:2*np.pi:100j, 0:np.pi:50j]
x_sphere = radius_mars * np.cos(u) * np.sin(v)
y_sphere = radius_mars * np.sin(u) * np.sin(v)
z_sphere = radius_mars * np.cos(v)
ax.plot_surface(x_sphere, y_sphere, z_sphere, color='r', alpha=0.5)

ax.plot(x_array_verlet[:,0], x_array_verlet[:,1], x_array_verlet[:,2], label='Verlet Integration', color='b')
ax.set_xlabel('X Position')
ax.set_ylabel('Y Position')
ax.set_zlabel('Z Position')
ax.set_title('3D Trajectory of the Mars Lander')
ax.set_box_aspect([1,1,1])
ax.legend()
plt.show()
