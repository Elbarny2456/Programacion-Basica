# Clase base o padre
class Animal:
    def __init__(self, nombre, raza, especie, color):
        self.nombre = nombre
        self.raza = raza
        self.especie = especie
        self.color = color

    def presentarse(self):
        return f"Hola, me llamo {self.nombre}, soy de la especie {self.especie}, de raza {self.raza} y de color {self.color}."

# Clase derivada o hija
class Perro(Animal):
    def __init__(self, nombre, raza, especie, color, ladrar):
        super().__init__(nombre, raza, especie, color)  # Llamada al constructor de la clase padre
        self.ladrar = ladrar

    def presentarse(self):
       
        return f"Hola, me llamo {self.nombre}, soy de la especie {self.especie}, de raza {self.raza}, hago el sonido {self.ladrar}."

# Otra clase derivada
class Gato(Animal):
    def __init__(self, nombre, raza, especie, color, maullar):
        super().__init__(nombre, raza, especie, color)
        self.maullar = maullar

    def presentarse(self):
        return f"Hola, me llamo {self.nombre}, soy de la especie {self.especie}, de raza {self.raza}, hago el sonido {self.maullar}."

# Programa principal
if __name__ == "__main__":
    animal = Animal("Animal genérico", "Desconocida", "Desconocida", "Gris")
    perro = Perro("Firulais", "Chihuahua", "Canino", "Blanco", "Guau guau")
    gato = Gato("Michi", "Siames", "Felino", "Negro", "Muauuu")

    print(animal.presentarse())
    print(perro.presentarse())
    print(gato.presentarse())