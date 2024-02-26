import web
import csv

# Clase controladora para insertar productos
class Insertar:
    def GET(self):
        return render.insertar_productos()  # Renderizar el formulario HTML

    def POST(self):
        # Obtener los datos del formulario enviado por el usuario
        datos = web.input()

        # Insertar el producto en el archivo CSV
        insertar_producto(datos)

        # Redirigir a la página de éxito o mostrar un mensaje de éxito
        return "Producto insertado exitosamente"

# Función para insertar un nuevo producto en el archivo CSV
def insertar_producto(datos):
    # Obtener los datos del formulario
    nombre = datos.get('nombre')
    descripcion = datos.get('descripcion')
    precio = datos.get('precio')
    existencia = datos.get('existencia')

    # Leer el último ID utilizado
    ultimo_id = obtener_ultimo_id('productos.csv')

    # Generar un nuevo ID
    nuevo_id = ultimo_id + 1

    # Insertar el producto en el archivo CSV
    with open('productos.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([nuevo_id, nombre, descripcion, precio, existencia])

# Función para obtener el último ID utilizado en el archivo CSV
def obtener_ultimo_id(nombre_archivo):
    with open(nombre_archivo, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            pass
        if row:
            ultimo_id = int(row[0])
        else:
            ultimo_id = 0
    return ultimo_id

# Rutas de los controladores
urls = (
    '/insertar', 'Insertar',
)

app = web.application(urls, globals())
render = web.template.render('mvc/views/')  # Ajusta la ubicación de los archivos de plantillas HTML

# Punto de entrada
if __name__ == "__main__":
    web.config.debug = False  # Configuración para desactivar el modo debug
    app.run()