import csv


def guardar_diccionarios_en_csv(archivo, datos):
    """Guarda una lista de diccionarios en un archivo CSV."""
    if datos:
        encabezados = datos[0].keys()
        with open(archivo, mode='w', newline='', encoding='utf-8') as archivo_csv:
            escritor = csv.DictWriter(archivo_csv, fieldnames=encabezados)
            escritor.writeheader()
            escritor.writerows(datos)
    else:
        print("La lista de datos está vacía.")

def leer_diccionarios_de_csv(archivo):
    """Lee un archivo CSV y devuelve una lista de diccionarios."""
    with open(archivo, mode='r', newline='', encoding='utf-8') as archivo_csv:
        lector = csv.DictReader(archivo_csv)
        datos = [fila for fila in lector]
    return datos


from Archivos import guardar_diccionarios_en_csv
# Nombre del archivo a leer y de la función a importar

archivo = "datos.csv"
# Nombre del archivo
datos = [
    {"Nombre": "Juan", "Edad": 25, "Ciudad": "Madrid"},
    {"Nombre": "Ana", "Edad": 30, "Ciudad": "Barcelona"},
    {"Nombre": "Luis", "Edad": 35, "Ciudad": "Valencia"}
]
#Diccionarios a guardar

# Guardar los diccionarios en un archivo csv
guardar_diccionarios_en_csv(archivo, datos)
try:
    datos_leidos = leer_diccionarios_de_csv(archivo)
    print("Datos leídos del archivo CSV:")
    for diccionario in datos_leidos:
        print(diccionario)
except FileNotFoundError:
    print(f"El archivo '{archivo}' no se encontró. Por favor, verifica que existe.")
except Exception as e:
    print(f"Ocurrió un error al leer el archivo: {e}")
