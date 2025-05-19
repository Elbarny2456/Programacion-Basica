def analizar_texto(texto):

    contador_vocales = 0
    contador_consonantes = 0
    contador_numeros = 0
    contador_otros = 0


    for caracter in texto:
        caracter = caracter.lower() 
        
        if caracter in 'aeiou':
            contador_vocales += 1
        elif caracter.isalpha():
            contador_consonantes += 1
        elif caracter.isdigit():
            contador_numeros += 1
        else:
            contador_otros += 1

    print("Vocales:", contador_vocales)
    print("Consonantes:", contador_consonantes)
    print("Números:", contador_numeros)
    print("Otros caracteres:", contador_otros)


texto = input("Introduce un texto para analizar: ")
analizar_texto(texto)