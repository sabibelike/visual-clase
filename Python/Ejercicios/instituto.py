'''
Ejercicio: Sistema de Gestión de Alumnos en un Instituto
Enunciado:
Desarrolla un programa para gestionar la información de los alumnos de un instituto. El programa debe permitir el manejo de los datos utilizando 
diccionarios para almacenar la información de cada alumno. Cada alumno tendrá un nombre y un diccionario con sus notas en diferentes asignaturas. El programa debe proporcionar las siguientes funcionalidades:
Agregar Alumno:
Modificar Notas:
Permitir al usuario modificar las notas de un alumno ya registrado.
Eliminar Alumno:
Permitir al usuario eliminar un alumno del sistema.
Mostrar Información de un Alumno:
Permitir al usuario ver la información completa de un alumno.
Mostrar el nombre del alumno y sus notas en todas las asignaturas.
Promedio de un Alumno:
Calcular y mostrar el promedio de las notas de un alumno.
Promedio General:
Calcular el promedio general de todas las asignaturas de todos los alumnos.
***Listado de Alumnos con Promedios Menores a 5:
Requisitos Adicionales:
Utilizar diccionarios para almacenar la información de los alumnos, donde la clave es el nombre del alumno y el valor es otro 
diccionario que contiene las asignaturas como claves y las notas como valores.
Gestionar entradas no válidas con mensajes de error apropiados.
Implementar un menú que permita al usuario elegir la funcionalidad que desea utilizar.
El objetivo de este ejercicio es que practiques con diccionarios en Python para manipular datos estructurados de una forma eficiente.

alumno1 = {"nombre": "Andrea", "biologia": 10, "programacion": 10}
alumno2 = {"nombre": "Luis", "biologia": 10, "programacion": 8}
alumno3 = {"nombre": "David", "biologia": 10, "programacion": 15}

alumnosNotas = {"Andrea": [10, 4, 8], "David": [11,10,10], "Luis": [8,10,20]}
listaAlumnos = []
listaAlumnos.append(alumno1)
listaAlumnos.append(alumno2)
listaAlumnos.append(alumno3)

print(list(map(lambda x : x, alumno1.keys())))
promedio = list(map(lambda x : (x[0]+x[1]+x[2])/3, alumnosNotas.values()))
promedioAlumnos = dict(map(lambda x,y : (x,y), alumnosNotas, promedio))
print(promedioAlumnos)
'''
class Alumno:
    def __init__(self, nombre):
        self.nombre = nombre
        self.notas = []
    
    def agregarNota(self, nuevaNota):
        self.notas.append(nuevaNota)
            
class Instituto:
    
    def __init__(self):
        self.listaEstudiantes = []
        self.diccionario = {}

        self.listaEstudiantes.append(self.diccionario)
                
    def agregarAlumno(self, Alumno):
        if Alumno in self.diccionario:
            print("Ya esta inscrito bro")
        else:
            self.diccionario[Alumno.nombre]= Alumno.notas
        
    
    def mostrarEstudiantes(self):
        print(list(map(lambda x : x, self.listaEstudiantes)))
    
    def promedioEstudiantes(self):
        promedio = list(map(lambda x : x))



alumno1 = Alumno("Andrea")
insti = Instituto()
insti.agregarAlumno(alumno1)
insti.mostrarEstudiantes()
alumno1.agregarNota(8)
insti.mostrarEstudiantes()
alumno2 = Alumno("Luis")
insti.agregarAlumno(alumno2)
insti.mostrarEstudiantes()









