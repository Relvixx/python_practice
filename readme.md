🚀 Python for Robotics: Foundation & Data Analytics

📌 Overview

Welcome to my Python practice repository. This project serves as a foundational sandbox developed during a 90-Day Robotics Challenge. It documents the progression from core object-oriented programming concepts to the advanced data manipulation and visualization techniques required for autonomous systems and hardware telemetry analysis.

The repository is structured logically, starting with basic algorithmic logic and scaling up to processing simulated hardware noise and visualizing 2D occupancy grids.

🗂️ Project Architecture

📂 python_practice/
│
├── 📁 Root/                            # Core Python Fundamentals
│   ├── Bank_account.py                 # OOP: Classes, Methods, State Management
│   ├── contact_CLI.py                  # File I/O & Persistent Data Storage
│   ├── student_topper_script.py        # Data Sorting & Lambda Functions
│   ├── FIZZBUZZ.py                     # Algorithmic Control Flow
│   └── (Calculater.py, Tip_Calculator.py, number_gussing.py, etc.)
│
├── 📁 numpy/                           # Vectorized Data Processing
│   ├── numpy_tutorial.py               # Arrays, Shapes, and Matrix Math
│   ├── excersice_1.py                  # 1D Autonomous Sensor Noise Filter
│   └── excersice_2.py                  # 2D Grid Occupancy Map (Broadcasting)
│
├── 📁 Matplotlib/                      # Data Visualization
│   ├── matplotlib_tutorial.py          # DataFrames, Bar Charts, and Pie Charts
│   ├── mat_excersice_1.py              # Ultrasonic Sensor Calibration Curve
│   ├── mat_excersice_2.py              # Transit Demand Dashboard (Subplots)
│   └── mat_excersice_3.py              # Autonomous Robot Trajectory Map 
│
└── 📁 Num_Mat_excersice/               # 🏆 Capstone Project
    ├── Num_Mat_excersice.py            # 24-Hour Hardware Thermal Simulation
    └── thermal_profile_export.png      # High-Res Output Graphic

🚀 Core Modules & Progression

Phase 1: Python Fundamentals & OOP

Focused on mastering standard Python syntax, control flow, and Object-Oriented Programming (OOP).

Highlights: Built a persistent Command-Line Interface (CLI) Contact Book that reads/writes to contacts.txt, and a My_Account class simulating secure banking transactions.

Phase 2: Vectorized Mathematics (NumPy)

Transitioned from standard for loops to high-performance array operations, a critical skill for processing high-frequency sensor data.

1D Noise Filter (excersice_1.py): Utilized boolean masking to eliminate impossible sensor glitches and np.convolve to apply a sliding window average.

2D Occupancy Grid Simulator (excersice_2.py): Utilized array broadcasting to instantly calculate the Euclidean distance from a robot to all nearby obstacles without a single loop.

Phase 3: Spatial & Temporal Visualization (Matplotlib)

Focused on translating raw matrices into readable engineering dashboards.

Trajectory Map (mat_excersice_3.py): Mapped out an autonomous robot's trajectory on a 1:1 aspect ratio coordinate plane, linking waypoint colors to velocity telemetry data and annotating sharp turns.

Transit Dashboard (mat_excersice_2.py): Utilized object-oriented Matplotlib (fig, ax = plt.subplots()) to create multi-panel dashboards visualizing network fluctuations.

📊 Capstone Highlight: Hardware Thermal Profile

(Found in Num_Mat_excersice/Num_Mat_excersice.py)

A comprehensive script synthesizing both NumPy and Matplotlib. It simulates a 24-hour thermal profile for an onboard hardware motor:

- Generates 1,440 minutes of baseline temperature data using a mathematical sine wave
- Injects randomized Gaussian noise (np.random.normal) to simulate hardware sensor inaccuracy
- Overlays a cleaned, smoothed trendline using 1D convolution
- Programmatically identifies and highlights the absolute thermal limits (Max/Min) using np.argmax
- Exports a professional, presentation-ready PNG dashboard

⚙️ How to Run

- Clone this repository to your local machine.
- Ensure you have the required engineering libraries installed:
  pip install numpy matplotlib pandas
- Navigate to the desired folder and run the scripts via terminal. For example:
  python "Num_Mat_excersice/Num_Mat_excersice.py"

Designed and built by Rahul Choudhary as part of the journey to mastering autonomous systems.
