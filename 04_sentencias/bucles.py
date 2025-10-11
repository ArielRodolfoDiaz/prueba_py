##### WHILE ####

moneda = 5

while moneda>0:
    print(f"Tengo {moneda} monedas")
    moneda-=1
else:
    print(f"Te quedaste sin monedas!!")

nombre = "Federico"
#### Continue
print("#### Continue ####")
for letra in nombre:
    if letra == 'r':
        continue

    print(letra)

#### Break
print("#### Break ####")
for letra in nombre:
    if letra == 'r':
        break

    print(letra)


respuesta = 's'
while respuesta == 's':
    respuesta = input("Quieres seguir s/n? ")
else:
    print("Nos vemos!!!")





"""
##### FOR ####
lista = ['a', 'b', 'c']

for letra in lista:
    numero = lista.index(letra)+1
    print(f'La letra {numero}: {letra}')

lista= ['pablo', 'laura', 'ariel', 'yesi', 'dani', 'agus']

for nombre in lista:
    if nombre.lower().startswith('a'):
        print(f'El nombre {nombre}, empieza con A')
    else:
         print(f'El nombre {nombre}, NO empieza con A')

numeros = [1,2,3,4,5,6]
res = 0

for numero in numeros:
    res += numero

print(res)

palabra = "Ariel"

for letra in palabra:
    print(letra)

dic = {"Nombre":"ariel", "Apellido":"Diaz", "Edad":39}

for dato in dic.values():
    print(dato)
for clave, valor in dic.items():
    print(clave, valor) 
"""