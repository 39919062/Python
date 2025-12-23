def f(n):
    return 8 * n + 5

print(f"La cantidad de petalos que produce en el día 17 es: {f(17)} petalos")

import numpy as np
from scipy.optimize import fsolve

def f(n):
    return 8 * n + 5 - 1669

solucion = fsolve(f,0)

print(f"Para que alcance si valor máximo de petalos tienen que transcurrir: {solucion[0]:.0f} días")

import numpy as np
from scipy.optimize import fsolve

def f(n):
    return 8 * n + 5 - 1540 

solucion = fsolve(f,0)

print(f"Para que la flor produzca 1540 pétalos tendrian que pasar: {solucion[0]:} días,")
print("por lo cual no existe un día exacto en que se produzcan 1540 pétalos")

flor_2 = []
for i in range(1, 7):
    flor_2.append(4 * 3 ** (i-1))
    print(f'Día {i}: Pétalos = {flor_2[i-1]} ') 

def g(n):
    return 4 * 3 ** (n-1)

def h(n):
    return 5 * (n-4)

total_petalos = 0

for i in range(1,7):
    total_petalos += g(i)

for i in range(7,31):
    total_petalos += h(i)

print(f"El total de pétalos que se van a perder en el mes es de: {total_petalos}")
