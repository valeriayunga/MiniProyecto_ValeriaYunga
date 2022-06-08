class Paciete:
    __nombre = str
    __cedula= str
    __numero=int
    __sintomas=str
    __diagnostico=str

    def __init__(self,nombre,cedula,numero,sintomas,diagnostico):
        self.__nombre=nombre
        self.__cedula=cedula
        self.__numero=numero
        self.__sintomas=sintomas
        self.__diagnostico=diagnostico
