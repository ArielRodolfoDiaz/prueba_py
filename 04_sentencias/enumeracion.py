
lista = ['a','b','c']
index =0

for item in lista:
    print(item)
    print(index)
    index+=1

for item in enumerate(lista):
    print(item)

for indece, item in enumerate(lista):
    print(item)
    print(indece)

mi_tupla = list(enumerate("Python"))
print(mi_tupla)