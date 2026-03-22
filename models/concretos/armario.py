from ..categorias.almacenamiento import Almacenamiento

class Armario(Almacenamiento):
    def __init__(self, nombre: str, material: str, color: str, precio_base: float,
                 numero_estantes: int, tiene_puertas: bool = True,
                 numero_puertas: int = 2, con_espejo: bool = False):
        super().__init__(nombre, material, color, precio_base, numero_estantes, tiene_puertas)
        self.numero_puertas = numero_puertas
        self.con_espejo = con_espejo
        
    @property
    def numero_puertas(self) -> int:
        return self._numero_puertas
        
    @numero_puertas.setter
    def numero_puertas(self, value: int):
        self._numero_puertas = value
        
    @property
    def con_espejo(self) -> bool:
        return self._con_espejo
        
    @con_espejo.setter
    def con_espejo(self, value: bool):
        self._con_espejo = value
        
    def calcular_precio(self) -> float:
        precio = self.precio_base + (self.numero_estantes * 10)
        if self.tiene_puertas:
            precio += self.numero_puertas * 30.0
        if self.con_espejo:
            precio += 50.0
        return round(precio, 2)
        
    def obtener_descripcion(self) -> str:
        base = super().obtener_info_almacenamiento()
        extra = f"Núm. Puertas: {self.numero_puertas}, Espejo: {'Sí' if self.con_espejo else 'No'}"
        return f"Armario '{self.nombre}' ({self.material}, {self.color}). {base}. {extra}. Precio: ${self.calcular_precio()}"
