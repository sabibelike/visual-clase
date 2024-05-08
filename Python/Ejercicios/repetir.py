'''
Ejercicio 1
Crea un programa que procese una lista de tuplas, donde cada tupla representa una venta y contiene el nombre del producto,
la cantidad vendida y el precio unitario (ejemplo: [("manzana", 30, 0.50), ("banana", 20, 0.75)])
Filtra aquellos datos que tengan pocas unidades(menos de 10).
Quiero saber el total de ingresos de las ventas de estos productos
'''
from functools import reduce
# Lista de ventas donde cada tupla contiene el nombre del producto, cantidad vendida y precio unitario
ventas = [("manzana", 30, 0.50), ("banana", 20, 0.75), ("naranja", 5, 1.00), ("pera", 8, 0.60), ("melon", 25, 3.00)]
pocasUnidades = list(filter(lambda x : x[1]<10, ventas))
print(pocasUnidades)
ventas = list(map(lambda x : x[1]*x[2], pocasUnidades))
ventasTotales = reduce(lambda x,y : x+y, ventas)
print(ventasTotales)

'''
Ejercicio 2
Dado un diccionario que contiene el nombre del estudiante y su lista de calificaciones 
(por ejemplo, {"Ana": [4.5, 7.0, 8.0], "Juan": [5.0, 7.5, 6.0]}). Se requiere calcular el promedio de calificaciones de cada estudiante
seleccionando solo aquellos estudiantes con un promedio superior a 6.0.
Además, se quiere determinar el número total de estudiantes que superan este promedio.
'''

# Diccionario con el nombre del estudiante y su lista de calificaciones
calificaciones = {
    "Ana": [4.5, 7.0, 8.0],
    "Juan": [5.0, 7.5, 6.0],
    "Maria": [7.0, 8.5, 9.0],
    "Luis": [5.5, 6.0, 5.0]
}

'''
Ejercicio 3
Considera que tienes una lista de diccionarios, cada uno representando a una persona con claves 
como nombre, edad y ciudad. Se quiere poder filtrar las personas para seleccionar solo las personas que pertenecen a una ciudad específica.
Los datos devueltos tienen que ser la edad promedio de las personas de la ciudad seleccionada.
'''

# Lista de personas, cada una representada por un diccionario con nombre, edad y ciudad
personas = [
    {"nombre": "Ana", "edad": 25, "ciudad": "Madrid"},
    {"nombre": "Carlos", "edad": 32, "ciudad": "Barcelona"},
    {"nombre": "Marta", "edad": 45, "ciudad": "Madrid"},
    {"nombre": "Pablo", "edad": 22, "ciudad": "Valencia"},
    {"nombre": "Lorena", "edad": 29, "ciudad": "Madrid"},
    {"nombre": "Jordi", "edad": 35, "ciudad": "Barcelona"}
]
ciudadFiltrada = "Madrid"

personasMad = list(filter(lambda x : x["ciudad"]== ciudadFiltrada, personas))
edades = reduce(lambda x,y : x+y["edad"], personasMad,0)
edadPromedio = edades/len(personasMad)
print("La edad promedio es:",edadPromedio)
print(personasMad)



