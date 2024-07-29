#!/usr/bin/env python3
#self._dinero este es un metodo protegido
#self.__dinero este es un metodo privado

class Ejemplo:
    def __init__(self):
        # Atrivuto privado
        self.__atrivuto_privado = "Este es un atrivuto privado"

ejemplo = Ejemplo()

#para poder llamarlo tenemos que pasarle el nombre de la clase, sino da error
print(ejemplo._Ejemplo__atrivuto_privado)
