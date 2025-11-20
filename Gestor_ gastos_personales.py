total_gastos = 0
gasto = 0
continuar = "si"
Sueldo = 0

Sueldo = int(input("¿Cuánto es tu sueldo?: $"))
print()

while continuar == "si":

    print("Gestor de gastos mensuales")
    print("---------------------------")
    print("1. Agua")
    print("2. Luz")
    print("3. Gas")
    print("4. Mercadería")
    print("5. Locomoción")
    print("6. Internet")
    print("7. Streaming (Netflix, Spotify, Disney, etc.)")
    print("8. Salud y cuidado personal")
    print("9. Peluquería / barbería")
    print("10. Ropa y accesorios")
    print("11. Cuidado para las mascotas")
    print("12. Ahorros")
    print("13. Otros")
    print()

    opcion = int(input("Escoja una opción: "))
    print()

    gasto = int(input("Ingrese el gasto a pagar de la categoría elegida: $"))
    print()

    total_gastos += gasto

    continuar = input("¿Desea seguir agregando más gastos mensuales? (si/no): ").lower()
    print()

print(f"El total de sus gastos mensuales es de ${total_gastos}")
print()
print(f"Tu sueldo: ${Sueldo} - tus gastos: ${total_gastos} = diferencia: ${Sueldo - total_gastos}")
