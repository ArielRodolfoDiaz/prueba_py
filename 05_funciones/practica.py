from random import choice


palabras= ['computadora', 'teclado', 'monitor', 'mause', 'impresora']
palabra_seleccionada=''
letras_ingresadas=''
letras_acertadas=''


def elegir_palabra(palabras):
    return choice(palabras)

def mostrar_asterisco_palabra(palabra_seleccionada):
    lista = ['-' for le in palabra_seleccionada]
    print(f'La palabra tiene {len(palabra_seleccionada)} letras')
    print(''.join(lista))

def pedir_letra(letras_ingresadas):
    letra ='6'
    abecedario = 'abcdefghijklmnñopqrstuvwxyz'
    letras_permitidas =''
    for item in abecedario:
        if item not in letras_ingresadas:
            letras_permitidas+=item
    while letra not in letras_permitidas:
        letra = input('Ingrese una letra: ')
        if len(letra)>1:
            letra='*'
    return letra

def controlar_aciertos(palabra_seleccionada, letras_acertadas, letra):
    if letra in palabra_seleccionada:
        letras_acertadas+=letra 
        return [letras_acertadas, True]
    return [letras_acertadas, False]

def contro_juego(letras_acertadas, palabra_seleccionada):
    palabra=['_' for le in palabra_seleccionada]

    for item in letras_acertadas:
        for index, sub_item in enumerate(palabra_seleccionada):
            if item == sub_item:
                palabra[index]=(item)

    palabra =''.join(palabra)
    if '_'in palabra:
        return [False, palabra]
    return [True, palabra]


palabra_seleccionada = elegir_palabra(palabras)
mostrar_asterisco_palabra(palabra_seleccionada)

intentos=6

while intentos>0:
    letra = pedir_letra(letras_ingresadas)
    letras_acertadas, acerto_alguna = controlar_aciertos(palabra_seleccionada, letras_acertadas, letra)
    ok, palabra = contro_juego(letras_acertadas, palabra_seleccionada)
    if ok:
        print(f'Ganaste la palabra es: {palabra_seleccionada}')
        break
    else:
        print(f'Vida: {intentos-1}')
        print(f'{palabra}')
        if not acerto_alguna:
            intentos-=1


#print(palabra_seleccionada)
#print(letras_acertadas)