#!/usr/bin/env python3

class Rectangulo:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    @property
    def area(self):
        """The area property."""
        return self.ancho * self.alto
    
    def __str__(self):
        return f"las propiedades son ancho {self.ancho} e alto {self.alto}"

rec1 = Rectangulo(20, 80)

#python interpreta que deve llamar a __str__
print(rec1)

print(f" el area es {rec1.area}")
#rec1.area propiedad del objeto sin ()


