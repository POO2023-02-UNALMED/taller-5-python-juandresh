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
        return(f'Mamíferos: {zooAnimales.Mamifero.cantidadMamiferos()}\nAves: {zooAnimales.Ave.cantidadAves()}\nReptiles: {zooAnimales.Reptil.cantidadReptiles()}\nPeces: {zooAnimales.Pez.cantidadPeces()}\nAnfibios: {zooAnimales.Anfibio.cantidadAnfibios()}')
    
    def toString(self):
        if self._zona == None:
            return(f'Mi nombre es {self._nombre}, dengo una edad de {self._edad}, habito en {self._habitat} y mi genero es {self._genero}') 
        else:   
            return(f'Mi nombre es {self._nombre}, dengo una edad de {self._edad}, habito en {self._habitat} y mi genero es {self._genero}, la zona en la que me ubico es {self._zona}, en el {self._zona}')
    