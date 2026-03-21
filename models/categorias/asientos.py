"""
Clase abstracta para muebles de asiento.
Esta clase agrupa las características comunes de sillas, sillones y sofás.
"""

from abc import ABC, abstractmethod
from ..mueble import Mueble

class Asiento(Mueble, ABC):
    """
    Clase abstracta para todos los muebles donde las personas se sientan.
    
    Hereda de Mueble y añade características específicas de los asientos
    como capacidad de personas, tipo de respaldo, etc.
    """
    
    def __init__(self, nombre: str, material: str, color: str, precio_base: float,
                 capacidad_personas: int, tiene_respaldo: bool, material_tapizado: str = None):
        """Constructor para muebles de asiento."""
        super().__init__(nombre, material, color, precio_base)
        self.capacidad_personas = capacidad_personas
        self.tiene_respaldo = tiene_respaldo
        self.material_tapizado = material_tapizado
        
    @property
    def capacidad_personas(self) -> int:
        """Getter para la capacidad de personas."""
        return self._capacidad_personas
        
    @capacidad_personas.setter
    def capacidad_personas(self, valor: int):
        """Setter para capacidad con validación."""
        if valor <= 0:
            raise ValueError("La capacidad de personas debe ser mayor a 0.")
        self._capacidad_personas = valor
        
    @property
    def tiene_respaldo(self) -> bool:
        """Getter para indicar si tiene respaldo."""
        return self._tiene_respaldo
        
    @tiene_respaldo.setter
    def tiene_respaldo(self, valor: bool):
        """Setter para respaldo con validación."""
        if not isinstance(valor, bool):
            raise TypeError("tiene_respaldo debe ser un valor booleano.")
        self._tiene_respaldo = valor
        
    @property
    def material_tapizado(self) -> str:
        """Getter para material tapizado."""
        return self._material_tapizado
        
    @material_tapizado.setter
    def material_tapizado(self, valor: str):
        """Setter para tapizado."""
        if valor is not None:
            if not isinstance(valor, str):
                raise TypeError("El material de tapizado debe ser una cadena de texto.")
            if not valor.strip():
                raise ValueError("El material de tapizado no puede estar vacío.")
            self._material_tapizado = valor.strip()
        else:
            self._material_tapizado = None
            
    def calcular_factor_comodidad(self) -> float:
        """Calcula factor de comodidad."""
        factor = 1.0
        if self.tiene_respaldo:
            factor += 0.1
            
        if self.material_tapizado:
            if self.material_tapizado.lower() == "cuero":
                factor += 0.2
            elif self.material_tapizado.lower() == "tela":
                factor += 0.1
                
        if self.capacidad_personas > 1:
            factor += 0.05 * (self.capacidad_personas - 1)
            
        return round(factor, 2)
        
    def obtener_info_asiento(self) -> str:
        """Obtiene información de asiento y retorna cadena de texto."""
        info = f"Capacidad: {self.capacidad_personas} personas"
        info += f", Respaldo: {'Sí' if self.tiene_respaldo else 'No'}"
        if self.material_tapizado:
            info += f", Tapizado: {self.material_tapizado}"
        return info
