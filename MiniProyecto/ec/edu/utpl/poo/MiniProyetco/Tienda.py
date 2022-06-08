
class Tienda:
    _contador=int=1
    __precio=float
    __articulo=str
    __cantidad=int
    __lista=[]

    def __init__(self,articulo,cantidad,precio):

            self.__articulo=articulo
            self.setPrecio(precio)
            self.setCantidad(cantidad)
            self.__lista.append({"Nombre del artículo":self.__articulo,"Cantidad del artículo":self.__cantidad,
                      "Precio del artículo" :self.__precio})

    """def __repr__(self):
        self.__precio = 0
        self.__cantidad = 0
        self._contador = 0
        self.__articulo = None"""

    def setPrecio(self,precio):
        if(self.__validarPrecio(precio)==True):
            self.__precio=precio


    def setCantidad(self, cantidad):
        if (self.__validarCantidad(cantidad) == True):
            self.__cantidad = cantidad

    def getPrecio(self):
        return self.__precio

    def getCantidad(self):
        return self.__cantidad
    def getAeticulo(self):
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
            self.__lista.append({"Nombre del artículo":articulo,"Cantidad de artículo":cantidad,"Precio del artículo":precio})

    def imprimirLista (self):

            print(self.__lista)

pass


