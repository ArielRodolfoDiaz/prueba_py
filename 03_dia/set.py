mi_set = {1,1,1,1,2,3,4,5,6}
mit_set = set([1,2,3,4,5,6,6,6,8])

print(mi_set)
print(mit_set)

print(len(mi_set))

consulta = 2 in mi_set
print(consulta)

union = mi_set.union(mit_set)
print(union)

union.add(9)
union.add(8)
print(union)

union.remove(5)
print(union)

union.discard(55)
print(union)

eleminado = union.pop()
print(union)
print(eleminado)

union.clear()
print(union)
