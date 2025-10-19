archivo = open('06_archivos/prueba.txt', 'w')
archivo.write('Soy coco\n')
archivo.write('soy moco\n')
archivo.write('''soy moco
              y estoy siendo literal
              kfokfof''')
archivo.writelines(['hola', 'mundo', 'aca', 'estoy'])
lista = ['hola', 'mundo', 'aca', 'estoy']
for p in lista:
    archivo.writelines(p+'\n')
archivo.close()


archivo = open('06_archivos/prueba.txt', 'a')
archivo.write('agregamos sin borrar cosas\n')
archivo.write('soy moco\n')
archivo.write('''soy moco
              y estoy siendo literal
              kfokfof''')
archivo.writelines(['hola', 'mundo', 'aca', 'estoy'])
lista = ['hola', 'mundo', 'aca', 'estoy']
for p in lista:
    archivo.writelines(p+'\n')
archivo.close()