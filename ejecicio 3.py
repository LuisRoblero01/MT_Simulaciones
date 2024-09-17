import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Parámetros
omega = 4.0  # Velocidad angular (rad/s)
theta = 0.5 # Ángulo de la varilla (rad)
g = 9.81  # Gravedad (m/s^2)
dt = 0.01  # Paso de tiempo (s)
t_max = 10  # Duración total de la simulación (s)

# Condiciones iniciales
r0 = 0.5  # Posición inicial de la partícula (m)
r_dot0 = 0.0  # Velocidad radial inicial (m/s)

# Definir la ecuación de movimiento
def r_dot_dot(r, t):
    return r * omega**2 * (np.sin(theta) + 1) - g * np.cos(theta)

# Resolver numéricamente la ecuación de movimiento
def solve_motion():
    t_vals = np.arange(0, t_max, dt)
    r = r0
    r_dot = r_dot0
    r_vals = [r]

    for t in t_vals[1:]:
        r_dot_dot_val = r_dot_dot(r, t)
        r_dot += r_dot_dot_val * dt
        r += r_dot * dt

        # Asegurarse de que r no sea negativo
        if r < 0:
            r = 0

        r_vals.append(r)

    return np.array(r_vals), t_vals

# Solucionar la ecuación de movimiento
r_vals, t_vals = solve_motion()

# Crear la función de actualización para la animación
def update(frame):
    r = r_vals[frame]
    x = r * np.cos(theta)
    y = r * np.sin(theta)

    # Actualizar la varilla (línea)
    line.set_data([0, x], [0, y])

    # Actualizar la partícula (punto rojo)
    particle.set_data([x], [y])

    return line, particle

# Configuración de la figura 2D
fig, ax = plt.subplots()
ax.set_xlim([-1, 20])
ax.set_ylim([-1, 20])
ax.set_xlabel('X (m)')
ax.set_ylabel('Y (m)')
ax.set_title('Simulación 2D de una partícula sobre una varilla giratoria')

# Crear la varilla (línea negra)
line, = ax.plot([], [], 'k-', lw=2)

# Crear la partícula (punto rojo)
particle, = ax.plot([], [], 'ro')

# Crear la animación
ani = FuncAnimation(fig, update, frames=len(t_vals), interval=30, blit=True)

# Mostrar la animación
plt.grid(True)
plt.show()