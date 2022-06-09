from Tienda import Tienda
if __name__ == '__main__':


    T1=Tienda("Moto",-6,100)
    T1.imprimirLista()

    T1.agregarProducto("Carro",3,2000)
    T1.imprimirLista()

    T2 = Tienda()
    T2.imprimirLista()

    T3=Tienda("Motoneta",2,100)
    T3.imprimirLista()
