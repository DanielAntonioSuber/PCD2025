# Crear un programa que genere 100 numeros aleatorios entre 1 y 1000
# inserte en un alista los pares y en otr alos impares
# Imprimir ambas listas y el tamaño de las mismas
import random

numeros = [ random.randint(1, 1000)  for i in range(100)]

filtrar_pares = lambda lista: [n for n in lista if n % 2 == 0]
filtrar_impares = lambda lista: [n for n in lista if n % 2 != 0]

pares = filtrar_pares(numeros)
impares = filtrar_impares(numeros)

print("La lista")
print(numeros)
print("")

print("Lista de impares")
print(impares)
print(f"La cantidad de impares es {len(impares)}\n")

print("Lista de pares")
print(pares)
print(f"La cantidad de pares es {len(pares)}")




