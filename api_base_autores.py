class Api_autores_bd:

    def __init__(self):
        self.lista_autores= []

    def registrar_autor(self, autor):
            self.lista_autores.append(autor)
        
    def extender_autor(self, nueva_lista):
        self.lista_autores.extend(nueva_lista)

    def insertar_autor(self, posicion):
        self.lista_autores.insert(posicion)
    
    def remover_autor(self, ):
        self.lista_autores.remove()

    def eliminar_autor(self, posicion):
        self.lista_autores.pop(posicion)

    def buscar_autor(self, poscicion):
        self.lista_autores.index(poscicion)

    def contar_lista(self):
        self.lista_autores.count()

    def ordenar_lista(self):
        self.lista_autores.sort()

    def revertir_lista(self):
        self.lista_autores.reverse()

    def ver_lista(self):
        print(f"{self.lista_autores}")

    def mostrar_lista_autores(self):
        """for autor in self.lista_autores:
            print(f"{autor}\n")"""
        
        for i in range(len(self.lista_autores)):
            
            nombre= self.lista_autores[i].get_nombre()
            correo= self.lista_autores[i].get_correo()
            contraseña= self.lista_autores[i].get_contraseña()
            cedula= self.lista_autores[i].get_cedula()

            print(f"Autor {i+1}:\n Nombre: {nombre} \n Correo: {correo} \n Contraseña: {contraseña} \n Cédula: {cedula} \n")