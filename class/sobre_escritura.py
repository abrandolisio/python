#!/usr/bin/env python3

class A:
    def __init__(self):
        print(f"Inicializando A")

class B(A):
    def __init__(self):
        print(f"Inicializando B")
        super().__init__() #sobreescrivo B, va a la clase padre

b = B()

