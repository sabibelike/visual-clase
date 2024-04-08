var = [1,1,1,2,3,3,4,5,5,5,6,6]
print(var)
#conjuntos se identifican con llaves
var1 ={1,1,1,2,3,3,4,5,5,5,6,6} #no se puede saber el indicide del elemento
print(var1)

var1.add(1)
var1.add("1")
print(var1)
#a un conjunto no le podemos poner listas, tuplas si 
#var1.add(1,2,3)
print(var1)
var1.discard(3)
print(var1)

#el + no sirven para los set
var2={"a","b"}
#var3 = var1+var2
var1.update(var2)
print(var1)

varlist=list(var1)
print(varlist)