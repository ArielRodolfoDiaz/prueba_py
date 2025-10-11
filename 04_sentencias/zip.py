# Es para unir dos lista

nombres = ['Agus', 'Ariel', 'Yesica']
apellidos = ['Diaz', 'Dias', 'Tello']
edades = [11,39,37]

combinados = zip(nombres, edades)
print(combinados)

combinados = list(zip(nombres, edades))
print(combinados)

combinados = list(zip(nombres, apellidos, edades))
print(combinados)

for nombre, apellido, edad in combinados:
    print(f'Hola {nombre}, {apellido} tiene {edad} anos')