class Libro_bd:
    def __init__(self):
        self.lista_libros= []

    def registrar_libro(self, libro):
        self.lista_libros.append(libro)
        
    def extender_libro(self, nueva_lista):
        self.lista_libros.extend(nueva_lista)

    def insertar_libro(self, posicion):
        self.lista_libros.insert(posicion) 
    def remover_libro(self, ):
        self.lista_libros.remove()

    def eliminar_libro(self, posicion):
        self.lista_libros.pop(posicion)

    def buscar_libro(self, poscicion):
        self.lista_libros.index(poscicion)

    def contar_lista(self):
        self.lista_libros.count()

    def ordenar_lista(self):
        self.lista_libros.sort()

    def revertir_lista(self):
        self.lista_libros.reverse()

    def ver_lista(self):
        print(f"{self.lista_libros}")

    def mostrar_lista_libros(self):
        """for libro in self.lista_libros:
            print(f"{libro}\n")"""
        
        for i in range(len(self.lista_libros)):
            
            tematica= self.lista_libros[i].get_tematica()
            fecha_publicacion= self.lista_libros[i].get_fecha_publicacion()
            cantidad_hojas= self.lista_libros[i].get_cantidad_hojas()

            print(f"Libro {i+1}:\n Fecha de publicación: {fecha_publicacion} \n Cantidad de hojas: {cantidad_hojas} \n Temática: {tematica} \n")
