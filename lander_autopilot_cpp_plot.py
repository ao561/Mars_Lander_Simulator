# Exercise 5
import matplotlib.pyplot as plt
import pandas as pd

from google.colab import files
uploaded = files.upload()

# Load data from files

data = pd.read_csv('lander_autopilot_cpp_results.txt', delim_whitespace=True, names=['altitude', 'descent_rate', 'target_rate'])

# Extracting columns into variables
altitude = data['altitude']
descent_rate = data['descent_rate']
target_rate = data['target_rate']

# Creating the plot
plt.figure(figsize=(15, 6))

# Plotting descent_rate against altitude
plt.plot(altitude, descent_rate, label='descent rate (m/s)', color='blue', marker='o')

# Plotting target_rate against altitude
plt.plot(altitude, target_rate, label='target rate (m/s)', color='red', marker='x')

# Adding labels and title
plt.xlabel('altitude (m)')
plt.ylabel('Values of descent and target rate (m/s)')
plt.title('Plot of descent and target rate (m/s) against altitude (m)')

# Adding a legend
plt.legend()

# Displaying the plot
plt.show()
