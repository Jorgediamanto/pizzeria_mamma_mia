class PedidoPizzaCSVBuilder:
    def crear_csv(self):
        with open('pedidos_pizza.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Cliente", "Tamano", "Masa", "Ingredientes", "Salsa", "Tecnica de coccion", "Presentacion"])
        file.close()

    def añadir_pedido(self, cliente, pizza):
        with open('pedidos_pizza.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([cliente] + pizza)
        file.close()