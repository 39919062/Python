total_ventas = 0.0
contador_ventas = 0

print("Bienvenido al sistema de ventas de videojuegos.")
print("Escriba 'salir' en cualquier momento para terminar.\n")

while True:
    try:
        num_ventas = int(input("¿Cuántas ventas desea registrar? "))
        if num_ventas <= 0:
            print("El número de ventas debe ser un entero positivo. Intente de nuevo.")
        else:
            break
    except ValueError:
        print("Error: Debe ingresar un número entero válido.")

for i in range(num_ventas):
    while True:
        precio = input(f"Ingrese el precio del videojuego #{i + 1}: ")

        if precio.lower() == 'salir':
            print("\nProceso finalizado por el usuario.")
            num_ventas = 0  
            break

        try:
            precio_float = float(precio)

            if precio_float < 0:
                print("El precio no puede ser negativo. Intente de nuevo.")
            else:
                total_ventas += precio_float
                contador_ventas += 1
                print(f"Venta registrada: ${precio_float:.2f}. Total acumulado: ${total_ventas:.2f}.\n")
                break

        except ValueError:
            print("Error: Ingrese un número válido.\n")

    if num_ventas == 0:
        break

print("\nResumen de ventas:")
print(f"Total de videojuegos vendidos: {contador_ventas}")
print(f"Ingresos totales: ${total_ventas:.2f}")
