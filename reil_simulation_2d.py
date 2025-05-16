import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.cm as cm

# --- Physical Constants ---
G = 6.67430e-11
c = 299792458

# --- Simulation Parameters ---
num_capsules = 100
mass = 1.0
velocity_init = 50.0
radius_core = 0.1
simulation_time = 60.0
time_step = 0.1
timesteps = int(simulation_time / time_step)
kick_threshold = 0.99

drag = 0.0  # Set >0 for realism

# --- Asymmetry Drift Test ---
# First half +10%, second half -10%
velocities_init = np.ones(num_capsules) * velocity_init
velocities_init[:num_capsules//2] *= 1.1
velocities_init[num_capsules//2:] *= 0.9

velocities = np.zeros((timesteps, num_capsules))
velocities[0] = velocities_init
energies = np.zeros(timesteps)
kicks = np.zeros(timesteps, dtype=int)
symbolic_ticks = np.zeros(timesteps, dtype=int)

# --- 2D Grid for Curvature Field ---
grid_size = 100
extent = 0.5  # meters from center
x = np.linspace(-extent, extent, grid_size)
y = np.linspace(-extent, extent, grid_size)
X, Y = np.meshgrid(x, y)
# Distance to torus center (assume torus at origin, radius_core)
radius_grid = np.sqrt(X**2 + Y**2)
curvature_grid = np.zeros((timesteps, grid_size, grid_size))

# --- Simulation Loop ---
for t in range(1, timesteps):
    velocities[t] = velocities[t-1] * (1 - drag * time_step)
    # Kick logic
    if np.any(velocities[t] < velocities_init * kick_threshold):
        velocities[t] = velocities_init
        kicks[t] = 1
    # Symbolic tick: increment if no kick
    symbolic_ticks[t] = symbolic_ticks[t-1] + (1 if kicks[t]==0 else 0)
    # Kinetic energy
    energies[t] = np.sum(0.5 * mass * velocities[t]**2)
    # Curvature field at each (x, y)
    # Avoid division by zero at torus core
    r2 = np.maximum(radius_grid**2, 1e-6)
    curvature_grid[t] = (8 * np.pi * G / c**4) * energies[t] / r2

# --- Visualization: Animated Heatmap ---
fig, ax = plt.subplots(figsize=(6,5))

cax = ax.imshow(curvature_grid[0], extent=[-extent, extent, -extent, extent], origin='lower', cmap=cm.plasma, vmin=0, vmax=np.max(curvature_grid))
cb = fig.colorbar(cax, ax=ax, label="Curvature Intensity")
ax.set_title("REIL Core 2D Curvature Field")
ax.set_xlabel("x (m)")
ax.set_ylabel("y (m)")

# For drift: track center of mass of curvature field
com_x = np.zeros(timesteps)
com_y = np.zeros(timesteps)
for t in range(timesteps):
    total = np.sum(curvature_grid[t])
    if total > 0:
        com_x[t] = np.sum(X * curvature_grid[t]) / total
        com_y[t] = np.sum(Y * curvature_grid[t]) / total
    else:
        com_x[t] = 0
        com_y[t] = 0

# Animation update
symbolic_colors = cm.winter(np.linspace(0,1,np.max(symbolic_ticks)+1))
def update(frame):
    cax.set_data(curvature_grid[frame])
    # Overlay symbolic tick color at center
    tick = symbolic_ticks[frame]
    ax.set_title(f"REIL Core 2D Curvature Field\nTime: {frame*time_step:.1f}s | Symbolic Ticks: {tick}")
    # Plot COM drift
    ax.plot(com_x[:frame], com_y[:frame], color='white', lw=1, alpha=0.7)
    return [cax]

ani = FuncAnimation(fig, update, frames=timesteps, blit=True)
ani.save("reil_core_curvature2d.gif", writer='pillow', fps=30)

# Print summary
print(f"Final kinetic energy at {simulation_time}s: {energies[-1]:.2f} J")
print(f"Total kick pulses required: {np.sum(kicks)}")
print(f"Max symbolic ticks: {np.max(symbolic_ticks)}")
print(f"COM drift: x={com_x[-1]:.3f} m, y={com_y[-1]:.3f} m")
