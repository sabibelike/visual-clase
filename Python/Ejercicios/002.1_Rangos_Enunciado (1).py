"""
Ejercicio 1: Creación de un Rango Simple
Define un rango que vaya desde 0 hasta 5 (inclusive).
Imprime el rango creado.
"""
for indice in range(5+1):
    print(str(indice))

"""
Ejercicio 2: Creación de un Rango con Inicio y Fin Específicos
Define un rango que vaya desde 5 hasta 10 (inclusive).
Imprime el rango creado.
"""
for indice in range(5,10+1):
    print(str(indice))

"""
Ejercicio 3: Creación de un Rango con Incremento Específico
Define un rango que vaya desde 1 hasta 10 (inclusive) con incremento de 2.
Imprime el rango creado.
"""
for indice in range(1,10+1,2):
    print(str(indice))

"""
Ejercicio 4: Iteración sobre un Rango Simple
Itera sobre un rango que vaya desde 0 hasta 3 (inclusive).
Imprime cada valor del rango en una línea separada.
"""
for indice in range(0,3+1):
    print(str(indice),end=" ")
"""
Ejercicio 5: Iteración sobre un Rango con Incremento Específico
Itera sobre un rango que vaya desde 0 hasta 10 (inclusive) con incremento de 2.
Imprime cada valor del rango en una línea separada.
"""
#listo
"""
Ejercicio 6: Uso de Rangos en Funciones de Control de Flujo
Itera sobre un rango que vaya desde 10 hasta 1 (inclusive) con decremento de 1.
Imprime cada valor del rango en una línea separada.
"""
for indice in range (10,1+1,-1):
    print(str(indice))
"""
Ejercicio 7: Uso de Rangos en Condicionales
Verifica si un número ingresado por el usuario está dentro de un rango predefinido.
"""
num = 5
if num in range(1,10):
    print("El numero esta en el rango")

"""
Ejercicio 8: Uso de Rangos para Generar Secuencias de Números
Genera una lista de números pares en el rango de 0 a 10 (inclusive).
Imprime la lista resultante.
"""

lista = list()
for indice in range (0,10+1,2):
    lista.append(indice)
print(lista)

"""
Ejercicio 9: Uso de Rangos para Sumar Elementos
Calcula la suma de todos los números en el rango de 1 a 100 (inclusive).
Imprime el resultado de la suma.
"""
num = 0
for indice in range(1,100+1):
    num+=indice
print(num)
"""
Ejercicio 10: Uso de Rangos para Contar Elementos
Cuenta cuántos números pares hay en el rango de 1 a 50 (inclusive).
Imprime el total de números pares.
"""
contador = 0
for indice in range(1,50+1):
    if indice%2==0:
        contador+=1
print("La cantidad de numeros pares es de:",contador)
contador = 0
contador=len(list(range(0,101,2)))
print("El numero de pares es:",contador)
"""
Ejercicio 11: Uso de Rangos en una Función
Define una función llamada `imprimir_rango` que reciba un parámetro `limite`.
La función debe imprimir todos los números desde 0 hasta el `limite` (inclusive) utilizando un rango.
"""
def imprimir_rango(limite):
    for indice in range(1,limite+1):
        print(str(indice))
"""
Ejercicio 12: Uso de Rangos en una Función con Paso Personalizado
Define una función llamada `imprimir_rango_paso` que reciba tres parámetros: `inicio`, `fin` y `paso`.
La función debe imprimir todos los números desde `inicio` hasta `fin` (inclusive) utilizando un rango con el paso especificado.
"""
def imprimir_rango_paso(inicio,fin,paso):
    for indice in range(inicio,fin+1,paso):
        print(str(indice))
"""
Ejercicio 13: Uso de Rangos para Generar Secuencias de Caracteres
Genera una lista de letras del alfabeto inglés (minúsculas) utilizando un rango.
Imprime la lista resultante.
"""
import string as st
for letra in range(97,122+1):
    print(chr(letra))

"""
Ejercicio 14: Uso de Rangos para Generar Patrones
Genera un patrón numérico en forma de triángulo utilizando un rango y la función `join()`.
Imprime el patrón resultante.
"""

num = list()
espacios = 15-1
for indice in range(1,9):
    num.append(str(indice))
    cadena = " ".join(num)
    print(espacios*" ",cadena)
    espacios-=1

"""
Ejercicio 15: Uso de Rangos para Generar Patrones (Otra Forma)
Genera un patrón numérico en forma de triángulo invertido utilizando un bucle for.
Imprime el patrón resultante.
"""
espacios2 = 0
num2 = list()
for indice in range(1,10):
    num2.append(str(indice))
for indice in range(9,1,-1):
    num2.remove(str(indice))
    cadena = " ". join(num2)
    print(espacios*" ",cadena)
    espacios+=1
    
"""
Ejercicio 16: Uso de Rangos para Generar Patrones (Otra Forma)
Genera un patrón de asteriscos en forma de pirámide utilizando un bucle for.
Imprime el patrón resultante.
"""
num = list()
espacios = 15-1
for indice in range(1,9):
    num.append("*"*1)
    cadena = " ".join(num)
    print(espacios*" ",cadena)
    espacios-=1
"""
Ejercicio 17: Uso de Rangos para Generar Patrones (Otra Forma)
Genera un patrón de números en forma de diamante utilizando un bucle for.
Imprime el patrón resultante.
"""
letra = list()
espacios = 26
for indice in range(97,123):
    letra.append(chr(indice))
    cadena = " ".join(letra)
    print(espacios*" ",cadena)
    espacios-=1
    
"""
Ejercicio 18: Uso de Rangos para Generar Patrones (Otra Forma)
Genera un patrón de letras en forma de pirámide utilizando un bucle for.
Imprime el patrón resultante.
"""
#listop
"""
Ejercicio 19: Uso de Rangos para Generar Patrones (Otra Forma)
Genera un patrón de letras en forma de pirámide invertida utilizando un bucle for.
Imprime el patrón resultante.
"""
#listop
"""
Ejercicio 20: Uso de Rangos para Generar Patrones (Otra Forma)
Genera un patrón de letras en forma de diamante utilizando un bucle for.
Imprime el patrón resultante.
"""
#listop