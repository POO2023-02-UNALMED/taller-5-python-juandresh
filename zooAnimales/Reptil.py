from zooAnimales.Animal import Animal

class Reptil(Animal):

    _listado = []
    iguanas = 0
    serpientes = 0

    def __init__(self, nombre, edad, habitat, genero, colorEscamas, largoCola):
        super().__init__(nombre, edad, habitat, genero)
        self._colorEscamas = colorEscamas
        self._largoCola = largoCola

    @staticmethod
    def cantidadReptiles():
        return(len(Reptil._listado))
    
    @classmethod
    def crearIguana(cls, nombre, edad, genero):
        cls.iguanas +=1
        return cls(nombre, edad, 'humedal', genero, 'verde', 3)
    
    @classmethod
    def crearSerpiente(cls, nombre, edad, genero):
        cls.serpientes +=1
        return cls(nombre, edad, 'jungla', genero, 'blanco', 1)