mascota = 'gato'

if mascota == 'nada':
    print("Es correcto")
elif mascota == 'gato':
    print("Medio correcto")
else:
    print("No Es correcto")


edad = 16
calificaciones = 7

if edad < 18:
    print("Eres menor de edad")
    if calificaciones >= 7:
        print("aprobaste el examen")
    else:
        print("desaprobaste el examen")
else:
     print("Eres Mayor de edad")