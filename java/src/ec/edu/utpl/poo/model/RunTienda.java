package ec.edu.utpl.poo.model;

public class RunTienda {
    public static void main(String[] args) {


        Tienda T1 = new Tienda();
        System.out.println(T1.getCantidad());
        T1.imprimir();
        T1.agregarProductos("Moto",3,200);
        T1.imprimir();

        Tienda T2 = new Tienda("Carro",5,300);
        T1.imprimir();

        Tienda T3= new Tienda("Patineta",12,100);
        T3.imprimir();
    }
}
