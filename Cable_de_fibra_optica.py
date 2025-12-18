import numpy as np
import matplotlib.pyplot as plt

def cable(t):
  return 1.85 * t

#Variable dependiente:    Largo del cable instalado
#Variable independiente:  Tiempo de colocado del cable
#Dominio contextualizado: [0, 3567] horas (6600 / 1.85)

t = np.linspace(0,6600,500)

plt.plot(t,cable(t))

plt.xlabel("Tiempo de la instalacion del cable")
plt.ylabel("Largo del cable instalado")
plt.title("Instalacióndel cable de fibra óptica")
plt.grid(True)
plt.show()

print(f"A las 148 horas de instalar cable se intalaron {cable(148)} metros de cable")
print(f"A las 2300 horas de instalar cable se intalaron {cable(2300)} metros de cable")
