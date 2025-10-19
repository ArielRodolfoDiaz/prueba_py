mi_archivo = open('06_archivos/prueba.txt', encoding='utf-8')

archivo = mi_archivo.read()
print('--- inicio ---')
print(archivo)
print('--- fin ---')

for l in archivo:
    print(f'Aca dice: {l}')

mi_archivo.close()