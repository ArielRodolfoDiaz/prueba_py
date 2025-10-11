# es un swich

serie = 'N-02'

if serie == 'N-01':
    print('Samsung')
elif serie == 'N-02':
    print('Nokia')
elif serie == 'N-03':
    print('Motorola')
else:
    print('No existe esa serie')

match serie:
    case 'N-01':
        print('Samsung')
    case 'N-02':
        print('Nokia')
    case 'N-03':
        print('Motorola')
    case _:
        print('No existe esa serie')

cliente ={'nombre':'Ariel', "edad":39, "ocupacion":'Operador'}
pelicula  = {'titulo': "matix", 'ficha_tecnica':{
    'protagonista':'Keanu reeves',
    'directores':'lana y lilly wachowski'
}}
cliente2 ={'nombre':'Yesica', "edad":37, "ocupacion":'Ama de casa'}
elementos = [ cliente, pelicula, 'libro', cliente2]

for elem in elementos:
    match elem:
        case {'nombre':nombre, 'edad':edad, 'ocupacion':ocupacion}:
            print('Es un cliente')
            print(nombre, edad, ocupacion)
        case {'titulo': titulo, 'ficha_tecnica':{
                'protagonista':protagonista,
                'directores':directores}}:
            print('Es una pelicula')
            print(titulo, protagonista, directores)
        case _:
            print('Es datos distintos')