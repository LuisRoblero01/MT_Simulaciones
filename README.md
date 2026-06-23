# Theoretical Mechanics — Physical System Simulations

Python simulations and animations of physical systems studied in **Theoretical
Mechanics**. Each script numerically integrates the equations of motion of a
system and produces an animated visualization of its dynamics.

## Contents

| Script | System |
|--------|--------|
| `ejercicio 1.py` | Pendulum / rigid rod under gravity |
| `ejercicio 3.py` | Rotating rod (angular dynamics) |
| `ejercicio 5.py` | Coupled two-mass system |
| `ejercicio 9.py` | Pendulum dynamics (solved with `solve_ivp`) |

## Methods

- Numerical integration of the equations of motion (`scipy.integrate.odeint`
  and `solve_ivp`).
- Real-time animation of the trajectories with `matplotlib.animation`.

## Tech stack

Python · NumPy · SciPy · Matplotlib

## Run

```bash
pip install numpy scipy matplotlib
python "ejercicio 1.py"
```
