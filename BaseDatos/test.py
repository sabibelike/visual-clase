import unittest
from libreria import Libreria  # Importamos la clase Libreria del módulo libreria

class TestLibreria(unittest.TestCase):
    def setUp(self):
        """Configura el contexto para las pruebas."""
        # Inicializamos una nueva instancia de la clase Libreria antes de cada prueba.
        self.biblioteca = Libreria()
        # Añadimos dos libros a la biblioteca como datos iniciales para las pruebas.
        self.biblioteca.anadir_libro('Cien años de soledad', 'Gabriel García Márquez', 'Novela', 1967)
        self.biblioteca.anadir_libro('', 'Ernesto Sábato', 'Novela', 1948) #Aqui nos dará un error por intentar agregar un libro sin titulo

    def test_anadir_libro(self):
        """Prueba que se añadan libros correctamente."""
        self.biblioteca.anadir_libro('1984', 'George Orwell', 'Ciencia Ficción', 1949)
        # Verificamos que el libro añadido está en la biblioteca.
        self.assertTrue(any(libro['titulo'] == '1984' for libro in self.biblioteca.libros))

    def test_buscar_libro(self):
        """Prueba la búsqueda de libros por título."""
        # Buscamos un libro por su título exacto.
        libros = self.biblioteca.buscar_libro('Cien años de soledad')
        # Verificamos que se encuentre exactamente un libro con ese título y que corresponda al buscado.
        self.assertTrue(len(libros) == 1 and libros[0]['titulo'] == 'Cien años de soledad')

    def test_buscar_por_autor(self):
        """Prueba la búsqueda de libros por autor."""
        # Buscamos libros que contengan el nombre del autor 'Gabriel García Márquez'.
        libros = self.biblioteca.buscar_por_autor('Gabriel García Márquez')
        # Verificamos que todos los libros devueltos tienen el autor correcto.
        self.assertTrue(len(libros) == 1 and libros[0]['autor'] == 'Gabriel García Márquez')

    def test_eliminar_libro(self):
        """Prueba que se pueden eliminar libros."""
        # Eliminamos un libro por su título.
        respuesta = self.biblioteca.eliminar_libro('El túnel')
        # Verificamos que el libro fue eliminado de la biblioteca.
        self.assertTrue('eliminado' in respuesta.lower() and not any(libro['titulo'] == 'El túnel' for libro in self.biblioteca.libros))

    def test_guardar_y_cargar_libros(self):
        """Prueba la funcionalidad de guardar y cargar libros."""
        # Guardamos la lista de libros en un archivo JSON.
        self.biblioteca.guardar_libros('libros_test.json')
        # Limpiamos la lista de libros para simular que la aplicación fue cerrada y reabierta.
        self.biblioteca.libros = []
        # Cargamos la lista de libros desde el archivo JSON.
        self.biblioteca.cargar_libros('libros_test.json')
        # Verificamos que se hayan cargado correctamente los libros.
        self.assertTrue(len(self.biblioteca.libros) == 2)

if __name__ == '__main__':
    unittest.main()
    
def test_actualizar_libro(self):
    """Prueba la actualización de los detalles de un libro."""
    self.biblioteca.anadir_libro('La sombra del viento', 'Carlos Ruiz Zafón', 'Novela', 2001)
    respuesta = self.biblioteca.actualizar_libro('La sombra del viento', 'La sombra del viento 2', 'Carlos Ruiz Zafón', 'Novela', 2002)
    libro_actualizado = self.biblioteca.buscar_libro('La sombra del viento 2')[0]
    self.assertTrue('actualizado' in respuesta.lower() and libro_actualizado['anio'] == 2002)