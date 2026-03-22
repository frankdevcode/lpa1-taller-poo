from ..mueble import Mueble

class Cama(Mueble):
    def __init__(self, nombre: str, material: str, color: str, precio_base: float,
                 tamano: str = "Matrimonial", incluye_colchon: bool = True):
        super().__init__(nombre, material, color, precio_base)
        self.tamano = tamano
        self.incluye_colchon = incluye_colchon
        
    @property
    def tamano(self) -> str:
        return self._tamano
        
    @tamano.setter
    def tamano(self, value: str):
        self._tamano = value
        
    @property
    def incluye_colchon(self) -> bool:
        return self._incluye_colchon
        
    @incluye_colchon.setter
    def incluye_colchon(self, value: bool):
        self._incluye_colchon = value
        
    def calcular_precio(self) -> float:
        precio = self.precio_base
        if self.tamano.lower() == "king":
            precio += 100.0
        if self.incluye_colchon:
            precio += 200.0
        return round(precio, 2)
        
    def obtener_descripcion(self) -> str:
        extra = f"Tamaño: {self.tamano}, Incluye colchón: {'Sí' if self.incluye_colchon else 'No'}"
        return f"Cama '{self.nombre}' ({self.material}, {self.color}). {extra}. Precio: ${self.calcular_precio()}"
