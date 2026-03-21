"""
Clase abstracta para muebles para superficies de trabajo o del hogar.
"""

from abc import ABC, abstractmethod
from ..mueble import Mueble

class Superficie(Mueble, ABC):
    """
    Clase abstracta para superficies como mesas y escritorios.
    """
    
    def __init__(self, nombre: str, material: str, color: str, precio_base: float,
                 forma: str, area: float):
        super().__init__(nombre, material, color, precio_base)
        self.forma = forma
        self.area = area
        
    @property
    def forma(self) -> str:
        return self._forma
        
    @forma.setter
    def forma(self, valor: str):
        if not isinstance(valor, str):
            raise TypeError("La forma debe ser una cadena de texto.")
        if not valor.strip():
            raise ValueError("La forma no puede estar vacía.")
        self._forma = valor.strip()
        
    @property
    def area(self) -> float:
        return self._area
        
    @area.setter
    def area(self, valor: float):
        if valor <= 0:
            raise ValueError("El área debe ser mayor a 0.")
        self._area = float(valor)
        
    def obtener_info_superficie(self) -> str:
        return f"Forma: {self.forma}, Área: {self.area} m²"
