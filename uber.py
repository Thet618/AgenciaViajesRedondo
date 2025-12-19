print("=== AGENCIA DE VIAJES REDONDO - UBER ===")

# Precios por pasajero según tipo de Uber
precio_uber_x = 95
precio_uber_comfort = 130
precio_uber_black = 180

# Ingresar número de pasajeros
pasajeros = int(input("Ingresa el número de pasajeros: "))

print("\nElige el tipo de vehículo Uber:")
print("1. UberX ($95 por pasajero)")
print("2. Uber Comfort ($130 por pasajero)")
print("3. Uber Black ($180 por pasajero)")

opcion = int(input("Ingresa una opción (1-3): "))

# Calcular costo total
if opcion == 1:
    total = pasajeros * precio_uber_x
    vehiculo = "UberX"
elif opcion == 2:
    total = pasajeros * precio_uber_comfort
    vehiculo = "Uber Comfort"
elif opcion == 3:
    total = pasajeros * precio_uber_black
    vehiculo = "Uber Black"
else:
    print("Opción no válida")
    total = 0
    vehiculo = None

# Mostrar resultado
if vehiculo is not None:
    print("\n=== RESUMEN DEL VIAJE ===")
    print(f"Vehículo: {vehiculo}")
    print(f"Pasajeros: {pasajeros}")
    print(f"Costo total: ${total}")
