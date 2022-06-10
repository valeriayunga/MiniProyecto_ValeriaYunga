package ec.edu.utpl.poo.model;

public class Tienda {

 protected  int contador;  //Atributo de clase
 private String articulo;  //Atributo de instancia
 private int cantidad;     //Atributo de instancia
 private double precio;    //Atributo de instancia
 private static String cadena="";
 public int maximoProductos=10; //Atributo de clase

 public Tienda (){
  this.articulo=null;
  this.cantidad=0;
  this.precio=0;
  contador=0;
 }

 public Tienda(String articulo, int cantidad, double precio) {
  if (validarCantidad(cantidad)==true&&validarPrecio(precio)==true){
   this.articulo=articulo;
   this.setCantidad(cantidad);
   this.setPrecio(precio);
   contador=1;
   cadena = String.format("%s%s\t\t\t%d\t\t%.2f\n",cadena, this.articulo,getCantidad(),getPrecio());
  }else{
   throw new IllegalArgumentException("Cantidad o precio no aptos");
  }
 }

 public int getCantidad() {
  return cantidad;
 }

 public void setCantidad(int cantidad) {
  this.cantidad = cantidad;
 }

 public double getPrecio() {
  return precio;
 }

 public void setPrecio(double precio) {
  this.precio = precio;
 }


 private boolean validarCantidad(int cantidad ) {
  if (cantidad >= 0 && cantidad <= maximoProductos) {
   return true;

  } else {
   return false;
  }
 }
  private boolean validarPrecio ( double precio) {
   if (cantidad >= 0) {
    return true;

   }else {
    return false;
   }
 }

 public void agregarProductos (String articulo, int cantidad,double precio){
  if (validarCantidad(cantidad)==true&&validarPrecio(precio)==true){
   this.articulo=articulo;
   this.setCantidad(cantidad);
   this.setPrecio(precio);
   contador=contador+1;
   cadena = String.format("%s%s\t\t\t%d\t\t%.2f\n",cadena, this.articulo,getCantidad(),getPrecio());
  }else{
   throw new IllegalArgumentException("Cantidad o precio no aptos");
  }
 }
 public void imprimir(){
  System.out.println("LISTA DE PRODUCTOS");
  System.out.println("ARTICULO\tCANTIDAD\tPRECIO");
  System.out.println(cadena);
  System.out.println("Número de productos agregados: "+contador);
 }
}