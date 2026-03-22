from ..categorias.asientos import Asiento

class Sillon(Asiento):
    def __init__(self, nombre: str, material: str, color: str, precio_base: float,
                 tiene_respaldo: bool = True, material_tapizado: str = "Cuero",
                 reclinable: bool = True, tiene_masajeador: bool = False):
        super().__init__(nombre, material, color, precio_base, 1, tiene_respaldo, material_tapizado)
        self.reclinable = reclinable
        self.tiene_masajeador = tiene_masajeador
        
    @property
    def reclinable(self) -> bool:
        return self._reclinable
        
    @reclinable.setter
    def reclinable(self, value: bool):
        self._reclinable = value
        
    @property
    def tiene_masajeador(self) -> bool:
        return self._tiene_masajeador
        
    @tiene_masajeador.setter
    def tiene_masajeador(self, value: bool):
        self._tiene_masajeador = value
        
    def calcular_precio(self) -> float:
        precio = self.precio_base * self.calcular_factor_comodidad()
        if self.reclinable:
            precio += 50000.0
        if self.tiene_masajeador:
            precio += 150000.0
        return round(precio, 2)
        
    def obtener_descripcion(self) -> str:
        base = super().obtener_info_asiento()
        extra = f"Reclinable: {'Sí' if self.reclinable else 'No'}, Masajeador: {'Sí' if self.tiene_masajeador else 'No'}"
        return f"Sillón '{self.nombre}' ({self.material}, {self.color}). {base}. {extra}. Precio: ${self.calcular_precio()}"
