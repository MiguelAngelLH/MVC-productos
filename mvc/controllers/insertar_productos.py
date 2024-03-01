import web
from mvc.models.modelo_productos import Producto

render = web.template.render('mvc/views/', base="layout")

class InsertarProducto:
    def GET(self):
        return render.insertar_productos()

    def POST(self):
        try:
            data = web.input()
            nombre = data.get('nombre')
            descripcion = data.get('descripcion')
            precio = float(data.get('precio'))
            existencias = int(data.get('existencias'))

            Producto.insertar_productos(nombre, descripcion, precio, existencias)
            
            # Redirigir después de la inserción exitosa
            raise web.seeother('/')
        except Exception as e:
            # Imprimir el error para diagnóstico
            print(f"Error al insertar producto: {e}")
            
            # Puedes personalizar esta respuesta de error según tus necesidades
            return "Error al insertar el producto. Por favor, verifica los datos e intenta nuevamente."