from ..categorias.asientos import Asiento

class Silla(Asiento):
    def __init__(self, nombre: str, material: str, color: str, precio_base: float,
                 tiene_respaldo: bool = True, material_tapizado: str = None,
                 altura_regulable: bool = False, tiene_ruedas: bool = False):
        super().__init__(nombre, material, color, precio_base, 1, tiene_respaldo, material_tapizado)
        self.altura_regulable = altura_regulable
        self.tiene_ruedas = tiene_ruedas
        
    @property
    def altura_regulable(self) -> bool:
        return self._altura_regulable
        
    @altura_regulable.setter
    def altura_regulable(self, value: bool):
        self._altura_regulable = value
        
    @property
    def tiene_ruedas(self) -> bool:
        return self._tiene_ruedas
        
    @tiene_ruedas.setter
    def tiene_ruedas(self, value: bool):
        self._tiene_ruedas = value
        
    def calcular_precio(self) -> float:
        precio = self.precio_base * self.calcular_factor_comodidad()
        if self.altura_regulable:
            precio += 20.0
        if self.tiene_ruedas:
            precio += 15.0
        return round(precio, 2)
        
    def obtener_descripcion(self) -> str:
        base = super().obtener_info_asiento()
        extra = f"Altura regulable: {'Sí' if self.altura_regulable else 'No'}, Ruedas: {'Sí' if self.tiene_ruedas else 'No'}"
        return f"Silla '{self.nombre}' ({self.material}, {self.color}). {base}. {extra}. Precio: ${self.calcular_precio()}"
        
    def regular_altura(self, nueva_altura: int) -> str:
        if self.altura_regulable:
            return f"Altura regulada a {nueva_altura} cm."
        return "Esta silla no es regulable en altura."
        
    def es_silla_oficina(self) -> bool:
        return self.tiene_ruedas and self.altura_regulable
