# Spacetime Curvature from Recursive Electromagnetic Inertial Loops (REIL):
## Simulation and Visualization of Toroidal Field-Induced Warp Shells in 2D

**Authors:** Gregory Betti, GreyOS Labs: Symbolic Physics Division

---

### Abstract
We present a simulation and visualization framework for the REIL Core (Recursive Electromagnetic Inertial Loop), a closed-loop, magnetically levitated kinetic engine designed to generate measurable spacetime curvature using only classical physics and symbolic recursion. The current open-source project focuses on a 2D toroidal system, with results visualized as animated heatmaps. The system tracks mass-energy, symbolic memory (ticks), and field asymmetry, providing a reproducible, physics-driven demonstration of a symbolic curvature bubble in 2D. All results are derived from first-principles equations and are fully reproducible.

---

### 1. Introduction
Traditional studies of spacetime curvature focus on high-mass gravitational phenomena or hypothetical exotic matter. The REIL Core project introduces a novel, energy-based approach: using recursive motion, magnetic stabilization, and kinetic energy density to produce gravitational effects in a toroidal geometry. This extends the concept of sealed kinetic flywheels into symbolic physics, where entropy-minimized, recursive motion reinforces spacetime distortions via continuous mass-energy retention. Our simulations bridge computational recursion and physical field reinforcement, offering new insight into classical, energy-driven spacetime manipulation.

---

### 2. System Design and Theoretical Basis
- **Device:** Toroidal vacuum chamber with 100 magnetically levitated capsules (1.0 kg each)
- **Stabilization:** Magnetic ring arrays; no energy harvesting; optional kick pulses to sustain motion
- **2D Torus Geometry:** Core radius 0.1 m (2D cross-section)
- **Simulation Time:** 60.0 s; time step 0.1 s
- **Energy Equation:**
  $E_{total} = \sum_{i=1}^{n} \frac{1}{2} m_i v_i^2$
- **Curvature Equation:**
  $R(x, y) = \frac{8\pi G}{c^4} \cdot \frac{E_{total}}{d^2}$
  where $d$ is the distance from a field point to the nearest point on the torus core in 2D.
- **Asymmetry Mode:** When enabled, capsule velocities are split (+10% / -10%) to induce field drift.

---

### 3. Simulation Methods
- **Backend:** Python 3.10+, NumPy, SciPy, Matplotlib, Pillow
- **2D Simulation:** Physics-based simulation of 100 capsules in a toroidal loop; curvature field computed on a 100×100 grid
- **Capsule Dynamics:** Velocities maintained by kick logic; drag optional; symbolic ticks count uninterrupted loops
- **Curvature Calculation:** At each grid point, distance to torus core is computed; curvature is calculated using the GR formula above
- **Visualization:**
  - Animated Matplotlib heatmap with overlays for symbolic ticks and real-time center-of-mass drift tracking

---

### 4. Results
- **2D Simulation (default parameters):**
  - Final kinetic energy at 60s: ~126,250 J
  - Total kick pulses required: 0 (ideal case)
  - Max symbolic ticks: 599
  - Center-of-mass drift: Tracked and visualized in real time
  - Visualization: Animated heatmap of curvature field, with overlays for symbolic ticks and COM drift

All results are reproducible by running `reil_simulation_2d.py` with default settings.

---

### 5. Discussion
The REIL Core 2D simulation provides a direct, math-based demonstration of recursive kinetic curvature using only classical physics and symbolic memory. The system does not rely on exotic matter or speculative physics. Instead, it shows that sealed, recursive motion can produce measurable spacetime curvature via conserved kinetic energy. Symbolic ticks provide a bridge between computational recursion and physical field reinforcement, and the inclusion of asymmetry demonstrates the tunability of the curvature field.

---

### 6. Conclusions
Our simulation and visualization framework confirms that spacetime curvature can be produced and visualized through sealed, recursive motion in a 2D toroidal geometry. The results support the hypothesis that symbolic motion structures can have physical gravitational consequences. All code, data, and results are open source and fully reproducible.

---

### 7. Code Availability
- All simulation and visualization code is available in this repository.
- Requirements: Python 3.10+, NumPy, SciPy, Matplotlib, Pillow
- See `README.md` for setup and usage instructions.

---

### 8. References
1. Einstein, A. (1916). The Foundation of the General Theory of Relativity. Annalen der Physik.
2. Thorne, K. S. (1994). Black Holes and Time Warps. Norton.
3. Relevant open-source physics and visualization libraries.

---

### 9. Acknowledgments
- Gregory Betti, for original concept and system design
- GreyOS Labs: Symbolic Physics Division

---

**Contact:** For questions or collaboration, please open an issue or contact the authors via GitHub.
