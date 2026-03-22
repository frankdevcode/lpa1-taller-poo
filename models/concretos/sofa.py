from ..categorias.asientos import Asiento

class Sofa(Asiento):
    def __init__(self, nombre: str, material: str, color: str, precio_base: float,
                 capacidad_personas: int = 3, tiene_respaldo: bool = True, material_tapizado: str = "Tela",
                 tiene_chaise_longue: bool = False):
        super().__init__(nombre, material, color, precio_base, capacidad_personas, tiene_respaldo, material_tapizado)
        self.tiene_chaise_longue = tiene_chaise_longue
        
    @property
    def tiene_chaise_longue(self) -> bool:
        return self._tiene_chaise_longue
        
    @tiene_chaise_longue.setter
    def tiene_chaise_longue(self, value: bool):
        self._tiene_chaise_longue = value
        
    def calcular_precio(self) -> float:
        precio = self.precio_base * self.calcular_factor_comodidad()
        if self.tiene_chaise_longue:
            precio += 100.0
        return round(precio, 2)
        
    def obtener_descripcion(self) -> str:
        base = super().obtener_info_asiento()
        extra = f"Chaise Longue: {'Sí' if self.tiene_chaise_longue else 'No'}"
        return f"Sofá '{self.nombre}' ({self.material}, {self.color}). {base}. {extra}. Precio: ${self.calcular_precio()}"
