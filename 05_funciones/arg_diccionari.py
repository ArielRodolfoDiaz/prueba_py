def sumar(**kwargs):
    total=0
    for clave,valor in kwargs.items():
        total+=valor
        print(clave, valor, total)
    

sumar(x=5,d=5)

def sumarCompleto(num1, num2, *args, **kwargs):
    print('sumarCompleto')
    print(num1, num2 )
    for num in args:
        print(num )
    for clave,valor in kwargs.items():
        print(clave, valor )
    

sumarCompleto(25,36, 1, 2, 3, 4, x=5,d=5)

args=25,36, 1, 2, 3, 4
kwargs ={
    'x':'uno',
    'y':"dos",
    'w':155
}
sumarCompleto(25,36,args,kwargs)