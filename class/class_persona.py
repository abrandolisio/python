#!/usr/bin/env python3

class Persona:
    def __init__(self, nombre, edad):# Persona.__init__(juan, nombre, edad)
        self.nombre = nombre # ests son variables del objeto, no de la clase
        self.edad = edad

# self hace referencia al objeto que le estamos pasando (juan)
# cls hace referencia a la clase
    def saludo(self): # Persona.saludo(juan)
        return f"Hola, mi nombre es {self.nombre} y mi edad es {self.edad}"

juan = Persona("juan", 23)

print(juan.saludo())

