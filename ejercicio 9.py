import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from scipy.integrate import solve_ivp

# Parámetros del sistema
g = 9.81  # Gravedad (m/s^2)
l = 0.5   # Longitud del péndulo (m)
omega = 3.0  # Velocidad angular del aro (rad/s)
a = 1.5  # Radio del aro

# Ecuación de movimiento: \ddtheta = f(t, theta, theta_dot)
def ecuacion_movimiento(t, y):
    theta, theta_dot = y
    dtheta_dt = theta_dot
    dtheta_dot_dt = (a * omega * (theta_dot * np.cos(theta - omega * t) - (theta_dot - omega) * np.cos(theta - omega * t)) - g * np.sin(theta)) / (l)
   
    return [dtheta_dt, dtheta_dot_dt]

# Condiciones iniciales
theta0 = np.radians(25)  # Ángulo inicial (en radianes)
theta_dot0 = 0.0  # Velocidad angular inicial

# Tiempo de simulación
t_span = (0, 10)  # Tiempo desde 0 hasta 10 segundos
t_eval = np.linspace(t_span[0], t_span[1], 1000)  # Puntos de tiempo para evaluar la solución

# Resolver la ecuación diferencial usando solve_ivp (Runge-Kutta de 4º orden por defecto)
sol = solve_ivp(ecuacion_movimiento, t_span, [theta0, theta_dot0], t_eval=t_eval)

# Extraer los resultados
theta = sol.y[0]  # Ángulo theta en función del tiempo
t = sol.t         # Tiempo

# Posición del péndulo en coordenadas x-y
def pos_pendulo(t, theta):
    # Coordenadas del soporte (en el aro giratorio)
    x_s = a * np.cos(omega * t)
    y_s = a * np.sin(omega * t)
    
    # Posición de la masa del péndulo
    x = x_s + l * np.sin(theta)
    y = y_s - l * np.cos(theta)
    
    return x, y, x_s, y_s

# Crear la figura y los ejes
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim([-2, 2])
ax.set_ylim([-2, 2])

# Graficar el círculo que representa el aro (trayectoria del soporte)
circle = plt.Circle((0, 0), a, color='b', fill=False, linestyle='--')
ax.add_artist(circle)

# Graficar el aro y el péndulo
line, = ax.plot([], [], '-', color='blue', lw=2)  # Péndulo (línea negra)
point, = ax.plot([], [], 'o', color='red')       # Masa (punto rojo)
support, = ax.plot([], [], 'bo', lw=2)  # Soporte del péndulo (punto azul)

# Función para inicializar la animación
def init():
    line.set_data([], [])
    point.set_data([], [])
    support.set_data([], [])
    return line, point, support

# Función de animación
def animate(i):
    x, y, x_s, y_s = pos_pendulo(t[i], theta[i])
    
    # Actualizar la línea del péndulo
    line.set_data([x_s, x], [y_s, y])
    point.set_data(x, y)  # Actualizar la posición de la masa
    support.set_data(x_s, y_s)  # Actualizar la posición del soporte
    return line, point, support

# Crear la animación
ani = FuncAnimation(fig, animate, init_func=init, frames=len(t), interval=20, blit=True)

# Mostrar la animación
plt.grid(True)
plt.show()