
from PizzaBuilder import *
from pizzaobserver import Observer

class Pizza(PizzaBuilder,Observer):
    def __init__(self):
        self.reset()

    def update(self, message):
        print(f"¡Nueva notificación para pizza!: {message}")
        
    def reset(self):    
        self.tamano = ""
        self.masa = ""
        self.ingredientes = []
        self.salsa = ""
        self.tecnica = ""
        self.presentacion = ""
    
    @property
    def pizza(self):
        pizza = [self.tamano, self.masa, ', '.join(self.ingredientes), self.salsa, self.tecnica, self.presentacion]
        self.reset()
        return pizza

    def crear_masa(self):
        while True:
            print("Elige el tipo de masa:")
            print("1 - Clasica")
            print("2 - Fina")
            print("3 - Con queso")
            opcion = input("Opcion: ")
            if opcion == '1':
                self.masa = "Clasica"
                break
            elif opcion == '2':
                self.masa = "Fina"
                break
            elif opcion == '3':
                self.masa = "Con queso"
                break
            else:
                print("Por favor, elige una opcion valida (1, 2, o 3)")


    def crear_tamano(self):
        while True:
            print("Elige el tamano:")
            print("1 - Familiar")
            print("2 - Normal")
            print("3 - Pequena")
            opcion = input("Opcion: ")
            if opcion == '1':
                self.tamano = "Familiar"
                break
            elif opcion == '2':
                self.tamano = "Normal"
                break
            elif opcion == '3':
                self.tamano = "Pequena"
                break
            else:
                print("Por favor, elige una opción valida (1, 2, o 3)")

    def crear_salsa(self):
        while True:
            print("Elige el tipo de salsa:")
            print("1 - Barbacoa")
            print("2 - Picante")
            print("3 - Carbonara")
            opcion = input("Opcion: ")
            if opcion == '1':
                self.salsa = "Barbacoa"
                break
            elif opcion == '2':
                self.salsa = "Picante"
                break
            elif opcion == '3':
                self.salsa = "Carbonara"
                break
            else:
                print("Por favor, elige una opcion valida (1, 2, o 3)")


    def crear_ingredientes(self):
        print("Elige los ingredientes para tu pizza (ingresa 'listo' cuando hayas terminado):")
        ingredientes_disponibles = ["Queso", "Pepperoni", "Champinones", "Jamon", "Pimientos", "Cebolla", "Aceitunas"]
        while True:
            print(f"Ingredientes disponibles: {', '.join(ingredientes_disponibles)}")
            ingrediente = input("Ingrediente: ")
            if ingrediente.lower() == 'listo':
                break
            if ingrediente in ingredientes_disponibles:
                self.ingredientes.append(ingrediente)
                ingredientes_disponibles.remove(ingrediente)
            else:
                print("Ingrediente no disponible. Elige otro.")

    def crear_tecnica(self):
        while True:
            print("Elige la tecnica de coccion:")
            print("1 - Horno")
            print("2 - Microondas")
            opcion = input("Opcion: ")
            if opcion == '1':
                self.tecnica = "Horno"
                break
            elif opcion == '2':
                self.tecnica = "Microondas"
                break
            else:
                print("Por favor, elige una opción valida (1 o 2)")

    def crear_presentacion(self):
        while True:
            print("Elige la presentacion:")
            print("1 - Para tomar aqui")
            print("2 - Para llevar")
            opcion = input("Opcion: ")
            if opcion == '1':
                self.presentacion = "Para tomar aqui"
                break
            elif opcion == '2':
                self.presentacion = "Para llevar"
                break
            else:
                print("Por favor, elige una opción valida (1 o 2)")