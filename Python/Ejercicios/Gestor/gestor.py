'''
Se quiere crear un programa en Python para gestionar una listade tareas pendientes. El programa
debe permitir al usuario agregar nuevas tareas, marcar tareas como completadas, eliminar tareas de la lista
y ver todas las tareas pendientes.
   
El programa debe de comenzar mostrando un menú de opciones al usuario, donde pueda seleccionar la
operación que desea realizar. Se elige agregar una nueva tarea, debe ingresar la descripción de la tarea y agreagarla
a la lista de tareas pendientes.Si se marca una tarea como completa, debe mostrar la lista de tareas pendientes
y permitir al usuario seleccionar la tarea que desea marcar como completa.
   
Cuando un usuario completa una tarea, debe eliminarse de la lista de tareas pendientes y agregarse a la lista
de tareas completas. Ahi se almacena su descripción y la fecha en la que se completo. El programa tambien debe
permitir a el usuario eliminar tareas pendientes si ya no son necesarias.
   
Para ayudar al usuario a mantenerse organizado debe haber una opción para ver tods las tareas pendientes mostrando
descripción y ID unico. Esto facilita la referencia cuando el usuario quiera eliminar una tarea.
'''
'''
tarea
descripcion de tarea 
marcar completas

gestor<lista de tareas(pendientes)
lista tareas completadas
agregar
eliminar 
ver todas las tareas pendientes
'''
class Tarea:
    def __init__(self, descripcion):
        self.descripcion = descripcion
        self.estado = "Pendiente"
        
    def cambiarEstado(self, nuevoEstado):
        self.estado = nuevoEstado
    
    def getEstado(self):
        print(self.estado)
    
    def getDescripcion(self):
        print(self.descripcion)
    
    def mostrarInfo(self):
        print("Descripcion:",self.descripcion,"estado:",self.estado)
        
'''     
class Gestor:
    def __init__(self):
        self.listaTareas = []
        
    def agregarTarea(self, Tarea):
        if Tarea in self.listaTareas:
            print("Ya esta dentro bro")
        else:
            self.listaTareas.append(Tarea)
    
    def eliminarTarea(self, Tarea):
        if Tarea in self.listaTareas:
            self.listaTareas.remove(Tarea)
        else:
            print("Mi loco, esa tarea ya no ta aqui")
            
    def mostrarTareas(self):
       print(list(map(Tarea.mostrarInfo(), self.listaTareas)))
 '''         

listaTareas = []
        
tarea1 = Tarea("Hacer la cama")
tarea2 = Tarea("No se")
tarea3 = Tarea("Estudia malparia")

listaTareas.append(tarea1)
listaTareas.append(tarea2)
listaTareas.append(tarea3)
print(list(map(Tarea.mostrarInfo, listaTareas)))
