
class Doctor:
    __nombre = str
    __especialidad=str
    __pacientes=

    def __init__(self,nombre, especialidad):
        self.__nombre=nombre
        self.__especialidad=especialidad



    def getNombre (self):
        return self.__nombre

    def setNombre (self,a):
        self.__nombre=a

    def geteEspecialidad(self):
        return self.__especialidad

    def setnEspecialidad(self, a):
        self.__nombre = a
pass
