import os
from pathlib import Path, PureWindowsPath

carpeta = Path( '/Proogramacion/python/curso-midudev/06_archivos/prueba.txt')

print(carpeta.read_text())
carpeta.write_text('Nuevo')
print(carpeta.read_text())
print(carpeta.name)
print(carpeta.suffix)
print(carpeta.stem)

carpeta = Path( '/Proogramacion/python/curso-midudev/06_archivos/prueba.txt')
if not carpeta.exists():
    print('Este archivo no existe')
else:
     print('Este archivo SI existe')

print(PureWindowsPath(carpeta))

print('\n##### mas  #####\n')
##### mas  #####
base = Path.home() #directorio principal del usuario actual
print(base)

guia = Path(base,'Europa', 'Espana', Path('Barcelona', 'Sagrada Familia.txt'))
guia2 = guia.with_name('la pedrera.txt')
print(guia)
print(guia2)
print(guia.parent)
print(guia.parent.parent)

directorios  = Path('/Proogramacion/python/curso-midudev/')
for py in Path(directorios).glob('**/*.py'):
     print(py)

guia = Path('/Proogramacion/python/curso-midudev/06_archivos/prueba.txt')
en_06_archivos = guia.relative_to(Path('python'))

print(en_06_archivos)
