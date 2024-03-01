import web
from mvc.models.modelo_productos import Producto

render = web.template.render('mvc/views/', base="layout")

class BorrarProducto:
    def GET(self, id_producto):
        try:
            producto = Producto.obtener_producto_por_id(int(id_producto))
            if producto:
                return render.borrar_productos(producto=producto)
            else:
                return "Producto no encontrado"
        except Exception as e:
            return f"Error al obtener detalles del producto: {str(e)}"

    def POST(self, id_producto):
        try:
            Producto.borrar_producto_por_id(int(id_producto))

            # Redirige a la lista de productos después de borrar
            raise web.seeother('/')
        except Exception as e:
            return f"Error al borrar el producto: {str(e)}"