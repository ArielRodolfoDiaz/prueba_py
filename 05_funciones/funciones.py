
def saludar_fijo():
    print(f'Hola fijo')
saludar_fijo()

def saludar_variable(nombre):
    print(f'Hola {nombre}')
saludar_variable('Ariel')
saludar_variable('Yesi')

def multiplicar (num1, num2):
    return num1*num2
print(multiplicar(25,585))

def invertir_palabra (palabra):
    return palabra[::-1].upper()
palabra = "Python"
print(invertir_palabra(palabra))

def chequear_3_cifras(numero):
    return numero in range(100,1000)
print(chequear_3_cifras(205))

def chequear_3_cifras_lista(lista):
    resultado =[]
    for n in lista:
        if n in range(100,1000):
            resultado.append(n)
        else:
            pass
    return resultado
print(chequear_3_cifras_lista([55,909,88,600]))

def todos_positivos(lista_numeros):
    for n in lista_numeros:
        if n<0:
            return False
        else:
            pass
    return True

lista_numeros = [152, 25, -39]
print (todos_positivos(lista_numeros))

def suma_menores(lista_numeros):
    suma=0
    for n in lista_numeros:
        if n>0 and n<1000:
            suma+=n
            
    return suma

lista_numeros = [12,25,2,37,8,8888,2,4777,-15,52]
print (suma_menores(lista_numeros))

def cantidad_pares(lista_numeros):
    cuenta=0
    for n in lista_numeros:
        if n%2==0:
            cuenta+=1
    return cuenta
    
lista_numeros= [12,25,2,37,8,8888,2,4777,-15,52]
print (cantidad_pares(lista_numeros))

lista_cafe = [('lateado',25.6), ('caafe',25555.2), ('mokate',451.25)]
for nombre, precio in lista_cafe:
    print(precio)

def cafe_mas_caro(lista_cafe):
    precio_mayor=0
    nombre_mayor=''
    for nombre, precio in lista_cafe:
        if precio_mayor<precio:
            nombre_mayor=nombre
            precio_mayor=precio
    return (nombre_mayor, precio_mayor)

print(cafe_mas_caro(lista_cafe))


lista_numeros=[1,2,15,7,2] 



def  reducir_lista(lista):
    lista_set = set(lista)
    maximo = max(lista_set)
    lista_set.remove(maximo)
    return lista_set
    
def promedio(lista):
    suma=0
    for num in lista:
         suma+=num
    return suma/len(lista)

lista = reducir_lista(lista_numeros)
print (promedio(lista))