from ..categorias.superficies import Superficie

class Escritorio(Superficie):
    def __init__(self, nombre: str, material: str, color: str, precio_base: float,
                 forma: str, area: float, numero_cajones: int = 0, tiene_pasacables: bool = True):
        super().__init__(nombre, material, color, precio_base, forma, area)
        self.numero_cajones = numero_cajones
        self.tiene_pasacables = tiene_pasacables
        
    @property
    def numero_cajones(self) -> int:
        return self._numero_cajones
        
    @numero_cajones.setter
    def numero_cajones(self, value: int):
        self._numero_cajones = value
        
    @property
    def tiene_pasacables(self) -> bool:
        return self._tiene_pasacables
        
    @tiene_pasacables.setter
    def tiene_pasacables(self, value: bool):
        self._tiene_pasacables = value
        
    def calcular_precio(self) -> float:
        precio = self.precio_base + (self.area * 15000)
        precio += self.numero_cajones * 20000.0
        if self.tiene_pasacables:
            precio += 10000.0
        return round(precio, 2)
        
    def obtener_descripcion(self) -> str:
        base = super().obtener_info_superficie()
        extra = f"Cajones: {self.numero_cajones}, Pasacables: {'Sí' if self.tiene_pasacables else 'No'}"
        return f"Escritorio '{self.nombre}' ({self.material}, {self.color}). {base}. {extra}. Precio: ${self.calcular_precio()}"
