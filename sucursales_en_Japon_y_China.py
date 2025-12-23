import numpy as np

J = np.array([[100,200,150],
              [120,210,170],
              [112,200,131],
              [124,310,170],
              [136,156,140]])

C = np.array([[110,190,160],
              [130,220,180],
              [146,190,141],
              [143,312,163],
              [137,116,156]])
#Respuesta 1
print("Orden de las matrices:", J.shape)  # (5, 3)

#Respuesta 2
j21 = J[1,0]   # fila 2, col 1
c12 = C[0,1]   # fila 1, col 2
print("j21 (J[1,0]) =", j21, "miles de dólares")
print("c12 (C[0,1]) =", c12, "miles de dólares")

#Respuesta 3
T = J + C
print("\nMatriz T = J + C:\n", T)

# Costo total por modelo (suma de columnas por fila)
totales_por_modelo = T.sum(axis=1)
print("\nCosto total por modelo (miles de dólares):")
for i, total in enumerate(totales_por_modelo, start=1):
    print(f"  Modelo {i}: {total} (=> ${total*1000:,.0f})")

#Respuesta 4
# Chequeo trabajador: producto 3, modelo 4
jap = J[3,2]
chi = C[3,2]
print(f"\nProducto 3, modelo 4 -> Japón: {jap}, China: {chi}")
print("El trabajador tiene razón." if jap > chi else "No tiene razón.")
