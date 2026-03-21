"""
Clase base abstracta Mueble
Este es el punto de partida de nuestra jerarquía de clases.
"""

from abc import ABC, abstractmethod


class Mueble(ABC):
    """
    Clase abstracta base para todos los muebles.
    
    Esta clase define la estructura común que deben tener todos los muebles
    de nuestra tienda, pero no puede ser instanciada directamente.
    
    Conceptos OOP aplicados:
    - Abstracción: Define una interfaz común sin implementación específica
    - Encapsulación: Usa atributos privados con getters/setters
    """
    
    def __init__(self, nombre: str, material: str, color: str, precio_base: float):
        """
        Constructor de la clase Mueble.
        
        Args:
            nombre: Nombre del mueble
            material: Material principal (madera, metal, plástico, etc.)
            color: Color del mueble
            precio_base: Precio base antes de aplicar modificadores
        """
        self.nombre = nombre
        self.material = material
        self.color = color
        self.precio_base = precio_base
    
    @property
    def nombre(self) -> str:
        """Getter del nombre."""
        return self._nombre

    @nombre.setter
    def nombre(self, valor: str):
        """Setter del nombre con validación de tipo."""
        if not isinstance(valor, str):
            raise TypeError("El nombre debe ser una cadena de texto.")
        if not valor.strip():
            raise ValueError("El nombre no puede estar vacío.")
        self._nombre = valor.strip()

    @property
    def material(self) -> str:
        """Getter del material."""
        return self._material

    @material.setter
    def material(self, valor: str):
        """Setter del material con validación."""
        if not isinstance(valor, str):
            raise TypeError("El material debe ser una cadena de texto.")
        if not valor.strip():
            raise ValueError("El material no puede estar vacío.")
        self._material = valor.strip()

    @property
    def color(self) -> str:
        """Getter del color."""
        return self._color

    @color.setter
    def color(self, valor: str):
        """Setter del color con validación."""
        if not isinstance(valor, str):
            raise TypeError("El color debe ser una cadena de texto.")
        if not valor.strip():
            raise ValueError("El color no puede estar vacío.")
        self._color = valor.strip()

    @property
    def precio_base(self) -> float:
        """Getter del precio base."""
        return self._precio_base

    @precio_base.setter
    def precio_base(self, valor: float):
        """Setter con validación de tipo y valor positivo."""
        if not isinstance(valor, (int, float)):
            raise TypeError("El precio base debe ser un número.")
        if valor < 0:
            raise ValueError("El precio base no puede ser negativo.")
        self._precio_base = float(valor)
    
    @abstractmethod
    def calcular_precio(self) -> float:
        """
        Calcula el precio final del mueble.
        Este método debe ser implementado por cada clase concreta.
        
        Returns:
            float: Precio final calculado
        """
        pass
    
    @abstractmethod
    def obtener_descripcion(self) -> str:
        """
        Obtiene una descripción detallada del mueble.
        Este método debe ser implementado por cada clase concreta.
        
        Returns:
            str: Descripción completa del mueble
        """
        pass
    
    def __str__(self) -> str:
        """
        Representación en cadena del mueble.
        Este método concreto puede ser usado por todas las clases hijas.
        """
        return f"{self.nombre} de {self.material} en color {self.color}"
    
    def __repr__(self) -> str:
        """
        Representación técnica del mueble para debugging.
        """
        return f"Mueble(nombre='{self.nombre}', material='{self.material}', color='{self.color}', precio_base={self.precio_base})"
