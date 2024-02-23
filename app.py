import web

# Rutas de los controladores
urls = (
    '/', 'mvc.controllers.lista_productos.Lista',
    '/insertar', 'mvc.controllers.insertar_productos.Insertar',
    '/detalle', 'mvc.controllers.detalles_productos.Detalle',
    '/borrar', 'mvc.controllers.borrar_productos.Borrar',
    '/actualizar', 'mvc.controllers.actualizar_productos.Actualizar',
)

app = web.application(urls, globals())

# Punto de entrada
if __name__ == "__main__":
    web.config.debug = False  # Configuración para desactivar el modo debug
    app.run()
