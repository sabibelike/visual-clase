from functools import reduce

num = [1,2,3,4,5,6]
def pares(x):
    return x%2==0
def redu(x,y):#siempre dos parametros y devuelve uno solo, de forma acumulativa
    return x+y
print(list(filter(pares,num)))

lista= list(range(1,1000))
#sin el reduce
aux = 0
for x in lista:
    if x%2==0:
        aux+=x
print(aux)
#con el reduce
def pares(x):
    return x%2==0
def sumar(x,y):
    return x+y
listFiltrada = filter(pares,lista)
sumaNumeros = reduce(sumar,listFiltrada)
print(sumaNumeros)