
estudiantes = {
    "Roberto": {"edad": 20},
    "saba": {"edad": 18},
    "Cristian": {"edad": 18},
    "Maria": {"edad": 20}
}

profesor = {
    "eduardo": {"Materia": "Programacion Basica", "Calificacion unidad3": 10},
    "marlenm": {"Materia": "Calculo Integral", "Calificacion unidad3": 10},
    "enrique": {"Materia": "Ciencia de los materiales", "Calificacion unidad3": 10},
    "Batista": {"Materia": "Estadistica", "Calificacion unidad3": 10},
}
print("Diccionario de estudiantes:")
for nombre, detalles in estudiantes.items():
    print(f"{nombre}: {detalles}")

