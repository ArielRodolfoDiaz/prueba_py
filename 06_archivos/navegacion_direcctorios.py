import os
from pathlib import Path

os.chdir('06_archivos') #cambiar de directorio
# os.makedirs('carpeta nueva') #crear carpeta
# os.rmdir('D:\\Proogramacion\\python\\curso-midudev\\06_archivos\\carpeta nueva') # Borrar carpeta

ruta = os.getcwd() #directorio actual
archivo = open('prueba.txt')
archivo.close()
print(ruta)

ruta = 'D:\\Proogramacion\\python\\curso-midudev\\06_archivos\\prueba.txt'
elemento = os.path.dirname(ruta) #en string 
elemento_tupla = os.path.split(ruta) #
print(elemento)
print(elemento_tupla)

##
carpeta = Path( '/Proogramacion/python/curso-midudev/06_archivos')/ 'prueba.txt'

datos = open(carpeta)
print(datos.readline())
datos.close()

print(os.path.basename(carpeta))