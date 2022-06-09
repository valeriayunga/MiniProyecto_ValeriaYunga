from tabulate import tabulate

#Definimos la clase "Tienda" usando la palabra reservada class, seguida de un espacio y el nombre comenzando por
#mayúscula de la clase,y el símnolo ":" que se usa para iniciar el conjunto de atributos y métodos que se
#usarán en la clase a partir de la identación.
class Tienda:

#Se declaran los atributos de la clase:
#Para que los atributos tengan un modoficador de acceso private se usan 2 guiones bajos "__", para protected se usa
# un guione bajo "_" y para prublic no es necesario ningún símbolo ya que por defecto los atributos son publicos
#Seguido del modificador de acceso nombramos nuestra atributo, y definimos el tipo de dato:
# str para cadenas, int para enteros, float para decimales, y [] para listas.
    _contador=int
    __precio=float
    __articulo=str
    __cantidad=int
    __lista=[]


#
    def __init__(self,articulo=None,cantidad=None,precio=None):
        if articulo is None and cantidad is None and precio is None:
            self.__articulo= None
            self.__cantidad=0
            self.__precio=0
            self.__lista.append([self.__articulo,self.__cantidad,self.__precio])
            self._contador=0
        else:
            if self.__validarPrecio(precio)==True and self.__validarCantidad(cantidad)==True:
                self.__articulo=articulo
                self.setPrecio(precio)
                self.setCantidad(cantidad)
                self.__lista.append([self.__articulo,self.getCantidad(),self.getPrecio()])
                self._contador = 1
            else:
                print(IOError("El precio  y la cantidad de productos debe ser mayor a 0"))
                self._contador = 0



    def setPrecio(self,precio):

            self.__precio=precio


    def setCantidad(self, cantidad):

            self.__cantidad = cantidad


    def getPrecio(self):
        return self.__precio

    def getCantidad(self):
        return self.__cantidad
    def getArticulo(self):
        return self.__articulo

    def __validarPrecio (self,precio):
         if (precio>=0 ):
            return True
         else:
            IOError("El precio debe ser mayor a 0")

    def __validarCantidad(self,cantidad):
         if (cantidad>=0 ):
            return True
         else:
           IOError("La cantidad debe ser mayor a 0")

    def agregarProducto(self,articulo,cantidad,precio):
        if (self.__validarPrecio(precio) == True and self.__validarCantidad(cantidad)== True):
            self.__lista.append([articulo,cantidad,precio])
            self._contador = self._contador + 1

    def imprimirLista (self):
        print("LISTA DE PRODUCTOS:")
        print(tabulate(self.__lista, headers=['Producto','Cantidad','Precio']))
        print(f"Numero de productos agregados: ",self._contador,"\n------------------------\n")




