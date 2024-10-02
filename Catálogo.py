#Implementación de la clase CatalogoPelicula
#Esta es la clase que va a gestionar todo el catálogo de películas
# Gestionar operaciones como agregar, listar y eliminar películas del catálogo.
# Atributos: nombre: El nombre del catálogo y 
# ruta_archivo: La ruta del archivo donde se va a guardar el catálogo.


class CatálogoPelícula:
    #Constructor
    def __init__(self, nombre_catálogo): 
        self.nombre= nombre_catálogo #Atributo
        self.ruta_archivo= f'{nombre_catálogo}.txt' #Debería abrir un archivo con el atributo


#Método agregar 'add' open(self.ruta_archivo, 'a')
#lo mismo con lo demás: listar, elminar, etc.

catalogo = CatálogoPelícula("MisPeliculas")
print(catalogo)