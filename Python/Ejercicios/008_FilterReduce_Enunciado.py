# Ejercicio 1
# 1. Multiplicar todos los elementos de una lista por 3:
lista_original = [1, 2, 3, 4, 5]
print(list(map(lambda x : x*3,lista_original)))

# Ejercicio 2
# 2. Filtrar los números pares de una lista:
lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(filter(lambda x : x%2==0, lista_numeros)))

# Ejercicio 3
# 3. Sumar todos los elementos de una lista:
from functools import reduce
lista_numeros = [1, 2, 3, 4, 5]
print(reduce(lambda x,y : x+y, lista_numeros))
#por que no necesita ser pasado a lista???
# Ejercicio 4
# 4. Filtrar los números mayores que 10 y multiplicarlos por 2:
lista_numeros = [5, 10, 15, 20, 25]
filtrados = list(filter(lambda x : x>=10, lista_numeros))
print(list(map(lambda x : x*2, filtrados)))

# Ejercicio 5
# 5. Filtrar las palabras que tienen más de 5 letras en una lista de palabras:
lista_palabras = ["python", "programacion", "aprendizaje", "desarrollo", "informatica"]
print(list(filter(lambda x : len(x)>6, lista_palabras)))

# Ejercicio 6
# 6. Calcular el producto de todos los elementos de una lista:
lista_numeros = [1, 2, 3, 4, 5]
#???????

# Ejercicio 7
# 7. Convertir todas las palabras en una lista a mayúsculas:
lista_palabras = ["hola", "python", "mundo", "programacion"]
print(list(map(lambda x : str.upper(x), lista_palabras)))

import math
# Ejercicio 8
# 8. Filtrar los números impares y elevarlos al cuadrado:
lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtra = list(filter(lambda x : x%2!=0, lista_numeros))
print("Numeros filtrados y elevados",list(map(lambda x : math.pow(x,2), filtra)))

# Ejercicio 9
# 9. Concatenar todas las palabras de una lista separadas por un guión:
lista_palabras = ["hola", "python", "mundo"]
print(reduce(lambda x,y : x+"-"+y, lista_palabras))


# Ejercicio 10
# 10. Filtrar los elementos de una lista que son cadenas de texto:
lista_mixta = [1, "python", 3.5, "programacion", True, "aprendizaje"]
print(list(filter(lambda x : type(x) == type("text"), lista_mixta)))


# Ejercicio 11
# 11. Multiplicar los elementos de dos listas elemento por elemento:
lista1 = [1, 2, 3, 4, 5]
lista2 = [2, 3, 4, 5, 6]
print(list(map(lambda x,y:x*y, lista1, lista2)))

# Ejercicio 12
# 12. Filtrar los números negativos de una lista y convertirlos a positivos:
lista_numeros = [-5, 10, -15, 20, -25]
numNegativos = list(filter(lambda x : x < 0, lista_numeros))
print(list(map(lambda x : abs(x), numNegativos)))

# Ejercicio 13
# 13. Filtrar las palabras que comienzan con una letra específica de una lista:
letra_busqueda = 'p'
lista_palabras = ["python", "programacion", "aprendizaje", "desarrollo", "informatica"]
print(list(filter(lambda x : str(x).startswith('p'), lista_palabras)))

# Ejercicio 14
# 14. Sumar los números pares de una lista:
lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numPares = list(filter(lambda x : x%2==0, lista_numeros))
print(reduce(lambda x,y : x+y, numPares))

# Ejercicio 15
# 15. Filtrar los números primos de una lista de números:
lista_numeros = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]


# Ejercicio 16
# 16. Concatenar solo las palabras que tienen más de 3 letras en una lista:
lista_palabras = ["hola", "python", "mundo", "programacion", "ai", "openai"]
palabrasMayor = list(filter(lambda x : len(x)>3, lista_palabras))
print(reduce(lambda x,y : x+" "+y, palabrasMayor))


# Ejercicio 17
# 17. Calcular el promedio de los elementos de una lista de números:
lista_numeros = [1, 2, 3, 4, 5]



# Ejercicio 18
# 18. Crear una lista de tuplas que contengan el número y su factorial:
lista_numeros = [1, 2, 3, 4, 5]

# Ejercicio 19
# 19. Calcular la suma de los dígitos de una lista de números:
lista_numeros = [123, 456, 789, 101112]

