class Libro:
    def __init__(self, fecha_publicacion , cantidad_hojas, tematica):
        self.fecha_publicacion= fecha_publicacion
        self.cantidad_hojas= cantidad_hojas
        self.tematica= tematica

    def get_fecha_publicacion(self):
        return self.fecha_publicacion
    
    def get_cantidad_hojas(self):
        return self.cantidad_hojas
    
    def get_tematica(self):
        return self.tematica
       
    def set_fecha_publicacion(self, fecha_publicacion):
        self.fecha_publicacion= fecha_publicacion

    def set_cantidad_hojas(self, cantidad_hojas):
        self.cantidad_hojas= cantidad_hojas

    def set_tematica(self, tematica):
        self.tematica= tematica