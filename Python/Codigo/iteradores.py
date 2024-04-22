#next() nos devuelve el siguiente elemento
#hasnext en java, es si hay un siguiente elemento
#yield es como un return, devuelve algo
def bucle():
    i=0
    while i !=10:
        yield "El valor de i es: "+ str(i)
        i+=1

print(bucle())
#se debe guardar en una variable 
iterador = bucle()
print(next(bucle()))

print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))

for item in iterador:
    print(item)
print("-----")
for item in iterador:
    print(item)
print("-----")
for item in bucle():
    print(item)

iterador2 = bucle()
while True:
    try:
        print(next(iterador2))
    except StopIteration:
        print("Ya no tengo mas elementos")
        break
    
lst= [1,2,3,4,5,6]
print(lst)
print(iter(lst))