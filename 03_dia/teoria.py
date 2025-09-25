"""
# index
mi_texto = "Esta es la una prueba"
resultado = mi_texto[-9]
print(resultado)
resultado = mi_texto.index("l")
print(resultado)
resultado = mi_texto.index("a")
print(resultado)
resultado = mi_texto.index("a",5) #iniciamos desde indice 5
print(resultado)
resultado = mi_texto.index("a",5,10)
print(resultado)
resultado = mi_texto.rindex("a") #Busca al revez
print(resultado)
"""

""" mi_texto = "ABCDEFGHIJKLMNOPQRSTVWYXZ"
resultado = mi_texto[2:7]
print(resultado)
resultado = mi_texto[:7]
print(resultado)
resultado = mi_texto[2:]
print(resultado)
resultado = mi_texto[2:10:2]
print(resultado)
resultado = mi_texto[::-1]
print(resultado) """

""" mi_texto = "Esta es la una Prueba"
resultado = mi_texto.upper()
print(resultado)
resultado = mi_texto[2].lower()
print(resultado)
resultado = mi_texto.lower()
print(resultado)
resultado = mi_texto.split()
print(resultado)
resultado = mi_texto.split('a') # se elige el separador
print(resultado)
#############
a = "aprender"
b="python"
c="es"
d="genial"
resultado = "-".join([a,b,c,d])
print(resultado)

resultado = mi_texto.find("n")
print(resultado)
resultado = mi_texto.find("w")
print(resultado)

resultado = mi_texto.replace("Prueba", "EstA")
print(resultado)

resultado = mi_texto.replace("a", "@")
print(resultado) """
"""
nombre = "Ariel"
apellido = "Diaz"
#nombre[0] = "a"
print(nombre + apellido)
print(nombre * 5)"""
#texto=
"""Yo quiero ser llorando el hortelano
de la tierra que ocupas y estercolas,
compañero del alma, tan temprano."""
"""print(texto)
print("alma" in texto)
print("almita" in texto)
print(len(texto))"""


lista = ['r','b','c',"a","f"]
print(type(lista))
otra_lista = ['a',1,26.5, True]
print(otra_lista)
print(len(otra_lista))
print(otra_lista[2])
print(otra_lista[:2])
print(otra_lista + lista)
otra_lista[2]="odlof"
print(otra_lista)
otra_lista.append(25+85j)
print(otra_lista)
elimindado = otra_lista.pop(2)
print(otra_lista)
print(elimindado)
lista.sort()
print(lista)
lista.reverse()
print(lista)