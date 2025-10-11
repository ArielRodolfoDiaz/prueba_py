
palabra = 'python'

lista=[]

for letra in palabra:
    lista.append(letra)

print(lista)

lista = [letra for letra in palabra]
print(lista)

numero = list(range(0,150,3))
lista = [num for num in numero]
print(lista)

lista = [num/2 for num in numero]
print(lista)

lista = [num for num in numero if num%2 == 0]
print(lista)

lista = [num for num in numero if num%2 != 0]
print(lista)


pies = [10,20,30,40,50]
metros =[num/3.281 for num in pies]
equibalencia = list(zip(pies, metros))

for pie, metro in equibalencia:
    print(f'{pie} pie son: {round(metro,2) } mts') 