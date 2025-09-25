import os
os.system("clear")

print("Sentencia simple")

edad = 28

if edad >18:
    print('mayor de edad 18')
elif edad == 18:
    print('tiene 18')
else:
     print('mocoso')


tiene_carnet=True

if edad >=25 and tiene_carnet:
    print("puedes manejar en Chile")

edad =17
tiene_carnet=False
if edad >=18 or tiene_carnet:
    print("puedes manejar en Arg")

if edad >=18 or not tiene_carnet:
    print("puedes manejar en cge")


print("manzana<manzane : ","manzana"<"manzane")
print("Hola = hola : ", "Hola"=="hola")

print('ternaria:')
print("valor si cumple if 'condicion' else valor si no cumple")
print ("'Es mayor de Edad' if edad >18 else 'Es menor'" )

edad =17
print("Es mayor de Edad" if edad >18 else "Es menor" )