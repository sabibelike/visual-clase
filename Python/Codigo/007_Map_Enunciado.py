# Ejercicio 1
#1. Multiplicar todos los elementos de una lista por 3:
lista_original = [1, 2, 3, 4, 5]
def multiplicar(x):
    return x*3
print(list(map(multiplicar,lista_original)))

# Ejercicio 2
#2. Convertir una lista de cadenas a mayúsculas:
lista_original = ['hola', 'mundo', 'python']
def toMayus(x):
    return str.upper(x)
print(list(map(toMayus,lista_original)))
# Ejercicio 3
#3. Calcular la raíz cuadrada de cada número en una lista y almacenar los resultados en un set:
import math
lista_original = [4, 9, 16, 25]
def raiz(x):
    return math.sqrt(x)
aux=set(map(raiz,lista_original))
print(aux)

# Ejercicio 4
#4. Duplicar las claves de un diccionario:
diccionario_original = {'a': 1, 'b': 2, 'c': 3}
def duplicar(x):
    return x*2
print(list(map(duplicar,diccionario_original)))
# Ejercicio 5
#5. Elevar al cubo todos los valores de un diccionario:
diccionario_original = {'a': 2, 'b': 3, 'c': 4}
def elevar(x):
    return math.pow(x,3)
print(list(map(elevar,diccionario_original.values())))

# Ejercicio 6
#6. Concatenar un sufijo a cada cadena en una lista:
lista_original = ['apple', 'banana', 'orange']
def sufijo(x):
    return x+"ito"
print(list(map(sufijo,lista_original)))
# Ejercicio 7
#7. Calcular el cuadrado de cada número en una lista y almacenar los resultados en un conjunto:
lista_original = [2, 3, 4, 5]
def cuadrado(x):
    return math.pow(x,2)
print(set(map(cuadrado,lista_original)))

# Ejercicio 8
#8. Dividir por 2 todos los valores de un diccionario:
diccionario_original = {'a': 10, 'b': 20, 'c': 30}
def dividir(x):
    return x/2
print(list(map(dividir,diccionario_original.values())))

# Ejercicio 9 no hacer
#9. Convertir cada número en una lista a su equivalente en binario y almacenar los resultados en una lista:
lista_original = [3, 6, 9, 12]


# Ejercicio 10
#10. Eliminar las vocales de cada cadena en una lista:
lista_original = ['hello', 'world', 'python']
def elimVocales(x):
    
    return 


# Ejercicio 11
#11. Dada una lista de estudiantes con sus calificaciones, calcular el promedio de cada estudiante y almacenar los resultados en un diccionario:
estudiantes_calificaciones = {'Juan': [85, 90, 95], 'María': [78, 82, 80], 'Pedro': [90, 92, 88]}


# Ejercicio 12
#12. En una lista de nombres, eliminar los nombres que contienen menos de 5 caracteres, convertir los restantes a minúsculas y ordenarlos alfabéticamente:
lista_nombres = ['Ana', 'Carlos', 'Eva', 'Juan', 'Maria', 'Pedro', 'Luisa']


# Ejercicio 13
#13. En un diccionario que contiene nombres de ciudades como claves y listas de temperaturas como valores, calcular el promedio de temperaturas de cada ciudad y almacenar los resultados en un nuevo diccionario:
temperaturas_ciudades = {'Boston': [68, 72, 70], 'Los Angeles': [75, 80, 78], 'Miami': [82, 85, 80]}


# Ejercicio 14
#14. Dada una lista de números, convertir cada número en su equivalente en hexadecimal y almacenar los resultados en una lista:
lista_numeros = [10, 20, 30, 40, 50]

# Ejercicio 15
#15. En una lista de palabras, eliminar las palabras que contienen la letra 'a', convertir las restantes a mayúsculas y ordenarlas alfabéticamente:
lista_palabras = ['apple', 'banana', 'orange', 'grape', 'kiwi', 'pear']


# Ejercicio 16
#16. Dada una lista de tuplas con nombres y edades, calcular la edad promedio y almacenar los resultados en un diccionario:
estudiantes_edades = [('Juan', 20), ('María', 22), ('Pedro', 19)]


# Ejercicio 17
#17. En una lista de oraciones, contar la cantidad de palabras en cada oración y almacenar los resultados en una lista:
lista_oraciones = ['Python es un lenguaje de programación.', 'Tiene una sintaxis sencilla y elegante.']

# Ejercicio 18
#18. En un diccionario que contiene nombres de estudiantes como claves y listas de calificaciones como valores, calcular la calificación más alta de cada estudiante y almacenar los resultados en un nuevo diccionario:
estudiantes_calificaciones = {'Juan': [85, 90, 95], 'María': [78, 82, 80], 'Pedro': [90, 92, 88]}

# Ejercicio 19
#19. Dada una lista de números, calcular el logaritmo natural de cada número y almacenar los resultados en una lista:
import math
lista_numeros = [1, 2, 3, 4, 5]

# Ejercicio 20
#20. En una lista de frases, eliminar las palabras que tengan menos de 3 letras, contar la cantidad de palabras en cada frase y almacenar los resultados en una lista:
lista_frases = ['Python es un lenguaje de programación.', 'Tiene una sintaxis sencilla y elegante.']
