<div align="center">
  <h1>🚀 Python for Robotics: Foundation & Data Analytics</h1>
  <p style="font-size:1.05rem; color:#444; max-width:740px; margin:auto;">
    A polished portfolio of Python practice work from a 90-Day Robotics Challenge, built to showcase core algorithms, vectorized sensor processing, and engineering-grade data visualization.
  </p>
  <p>
    <img alt="Python" src="https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python" />
    <img alt="NumPy" src="https://img.shields.io/badge/NumPy-Scientific-orange?style=for-the-badge&logo=numpy" />
    <img alt="Matplotlib" src="https://img.shields.io/badge/Matplotlib-Visualization-purple?style=for-the-badge&logo=matplotlib" />
    <img alt="Run on Colab" src="https://img.shields.io/badge/Run_on-Colab-4285F4?style=for-the-badge&logo=googlecolab" />
  </p>
</div>

---

## 📚 Table of Contents

- [Overview](#overview)
- [Project Architecture](#project-architecture)
- [Core Modules & Progression](#core-modules--progression)
- [Capstone Highlight](#capstone-highlight-hardware-thermal-profile)
- [How to Run](#-how-to-run)
- [Why This Repository Matters](#-why-this-repository-matters)

---

## 📌 Overview

This repository is a structured Python sandbox created during a 90-Day Robotics Challenge. It captures the progression from fundamental Python and OOP to advanced sensor data processing and engineering visualization for autonomous systems.

> [!NOTE]
> The repository is optimized for both robotics learners and engineering reviewers, with a focus on signal processing, visualization, and reproducible telemetry workflows.

> [!IMPORTANT]
> The capstone includes a production-style thermal dashboard export and demonstrates end-to-end data pipeline thinking.

---

## 🗂️ Project Architecture

<details>
<summary><strong>Expand the file tree</strong></summary>

```text
python_practice/
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
```

</details>

---

## 🚀 Core Modules & Progression

| Phase | Focus Area | Key Outcome |
|---|---|---|
| Phase 1 | Python Fundamentals & OOP | Built CLI persistence and object models for banking & contact management |
| Phase 2 | NumPy Vectorization | Developed sensor noise filters and occupancy grid math without loops |
| Phase 3 | Matplotlib Visualization | Produced engineering dashboards and trajectory analytics |
| Capstone | Thermal Simulation & Export | Simulated 24-hour thermal telemetry, smoothed noisy data, and exported a PNG dashboard |

> [!WARNING]
> Advanced reviewers: this repo is intentionally structured for quick vetting, with the full signal processing and visualization workflow isolated in the capstone folder.

---

## 📊 Capstone Highlight: Hardware Thermal Profile

This capstone is the visual signature of the repository. It combines NumPy-driven signal synthesis with Matplotlib dashboard construction to make thermal telemetry instantly interpretable.

<table>
<tr>
<td valign="top" width="45%" style="padding-right:24px;">

### What the capstone delivers

- 1,440 minutes of baseline temperature using a sine wave model
- Gaussian noise injection with `np.random.normal`
- Smoothed trendline via `np.convolve`
- Max/min detection using `np.argmax` and `np.argmin`
- Presentation-ready PNG export for technical reporting

> [!NOTE]
> The graph is generated dynamically by `Num_Mat_excersice/Num_Mat_excersice.py` and exported as `thermal_profile_export.png`.

</td>
<td valign="top" width="55%">
  <a href="Num_Mat_excersice/thermal_profile_export.png" target="_blank">
    <img src="Num_Mat_excersice/thermal_profile_export.png" alt="Thermal Profile Graph" width="100%" style="border:1px solid #ddd; border-radius:14px; box-shadow:0 14px 36px rgba(0,0,0,0.15);" />
  </a>
</td>
</tr>
</table>

---

## ⚙️ How to Run

1. Clone the repository.
2. Install dependencies:
   ```bash
   pip install numpy matplotlib pandas
   ```
3. Run the capstone script:
   ```bash
   python "Num_Mat_excersice/Num_Mat_excersice.py"
   ```

> [!IMPORTANT]
> If you want to reproduce the graph exactly, run the script from the repository root so the image export path resolves correctly.

---

## 💡 Why This Repository Matters

This repository is more than practice code; it is a curated trajectory from basic Python to robotics-aware data analysis. The files show how to move from syntax to sensor fusion, then into polished visual storytelling for engineering teams.

---

<p align="center">Designed and built by <strong>Rahul Choudhary</strong> as part of the journey to mastering autonomous systems.</p>
