import numpy as np

# Physical constants
G = 6.67430e-11  # m^3 kg^-1 s^-2
c = 299792458    # m/s


def simulate_reil_core(num_capsules=100, major_radius=0.25, minor_radius=0.05, sim_time=60.0, dt=0.1, mass=1.0, velocity_init=50.0, kick_threshold=0.99, drag=0.0, asymmetry=False):
    timesteps = int(sim_time / dt)
    # Capsule velocities (optionally asymmetric)
    velocities_init = np.ones(num_capsules) * velocity_init
    if asymmetry:
        velocities_init[:num_capsules//2] *= 0.9
        velocities_init[num_capsules//2:] *= 1.1
    velocities = np.zeros((timesteps, num_capsules))
    velocities[0] = velocities_init
    energies = np.zeros(timesteps)
    kicks = np.zeros(timesteps, dtype=int)
    symbolic_ticks = np.zeros(timesteps, dtype=int)
    # Capsule positions: [timesteps, num_capsules, 3]
    capsule_positions = np.zeros((timesteps, num_capsules, 3))
    theta0 = np.linspace(0, 2 * np.pi, num_capsules, endpoint=False)

    for t in range(1, timesteps):
        velocities[t] = velocities[t-1] * (1 - drag * dt)
        # Kick logic
        if np.any(velocities[t] < velocities_init * kick_threshold):
            velocities[t] = velocities_init
            kicks[t] = 1
        # Symbolic tick: increment if no kick
        symbolic_ticks[t] = symbolic_ticks[t-1] + (1 if kicks[t]==0 else 0)
        # Kinetic energy sum
        energies[t] = np.sum(0.5 * mass * velocities[t]**2)
        # Capsule positions (parametric torus)
        # Each capsule advances along the torus by arc length
        phi = (theta0 + (velocities[t] / major_radius) * t * dt) % (2 * np.pi)
        x = (major_radius + minor_radius * np.cos(0)) * np.cos(phi)
        y = (major_radius + minor_radius * np.cos(0)) * np.sin(phi)
        z = minor_radius * np.sin(0) * np.ones_like(phi)
        capsule_positions[t] = np.stack([x, y, z], axis=-1)

    # Initial frame
    energies[0] = np.sum(0.5 * mass * velocities[0]**2)
    phi = (theta0) % (2 * np.pi)
    x = (major_radius + minor_radius * np.cos(0)) * np.cos(phi)
    y = (major_radius + minor_radius * np.cos(0)) * np.sin(phi)
    z = minor_radius * np.sin(0) * np.ones_like(phi)
    capsule_positions[0] = np.stack([x, y, z], axis=-1)

    return capsule_positions, energies, kicks, symbolic_ticks
