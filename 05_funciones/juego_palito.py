from random import shuffle

#lista inicial
palitos = ['-','--','---','----']

#mezclar plalitos
def mezclar(lista):
    shuffle(lista)
    return lista

#pedrir intento
def probar_suerte():
    intento='' 
    while intento not in ['1','2','3','4']:
        intento = input('Elige una opcion 1/2/3/4: ')
    return int(intento)


#chequear intento

def chequear_intento(lista, intentos):
    if lista[intentos-1]== '-':
        print('Pediste')
    else:
        print('Pasaste')
    print(f'Te a tocado {lista[intentos-1]}')


palitos_mescaclado = mezclar(palitos)

seleccion = probar_suerte()

chequear_intento(palitos_mescaclado, seleccion)