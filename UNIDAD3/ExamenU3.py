import time  # Primera librería: Para agregar pausas y simular procesos
import random  # Segunda librería: Para generar valores aleatorios

# Menú principal
def mostrar_menu():
    print("\n=== Menú Principal ===")
    print("1. Agregar datos al diccionario 1")
    print("2. Agregar datos al diccionario 2")
    print("3. Eliminar datos del diccionario")
    print("4. Mostrar contenido de los diccionarios")
    print("5. Agregar datos aleatorios a los diccionarios")
    print("6. Salir")

# Diccionarios iniciales
diccionario1 = {}
diccionario2 = {}
# Función para generar datos aleatorios
def agregar_dato_aleatorio():
    clave = f"clave_{random.randint(1, 100)}"  # Clave aleatoria
    valor = f"valor_{random.randint(1, 100)}"  # Valor aleatorio
    if random.choice([True, False]):  # Elegir diccionario aleatoriamente
        diccionario1[clave] = valor
        print(f"Dato aleatorio agregado al diccionario 1: {clave} -> {valor}")
    else:
        diccionario2[clave] = valor
        print(f"Dato aleatorio agregado al diccionario 2: {clave} -> {valor}")
# Bucle principal
while True:
    mostrar_menu()
    opcion = input("Selecciona una opción (1-6): ")
    
    if opcion == "1":
        # Agregar datos al diccionario 1
        clave = input("Introduce la clave: ")
        valor = input("Introduce el valor: ")
        diccionario1[clave] = valor
        print(f"Dato agregado al diccionario 1: {clave} -> {valor}")

    elif opcion == "2":
        # Agregar datos al diccionario 2
        clave = input("Introduce la clave: ")
        valor = input("Introduce el valor: ")
        diccionario2[clave] = valor
        print(f"Dato agregado al diccionario 2: {clave} -> {valor}")

    elif opcion == "3":
        # Eliminar datos del diccionario
        clave = input("Introduce la clave a eliminar: ")
        if clave in diccionario1:
            del diccionario1[clave]
            print(f"Clave '{clave}' eliminada del diccionario 1.")
        elif clave in diccionario2:
            del diccionario2[clave]
            print(f"Clave '{clave}' eliminada del diccionario 2.")
        else:
            print("La clave no existe en ninguno de los diccionarios.")

    elif opcion == "4":
        # Mostrar el contenido de los diccionarios
        print("\nContenido del diccionario 1:")
        for clave, valor in diccionario1.items():
            print(f"{clave}: {valor}")
        print("\nContenido del diccionario 2:")
        for clave, valor in diccionario2.items():
            print(f"{clave}: {valor}")
    elif opcion == "5":
        # Agregar datos aleatorios a un diccionario
        agregar_dato_aleatorio()

    elif opcion == "6":
        # Salir del programa
        print("Saliendo del programa...")
        time.sleep(1)  # Simular una pausa
        break

    else:
        # Opción inválida
        print("Opción no válida. Por favor, selecciona una opción del menú.")