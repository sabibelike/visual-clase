#Esto es un comentario
'''
Comentarios 
en varias 
lineas jejejeje
'''
'''
Tipos de datos en python:
    -booleanos
    -entero
    -decimales
    -textos
    -listas
    -tuplas(array)
    -conjuntos(set, no admiten valores repetidos)
    -diccionarios(hash maps)
'''

numeroEntero = 5
numeroDecimal = 5.90


print("El numero entero es: " + str(numeroEntero))#hay que convertir el numero en string, porque no se pueden concatenar numero con string
print("El numero entero es:",numeroEntero)#la coma te pone un espacio

variableString= "esto es un texto"

print(variableString)

variableTipoBool = True
print("variable tipo booleano",variableTipoBool)

'''
Operadores
    -operadores aritmeticos +-*/%
    -operador de python **(exponentes) //(division exacta, sin resto)
    -operadores relacionales <> <= >= == !=
    -operadores de asignacion = += -= *= /= 
    -operadores logicos and, or, not(primero not, luego and y despues el or)
    -operadores de pertenencia in(para saber si un valir esta dentro de otro)
    -operador de identidad is (para saber si un elemento es igual a otro(objeto))
'''
'''
Parsers:
    -int()
    -float()
    -str()
    -bool()
    -list()
    -tuple()
    -set()
    -dict()
'''

var="hola me llamo pepito los palotes"
#función para obtener la cantidad de elementos
print(len(var))


print(round(3.3/3))#redondea a la unidad mas cercana
print(abs(-5))

n=2
print(eval("5+9/7 *n"))#coge una operacion matematica en string y la ejecuta

#te devuelve el tipo de dato
print(type(5))
print(type("5"))
print(type(5.1))
print(type(True))

'''
Rangos
posicion inicial hasta el ultimo menos 1
'''
print(range(10))
print(range(5,10))
print(range(5,10,2))#el tercer paso dirá de cuanto en cuanto, y siempre hacia adelante, lo convertimos a una lista y vemos los datos que tenemos


print(list(range(10)))
print(list(range(0,10,2)))

#sintaxis del if
num=4
if num<10:
    print("El numero es menor que 10")
elif num==5:
    print("El numero es igual a 5")
else:
    print("El numero es mayor a 10")
    
#sintaxis del for
for indicice in range(5):
    print(indicice)

#ejemplo de recorrer un string
for letra in range(5,len(var),3):
    print(var[letra])

#ejemplo2 de recorrer string de forma mas directa
for letra in var:
    print(letra)
    

numero1= int(input("Dame un numero jeje "))
numero2= int(input("Dame otro numero "))

print("La suma de",str(numero1),"y",str(numero2),"es",numero1+numero2)
