import web

urls = (
    '/', 'mvc.controllers.lista_productos.MostrarListaProductos',
    '/insertar', 'mvc.controllers.insertar_productos.InsertarProducto',
    r'/detalle_producto/(\d+)', 'mvc.controllers.detalle_productos.DetalleProducto',
    r'/borrar_producto/(\d+)', 'mvc.controllers.borrar_productos.BorrarProducto',
    r'/actualizar_producto/(\d+)', 'mvc.controllers.actualizar_productos.ActualizarProducto'
)

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
