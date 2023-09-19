from gestion.Zona import Zona
class Zoologico():

    _zonas=[]

    def __init__(self, nombre, ubicacion):
        self._nombre = nombre
        self._ubicacion = ubicacion

    def cantidadTotalAnimales(self):
        total=0
        for Zona in self._zonas:
            total += Zona.cantidadAnimales

    def agregarZonas(self, zona):
        self._zonas.append(zona)

            