#/usr/bin/env python3

#creo y abro el file
f = open("algo.txt", "w")

f.write("Hola Boludo")

#cierro el file
f.close()

#una opcion mas obtimal es con with, porque cierra en automatico

with open("algo.txt", "w") as f:
    f.write("dale boludo")

with open("/etc/hosts", "r") as h:
    for line in h:
        print(line.strip())
