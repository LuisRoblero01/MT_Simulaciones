import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from scipy.integrate import odeint

# Parámetros del sistema
m1 = 2.0  # masa de m1
m2 = 5.0  # masa de m2
l = 1.0   # longitud de la varilla
g = 9.81  # aceleración gravitacional
k = 10.0   # constante elástica

# Condiciones iniciales
x2_0 = 0.0      # posición inicial de x2
vx2_0 = 0.0     # velocidad inicial de x2
theta_0 = 1.5  # ángulo inicial
vtheta_0 = 0.0  # velocidad angular inicial

# Ecuaciones de movimiento
def derivadas(y, t):
    x2, vx2, theta, vtheta = y
    # Calcular ddtheta primero
    ddtheta = (np.sin(theta) * (vx2 * vtheta - g) - np.cos(theta) * (- 2 * k * x2 - m1 * l * (- (vtheta**2) * np.sin(theta)) / (m1 + m2))) / l

    # Luego calcular ddx1 usando el valor de ddtheta
    ddx2 = (- 2 * k * x2 - m1 * l * (ddtheta * np.cos(theta) - (vtheta**2) * np.sin(theta)) / (m1 + m2))

    return [vx2, ddx2, vtheta, ddtheta]

# Vector de condiciones iniciales
y0 = [x2_0, vx2_0, theta_0, vtheta_0]

# Tiempo de simulación
t = np.arange(0, 10, 0.1)

# Solución de las ecuaciones diferenciales
sol = odeint(derivadas, y0, t)

# Separar las soluciones
x2_sol = sol[:, 0]
theta_sol = sol[:, 2]

# Animación
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)

line, = ax.plot([], [], 'o-', lw=2)

def init():
    line.set_data([], [])
    return line,

def update(i):
    x2 = x2_sol[i]
    theta = theta_sol[i]
    x_mass2 = x2 + l * np.sin(theta)
    y_mass2 = -l * np.cos(theta)
    line.set_data([x2, x_mass2], [0, y_mass2])
    return line,

ani = FuncAnimation(fig, update, frames=len(t), init_func=init, blit=True)
plt.grid(True)
plt.show()