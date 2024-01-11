from abc import ABC, abstractmethod
class PizzaBuilder(ABC):
    @abstractmethod
    def crear_masa(self):
        pass
    
    @abstractmethod
    def crear_tamano(self):
        pass
    
    @abstractmethod
    def crear_salsa(self):
        pass
    
    @abstractmethod
    def crear_ingredientes(self):
        pass
    
    @abstractmethod
    def crear_tecnica(self):
        pass
    
    @abstractmethod
    def crear_presentacion(self):
        pass