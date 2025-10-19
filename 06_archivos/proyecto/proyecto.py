from pathlib import Path
from os import system, getcwd

def navegar_categoria():
    categorias = Path(getcwd(),'06_archivos','proyecto', 'recetas')
    lista_categoria = []
    filtro_cat =''
    entrada_cat ='e'
    
    while True:
        system('cls')
        print('Categorias')
        print('Escriba "Enter" para volver')
        for index, cat in enumerate( Path(categorias).glob('*')):
            lista_categoria.append(cat)
            filtro_cat+=str(index)
            print(f'[{index}] - {cat.stem}')
        entrada_cat = input('Ingrese Alguna categoria: ')
        if entrada_cat == "":  
            return False
        if entrada_cat in filtro_cat:
            return Path(lista_categoria[int(entrada_cat)])
    
def crear_receta():
    recetas = navegar_categoria()
    if recetas== False:
        return
    system('cls')
    print('Crear Recetas')
    print('Escriba "Enter" para volver')
    creado = False
    while not creado:
        nombre = input('Ingrese el nombre de la receta: ')
        if nombre == "":  
            break 
        if len(nombre)>3:
            arch = Path(recetas,f'{nombre}.txt')
            print('Contenido')
            contenido = input('Ingredientes: ')
            arch.write_text(contenido)
            #arch.write_text("Ingredientes:\n- Manzanas\n- Harina\n- Azúcar\n\nPreparación:\nMezclar todo y hornear.")
            creado =True
        else:
            print('Nombre muy corto')

def leer_borrar_receta(accion):
    # 0 = Lee
    # 1 = Borra
    lista_recetas = []
    filtro_rec = ''
    entrada_rec ='e'
    recetas = navegar_categoria()
    if receta== False:
        return
    
    while True:
        system('cls')
        print('Recetas')
        print('Escriba "Enter" para volver')
        for index_rec, rec in enumerate( Path(recetas).glob('*')):
            lista_recetas.append(rec)
            filtro_rec+=str(index_rec)
            print(f'[{index_rec}] - {rec.stem}')

        entrada_rec = input('Ingrese Alguna receta: ')
        if entrada_rec == "":  
            break  
        if entrada_rec in filtro_rec:
            receta = Path(lista_recetas[int(entrada_rec)])
            if accion== 0: #lee el archivo
                print(f'{receta.stem}:')
                print(receta.read_text())
                input('\nToque "enter" para salir.')
            elif accion== 1: # borra el archivo
                receta.unlink()
                print(f'La receta {receta.stem}, se borro.')
                input('\nToque "enter" para salir.')
                        


def leer_recetas(direccion):
    1+1

entrada = '7'
while entrada != '6':
    system('cls')
    print('''
          [1] - Leer Recetas
          [2] - Crear Recetas
          [3] - Crear Categoria
          [4] - Eliminar Receta
          [5] - Eliminar Categoria
          [6] - Finalizar Programa
          ''')
    entrada = input('Ingrese Alguna opcion: ')
    match entrada:
        case '1':
            leer_borrar_receta(0)
        case '2':
            crear_receta(2)
        case '3':
            leer_recetas()
        case '4':  
            leer_borrar_receta(1)      
        case '5':
            leer_recetas()
        case '6':
            continue
        case _:
            print('La opcion no existe')