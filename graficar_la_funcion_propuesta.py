import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**3-12

x=np.arange(0,15,0.1)

plt.plot(x,f(x),label='f(x)')

plt.title('Título')
plt.xlabel('Eje x')
plt.ylabel('Eje y')

plt.legend()
plt.grid()
plt.show()
