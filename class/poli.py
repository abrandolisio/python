#/usr/bin/env python3
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        pass

class Gato(Animal): #hereda la clase como parametro
    def hablar(self):
        return f"Miui"

class Perro(Animal):
    def hablar(self):
        return f"Guau"

def hacer_hablar(objeto):
    print(f"{objeto.nombre} dice {objeto.hablar()}")

gato = Gato("Chucho")
perro = Perro("Cane")

hacer_hablar(gato)
hacer_hablar(perro)


