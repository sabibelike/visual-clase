#en python todo es publico, no como en java que podría ser privado 
def funcionQueNoDevuelveNada():
    print("Hola")

print(funcionQueNoDevuelveNada())
funcionQueNoDevuelveNada()

#sobrecarga de funciones, cuando la llames y le pases por parametro algo va a escoger la funcion que mas se acomode(con respecto a los parametros)
def funcionConParametro(parametro1,parametro2):
    print("El 1º parametro es:",parametro1)
    print("El 2º parametro es:",parametro2)

def funcionConParametro(parametro1):
    print("El 1º parametro es:",parametro1)
    
funcionConParametro(123)

def funcionConReturn():
    return "Este es el return"
print(funcionConReturn)

def funcionConMultiplesReturn():
    return 1,2,3,4
print(funcionConMultiplesReturn)#tuplas
var,var1,var2,var3= funcionConMultiplesReturn()
#var,var1,var2,_=funcionConMultiplesReturn() #la barra baja sirve para ignorar uno de los valores 
print(var)
print(var1)
print(var2)
print(var3)

#recursividad, necesita una solucion de salida
def fibonacci(n):
    f=[0,1]
    r=0
    for x in range (0,n-1):
        r=f[x]+f[x+1]
        f.append(r)
    return f
print(fibonacci(10))

def fibonacciR(n):
    if n==0:
        return 0
    if n==1:
        return 1
    else:
        return fibonacciR(n-1)+fibonacciR(n-2)
print(fibonacciR(10))

