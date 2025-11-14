#Sacar el promedio de 3 notas

nota1 = float(input("Ingrese la primera nota: "))
nota2 = float(input("Ingrese la segunda nota: "))
nota3 = float(input("Ingrese la tercera nota: "))

promedio = (nota1*0.3*nota2*0.3*nota3*0.4)
print("Su nota promedio es de", promedio)

if promedio>= 4.0:
  print("Curso aprobado!!!")
else:
  if promedio<= 3.9:
    print("Curso reprobado x")
