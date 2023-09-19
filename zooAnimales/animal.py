import zooAnimales

class Animal():

    _totalAnimales = 0

    def __init__(self, nombre, edad, habitat, genero, zona=None):
        self._nombre =nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        self._zona = zona
        Animal._totalAnimales += 1

    @staticmethod
    def totalPorTipo():
        mamiferos = zooAnimales.mamifero.Mamifero.cantidadMamiferos()
        aves = zooAnimales.ave.Ave.cantidadAves()
        reptiles = zooAnimales.reptil.Reptil.cantidadReptiles()
        peces = zooAnimales.pez.Pez.cantidadPeces()
        anfibios = zooAnimales.anfibio.Anfibio.cantidadAnfibios()
        return(f'Mamíferos: {mamiferos}\nAves: {aves}\nReptiles: {reptiles}\nPeces: {peces}\nAnfibios: {anfibios}')
    
    def toString(self):
        if self._zona is None:
            return(f'Mi nombre es {self._nombre}, dengo una edad de {self._edad}, habito en {self._habitat} y mi genero es {self._genero}') 
        else:   
            return(f'Mi nombre es {self._nombre}, dengo una edad de {self._edad}, habito en {self._habitat} y mi genero es {self._genero}, la zona en la que me ubico es {self._zona.getZona()}, en el {self._zona.getZoo().getNombre()}')
    
    @classmethod
    def setTotalAnimales(cls, totalAnimales):
        cls._totalAnimales = totalAnimales
    
    @classmethod
    def getTotalAnimales(cls):
        return cls._totalAnimales
    
    def setNombre(self, nombre):
        self._nombre = nombre
    
    def getNombre(self):
        return self._nombre
    
    def setEdad(self, edad):
        self._edad = edad
    
    def getEdad(self):
        return self._edad
    
    def setHabitat(self, habitat):
        self._habitat = habitat
    
    def getHabitat(self):
        return self._habitat
    
    def setGenero(self, genero):
        self._genero = genero
    
    def getGenero(self):
        return self._genero
    
    @classmethod
    def setZona(cls, zona):
        cls._zona = zona
    
    @classmethod
    def getZona(cls):
        return cls._zona