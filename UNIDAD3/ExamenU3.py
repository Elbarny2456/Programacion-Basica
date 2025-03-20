import time  # Primera librería: Para agregar pausas y simular procesos
import random  # Segunda librería: Para generar valores aleatorios
import csv

# Menú principal
def mostrar_menu():
    print("\n=== Menú Principal ===")
    print("1. Agregar datos al diccionario 1")
    print("2. Agregar datos al diccionario 2")
    print("3. Eliminar datos del diccionario")
    print("4. Mostrar contenido de los diccionarios")
    print("5. Agregar datos aleatorios a los diccionarios")
    print("6. Guardar archivos en CVS")
    print("7. Salir")

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

def guardar_diccionarios_combinados_en_csv(nombre_archivo, diccionario1, diccionario2):
    lista_combinada = [
        {"Diccionario": "Diccionario 1", "Clave": clave, "Valor": valor}
        for clave, valor in diccionario1.items()
    ] + [
        {"Diccionario": "Diccionario 2", "Clave": clave, "Valor": valor}
        for clave, valor in diccionario2.items()
    ]
    
    if lista_combinada:
        with open(nombre_archivo, mode='w', newline='', encoding='utf-8') as archivo_csv:
            escritor = csv.DictWriter(archivo_csv, fieldnames=["Diccionario", "Clave", "Valor"])
            escritor.writeheader()
            escritor.writerows(lista_combinada)
        print(f"Ambos diccionarios guardados en {nombre_archivo}.")
    else:
        print("Ambos diccionarios están vacíos, no se guardó el archivo.")
# Bucle principal
while True:
    mostrar_menu()
    opcion = input("Selecciona una opción (1-7): ")
    
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
      guardar_diccionarios_combinados_en_csv("diccionarios_combinados.csv", diccionario1, diccionario2)

    elif opcion == "7":
        # Salir del programa
        print("Saliendo del programa...")
        time.sleep(1)  # Simular una pausa
        break

    else:
        # Opción inválida
        print("Opción no válida. Por favor, selecciona un numero del 1 al 7 mensote.")
