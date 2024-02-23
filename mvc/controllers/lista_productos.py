import csv
from web import template

class Lista:
    def GET(self):
        productos = []
        with open('productos.csv', 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                productos.append(row)
        
        render = template.render('mvc/views/')  
        return render.lista_productos(productos)
