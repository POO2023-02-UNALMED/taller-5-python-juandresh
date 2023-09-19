#from gestion.Zona import Zona
class Zoologico():

    _zonas=[]

    def __init__(self, nombre, ubicacion):
        self._nombre = nombre
        self._ubicacion = ubicacion

    def cantidadTotalAnimales(self):
        total=0
        for Zona in self._zonas:
            total += Zona.cantidadAnimales
        return total

    def agregarZonas(self, zona):
        self._zonas.append(zona)

    def setNombre(self, nombre):
        self._nombre = nombre
    
    def getNombre(self):
        return self._nombre

    def setUbicacion(self, ubicacion):
        self._ubicacion = ubicacion
    
    def getUbicacion(self):
        return self._ubicacion
    
    @classmethod
    def setZonas(cls, zonas):
        cls._zonas = zonas
    
    @classmethod
    def getZonas(cls):
        return cls._zonas

            