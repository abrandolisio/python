#/usr/bin/env python
juegos = {"juego 1", "juego 2", "juego 3"}

tope = 27

generos = {
    "juego 1": "accion",
    "juego 2": "adventura",
    "juego 3": "fantacia"
}

ventas_stock = {
    "juego 1": (150, 23),
    "juego 2": (30, 45),
    "juego 3": (23, 89)
}

clientes = {
    "juego 1": {"juan", "pedro", "charly"},
    "juego 2": {"pedro", "sara", "ofelia"},
    "juego 3": {"sebastian", "sara", "cris"}
}

def sumario(juego):
    print(f"\n[i] Resumen del juego {juego}")
    print(f"[+] El genero del juego es {generos[juego]}")
    print(f"[+] Las ventas de este juego son {ventas_stock[juego][0]}")
    print(f"[+] El stock de este juego es {ventas_stock[juego][1]}")
    print(f"[+] Los clientes que han comprardo este juego son {', '.join(clientes[juego])}")



for juego in juegos:
    if ventas_stock[juego][0] > tope:
        sumario(juego)

ventas_totales = lambda : sum( ventas for juego, (ventas, _) in ventas_stock.items() if ventas_stock[juego][0] > tope)

print(f"\n Las ventas totales del juego son {ventas_totales()}")




