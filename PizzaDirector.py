from pizzaobserver import Observer, Subject

class PizzaDirector(Subject):
    def __init__(self, builder):
        self._builder = builder
        self._observers = []

    def add_observer(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify_observers(self, message):
        for observer in self._observers:
            observer.update(message)

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



