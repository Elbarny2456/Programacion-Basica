
nombres = ["Sabayd", "luis", "Lupita", "victor", "Roberto", "cristian"]
edades = [18, 20, 30, 18, 19, 22, 24, 27]
Libre = ["caguama", 3, 4, "1 kilo de azucar", 54, "agua de melon"]
Materias = ["Programacion basica", "Calculo integral", "Ciencias de los materiales", "Algebra Lineal", "Contabilidad y administracion" "Estadistica y control"]
Profes = ["Eduardo Flores", "Marlem solis", "Enrique"]
print(len(nombres))#es para contar el numero de articulos en la lista
print(max(edades))#el numero max
print(min(edades))#el numero minimo
edades.sort()#ordenar menor a mayor y orden algebraico
print(edades)
#Materias.append()
Materias.remove("Programacion basica")#removeralgo de la lista#agregar elemento si le pones un numero y luego una coma lo pone en la posicion que le digas
Materias.insert(0, "Programacion Avanzada")
print(Materias)
print(Libre)
print(Profes)
for Materia in Materias:
    print(Materia)