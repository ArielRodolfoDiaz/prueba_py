from random import randint

print('##### Adivina #####')

numero_alazar = randint(0,100)

control = 0
numero = 0

while control<8:
    numero = int(input('Ingresa un numero de 0 a 100: '))
    if numero >= 0 or numero <= 100:
        if numero ==numero_alazar:
            print (f'Ganaste!!! el numero es: {numero_alazar}, lo hiciste en: {control+1} intentos')
            break
        elif numero< numero_alazar:  
            print ('Es mas grande')
        else:
            print ('Es mas chico')
    else:  
         print('El numero no esta en el rango de 0 a 100')
    control+=1
else:
    print (f'Perdiste!!! el numero era: {numero_alazar}')