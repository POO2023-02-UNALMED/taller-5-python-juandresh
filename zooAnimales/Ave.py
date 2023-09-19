from zooAnimales.Animal import Animal

class Ave(Animal):

    _listado = []
    halcones = 0
    aguilas = 0

    def __init__(self, nombre, edad, habitat, genero, colorPlumas):
        super().__init__(nombre, edad, habitat, genero)
        self._colorPlumas = colorPlumas

    @staticmethod
    def cantidadAves():
        return(len(Ave._listado))
    
    @classmethod
    def crearHalcon(cls, nombre, edad, genero):
        cls.halcones +=1
        return cls(nombre, edad, 'montanas', genero, 'cafe glorioso')
    
    @classmethod
    def crearAguila(cls, nombre, edad, genero):
        cls.aguilas +=1
        return cls(nombre, edad, 'montanas', genero, 'blanco y amarillo')
    
    def setColorPlumas(self, colorPlumas):
        self._colorPlumas = colorPlumas
    
    def getColorPlumas(self):
        return self._colorPlumas
    

