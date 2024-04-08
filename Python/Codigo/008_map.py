'''
    map(funcion,cosaArecorrer)
    map(nombrefuncion,cosaArecorrer) y la funcion sin parentesis
    y al menos un parametro en la funcion
'''
import time 

def sumar1(x):
    return x+1

def sumarList(x,y):
    return x+y

lst=[1,2,3,4,5,6,7]
lst1=[10,20,30,40,50,60,70]

#se usa el map porque esta bien optimizada 
print(list(map(sumar1,lst)))

#Deben tener el mismo tamaño para poder sumar elemento por elemento
print(list(map(sumarList, lst, lst1)))

lst2=["hola","que","tal"]

print(list(map(len,lst2)))

print(list(map(str.upper,lst2)))

def sumarEdad(x):
    x["edad"]+=1
    return x

di=[{"persona":"Andrés","edad":30},
    {"persona1":"Andrés","edad":30},
    {"persona2":"Andrés","edad":30},
    {"persona3":"Andrés","edad":30}]

print(list(map(sumarEdad,di)))
print(di)

lst4=list(range(1,10000000))
lst5=list(range(1,10000000))

inicio = time.time()
print(inicio)


inicio1 = time.time()
for x in range(len(lst4)):
    lst4[x]+=1
fin1= time.time()
print("el bucle for ha tardado",fin1-inicio1)

inicio2 = time.time()
list(map(sumar1,lst4))
fin2 = time.time()
print("El mapa for ha tardado",fin2-inicio2)

    