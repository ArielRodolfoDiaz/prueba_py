texto = input('Ingrese un texto: ').lower()
letras = input("Ingrese tres letras separada por un espacio:").lower().split()

for letra in letras:
    print(f'La letra {letra}, se repite: {texto.count(letra)} veces.')

palabras = texto.split()
print(f'El texto tiene: {len(palabras)} palabras.')
print(f'La primer letra del texto es: "{texto[0]}", la ultima es: "{texto[-1]}".')
palabras.reverse()
print(f'Texto con palabras invertidos: {" ".join(palabras)}')
no_esta=texto.find('python')==-1
print(f'La palabra "python": {"No esta" if no_esta else "Si esta"}.')