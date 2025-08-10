# Mars Lander Simulator

A physics-based simulator for a Mars lander, built in C++. This project simulates the descent of a spacecraft onto the Martian surface, incorporating realistic physics, user controls, and data logging for analysis. The simulator is designed to demonstrate principles of mechanics and control systems in a computational environment.

## 🛠️ Features

* **Physics-based Simulation:** Accurately models the forces acting on the lander, including gravity, thrust, and drag.

* **Realistic Descent Profile:** Simulates a lander's trajectory, velocity, and fuel consumption.

* **Manual Control Interface:** Allows a user to control the lander's thrust during descent.

* **Data Logging:** Outputs key simulation data (e.g., position, velocity, fuel) for post-simulation analysis.

* **Python Plotting Scripts:** Includes helper scripts in Python to visualise the results of the simulation.

## 📁 Project Structure

The project is structured to separate the core simulation logic from the plotting and analysis tools:

* **`lander.cpp`**: The main C++ source file containing the simulation loop and physics engine. This file outputs simulation data to `lander_autopilot_cpp_results.txt`.

* **`lander.h`**: The header file defining the `Lander` class and other necessary structures.

* **`graphics.cpp`**: A C++ file for handling the graphical rendering of the simulation.

* **`lander_autopilot_cpp_plot.py`**: A Python script to visualise the results of an autopilot simulation by processing the data from `lander_autopilot_cpp_results.txt`.

## 💻 Technology Stack

* **Language**: C++

* **Plotting/Analysis**: Python, leveraging libraries like `matplotlib`.

## 🏁 Getting Started

To compile and run the simulator, you will need a C++ compiler and the ability to run Python scripts.

### 📋 Prerequisites

* A C++ compiler (e.g., g++).

* Python 3.8 or higher.

* `matplotlib` and `numpy` Python libraries for plotting.

### ⬇️ Installation

1.  **Clone the repository:**

    ```
    git clone [https://github.com/ao561/Mars_Lander_Simulator.git](https://github.com/ao561/Mars_Lander_Simulator.git)
    cd Mars_Lander_Simulator
    ```

2.  **Install Python dependencies for plotting:**

    ```
    pip install matplotlib numpy
    ```

### ▶️ Compilation and Usage

1.  **Compile the C++ code:**

    ```
    g++ -o lander lander.cpp
    ```

2.  **Run the compiled executable:**

    ```
    ./lander
    ```

3.  The program will output a data file named `lander_autopilot_cpp_results.txt`. You can then use the Python scripts to visualise the results. For example:

    ```
    python lander_autopilot_cpp_plot.py
    ```
