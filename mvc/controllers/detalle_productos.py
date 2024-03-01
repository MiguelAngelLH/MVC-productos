import web
from mvc.models.modelo_productos import Producto

render = web.template.render('mvc/views/', base="layout")

class DetalleProducto:
    def GET(self, id_producto):
        try:
            print("ID del Producto:", id_producto)  # Agrega esta línea para imprimir el ID del producto
            producto = Producto.obtener_producto_por_id(int(id_producto))
            if producto:
                return render.detalle_productos(producto=producto)
            else:
                return "Producto no encontrado"
        except Exception as e:
            return f"Error al obtener detalles del producto: {str(e)}"