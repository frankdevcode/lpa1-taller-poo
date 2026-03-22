"""
Clase SofaCama que implementa herencia múltiple.
Esta clase hereda tanto de Sofa como de Cama.
"""

from .sofa import Sofa
from .cama import Cama

class SofaCama(Sofa, Cama):
    """
    Clase que implementa herencia múltiple heredando de Sofa y Cama.
    
    Un sofá-cama es un mueble que funciona tanto como asiento durante el día
    como cama durante la noche.
    """
    
    def __init__(self, nombre: str, material: str, color: str, precio_base: float,
                 capacidad_personas: int = 3, material_tapizado: str = "tela",
                 tamano_cama: str = "matrimonial", incluye_colchon: bool = True,
                 mecanismo_conversion: str = "plegable"):
        
        # Inicializar el primer padre en el MRO (Sofa)
        super().__init__(nombre, material, color, precio_base, capacidad_personas, True, material_tapizado)
        
        # Inicializar manualmente los atributos de Cama al no ser llamada por super() con los args correctos
        self.tamano_cama = tamano_cama
        self.incluye_colchon = incluye_colchon
        
        # Inicializar atributos únicos del sofá-cama
        self.mecanismo_conversion = mecanismo_conversion
        self._modo_actual = "sofa"  # Puede ser "sofa" o "cama"
        
    @property
    def mecanismo_conversion(self) -> str:
        return self._mecanismo_conversion
        
    @mecanismo_conversion.setter
    def mecanismo_conversion(self, value: str):
        self._mecanismo_conversion = value

    @property
    def modo_actual(self) -> str:
        return self._modo_actual

    # Las propiedades tamaño_cama e incluye_colchon se heredan de Cama (sus setters/getters siguen funcionando
    # porque operan sobre self._tamaño_cama / self._incluye_colchon)
    # Solo necesitamos asegurarnos de que tengan el mismo nombre que usamos en init.
    # En cama.py usamos `tamano` no `tamaño_cama`. Ajustemos aquí para usar self.tamano
    @property
    def tamano_cama(self):
        return self.tamano
        
    @tamano_cama.setter
    def tamano_cama(self, value):
        self.tamano = value
        
    def convertir_a_cama(self) -> str:
        if self._modo_actual == "cama":
            return "El sofá-cama ya está en modo cama"
        
        self._modo_actual = "cama"
        return f"Sofá convertido a cama usando mecanismo {self.mecanismo_conversion}"
        
    def convertir_a_sofa(self) -> str:
        if self._modo_actual == "sofa":
            return "El sofá-cama ya está en modo sofá"
        
        self._modo_actual = "sofa"
        return f"Cama convertida a sofá usando mecanismo {self.mecanismo_conversion}"
        
    def calcular_precio(self) -> float:
        precio = self.precio_base
        precio *= self.calcular_factor_comodidad()
        precio *= 1.5  # 50% más caro por ser dual
        
        if self.mecanismo_conversion == "electrico":
            precio += 200000
        elif self.mecanismo_conversion == "hidraulico":
            precio += 150000
        else:
            precio += 100000
            
        if self.incluye_colchon:
            precio += 300000
            
        return round(precio, 2)
        
    def obtener_descripcion(self) -> str:
        descripcion = f"Sofá-cama '{self.nombre}' fabricado en {self.material} color {self.color}."
        descripcion += f" {self.obtener_info_asiento()}."
        descripcion += f" Tamaño de cama: {self.tamano_cama}."
        descripcion += f" Mecanismo: {self.mecanismo_conversion}."
        descripcion += f" Colchón incluido: {'Sí' if self.incluye_colchon else 'No'}."
        descripcion += f" Modo actual: {self.modo_actual}."
        descripcion += f" Precio: $ {self.calcular_precio():,.0f} COP"
        return descripcion
        
    def obtener_capacidad_total(self) -> dict:
        capacidades = {
            "como_sofa": self.capacidad_personas,
            "como_cama": 2 if self.tamano_cama.lower() in ["matrimonial", "queen", "king"] else 1
        }
        return capacidades
        
    def puede_usar_como_cama(self) -> bool:
        return self._modo_actual == "cama"
        
    def puede_usar_como_sofa(self) -> bool:
        return self._modo_actual == "sofa"
        
    def __str__(self) -> str:
        return f"Sofá-cama {self.nombre} (modo: {self.modo_actual})"
