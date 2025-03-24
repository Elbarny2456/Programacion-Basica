import csv  # Librería para leer datos del archivo CSV


def leer_archivo_csv(nombre_archivo):
    try:
        with open(nombre_archivo, mode='r', encoding='utf-8') as archivo_csv:
            lector = csv.DictReader(archivo_csv)
            print("\n=== Contenido del archivo CSV ===")
            for fila in lector:
                print(f"Diccionario: {fila['Diccionario']}, Clave: {fila['Clave']}, Valor: {fila['Valor']}")
    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo}' no existe. Por favor, verifica su nombre y ubicación.")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")


nombre_archivo = "diccionarios_combinados.csv"


leer_archivo_csv(nombre_archivo)