class Zona():

    _animales = []

    def __init__(self, nombre, zoo):
        self._nombre = nombre
        self._zoo = zoo

    def agregarAnimales(self, animal):
        self._animales.append(animal)

    def cantidadAnimales(self):
        return (len(self._animales))