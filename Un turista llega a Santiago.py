import numpy as np
import matplotlib.pyplot as plt

#Metro
def f(t):
  return 0.4 * t

#Bus
def g(t):
  return 0.3 * t

y1 = f(t)
y2 = g(t)
t = np.linspace(0,10,500)

plt.plot(t,y1)
plt.plot(t,y2)
plt.xlabel("Tiempo en minutos")
plt.ylabel("Distancia recorrida")
plt.title("Distancia recorrida en metro y bus en función del tiempo")
plt.grid(True)
plt.show()
print()
print("El dominio contextualizado es [0, 15.3] minutos")
print("El medio de transporte es más conveniente en términos de tiempo, para el turista seria el metro ya que recorre 4 km en 10 min")
print("El turista tardara en llegar a su destino con cada una de las opciones alrededor de unos 10 min")
