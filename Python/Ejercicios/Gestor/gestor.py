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
    def __init__(self, id, descripcion, fecha):
        self.id = id
        self.descripcion = descripcion
        self.estado = "Pendiente"
        self.fecha = fecha
        
    def cambiarEstado(self, nuevoEstado, nuevaFecha):
        self.estado = nuevoEstado
        self.fecha = nuevaFecha

class Gestor(Tarea):
    def __init__(self, id, descripcion):
        super().__init__(id, descripcion)
        self.listaTarea = []
        
    def agregarTarea(self, Tarea):
        self.listaTarea.append(Tarea)
    
    def eliminarTarea(self, Tarea):
        if Tarea in self.listaTarea:
            self.listaTarea.remove(Tarea)
        else: 
            print("Papito no existe esa tarea")
    
    def mostrarTareas(self):
        listado = self.listaTarea
        for x in range listado:
            print(x)

tarea1 = Tarea(1, "Hacer la cama", None)
tarea2 = Tarea(2, "Llamar cita", None)
tarea3 = Tarea(3, "Ah mamar", None)

gestoria = Gestor
gestoria.agregarTarea(tarea1)
gestoria.agregarTarea(tarea2)
gestoria.agregarTarea(tarea3)

gestoria.mostrarTareas