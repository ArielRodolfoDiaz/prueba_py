def suma(a,b):
    return a+b

print(suma(215,63))

def sumaa(*args):
    total =0
    for arg in args:
        total+=arg
    return total


print(sumaa(215,63,7552,755))