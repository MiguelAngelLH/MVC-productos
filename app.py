import web

# Rutas de los controladores
urls = (
    '/', 'mvc.controllers.lista_productos.Lista',
    '/insertar', 'mvc.controllers.insertar_productos.Insertar',
    '/detalle/(\d+)', 'mvc.controllers.detalle_productos.Detalle',
     r'/borrar_producto/(\d+)', 'mvc.controllers.borrar_productos.BorrarProducto',
    r'/actualizar_producto/(\d+)', 'mvc.controllers.actualizar_productos.ActualizarProducto'
)  # Actualizamos la URL para que coincida con el formulario en el HTML


app = web.application(urls, globals())

# Punto de entrada
if __name__ == "__main__":
    web.config.debug = False  # Configuración para desactivar el modo debug
    app.run()