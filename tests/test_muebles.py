"""
Pruebas unitarias para las clases de muebles.
Estas pruebas validan el correcto funcionamiento de todos los conceptos OOP implementados.
"""

import pytest
from models.mueble import Mueble
from models.concretos.silla import Silla
from models.concretos.sofacama import SofaCama
from models.concretos.mesa import Mesa


class TestMuebleBase:
    """Pruebas para la clase base abstracta Mueble."""
    
    def test_no_puede_instanciar_mueble_directamente(self):
        with pytest.raises(TypeError):
            mueble = Mueble("Test", "Madera", "Café", 100000.0)


class TestSilla:
    """Pruebas para la clase Silla."""
    
    def setup_method(self):
        self.silla_basica = Silla(
            nombre="Silla Básica",
            material="Madera",
            color="Café",
            precio_base=150000.0,
            tiene_respaldo=True
        )

        self.silla_oficina = Silla(
            nombre="Silla Oficina",
            material="Metal",
            color="Negro",
            precio_base=300000.0,
            tiene_respaldo=True,
            material_tapizado="cuero",
            altura_regulable=True,
            tiene_ruedas=True
        )
    
    def test_creacion_silla_basica(self):
        assert self.silla_basica.nombre == "Silla Básica"
        assert self.silla_basica.material == "Madera"
    
    def test_calculo_precio_silla_basica(self):
        precio = self.silla_basica.calcular_precio()
        assert precio == 165000.0
    
    def test_calculo_precio_silla_oficina(self):
        precio = self.silla_oficina.calcular_precio()
        # factor: 1 + 0.1 (respaldo) + 0.2 (cuero) = 1.3
        # price: 300 * 1.3 = 390
        # ruedas (+15), regulable (+20) -> 390 + 35 = 425
        assert precio == 425000.0
    
    def test_es_silla_oficina(self):
        assert self.silla_oficina.es_silla_oficina() is True
        assert self.silla_basica.es_silla_oficina() is False
    
    def test_regular_altura_silla_sin_mecanismo(self):
        resultado = self.silla_basica.regular_altura(50)
        assert "no es regulable" in resultado
    
    def test_regular_altura_silla_con_mecanismo(self):
        resultado = self.silla_oficina.regular_altura(50)
        assert "regulada a 50 cm" in resultado
    
    def test_validaciones_setter(self):
        with pytest.raises(ValueError):
            self.silla_basica.nombre = ""
        with pytest.raises(ValueError):
            self.silla_basica.precio_base = -100
    
    def test_obtener_descripcion(self):
        descripcion = self.silla_basica.obtener_descripcion()
        assert "Silla Básica" in descripcion
    
    def test_polimorfismo_herencia(self):
        from models.categorias.asientos import Asiento
        assert isinstance(self.silla_basica, Asiento)
        assert hasattr(self.silla_basica, 'calcular_precio')
        assert hasattr(self.silla_basica, 'obtener_descripcion')


class TestSofaCama:
    """Pruebas para la clase SofaCama."""
    
    def setup_method(self):
        self.sofacama = SofaCama(
            nombre="SofaCama Deluxe",
            material="Tela",
            color="Gris",
            precio_base=800000.0,
            capacidad_personas=3,
            material_tapizado="tela",
            tamano_cama="matrimonial",
            incluye_colchon=True,
            mecanismo_conversion="plegable"
        )
    
    def test_creacion_sofacama(self):
        assert self.sofacama.nombre == "SofaCama Deluxe"
        assert self.sofacama.capacidad_personas == 3
        assert self.sofacama.tamano_cama == "matrimonial"
    
    def test_conversion_modos(self):
        resultado = self.sofacama.convertir_a_cama()
        assert "convertido a cama" in resultado.lower()
        assert self.sofacama.modo_actual == "cama"
        resultado2 = self.sofacama.convertir_a_cama()
        assert "ya está en modo cama" in resultado2.lower()
        resultado3 = self.sofacama.convertir_a_sofa()
        assert "convertida a sofá" in resultado3.lower()
        
    def test_calculo_precio_dual(self):
        # Base: 800. factor tela + respaldo + cap = 1.0 + 0.1(tela) + 0.1(resp) + 0.05*2(cap) = 1.3
        # price * 1.5 = 1560
        # +100 plegable, +300 colchon = 1960
        assert self.sofacama.calcular_precio() == 1960000.0
    
    def test_capacidad_total(self):
        capacidades = self.sofacama.obtener_capacidad_total()
        assert capacidades['como_sofa'] == 3
        assert capacidades['como_cama'] == 2
