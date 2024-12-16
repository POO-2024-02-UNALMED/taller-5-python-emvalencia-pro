class Zona:
    def __init__(self, nombre=None, zoo=None):
        self._nombre = nombre
        self._zoo = zoo
        self._animales = []

    def nombre(self):
        return self._nombre

    def nombre(self, nombre):
        self._nombre = nombre

    def zoo(self):
        return self._zoo

    def zoo(self, zoo):
        self._zoo = zoo

    def animales(self):
        return self._animales

    def animales(self, animales):
        self._animales = animales
        
    def agregar_animal(self, animal):
        self._animales.append(animal)

    def cantidad_animales(self):
        return len(self._animales)
