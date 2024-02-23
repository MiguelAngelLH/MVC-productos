import csv
import web

class Insertar:
    def GET(self):
        return csv.reader.insertar_productos()

    def POST(self):
        data = web.input()
        nuevo_producto = {
            'id': data.id,
            'nombre': data.nombre,
            'descripcion': data.descripcion,
            'precio': data.precio,
            'existencia': data.existencia
        }
        
        with open('productos.csv', 'a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['id', 'nombre', 'descripcion', 'precio', 'existencia'])
            writer.writerow(nuevo_producto)
        
        return "¡Producto agregado correctamente!"
