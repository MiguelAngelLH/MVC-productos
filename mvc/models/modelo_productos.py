import web
import csv

class Producto:
    def __init__(self, id_producto, nombre, descripcion, precio, existencias):
        self.id_producto = id_producto
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.existencias = existencias
    # Carga los productos del csv a la vista
    @classmethod
    def cargar_productos_desde_csv(cls, archivo_csv):
        productos = []
        with open(archivo_csv, newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                producto = cls(
                    id_producto=int(row['id_producto']),
                    nombre=row['nombre'],
                    descripcion=row['descripcion'],
                    precio=float(row['precio']),
                    existencias=int(row['existencias'])
                )
                productos.append(producto)
        return productos
    # Metodo para Registrar un nuevo producto al csv
    @classmethod
    def insertar_productos(cls, nombre, descripcion, precio, existencias):
        nuevo_producto = cls.obtener_ultimo_id() + 1  # Generar nuevo ID
        nuevo_producto_obj = cls(nuevo_producto, nombre, descripcion, precio, existencias)

        with open("productos.csv", mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([nuevo_producto_obj.id_producto, nuevo_producto_obj.nombre,
                             nuevo_producto_obj.descripcion, nuevo_producto_obj.precio,
                             nuevo_producto_obj.existencias])

    @classmethod
    def obtener_ultimo_id(cls):
        productos = cls.cargar_productos_desde_csv("productos.csv")
        if productos:
            return max(producto.id_producto for producto in productos)
        else:
            return 0
    # Metodo para cargar un producto en la vista detalle_producto.html
    @classmethod
    def obtener_producto_por_id(cls, id_producto):
        productos = cls.cargar_productos_desde_csv("productos.csv")
        for producto in productos:
            if producto.id_producto == id_producto:
                return producto
        return None
    # Metodo para cargar un producto en la vista borrar_productos.html
    @classmethod
    def obtener_producto_delete(cls, id_producto):
        productos = cls.cargar_productos_desde_csv("productos.csv")
        for producto in productos:
            if producto.id_producto == id_producto:
                return producto
        return None

    @classmethod
    def borrar_producto_por_id(cls, id_producto):
        productos = cls.cargar_productos_desde_csv("productos.csv")

        # Filtrar los productos, excluyendo el que queremos borrar
        productos_actualizados = [p for p in productos if p.id_producto != id_producto]

        # Guardar los productos actualizados en el archivo CSV
        cls.guardar_productos_en_csv(productos_actualizados)

    @classmethod
    def guardar_productos_en_csv(cls, productos):
        with open("productos.csv", mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["id_producto", "nombre", "descripcion", "precio", "existencias"])
            for producto in productos:
                writer.writerow([producto.id_producto, producto.nombre, producto.descripcion, producto.precio, producto.existencias])
                
    # Metodo para cargar un producto en la vista actualizar_productos.html
    @classmethod
    def obtener_producto_update(cls, id_producto):
        productos = cls.cargar_productos_desde_csv("productos.csv")
        for producto in productos:
            if producto.id_producto == id_producto:
                return producto
        return None

    # En el modelo (modelo_productos.py)
    @classmethod
    def actualizar_producto(cls, id_producto, nombre, descripcion, precio, existencias):
        productos = cls.cargar_productos_desde_csv("productos.csv")

        for producto in productos:
            if producto.id_producto == id_producto:
                # Actualizar los detalles del producto
                producto.nombre = nombre
                producto.descripcion = descripcion
                producto.precio = precio
                producto.existencias = existencias

        # Guardar los productos actualizados en el archivo CSV
        cls.guardar_productos_en_csv(productos)