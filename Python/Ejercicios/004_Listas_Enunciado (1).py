"""
Ejercicio 1:
Crear una lista vacía y agregar elementos.
Escribe un programa que cree una lista vacía llamada "mi_lista" y agregue los números del 1 al 5 a esta lista.
"""
list1 = list()
list1.append(1)
list1.append(2)
list1.append(3)
list1.append([4,5,6,7])


"""
Ejercicio 2:
Acceder a elementos de una lista.
Escribe un programa que defina una lista llamada "colores" que contenga los nombres de varios colores y muestre el primer y el último elemento de la lista.
"""
list2 = list()
list2.append("Amarillo")
list2.append("Azul")
list2.append("Verde")
print(list2[0],list2[len(list2)-1])

"""
Ejercicio 3:
Modificar elementos de una lista.
Escribe un programa que tenga una lista de números del 1 al 5 y cambie el tercer elemento de la lista por el número 10.
"""
list3 = [1,2,3,4,5]
list3[2] = 10
print(list3)
"""
Ejercicio 4:
Eliminar elementos de una lista.
Escribe un programa que tenga una lista de nombres de frutas y elimine el segundo elemento de la lista.
"""
list4 = ["Manzana", "Naranja","Fresa", "Mandarina"]
list4.pop(1)
print(list4)
"""
Ejercicio 5:
Contar elementos de una lista.
Escribe un programa que cuente cuántas veces aparece la palabra "perro" en una lista dada.
"""

lista5 =["perro","perro","perro", "gato","perro"]
print(lista5.count("perro"))
"""
Ejercicio 6:
Crear una lista a partir de elementos ingresados por el usuario.
Escribe un programa que solicite al usuario ingresar 5 nombres y cree una lista con estos nombres.
"""
def listaNombre():
    listNombres = []
    nombres = input("Escribe un nombre")
    for x in range(5):
        listNombres.append(nombres)
    
"""
Ejercicio 7:
Concatenar dos listas.
Escribe un programa que tenga dos listas de números y las concatene para formar una sola lista.
"""
lista1 = [1,2,3,4]
lista2 = [5,6,7]
print(lista1+lista2)

"""
Ejercicio 8:
Ordenar una lista alfabéticamente.
Escribe un programa que tenga una lista de nombres de países y los ordene alfabéticamente.
"""
paises = ["españa", "hungria", "argentina", "colombia"]
paises.sort()
print(paises)

"""
Ejercicio 9:
Reemplazar elementos de una lista.
Escribe un programa que tenga una lista de números del 1 al 5 y reemplace los elementos del segundo al cuarto por el número 0.
"""
numero = [1,2,3,4,5]
for i in range(1,len(numero)):
    numero[i] = 0
print(numero)

"""
Ejercicio 10:
Buscar un elemento en una lista.
Escribe un programa que tenga una lista de números y verifique si el número 5 está presente en la lista.
"""
numm = [1,2,3,4,5]
if 5 in numm:
    print("El número 5 está en la lista")
else:
    print("No se encuentra")
"""
Ejercicio 11:
Calcular la longitud de una lista.
Escribe un programa que tenga una lista de colores y calcule cuántos elementos tiene la lista.
"""
print(len(numm))
"""
Ejercicio 12:
Crear una lista de números pares.
Escribe un programa que cree una lista de los primeros 5 números pares a partir de un rango.
Agrega esos números pares a una lista
"""
par = []
for i in range(2,12,2):
    if i %2==0:
        par.append(i)
print(par)

"""
Ejercicio 13:
Sumar todos los elementos de una lista.
Escribe un programa que tenga una lista de números y sume todos sus elementos.
"""
uno = [1,2,3]
print(sum(uno))

"""
Ejercicio 14:
Contar elementos mayores que un número dado.
Escribe un programa que tenga una lista de números y cuente cuántos elementos son mayores que 5.
"""
mayores = [10,3,5,6,7,8]
contador = 0
for i in range(0,len(mayores)):
    if mayores[i] > 5:
        contador+=1
print("La cantidad de numeros mayores a 5 son:",contador)
"""
Ejercicio 15:
Eliminar duplicados de una lista.
Escribe un programa que tenga una lista con elementos duplicados y elimine los duplicados de la lista.
"""
duplicados = [1,1,1,2,3,4,5,5]
#sinDuplicar = set(duplicados)
print(set(duplicados))

"""
Ejercicio 16:
Multiplicar todos los elementos de una lista.
Escribe un programa que tenga una lista de números y multiplique todos sus elementos entre sí.
"""
multi = 1
for i in range(len(duplicados)):
      multi *= duplicados[i]
print("El resultado es:",multi)

"""
Ejercicio 17:
Comprobar si una lista está vacía.
Escribe un programa que determine si una lista dada está vacía o no.
"""
vacia = []
if len(vacia) == 0:
    print("Lista vacia")
else:
    print("lista llena")

"""
Ejercicio 18:
Calcular el promedio de una lista de números.
Escribe un programa que tenga una lista de números y calcule el promedio de esos números.
"""
nume = [1,2,3,4,5,6]
print(sum(nume)/len(nume))

"""
Ejercicio 19:
Calcular la suma de los elementos pares de una lista.
Escribe un programa que tenga una lista de números y calcule la suma de todos los elementos pares en la lista.
"""
otra = [1,2,3,4,5,6]
result = 0
for i in range(len(otra)):
    if otra[i]%2==0:
        result+=otra[i]
print("El resultado es",result)

"""
Ejercicio 20:
Reemplazar todos los elementos de una lista con un valor dado.
Escribe un programa que tenga una lista de números y reemplace todos sus elementos por un valor dado.
"""
valor = 5
for i in range(len(otra)):
    otra[i] = valor
print(otra)

"""
Ejercicio 21:
Invertir una lista.
Escribe un programa que tenga una lista de números y la invierta, es decir, que el primer elemento se convierta en el último y viceversa.
"""
una = [1,2,3,4,5]
dos = []
for i in range (len(una)-1,-1,-1):
    dos.append(una[i])
print(dos)

#other way
una.reverse()
print(una)
"""
Ejercicio 22:
Dividir una lista en partes iguales.
Escribe un programa que tenga una lista de números y la divida en partes iguales de longitud especificada por el usuario.
"""
print("*****************")
dividirlista=[1,2,3,4,5,6,7,8,9,1]
longitud=2
for i in range(0,len(dividirlista),longitud):
    print(dividirlista[i:i+longitud])

"""
Ejercicio 23:
Ordenar una lista en orden descendente.
Escribe un programa que tenga una lista de números y la ordene en orden descendente.
"""
dividirlista.sort()
dividirlista.reverse()
print(dividirlista)

"""
Ejercicio 24:
Unir dos listas en una sola.
Escribe un programa que tenga dos listas de números y las una en una sola lista.
"""
dividirlista.extend(una)
print(dividirlista)
"""
Ejercicio 25:
Eliminar todos los elementos duplicados de una lista.
Escribe un programa que tenga una lista con elementos duplicados y elimine todos los duplicados, dejando solo una ocurrencia de cada elemento.
"""
#usar set 
'''
Ejercicio 26:
Ordenar una lista de cadenas alfabéticamente sin distinción entre mayúsculas y minúsculas:

Escribe un programa que solicite al usuario ingresar una lista de palabras 
y luego ordene la lista alfabéticamente sin distinguir entre mayúsculas y minúsculas.
Además, el programa debe eliminar cualquier palabra duplicada antes de realizar la ordenación.
'''
st = ["ANDREA","PEPE","JULIO"]
##pasatelo a una forma facil de entender jejeje
lista_original = ["Hola", "MUNDO", "¿CÓMO", "estás?"]
lista_en_minusculas = [elemento.lower() for elemento in lista_original]
lista_en_minusculas.sort()
print(lista_en_minusculas)

'''
Ejercicio 27
Escribe un programa que genere dos listas de números aleatorios entre 1 y 20 
y luego calcule e imprima la intersección de estas dos listas,
es decir, los números que aparecen en ambas listas.
Asegúrate de que no haya duplicados en las listas generadas.
'''
import random as rd
pene = []
totona = []
for i in range(6):
    num1= rd.randint(1,20)
    num2 = rd.randint(1,20)
    if num1 not in pene:
        pene.append(num1)
    if num2 not in totona:
        totona.append(num2)
print(pene," y ",totona)
otro = []
for i in range(len(pene)):
    if pene[i] in totona:
        otro.append(pene[i])      
print(otro)
'''
Ejercicio 28
Eliminar elementos repetidos de una lista manteniendo el orden original:

Escribe un programa que reciba una lista de números y elimine los elementos 
repetidos de la lista manteniendo el orden original.
'''
#usar set
'''
Ejercicio 29
Calcular la media de una lista de números:
Escribe un programa que calcule la media de una lista de números ingresada por el usuario.
'''
#usar sum, divides la suma por el len de la lista
'''
Ejercicio 30
Encontrar el elemento más grande y el más pequeño en una lista:
Escribe un programa que encuentre el elemento más grande y el más pequeño en una lista de números.
'''
webo = [1,2,3,10]
print("El maximo es:",max(webo),"el minimo es:",min(webo))