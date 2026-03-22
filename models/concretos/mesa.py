from ..categorias.superficies import Superficie

class Mesa(Superficie):
    def __init__(self, nombre: str, material: str, color: str, precio_base: float,
                 forma: str, area: float, es_extensible: bool = False):
        super().__init__(nombre, material, color, precio_base, forma, area)
        self.es_extensible = es_extensible
        
    @property
    def es_extensible(self) -> bool:
        return self._es_extensible
        
    @es_extensible.setter
    def es_extensible(self, value: bool):
        self._es_extensible = value
        
    def calcular_precio(self) -> float:
        precio = self.precio_base + (self.area * 10000)
        if self.es_extensible:
            precio += 40000.0
        return round(precio, 2)
        
    def obtener_descripcion(self) -> str:
        base = super().obtener_info_superficie()
        extra = f"Extensible: {'Sí' if self.es_extensible else 'No'}"
        return f"Mesa '{self.nombre}' ({self.material}, {self.color}). {base}. {extra}. Precio: ${self.calcular_precio()}"
