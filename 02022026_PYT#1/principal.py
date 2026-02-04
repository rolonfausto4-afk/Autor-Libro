from libro import Libro
from autor import Autor
from libro_bd import Libro_bd
from api_base_autores import Api_autores_bd

api_autores_bd= Api_autores_bd()
bd_libro= Libro_bd()

libro1= Libro("23/34/7890", 250, "Ficción")
libro2= Libro("12/45/6789", 300, "Ciencia")
libro3= Libro("56/78/9012", 150, "Historia")

autor1= Autor("michelle","r5@gmail.com","milleo", "34565324")
autor2= Autor("auron","au@gmail.com","elvrsito","456532")

lista_libros= [libro1, libro2, libro3]

api_autores_bd.registrar_libro(autor1)
api_autores_bd.registrar_libro(autor2)

bd_libro.extender_libro(lista_libros)

bd_libro.mostrar_lista_libros()

api_autores_bd.mostrar_lista_autores()