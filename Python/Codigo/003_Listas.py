var1 = "Hola buenos dias"

#Te muestra el numero de posicion y el valor de esa posicion
for indice,letra in enumerate(var1):
    print("La letra es:",letra," y su índice es:",indice)

#LISTAS
varLista = [5,5,7] #Lista vacía si no se rellena
varLista1 = list([4,6,7]) #Lo que se pase por parámetro se pasa a una lista
print(varLista, varLista1) #Se pueden ver listas directamente

#AÑADIR ELEMENTOS A LA LISTA : append() (lo agrega al final de la lista)
lst = list()
lst.append(1)
lst.append(21)
lst.append([54,8,5,2])
lst.append(45)
lst.append(59)
lst.append(1)

#ACCEDER A UNA POSICION CONCRETA
lst[1] #si se pone en negativo se cuenta desde el final, el indice 0 se mantiene
#print(lst[-800]) se sale de rango

#RECORRER DESDE UNA POSICION HASTA OTRA DETERMINADA
print( lst [2 : 5]) #posición final -1
print( lst[ 1 : 5 : 2]) # el 2 es el numero de cuanto en cuanto

#VER SI UN ELEMENTO DE LA LISTA ESTÁ REPETIDO
print("El número 1 está repetido:",lst.count(1)) #te muestra la cantidad de veces que esta repetido

#PARA VER LA PRIMERA POSICION DE UN VALOR
print("El numero 1 esta en la posición:",lst.index(59))

#ELIMINAR ELEMENTOS EN LISTAS
lst.remove(1) # solo elimina el primer valor 
print(lst)
#para eliminar por valor
print(lst.pop(3))

#PARA GENERAR UNA LISTA CON VALORES RÁPIDO
lst = [0, 5] * 5 # multiplica los valores, no entre ellos
print("****",lst)
#si se suman listas, se concatenan, hay que guardarla en otra lilsta

print("------------------")

#PRACTICA: eliminar los valores repetidos
lstPractica = [1,1,1,5,7,0,9,8]
print(lstPractica)

while lstPractica.count(1) > 1:
    lstPractica.remove(1)
    print(lstPractica)

