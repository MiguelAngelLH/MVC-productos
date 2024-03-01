import web
from mvc.models.modelo_productos import Producto

render = web.template.render('mvc/views/', base="layout")
    
# En el controlador (actualizar_productos.py)
class ActualizarProducto:
    def GET(self, id_producto):
        try:
            producto = Producto.obtener_producto_update(int(id_producto))
            if producto:
                return render.actualizar_productos(producto=producto)
            else:
                return "Producto no encontrado"
        except Exception as e:
            return f"Error al obtener detalles del producto: {str(e)}"

    def POST(self, id_producto):
        try:
            # Obtener datos del formulario
            data = web.input()
            nombre = data.get('nombre')
            descripcion = data.get('descripcion')
            precio = float(data.get('precio'))
            existencias = int(data.get('existencias'))

            # Actualizar el producto
            Producto.actualizar_producto(int(id_producto), nombre, descripcion, precio, existencias)

            # Redirige a la lista de productos después de actualizar
            raise web.seeother('/')
        except Exception as e:
            return f"Error al actualizar el producto: {str(e)}"