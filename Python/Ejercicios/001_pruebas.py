num1 = 5
num2 = 9.5

print("El resultado es:",num1+num2)
print(num1 < num2)
print(num1**num1)
print(num1 is num2)

print(num2//num1)
print(num2/num1)

print(3.3/3)
print("hola"*4)

'''stg1 = "hola"
stg2 = "holahola"
print(stg2-stg1)#no soportó
'''
stg = "hola"
print(stg,stg,stg, sep="5", end="**")
print(stg,stg,stg)

"""
Ejercicio 1:
Crear un programa que calcule el área de un triángulo rectángulo dado su base y altura.
Utiliza variables para almacenar la base, la altura y el resultado del cálculo del área.
"""
base= 5
altura= 20
area = (base*altura)/2
print(area)

"""
Ejercicio 2:
Escribir un programa que convierta grados Celsius a grados Fahrenheit.
Utiliza una variable para almacenar los grados Celsius, realiza el cálculo y muestra el resultado.
"""
celcius = 25
aFar= (celcius * 9/5) +32
print("De celcius a farhe",aFar)

"""
Ejercicio 3:
Crear un programa que calcule el perímetro y el área de un círculo dado su radio.
Utiliza una variable para almacenar el radio, realiza los cálculos y muestra los resultados.
"""
import math
radio= 30
areaCircu = math.pi*radio**2
print("El area del circulo es:",areaCircu)

"""
Ejercicio 4:
Escribir un programa que determine si un número dado es par o impar.
Utiliza una variable para almacenar el número, aplica el operador de módulo y muestra el resultado.
"""

num=2
if num%2==0:
    print("El numero es par")
else:
    print("El número es impar :)")
    
"""
Ejercicio 5:
Crear un programa que calcule la hipotenusa de un triángulo rectángulo dado sus catetos.
Utiliza dos variables para almacenar los catetos, aplica el teorema de Pitágoras y muestra el resultado.
"""
cateto1= 4
cateto2= 9
hipotenusa= cateto1**2+cateto2**2
print("La hipotenusa es:",math.sqrt(hipotenusa))

"""
Ejercicio 6:
Crear un programa que calcule el área y el perímetro de un rectángulo dados su base y su altura.
Utiliza variables para almacenar la base, la altura y realiza los cálculos correspondientes.
"""

altura=20
ancho=10
perimetro=2*altura+2*ancho
area=altura*ancho
print("El perimetro del rectangulo es",perimetro,"y el area es",area)

"""
Ejercicio 7:
Escribir un programa que determine si un año es bisiesto o no.
Utiliza una variable para almacenar el año, aplica las reglas para determinar si es bisiesto y muestra el resultado.
"""

año=2023
if año%400==0 or año%4==0 and año%100!=0:
    print("El año es bisiesto")
else:
    print("El año no es bisiesto")

"""
Ejercicio 8:
Crear un programa que convierta una cantidad de dólares a euros.
Utiliza una variable para almacenar la cantidad de dólares, realiza la conversión y muestra el resultado.
"""
dolares = 100
valorHoy= 0.92
conversion = dolares*valorHoy
print("Tendras",conversion,"euros")

"""
Ejercicio 9:
Escribir un programa que determine si un número dado es positivo, negativo o cero.
Utiliza una variable para almacenar el número, aplica condiciones y muestra el resultado.
"""
num= 0
if num>0:
    print("El numero es positivo")
elif num<0:
    print("El numero es negativo")
else:
    print("El numero es igual a 0")


"""
Ejercicio 10:
Crear un programa que calcule el promedio de tres números dados.
Utiliza tres variables para almacenar los números, realiza el cálculo y muestra el resultado.
"""
nota1=2
nota2=10
nota3=7
print("El promedio es de:",round((nota1+nota2+nota3)/3))

"""
Ejercicio 11:
Crear un programa que determine si un número dado es primo o no.
Utiliza una variable para almacenar el número, aplica las reglas para determinar si es primo y muestra el resultado.
num3= 5
if num%1==0 and num%num==0:
    print("El numero es primo")
"""

"""
Ejercicio 12:
Escribir un programa que determine si un número dado es múltiplo de otro.
Utiliza dos variables para almacenar los números, aplica el operador de módulo y muestra el resultado.
"""


"""
Ejercicio 13:
Crear un programa que calcule el factorial de un número dado.
Utiliza una variable para almacenar el número, realiza el cálculo del factorial y muestra el resultado.
"""
