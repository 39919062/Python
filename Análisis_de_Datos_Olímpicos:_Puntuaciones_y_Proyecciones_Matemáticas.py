import numpy as np

# ------------------------------------------------------------
# 1) MATRICES DE SEMANA 1 Y 2
# ------------------------------------------------------------

# Primera Semana (A)
# gm = gimnasia artística
# s  = saltos ornamentales (clavados)
# ta = tiro con arco
A = np.array([[9.5, 9.4, 9.0],   # Estados Unidos
              [9.5, 9.6, 8.8],   # China
              [8.8, 9.3, 9.2]])  # Francia

# Segunda Semana (B)
B = np.array([[9.6, 9.4, 9.2],   # Estados Unidos
              [9.7, 9.7, 9.0],   # China
              [8.8, 9.1, 9.6]])  # Francia

# a) Matriz D = mejora de la semana 2 respecto a la 1
D = B - A

print("Matriz D (Mejoras de la semana 2 respecto a la 1)")
print(D)
print()

# Interpretación de d31
print(f"Interpretación d31: {D[2,0]}")
print("Francia no mejoró ni empeoró en gimnasia artística entre semana 1 y 2.")
print()


# ------------------------------------------------------------
# 2) PROYECCIÓN: 3% DE MEJORA RESPECTO A LA SEMANA 1
# ------------------------------------------------------------

E = A * 1.03   # aumentar un 3%

# Redondeo a centésima
E = np.round(E, 2)

print("Matriz E (Proyección de la semana 3 con 3% de mejora)")
print(E)
print()

# Interpretación de e22
print(f"Interpretación e22: {E[1,1]}")
print("e22 representa la proyección del puntaje de China en saltos ornamentales para la semana 3.")
print()


# ------------------------------------------------------------
# 3) PUNTAJE TOTAL POR PAÍS SEGÚN MEDALLAS
# ------------------------------------------------------------

# F: medallas por país
# Filas: Oro, Plata, Bronce
# Columnas: EE.UU., China, Francia
F = np.array([[42, 43, 31],   # Oro
              [40, 35, 20],   # Plata
              [30, 15, 16]])  # Bronce

# G: puntaje por tipo de medalla
G = np.array([[3],   # Oro
              [2],   # Plata
              [1]])  # Bronce

# Puntaje total por país: H = F^T * G
H = np.dot(F.T, G)

print("Matriz H (Puntaje total por país)")
print(H)
print()

# Interpretación de la diferencia h11 - h21
print(f"h11 - h21 = {H[0,0]} - {H[1,0]} = {H[0,0] - H[1,0]}")
print("La diferencia indica cuántos puntos más obtuvo EE.UU. respecto a China.")
print()


# ------------------------------------------------------------
# 4) SISTEMA DE ECUACIONES PARA ORO/PLATA/BRONCE
# ------------------------------------------------------------

A_sys = np.array([[1, 1, 1],
                  [3, 2, 1],
                  [53, 40, 20]])

B_sys = np.array([[10],
                  [17],
                  [326]])

A_inv = np.linalg.inv(A_sys)
X = np.dot(A_inv, B_sys)

X = np.round(X).astype(int)  # redondeo a enteros (número de medallas)

oro, plata, bronce = X.flatten()

print("Resultados del sistema:")
print(f"Oro    (x) = {oro}")
print(f"Plata  (y) = {plata}")
print(f"Bronce (z) = {bronce}")
print()

print("Interpretación final:")
print(f"El país obtuvo {oro} oros, {plata} platas y {bronce} bronces,")
print("cumpliendo el total de medallas, el puntaje y los aportes estatales.")
