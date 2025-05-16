import numpy as np
import pyvista as pv
from scipy.spatial.distance import cdist
from reil_simulation import simulate_reil_core

# --- Torus Parameters ---
MAJOR_RADIUS = 0.25  # meters (center to tube)
MINOR_RADIUS = 0.05  # meters (tube radius)
NUM_CAPSULES = 100

# --- Simulation Parameters ---
SIM_TIME = 60.0
DT = 0.1
ASYMMETRY = False  # Default: off

# --- Load simulation data from backend ---
# The backend must provide: capsule_positions, energies, kicks, symbolic_ticks, etc.
capsule_positions, energies, kicks, symbolic_ticks = simulate_reil_core(
    num_capsules=NUM_CAPSULES,
    major_radius=MAJOR_RADIUS,
    minor_radius=MINOR_RADIUS,
    sim_time=SIM_TIME,
    dt=DT,
    asymmetry=ASYMMETRY
)

# --- 3D Grid for Curvature Field ---
grid_res = 40
extent = 0.5  # meters
x = np.linspace(-extent, extent, grid_res)
y = np.linspace(-extent, extent, grid_res)
z = np.linspace(-extent, extent, grid_res)
X, Y, Z = np.meshgrid(x, y, z, indexing='ij')
points = np.stack([X, Y, Z], axis=-1).reshape(-1, 3)

# --- Torus Path (for distance calculation) ---
theta = np.linspace(0, 2 * np.pi, NUM_CAPSULES, endpoint=False)
torus_path = np.stack([
    (MAJOR_RADIUS + MINOR_RADIUS * np.cos(0)) * np.cos(theta),
    (MAJOR_RADIUS + MINOR_RADIUS * np.cos(0)) * np.sin(theta),
    np.zeros_like(theta)
], axis=-1)

# --- Curvature Field Calculation (sample frame) ---
frame = -1  # Final frame
energy = energies[frame]

# Compute minimum distance from each grid point to the torus path
# (approximate as closest point on the torus loop)
dists = cdist(points, torus_path)
min_dists = np.min(dists, axis=1)

# Physics-based curvature field
G = 6.67430e-11
c = 299792458
curvature = (8 * np.pi * G / c**4) * energy / np.maximum(min_dists ** 2, 1e-6)
curvature_field = curvature.reshape((grid_res, grid_res, grid_res))

# --- PyVista Visualization ---
pl = pv.Plotter()

# Torus mesh
torus = pv.ParametricTorus(MAJOR_RADIUS, MINOR_RADIUS)
pl.add_mesh(torus, color='orange', opacity=0.3, label='REIL Core Torus')

# Capsules
capsule_xyz = capsule_positions[frame]
pl.add_points(capsule_xyz, color='blue', point_size=10, render_points_as_spheres=True, label='Capsules')

# Curvature field isosurface
iso_value = np.percentile(curvature_field, 99.5)
field_grid = pv.wrap(curvature_field)
field_grid = field_grid.cast_to_unstructured_grid()
field_grid = field_grid.translate((x[0], y[0], z[0]))
contours = field_grid.contour([iso_value])
pl.add_mesh(contours, opacity=0.5, cmap='plasma', label='Curvature Shell')

# Overlay symbolic tick counter and intensity meter
tick = symbolic_ticks[frame]
pl.add_text(f'Symbolic Ticks: {tick}', position='upper_left', font_size=12)
pl.add_text(f'Curvature Intensity: {iso_value:.2e}', position='lower_left', font_size=10)

# Camera controls and GUI
pl.add_axes()
pl.show_grid()
pl.enable_anti_aliasing()
pl.show(title='REIL Core 3D Curvature Viewer')
