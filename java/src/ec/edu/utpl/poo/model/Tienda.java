package ec.edu.utpl.poo.model;

public class Tienda {
 protected  int contador;
 private String articulo;
 private int cantidad;
 private double precio;
 private static String cadena="";
 private static int maximoProductos=10;

 public Tienda (){
  this.articulo=null;
  this.cantidad=0;
  this.precio=0;
  contador=0;

 }

 public Tienda(String articulo, int cantidad, double precio) {
  if (validarCantidad(cantidad)==true&&validarPrecio(precio)==true){
   this.setArticulo(articulo);
   this.setCantidad(cantidad);
   this.setPrecio(precio);
   contador=1;
   cadena = String.format("%s%s\t\t\t%d\t\t%.2f\n",cadena, this.getArticulo(),getCantidad(),getPrecio());
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
 public String getArticulo() {
  return articulo;
 }

 public void setArticulo(String articulo) {
  this.articulo = articulo;
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
   this.setArticulo(articulo);
   this.setCantidad(cantidad);
   this.setPrecio(precio);
   contador=contador+1;
   cadena = String.format("%s%s\t\t\t%d\t\t%.2f\n",cadena, this.getArticulo(),getCantidad(),getPrecio());
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