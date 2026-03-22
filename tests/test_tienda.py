import pytest
from services.tienda import TiendaMuebles
from models.concretos.silla import Silla
from models.concretos.mesa import Mesa

class TestTiendaMuebles:
    def setup_method(self):
        self.tienda = TiendaMuebles("Muebleria Test")
        self.silla = Silla("Silla Oficina", "Metal", "Negro", 100.0)
        self.mesa = Mesa("Mesa Centro", "Vidrio", "Claro", 200.0, "redonda", 4.0)
        self.tienda.agregar_mueble(self.silla)
        self.tienda.agregar_mueble(self.mesa)
        
    def test_agregar_y_buscar(self):
        assert self.tienda.total_muebles == 2
        
        resultados = self.tienda.buscar_muebles_por_nombre("Silla")
        assert len(resultados) == 1
        assert resultados[0].nombre == "Silla Oficina"
        
    def test_filtrar(self):
        res_precio = self.tienda.filtrar_por_precio(0, 150)
        assert len(res_precio) == 1
        res_material = self.tienda.filtrar_por_material("vidrio")
        assert len(res_material) == 1
        
    def test_ventas_y_descuentos(self):
        self.tienda.aplicar_descuento("silla", 10)
        venta = self.tienda.realizar_venta(self.silla, "Cliente Prueba")
        assert "error" not in venta
        assert self.tienda.total_muebles == 1
        assert self.tienda.obtener_estadisticas()["ventas_realizadas"] == 1
