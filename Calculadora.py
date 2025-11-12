while True:

  print("Calculadora")
  print("***********")
  print("1. Suma")
  print("2. Resta")
  print("3. Multiplicación")
  print("4. División")
  print("5. Porcentaje")
  print()
  eleccion = int(input("Escoja una opción: "))
  print()

  if eleccion == 1:
      print("Escogiste Suma")
      num1 = int(input("Ingrese un numero: "))
      num2 = int(input("Ingrese otro numero: "))
      print(f"El resultado de la suma es de {num1 + num2}")

  elif eleccion == 2:
      print("Escogiste Resta")
      num1 = int(input("Ingrese un numero: "))
      num2 = int(input("Ingrese otro numero: "))
      print(f"El resultado de la resta es de {num1 - num2}")

  elif eleccion == 3:
      print("Escogiste Multiplicación")
      num1 = int(input("Ingrese un numero: "))
      num2 = int(input("Ingrese otro numero: "))
      print(f"El resultado de la multiplicación es de {num1 * num2}")

  elif eleccion == 4:
      print("Escogiste División")
      num1 = int(input("Ingrese un numero: "))
      num2 = int(input("Ingrese otro numero: "))
      if num2 == 0:
          print("Error: no se puede dividir por cero.")
      else:
          print(f"El resultado de la división es de {round(num1 / num2, 2)}")

  elif eleccion == 5:
      print("Escogiste Porcentaje")
      num1 = int(input("Ingrese un numero: "))
      num2 = int(input("Ingrese el porcentaje: "))
      print(f"El {num2}% de {num1} es {(num1 * num2) / 100}")

  else:
      print("Opción no válida, por favor elija del 1 al 5.")
  print()

  continuar = input("Desea volver hacer alguna operación?(s/n)").lower()
  print()
  if continuar != "s":
    print("¡Gracias por usar la calculadora! 👋")
    break
