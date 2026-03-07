import numpy as np
import matplotlib.pyplot as plt

# Parámetros
epsilon_0 = 1.0
lambda_ = 0.05
t_values = np.linspace(0, 120, 240)

# Funciones de decaimiento
def linear_decay(t, epsilon_0, lambda_):
    return np.maximum(epsilon_0 - t * lambda_, 0)

def exponential_decay(t, epsilon_0, lambda_):
    return epsilon_0 * np.exp(-lambda_ * t)

def inverse_decay(t, epsilon_0, lambda_):
    return epsilon_0 / (1 + lambda_ * t)

# Cálculo de los valores
epsilon_linear = linear_decay(t_values, epsilon_0, lambda_)
epsilon_exponential = exponential_decay(t_values, epsilon_0, lambda_)
epsilon_inverse = inverse_decay(t_values, epsilon_0, lambda_)

# Gráfico
plt.figure(figsize=(8, 5))
plt.plot(t_values, epsilon_linear, label="Decaimiento Lineal")
plt.plot(t_values, epsilon_exponential, label="Decaimiento Exponencial")
plt.plot(t_values, epsilon_inverse, label="Decaimiento Inversamente Proporcional")
plt.xlabel("Paso $t$")
plt.ylabel("$\epsilon_t$")
plt.title("Comparación de Funciones de Decaimiento de $\epsilon$")
plt.legend()
plt.grid(True)

# Guardar el gráfico
plt.savefig("epsilon_decay_comparison.png")
