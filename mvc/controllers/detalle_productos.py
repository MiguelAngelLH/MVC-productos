import web
import csv

render = web.template.render('mvc/views/')  # Asegúrate de que la ruta 'mvc/views/' sea la correcta

urls = (
    '/', 'Lista',
    '/productos/(\d+)', 'Detalle'
)

app = web.application(urls, globals())

class Lista:
    def GET(self):
        productos = self.obtener_productos()  # Obtener los productos desde el archivo CSV
        return render.lista_productos(productos)

    def obtener_productos(self):
        productos = []
        with open('productos.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                productos.append(row)
        return productos

class Detalle:
    def GET(self, producto_id):
        producto = self.obtener_producto(producto_id)  # Obtener el producto según su ID
        return render.detalle_productos(producto)

    def obtener_producto(self, producto_id):
        with open('productos.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if int(row['id']) == int(producto_id):
                    return row
        return None

if __name__ == "__main__":
    app.run()