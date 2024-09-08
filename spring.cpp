#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int main() {

  // declare variables
  double m, k, x_position, v_velocity, t_max, dt, t, a_verlet;
  vector<double> t_list, x_verlet, v_verlet;

  // mass, spring constant, initial position and velocity
  m = 1;
  k = 1;
  x_position = 0;
  v_velocity = 1;

  // simulation time and timestep
  t_max = 100;
  dt = 0.1;


  // Verlet integration
  for (t = 0; t <= t_max; t = t + dt) {

    // append current state to trajectories
    t_list.push_back(t);
    x_verlet.push_back(x_position);
    v_verlet.push_back(v_velocity);

    if (t < dt) {
      // approximate using initial velocity
      a_verlet = -k * x_position / m;
      x_position = x_position + v_velocity * dt;
      v_velocity = v_velocity + a_verlet * dt;

    } else {

      // calculate new position and velocity
      a_verlet = -k * x_verlet[x_verlet.size()-1] / m;
      x_position = 2*x_verlet[x_verlet.size()-1] - x_verlet[x_verlet.size()-2] + dt * dt * a_verlet;
      v_velocity =  1/dt * (x_position - x_verlet[x_verlet.size()-1]);
      
    }
  }

  // Write the trajectories to file
  ofstream fout;
  fout.open("trajectories.txt");
  if (fout) { // file opened successfully
    for (int i = 0; i < t_list.size(); i = i + 1) {
      fout << t_list[i] << ' ' << x_verlet[i] << ' ' << v_verlet[i] << endl;
    }
  } else { // file did not open successfully
    cout << "Could not open trajectory file for writing" << endl;
  }

  /* The file can be loaded and visualised in Python as follows:

  import numpy as np
  import matplotlib.pyplot as plt
  results = np.loadtxt('trajectories.txt')
  plt.figure(1)
  plt.clf()
  plt.xlabel('time (s)')
  plt.grid()
  plt.plot(results[:, 0], results[:, 1], label='x (m)')
  plt.plot(results[:, 0], results[:, 2], label='v (m/s)')
  plt.legend()
  plt.show()

  */
}
