dicc={"elemen1":1, "eleme2":[1,2,3,[4,5]]}
print(dicc)

#print(dicc["eleme2"][2][2])

for key in dicc:
    print(key)
    
verclaves= dicc.keys()
print(list(verclaves)[0])
verValores=dicc.values()
print(verValores)

for k,v in dicc.items:
    print("La clave es:",k,"el valor es:",v)

print(dicc.get("elemen1"))
print(dicc["elemen1"])

#Buscar como copiar datos en java
var =[1,2,3]
var1=var
var1.append(4)

print(var)
print(var1)