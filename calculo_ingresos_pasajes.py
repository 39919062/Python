cantidad_pasajes = int(input("Ingrese la cantidad de pasajes a vender: "))

total_ingresos = 0

for i in range(cantidad_pasajes):
    while True:
        try:
            precio_pasaje = float(input(f"Ingrese precio del pasaje {i+1}: $"))
            total_ingresos += precio_pasaje
            break
        except ValueError:
            print("Por favor, ingrese un valor numérico válido.")

print(f"Total de ingresos por la venta de pasajes: ${total_ingresos:.2f}")
