import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0,21,10)
y = x**3

z = np.arange(0,21,10)
xyz = x**5 + 3


plt.plot(x, y, 'r--o')
plt.plot(z,xyz,"r")
#plt.label es para poner el titulo de ambos lados segun sea xlabel o ylabel
plt.xlabel("Lado de x")
plt.ylabel("Lado de y")
#plt.title es para poner el titulo
plt.title("Grafico de coseno")
#plt.legend es para escribir el nombre de las lineas en el grafico
plt.grid(color="green", linestyle="--", linewidth=1)
plt.legend(["Uno","Dos"])
#si se le agrega una letra entre " se puede cambiar el color de la linea
#por ejemplo asi plt.plot(x,y,"r"), es segun la inicial del color, red = r, blue = b, y asi...

#Tambien existen mas caracteres:

#Estilos de línea (linestyle o ls)
#'-'	Línea sólida
#'--'	Línea discontinua
#'-.'	Línea punto-guion
#':'	Línea punteada (dots)

#Marcadores (marker)
#'.'	Punto
#','	Pixel
#'o'	Círculo
#'s'	Cuadrado
#'D'	Rombo
#'d'	Rombo delgado
#'^'	Triángulo ↑
#'v'	Triángulo ↓
#'<'	Triángulo ←
#'>'	Triángulo →
#'p'	Pentágono
#'*'	Estrella
#'h'	Hexágono 1
#'H'	Hexágono 2
#'+'	Cruz
#'x'	X
#.
#Ejemplo de como combinar todo en una sola cadena
# plt.plot(x, y, 'r--o')
# Rojo, línea discontinua, círculos

plt.show()
