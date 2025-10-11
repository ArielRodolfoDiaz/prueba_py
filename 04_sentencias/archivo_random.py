from random import *

aleatorio = randint(1,50)

print(aleatorio)

aleatorio = uniform(1,5)
print(aleatorio)
print(round(aleatorio,2))

aleatorio = random()
print(aleatorio)
print(round(aleatorio,2))

colores = ['azul', 'rojo', 'verde', 'amarilla']
aleatorio = choice(colores)
print(aleatorio)

numeros = list(range(5,51,5))
print(numeros)

shuffle(numeros)
print(numeros)