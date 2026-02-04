class Autor:
    def __init__(self,nombre, correo, contraseña, cedula):
        self.nombre= nombre
        self.correo= correo
        self.contraseña= contraseña
        self.cedula= cedula

    def get_nombre(self):
        return self.nombre
    
    def get_correo(self):
        return self.correo
    
    def get_contraseña(self):
        return self.contraseña
    
    def get_cedula(self):
        return self.cedula
    
    def registrar_nombre(self):
        nombre= str(input("Nombre del autor: "))
        self.nombre = nombre

    def registrar_correo(self):
        correo= str(input("Correo del autor: "))
        self.correo = correo

    def registrar_contraseña(self):
        contraseña= str(input("Contraseña del autor: "))
        self.contraseña = contraseña

    def registrar_cedula(self):
        cedula= str(input("Cédula del autor: "))
        self.cedula = cedula