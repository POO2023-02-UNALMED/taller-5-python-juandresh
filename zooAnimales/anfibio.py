from zooAnimales.animal import Animal

class Anfibio(Animal):

    _listado = []
    ranas = 0
    salamandras = 0

    def __init__(self, nombre, edad, habitat, genero, colorPiel, venenoso):
        super().__init__(nombre, edad, habitat, genero)
        self._colorPiel =colorPiel
        self._venenoso = venenoso

    #@classmethod
    #def cantidadAnfibios(cls):
    #    return(len(cls._listado))

    @classmethod
    def cantidadAnfibios(cls):
        return cls.ranas + cls.salamandras
    
    @classmethod
    def crearRana(cls, nombre, edad, genero):
        cls.ranas +=1
        return cls(nombre, edad, 'selva', genero, 'rojo', True)
    
    @classmethod
    def crearSalamandra(cls, nombre, edad, genero):
        cls.salamandras +=1
        return cls(nombre, edad, 'selva', genero, 'negro y amarillo',True)
    
    def setColorPiel(self, colorPiel):
        self._colorPiel = colorPiel
    
    def getColorPiel(self):
        return self._colorPiel
    
    def setVenenoso(self, venenoso):
        self._venenoso = venenoso
    
    def isVenenoso(self):
        return self._venenoso