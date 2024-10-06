#Implementación de la clase CatálogoPelicula
#Esta es la clase que va a gestionar todo el catálogo de películas
#Gestionar operaciones como agregar, listar y eliminar películas del catálogo.
#Atributos: nombre: El nombre del catálogo y 
#ruta_archivo: La ruta del archivo donde se va a guardar el catálogo.


class CatálogoPelícula:
    #Constructor
    def __init__(self, título_catálogo): 
        self.nombre= título_catálogo #Atributo
        self.ruta_archivo= f'{título_catálogo}.txt' #Debería abrir un archivo con el atributo

#Método agregar 'add' open(self.ruta_archivo, 'a')
    def agregar(self,película):  #Agregar
        with open(self.ruta_archivo, 'a') as file: #Se crea y agrega 
            file.write(f'{película.título}, {película.director}, {película.año} \n') #imprimen los detalles de la película agregada

    def listar(self): #listar
        try:
    
    def eliminar(self): #eliminar
        

#lo mismo con lo demás: listar, elminar, etc.

catálogo = CatálogoPelícula('MisPeliculas')
print(catalogo)