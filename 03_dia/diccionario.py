diccionario={
    "c1":"valor 1",
    "c2": 2.52
}

print(diccionario)
print(diccionario["c1"])
print(diccionario.keys())

cliente={
    "nombre":"Ariel Rodolfo",
    "apellido":"Diaz",
    "peso":253.6845,
    "edad":52,
    "esCasado":True,
    "hijos":[{"nombre":"Agustin", "edad":11}, {'nombre':'Daniel', 'edad':7}]
}

consulta = cliente["hijos"]

print(consulta[1]["edad"])

dic={'c1':['a', 'b','c'], 'c2':['d','e','f']}

print(dic["c2"][1].upper())

dic['c3'] = {'ji':42, "jo":85}

print(dic)
dic['c3'] = {'42':42, "jo":857}

print(dic)
print(dic.values())
print(dic.keys())
print(dic.items())