# Herencia
# Clase base o padre
class Animal:
    def __init__(self, nombre, raza):
        self.nombre = nombre
        self.raza = raza
   
        self.color = color
        self.comer = comer
        self.especie = especie

    def presentarse(self):
        return f"Hola, me llamo {self.nombre} y mi especie es {self.especie} ."

# Clase derivada o hija
class Perro(Animal):
    def __init__(self, nombre, especie):
        super().__init__(nombre, especie)  # Llamada al constructor de la clase padre
        self.ladrar = ladrar

    def presentarse(self):
        # Sobrescribimos el método de la clase padre
        return f"Hola, me llamo {self.nombre}, mi especie es {self.especie} y el sonido que yo hago es {self.ladrar}."

# Otra clase derivada
class Gato(Animal):
    def __init__(self, nombre, especie):
        super().__init__(nombre, especie)
        self.maullar = maullar

    def presentarse(self):
        return f"Hola, me llamo {self.nombre}, mi especie es {self.especie} y el sonido que yo hago {self.maullar}."

# Programa principal
if __name__ == "__main__":
    animal = Animal("animal",50)
    perro = Perro("PERRO", vivipeda, "Ladrar")
    gato = Gato("Gato", vivipeda, "maullar")

    print(animal.presentarse())
    print(perro.presentarse())
    print(gato.presentarse())