def contar_palabras():
    nombre_programa = input("introduce el nombre del programa:")
    print("has iniciado el programa", nombre_programa)
    texto_usuario = input("escribe una frase o texto:")
    cantidad_palabras = len(texto_usuario.split())
    print("el texto contiene", cantidad_palabras, "palabras")
contar_palabras()