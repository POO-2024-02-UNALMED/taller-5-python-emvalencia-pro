class Zoologico:
    def __init__(self, nombre=None, ubicacion=None):
        self._nombre = nombre
        self._ubicacion = ubicacion
        self._zonas = []

    def getNombre(self):
        return self._nombre

    def setNombre(self, nombre):
        self._nombre = nombre

    def getUbicacion(self):
        return self._ubicacion
    
    def setUbicacion(self, ubicacion):
        self._ubicacion = ubicacion
        
    def getZonas(self):
        return self._zonas

    def setZonas(self, zonas):
        self._zonas = zonas
        
    def agregar_zona(self, zona):
        self._zonas.append(zona)

    def cantidad_total_animales(self):
        total = 0
        for zona in self._zonas:
            total += zona.cantidad_animales()
        return total