class PizzaDirector:
    def __init__(self, builder):
        self._builder = builder
    
    def crear_pizza(self):
        self._builder.crear_tamano()
        self._builder.crear_masa()
        self._builder.crear_ingredientes()
        self._builder.crear_salsa()
        self._builder.crear_tecnica()
        self._builder.crear_presentacion()
        @property
        def builder(self):
            return self._builder
        
        @builder.setter
        def builder(self, builder):
            self._builder = builder