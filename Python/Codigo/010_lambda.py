from functools import reduce

lst = [1,2,3,4,5,6,7]
def pares(x):
    return x%2==0
print(list(filter(pares,lst)))


num= [1,2,3,4,5,6,7,8,9]
print(list(filter(lambda x: x%2==0, num)))
print(list(filter(lambda x: x%2==0 and x>5, num))) #el AND es como usar un if 
print(list(map(lambda x: x+1, num)))


#el *args es utilizado para que se utilicen todos los parametros que sean necesarios 
def suma(*args):
    resultado = 0
    for numero in args:
        resultado += numero
    return resultado

print(suma(1,2))
print(suma(1,2,3,4,5,6,7,8,9,10))