print("=== AGENCIA DE VIAJES REDONDO ===")

# Precios por pasajero
precio_destino_1 = 110   # Playa
precio_destino_2 = 120   # Ciudad
precio_destino_3 = 180   # Internacional

# Ingresar número de pasajeros
pasajeros = int(input("Ingresa el número de pasajeros: "))

print("\nElige tu destino:")
print("1. Kiosko ($110 por pasajero)")
print("2. Ciudad ($120 por pasajero)")
print("3. Planta industrial ($180 por pasajero)")

opcion = int(input("Ingresa una opción (1-3): "))

# Calcular costo total
if opcion == 1:
    total = pasajeros * precio_destino_1
    destino = "Kiosko"
elif opcion == 2:
    total = pasajeros * precio_destino_2
    destino = "Ciudad"
elif opcion == 3:
    total = pasajeros * precio_destino_3
    destino = "Planta industrial"
else:
    print("Opción no válida")
    total = 0
    destino = None

# Mostrar resultado
if destino is not None:
    print("\n=== RESUMEN DEL VIAJE ===")
    print(f"Destino: {destino}")
    print(f"Pasajeros: {pasajeros}")
    print(f"Costo total: ${total}")
