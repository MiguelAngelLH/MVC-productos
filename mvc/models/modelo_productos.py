import csv

class ModeloProductos:
    @staticmethod
    def obtener_productos():
        productos = []
        with open('productos.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                productos.append(row)
        
        return productos
