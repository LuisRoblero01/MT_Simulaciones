import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Parámetros
g = 9.81  # Gravedad (m/s^2)
L = 1.0  # Longitud de la varilla (m)
dt = 0.01  # Paso de tiempo (s)
t_max = 10  # Duración total de la simulación (s)

# Condiciones iniciales
alpha0 = 1.0  # Ángulo inicial (rad)
alpha_dot0 = 0.0  # Velocidad angular inicial (rad/s)
m = 1.0  # Masa de las partículas (kg)

# Definir la ecuación de movimiento para alpha
def alpha_dot_dot(alpha):
    return   - g * np.cos(alpha)

# Resolver numéricamente la ecuación de movimiento
def solve_motion():
    t_vals = np.arange(0, t_max, dt)
    alpha = alpha0
    alpha_dot = alpha_dot0
    alpha_vals = [alpha]

    for t in t_vals[1:]:
        alpha_dot_dot_val = alpha_dot_dot(alpha)
        alpha_dot += alpha_dot_dot_val * dt
        alpha += alpha_dot * dt
        alpha_vals.append(alpha)

    return np.array(alpha_vals), t_vals

# Solucionar la ecuación de movimiento
alpha_vals, t_vals = solve_motion()

# Crear la función de actualización para la animación
def update(frame):
    alpha = alpha_vals[frame]
    
    # Posiciones de las partículas
    x1 = 0  # Partícula 1 siempre en el eje x = 0
    y1 = L * np.sin(alpha)  # Partícula 1 se mueve solo en y (V1)
    x2 = L * np.cos(alpha)  # Partícula 2 se mueve solo en x (V2)
    y2 = 0  # Partícula 2 siempre en el eje y = 0

    # Actualizar la varilla (línea)
    line.set_data([x1, x2], [y1, y2])

    # Actualizar las partículas (puntos rojos)
    particle1.set_data([x1], [y1])
    particle2.set_data([x2], [y2])

    return line, particle1, particle2

# Configuración de la figura 2D
fig, ax = plt.subplots()
ax.set_xlim([-L, L])
ax.set_ylim([-L, L])
ax.set_xlabel('X (m)')
ax.set_ylabel('Y (m)')
ax.set_title('Simulación de Partículas Conectadas por Varilla')

# Crear la varilla (línea negra)
line, = ax.plot([], [], 'k-', lw=2)

# Crear las partículas (puntos rojos)
particle1, = ax.plot([], [], 'ro')  # Partícula 1 (solo en eje y)
particle2, = ax.plot([], [], 'ro')  # Partícula 2 (solo en eje x)

# Crear la animación
ani = FuncAnimation(fig, update, frames=len(t_vals), interval=30, blit=True)

# Mostrar la animación
plt.grid(True)
plt.show()