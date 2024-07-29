#!/usr/bin/env python3

class Libro:

    IVA = 0.21


    def __init__(self, titulo, autor, precio):
        self.titulo = titulo
        self.autor = autor
        self.precio = precio

    @staticmethod #gracias a este decorador no lleva self
    def es_bestseller(total_ventas):
        return total_ventas > 5000

    @classmethod #reciven como argumento la clase, ponemos cls
    def precio_con_iva(cls, precio):
        return precio + precio * cls.IVA

mi_libro = Libro("principito", "yo", 55)

#gracias a staticmethod se llama directamente a la clase
print(Libro.es_bestseller(2000))

print(f" el precio con IVA es {Libro.precio_con_iva(mi_libro.precio)}")

