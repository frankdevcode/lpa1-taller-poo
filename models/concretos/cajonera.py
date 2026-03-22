from ..categorias.almacenamiento import Almacenamiento

class Cajonera(Almacenamiento):
    def __init__(self, nombre: str, material: str, color: str, precio_base: float,
                 numero_estantes: int = 0, tiene_puertas: bool = False,
                 numero_cajones: int = 4, con_ruedas: bool = False):
        super().__init__(nombre, material, color, precio_base, numero_estantes, tiene_puertas)
        self.numero_cajones = numero_cajones
        self.con_ruedas = con_ruedas
        
    @property
    def numero_cajones(self) -> int:
        return self._numero_cajones
        
    @numero_cajones.setter
    def numero_cajones(self, value: int):
        self._numero_cajones = value
        
    @property
    def con_ruedas(self) -> bool:
        return self._con_ruedas
        
    @con_ruedas.setter
    def con_ruedas(self, value: bool):
        self._con_ruedas = value
        
    def calcular_precio(self) -> float:
        precio = self.precio_base + (self.numero_cajones * 25000.0)
        if self.con_ruedas:
            precio += 15000.0
        return round(precio, 2)
        
    def obtener_descripcion(self) -> str:
        base = super().obtener_info_almacenamiento()
        extra = f"Cajones: {self.numero_cajones}, Ruedas: {'Sí' if self.con_ruedas else 'No'}"
        return f"Cajonera '{self.nombre}' ({self.material}, {self.color}). {base}. {extra}. Precio: ${self.calcular_precio()}"
