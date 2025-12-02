puntaje = 0

print("¿Cuál de los siguientes animales vive en el agua?")
print("1) Perro")
print("2) Cocodrilo")
print("3) Conejo")
print("4) Tiburón")

resp = int(input("Ingrese número de respuesta: "))

if resp == 1:
    puntaje += 0
    print("Tu puntaje es 0")
elif resp == 2:
    puntaje += 0.5
    print("Tu puntaje es 0.5")
elif resp == 3:
    puntaje += 0
    print("Tu puntaje es 0")
elif resp == 4:
    puntaje += 1
    print("Tu puntaje es 1.0")
else:
    print("Respuesta inválida")

print("Su puntaje total es:", puntaje)
