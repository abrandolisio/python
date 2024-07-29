#!/usr/bin/env python

# Definizione classe con la parola riservata class,
# Il nome della classe deve iniziare con maiuscola seguito dai :
class Aniaml:
    # È un metodo di istanza che funge da costruttore per la classe 
    # Viene chiamato automaticamente quando viene creata una nuova istanza
    # della classe, permettendo di inizializzare gli attributi dell'oggetto.
    def __init__(self, nombre):
        # Il termine self è una convenzione utilizzata per rappresentare l'istanza
        # della classe.
        # E il primo parametro di qualsiasi metodo di istanza in una classe,
        # ed è attraverso self che possiamo accedere agli attributi e ai metodi
        # della classe stessa.
        self.nombre = nombre # Attributo di istanza 

        def hablar(self):
            pass


class Gato(Animal):
    def hablar(self):
        return f"Miau"

class Perro(Animal):
    def hablar(self):
        return f"Guau"

def hacer_hablar(obj):
    print(f"{obj.nombre} dice {obj.hablar()}")

gato = Gato("Chucho")
perro = Perro("Cane")

hacer_hablar(gato)
hacer_hablar(perro)
