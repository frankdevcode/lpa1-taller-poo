"""
Clase abstracta para muebles de almacenamiento.
"""

from abc import ABC, abstractmethod
from ..mueble import Mueble

class Almacenamiento(Mueble, ABC):
    """
    Clase abstracta para muebles de almacenamiento como estanterías, armarios, etc.
    """
    
    def __init__(self, nombre: str, material: str, color: str, precio_base: float,
                 numero_estantes: int, tiene_puertas: bool):
        super().__init__(nombre, material, color, precio_base)
        self.numero_estantes = numero_estantes
        self.tiene_puertas = tiene_puertas
        
    @property
    def numero_estantes(self) -> int:
        return self._numero_estantes
        
    @numero_estantes.setter
    def numero_estantes(self, valor: int):
        if valor < 0:
            raise ValueError("El número de estantes no puede ser negativo.")
        self._numero_estantes = valor
        
    @property
    def tiene_puertas(self) -> bool:
        return self._tiene_puertas
        
    @tiene_puertas.setter
    def tiene_puertas(self, valor: bool):
        if not isinstance(valor, bool):
            raise TypeError("tiene_puertas debe ser un valor booleano.")
        self._tiene_puertas = valor
        
    def obtener_info_almacenamiento(self) -> str:
        info = f"Estantes: {self.numero_estantes}"
        info += f", Puertas: {'Sí' if self.tiene_puertas else 'No'}"
        return info
