class Zona():

    _animales = []

    def __init__(self, nombre, zoo):
        self._nombre = nombre
        self._zoo = zoo

    def agregarAnimales(self, animal):
        self._animales.append(animal)

    def cantidadAnimales(self):
        return (len(self._animales))
    
    def setNombre(self, nombre):
        self._nombre = nombre
    
    def getNombre(self):
        return self._nombre

    def setZoo(self, zoo):
        self._zoo = zoo
    
    def getZoo(self):
        return self._zoo
    
    @classmethod
    def setAnimales(cls, animales):
        cls._animales = animales
    
    @classmethod
    def getAnimales(cls):
        return cls._animales