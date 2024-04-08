import random as rd #podemos sobreescribir
import string as str


print("Letras en mayus",str.ascii_uppercase)
print("Letras en minus",str.ascii_lowercase)
print("Letras en general",str.ascii_letters)
print("Todos los numeros",str.digits)
print("Todos los numeros hexadecimal",str.hexdigits)
print("Todas las formas de representar un espacio",list(str.whitespace))#convirtiendolo en una lista nos muestra los elementos
print("Signos de puntuacion",str.punctuation)



#funcion para poner la primera letra de una frase en mayus
print(str.capwords("esta es una frase"))


#random
print("Numero aleatorio entre [0,1)",rd.random)
print("Numeros aleatorios entre 2 valores",rd.randint(1,2))#nos da un valor aleatorio incluyendo el inicio y el final
print("numero aleatorio dentro de un rango",rd.randrange)
lst = list(str.ascii_letters)
print(rd.choice(lst))#devuelve un elemento aleatorio de una secuencia dada


#desordena de forma aleatoria lo que le pases 
rd.shuffle(lst)
print(lst,"***")

#la K te da una muestra de las posibilidades, en el primer parametro le das los valores y en el segundo el porcentaje que quieresque salga
print(rd.choices([1,2,3,4,5],[80,5,5,5,5],k=1))

print(rd.uniform(5,10))#nos da valores decimales