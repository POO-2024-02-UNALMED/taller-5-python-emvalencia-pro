from zooAnimales.mamifero import Mamifero
from zooAnimales.anfibio import Anfibio
from zooAnimales.ave import Ave
from zooAnimales.pez import Pez
from zooAnimales.reptil import Reptil
class Animal:
    totalAnimales = 0

    def __init__(self, nombre=None, edad=None, habitat=None, genero=None):
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        self._zona = None
        Animal.totalAnimales += 1

    def getNombre(self):
        return self._nombre

    def setNombre(self, nombre):
        self._nombre = nombre

    def getEdad(self):
        return self._edad

    def setEdad(self, edad):
        self._edad = edad

    def getHabitat(self):
        return self._habitat

    def setHabitat(self, habitat):
        self._habitat = habitat

    def getGenero(self):
        return self._genero

    def setGenero(self, genero):
        self._genero = genero

    def getZona(self):
        return self._zona

    def setZona(self, zona):
        self._zona = zona

    @classmethod
    def getTtotalAnimales(cls):
        return cls.totalAnimales

    @classmethod
    def setTotalAnimales(cls, total):
        cls.totalAnimales = total

    @staticmethod
    def totalPorTipo():
        return (f"Mamiferos: {Mamifero.cantidad_mamiferos()}\n"
                f"Aves: {Ave.cantidad_aves()}\n"
                f"Reptiles: {Reptil.cantidad_reptiles()}\n"
                f"Peces: {Pez.cantidad_peces()}\n"
                f"Anfibios: {Anfibio.cantidad_anfibios()}")

    def __str__(self):
        if self._zona is None:
            return (f"Mi nombre es {self._nombre}, tengo una edad de {self._edad}, habito en {self._habitat} y mi genero es {self._genero}")
        else:
            return (f"Mi nombre es {self._nombre}, tengo una edad de {self._edad}, habito en {self._habitat} y mi genero es {self._genero}, la zona en la que me ubico es {self._zona}, en el {self._zona.zoo}")

    def movimiento(self):
        return "desplazarse"
