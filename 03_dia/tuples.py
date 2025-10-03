mi_tuple = (1,2,3,4,5,6,True,"Ariel")

print(mi_tuple)
print(mi_tuple[5])
print(mi_tuple[-5])

mi_lista = list(mi_tuple)
print(mi_lista)
mi_lista[1]=52
print(mi_lista)

tv = 1,2 ,3
x,y,z = tv
print(x,y,z)

tt = 1,2 ,3,1
print(len(tt))
print(tt.count(1))
print(tt.index(3))