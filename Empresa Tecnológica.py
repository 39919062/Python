import numpy as np

# Software (Norte, Sur, Este, Oeste)
S = np.array([[260,320,240,480],   #P1
              [440,360,180,250],   #P2
              [380, 90,280,250]])  #P3

# Hardware (Norte, Sur, Este, Oeste)
H = np.array([[360,450,290,250],   #P1
              [500,300,300,350],   #P2
              [460,250,380,400]])  #P3

T = S + H

# Respuesta 1
print("Matriz T")
print(T)
print()

# Respuesta 2
print(f"Software zona sur: {S[:,1].sum()}")
print(f"Hardware zona sur: {H[:,1].sum()}")
print("Es correcta su afirmación, ya que en la zona sur se vendieron más productos de hardware que de software.")
print()

# Respuesta 3
S_nueva = S * 1.07
H_nueva = H * 1.03
M = S_nueva + H_nueva
np.set_printoptions(precision=2)
print("Matriz Black Friday")
print(M)
print(zdvzdzvd)

# Respuesta 4
print(f"El elemento T24 es: {T[1,3]} y representa el total del producto P2 en la zona oeste.")
print(f"El elemento M31 es: {M[2,0]} y representa el total del producto P3 en la zona norte durante el Black Friday.")
print()

# Respuesta 5
M_t = M.T
print("Matriz M traspuesta")
print(M_t)
print()
print(f"El elemento M.T41 es: {M_t[3,0]} y representa el total del producto P1 en la zona oeste durante el Black Friday.")
