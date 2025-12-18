import numpy as np
import matplotlib.pyplot as plt

def T(t):
    return -0.5 * t**2 + 3 * t + 20

# Gráfico
t = np.linspace(0, 9, 500)
y = T(t)

plt.plot(t, y)
plt.xlabel("Tiempo (horas)")
plt.ylabel("Temperatura (°C)")
plt.title("Temperatura del servidor durante la jornada laboral")
plt.grid(True)
plt.show()

# Cálculo del máximo
a = -0.5
b = 3
t_max = -b / (2 * a)
T_max = T(t_max)

print("Máxima temperatura en t =", t_max)
print("Temperatura máxima =", T_max)

# Valores pedidos
print("Temperatura a las 13:00 =", T(5))
print("Temperatura a las 17:00 =", T(9))
