import web
from mvc.models.modelo_productos import Producto

render = web.template.render('mvc/views/', base='layout')

class MostrarListaProductos:
    def GET(self):
        # Lógica para leer productos desde el archivo CSV
        productos = Producto.cargar_productos_desde_csv("productos.csv")
        
        # Renderizar la lista de productos utilizando el archivo HTML
        return render.lista_productos(productos=productos)
