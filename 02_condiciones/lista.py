## Listas

lista =[1,2,3,4,5]
lista2= ["a", "b", "c", "d","e"]
lista3= [1, "b", 25.8, "d", True]

print(lista)
print(lista2)
print(lista2[0])
print(lista2[-1])
print(lista3)

print('Matrices')
matris = [[1,1],[1,2],[2,1],[2,2]]

print(matris)
print(matris[2][1])

print("slicing - cortar lista")
print(lista2)
print(lista2[1:4])
print(lista2[:4])
print(lista2[2:])
print(lista2[:])
print("dar vuelta lista")
print(lista2[::-1])

print("modificar lista")
lista =[1,2,3,4,5,6,7,8,9,10]
print(lista)
lista[5]=8
print(lista)

lista=lista + [11,12,13]
print(lista)

lista += [14,15,16]
print(lista)

print(f"La longitud de la lista: {len(lista)}")
