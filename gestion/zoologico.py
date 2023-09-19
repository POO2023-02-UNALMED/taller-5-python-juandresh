class Zoologico():

    _zonas=[]

    def __init__(self, nombre, ubicacion):
        self._nombre = nombre
        self._ubicacion = ubicacion
        #self._zonas=[]

    def cantidadTotalAnimales(self):
        total=0
        for zona in self._zonas:
            total += zona.cantidadAnimales()
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
    
    #def setZona(self, zona):
    #    self._zonas = zona
    
    def getZona(self):
        return self._zonas