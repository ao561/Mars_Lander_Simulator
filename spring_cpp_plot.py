# Exercise 3
import matplotlib.pyplot as plt
import pandas as pd


from google.colab import files
uploaded = files.upload()

# Load data from files

data = pd.read_csv('trajectories.txt', delim_whitespace=True, names=['t', 'x', 'v'])

# Extracting columns into variables
t = data['t']
x = data['x']
v = data['v']

# Creating the plot
plt.figure(figsize=(15, 6))

# Plotting x against t
plt.plot(t, x, label='x_verlet (m)', color='blue', marker='o')

# Plotting v against t
plt.plot(t, v, label='v_verlet (m/s)', color='red', marker='x')

# Adding labels and title
plt.xlabel('time (s)')
plt.ylabel('Values of x_verlet (m) and v_verlet (m/s)')
plt.title('Plot of x_verlet (m) and v_verlet (m/s) against time')

# Adding a legend
plt.legend()

# Displaying the plot
plt.show()
