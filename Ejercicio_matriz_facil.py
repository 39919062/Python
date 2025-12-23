#Respuesta 1
print("Son matrices de 3 filas con 4 columnas")
print()
import numpy as np

A = np.array([[2.6,4.8,1.8,0.9],
              [3.2,4.4,2.5,2.8],
              [2.4,3.6,3.8,2.5]])

B = np.array([[3.6,2.5,3.0,2.5],
              [4.5,5.0,3.5,3.8],
              [2.9,3.0,4.6,4.0]])

S = A + B
D = B - A
#Respuesta 2
print("Suma de ambas matrices")
print(S)
print()
#Respuesta 3
print("Resta de ambas matrices")
print(D)
print()

#Respuesta 4
print("El valor s24 es: 6.6")
print("El valor d24 es: 1.0")


print(S[1,3]) #Tambien se puede sacando con un codigo pero restandole -1 porque en python todo parte de 0
print()
#Respuesta 5
print("No se puede realizar la suma, porque la matriz E no tiene el mismo orden que A y B.")
