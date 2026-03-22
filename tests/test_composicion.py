import pytest
from models.concretos.silla import Silla
from models.concretos.mesa import Mesa
from models.composicion.comedor import Comedor

class TestComedor:
    def setup_method(self):
        self.mesa = Mesa("Mesa", "Madera", "Roble", 500.0, "rectangular", 6.0)
        self.sillas = [Silla(f"Silla {i}", "Madera", "Roble", 120.0) for i in range(2)]
        self.comedor = Comedor("Comedor Familiar", self.mesa, self.sillas)
    
    def test_creacion_comedor(self):
        assert self.comedor.nombre == "Comedor Familiar"
        assert self.comedor.mesa == self.mesa
        assert len(self.comedor.sillas) == 2
    
    def test_agregar_quitar_silla(self):
        silla3 = Silla("Silla 3", "Madera", "Roble", 120.0)
        self.comedor.agregar_silla(silla3)
        assert len(self.comedor.sillas) == 3
        
        self.comedor.quitar_silla(-1)
        assert len(self.comedor.sillas) == 2
        
    def test_descuento_set_completo(self):
        for i in range(2):
            self.comedor.agregar_silla(Silla(f"Silla Nueva {i}", "Madera", "Roble", 120.0))
        # Total sillas = 4. 
        # Price: mesa(500 + 6*10=560). silla = 120 * 1.2 = 144
        # Total sin descuento = 560 + 4*132 = 1088
        # Con 5% descuento (0.95) = 1033.6
        assert self.comedor.calcular_precio_total() == 1033.6
