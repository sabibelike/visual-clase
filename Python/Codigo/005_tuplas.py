#Es como una lista pero no podemos cambiar nada de ellas
'''
que podemos hacer?
    -crear
    -saber elementos de una lista
    -saber el numero de elementos
'''
#Se diferencia de una lista porque se crea con parentesis, no corchetes
objTupla = (1,2,3,4,4,4,4,4,4)
print(objTupla[3])
for x in objTupla:
    print([x])
    
print("Numero de 4",objTupla.count(4))
print("Numero de elementos",len(objTupla))
print("Tipo de elemento",type(objTupla))