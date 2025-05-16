# REIL Core: Spacetime Curvature from Recursive Electromagnetic Inertial Loops

**Authors:** Gregory Betti, GreyOS Symbolic Physics Division; ChatGPT-4o (Co-simulation support)

---

## Project Summary
This open-source project provides a simulation and interactive visualization suite for the REIL Core—a closed-loop, magnetically levitated kinetic engine that generates spacetime curvature using only classical physics and symbolic recursion. The project simulates a 2D toroidal system, with all results derived from first-principles equations and fully reproducible.

- **Backend:** Physics-based simulation of 100 capsules in a 2D toroidal loop
- **2D Visualization:** Animated Matplotlib heatmap with symbolic tick overlay and center-of-mass drift tracking
- **Symbolic Memory:** Tracks recursive loops (symbolic ticks) without intervention
- **Asymmetry Mode:** Demonstrates field drift and directional bias

---

## Installation
1. Clone the repository:
   ```
   git clone https://github.com/YOUR_GITHUB_USERNAME/reil-core-sim.git
   cd reil-core-sim
   ```
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

---

## Usage
- **Run the 3D Viewer:**
  ```
  python reil_viewer_3d.py
  ```
  - Visualizes the 3D toroidal device, capsule positions, curvature shell, symbolic ticks, and curvature intensity.
- **Run the 2D Simulation:**
  ```
  python reil_simulation_2d.py
  ```
  - Produces an animated heatmap of the curvature field and tracks center-of-mass drift and symbolic ticks in 2D.
- **Run the basic backend simulation:**
  ```
  python reil_simulation.py
  ```
  - Computes all physics and outputs core simulation results (energies, kicks, ticks, positions).
- All parameters (capsule count, mass, velocity, symmetry, etc.) can be edited in the scripts.

---

## File Structure
- `reil_simulation.py`: Physics backend (energy, capsule positions, curvature)
- `reil_simulation_2d.py`: 2D simulation and animated curvature field
- `reil_viewer_3d.py`: 3D visualization and GUI
- `requirements.txt`: Dependencies
- `REIL_Scientific_Paper.md`: Scientific manuscript with results
- `README.md`: This file

---

## Requirements
- Python 3.10+
- numpy
- scipy
- matplotlib
- pillow
- pyvista
- vtk

Install all dependencies using `pip install -r requirements.txt`.

---

## Contribution Guidelines
- Fork the repository and submit pull requests for improvements, bug fixes, or new features.
- Please ensure all new code is physics-driven and well documented.
- Open issues for questions, feature requests, or collaboration.

---

## License
This project is open source under the MIT License. See `LICENSE` for details.

---

## Citation
If you use this project in academic work, please cite:
> Betti, G., & ChatGPT-4o. (2025). Spacetime Curvature from Recursive Electromagnetic Inertial Loops (REIL): A Simulation-Based Analysis of Toroidal Field-Induced Warp Shells. [Open Source Software].

---

## Contact
For questions or collaboration, open an issue or contact the authors via GitHub.

---

**Keywords:** REIL Core, symbolic physics, recursive energy, spacetime curvature, warp bubble, closed-loop motion, magnetic levitation, kinetic gravity
