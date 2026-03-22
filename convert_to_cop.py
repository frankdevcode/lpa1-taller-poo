import os

def rep(file, old, new):
    if not os.path.exists(file): return
    with open(file, 'r', encoding='utf-8') as f:
        c = f.read()
    c = c.replace(old, new)
    if "models/concretos/" in file:
        c = c.replace("Precio: ${self.calcular_precio():.2f}", "Precio: $ {self.calcular_precio():,.0f} COP")
    with open(file, 'w', encoding='utf-8') as f:
        f.write(c)

# --- ESCALAR 1000x ---

# main.py
for val in ["150.0", "350.0", "80.0", "500.0", "300.0", "450.0", "800.0", "1200.0", "2000.0", "600.0", "180.0", "1000.0", "400.0", "750.0", "1500.0", "120.0"]:
    rep("main.py", f"precio_base={val}", f"precio_base={float(val)*1000}")

# concretos
rep("models/concretos/silla.py", "+= 20.0", "+= 20000.0")
rep("models/concretos/silla.py", "+= 15.0", "+= 15000.0")
rep("models/concretos/sofa.py", "+= 100.0", "+= 100000.0")
rep("models/concretos/sillon.py", "+= 50.0", "+= 50000.0")
rep("models/concretos/sillon.py", "+= 150.0", "+= 150000.0")
rep("models/concretos/cama.py", "+= 100.0", "+= 100000.0")
rep("models/concretos/cama.py", "+= 200.0", "+= 200000.0")
rep("models/concretos/mesa.py", " * 10)", " * 10000)")
rep("models/concretos/mesa.py", "+= 40.0", "+= 40000.0")
rep("models/concretos/escritorio.py", " * 15)", " * 15000)")
rep("models/concretos/escritorio.py", " * 20.0", " * 20000.0")
rep("models/concretos/escritorio.py", "+= 10.0", "+= 10000.0")
rep("models/concretos/armario.py", " * 10)", " * 10000)")
rep("models/concretos/armario.py", " * 30.0", " * 30000.0")
rep("models/concretos/armario.py", "+= 50.0", "+= 50000.0")
rep("models/concretos/cajonera.py", " * 25.0", " * 25000.0")
rep("models/concretos/cajonera.py", "+= 15.0", "+= 15000.0")
rep("models/concretos/sofacama.py", "+= 100", "+= 100000")
rep("models/concretos/sofacama.py", "+= 150", "+= 150000")
rep("models/concretos/sofacama.py", "+= 200", "+= 200000")
rep("models/concretos/sofacama.py", "+= 300", "+= 300000")

# FORMAT UI AND COMEDOR
rep("ui/menu.py", 'precio = f"${mueble.calcular_precio():.2f}"', 'precio = f"$ {mueble.calcular_precio():,.0f} COP"')
rep("ui/menu.py", 'f"${stats[\'valor_inventario\']:,.2f}"', 'f"$ {stats[\'valor_inventario\']:,.0f} COP"')
rep("ui/menu.py", '${venta[\'precio_original\']:.2f}', '$ {venta[\'precio_original\']:,.0f} COP')
rep("ui/menu.py", '${venta[\'precio_final\']:.2f}', '$ {venta[\'precio_final\']:,.0f} COP')
rep("models/composicion/comedor.py", 'TOTAL: ${self.calcular_precio_total():.2f}', 'TOTAL: $ {self.calcular_precio_total():,.0f} COP')

# Fix the bug from before:
rep("services/tienda.py", "inventario']:,.2f}\",", "inventario']:,.0f} COP}\",")
rep("services/tienda.py", "inventario']:,.2f}\\n\"", "inventario']:,.0f} COP}\\n\"")

rep("main.py", "inventario']:,.2f}\")", "inventario']:,.0f} COP}\")")

# TESTS
rep("tests/test_muebles.py", "150.0", "150000.0")
rep("tests/test_muebles.py", "300.0", "300000.0")
rep("tests/test_muebles.py", "165.0", "165000.0")
rep("tests/test_muebles.py", "425.0", "425000.0")
rep("tests/test_muebles.py", "100.0", "100000.0")
rep("tests/test_muebles.py", "800.0", "800000.0")
rep("tests/test_muebles.py", "1960.0", "1960000.0")

rep("tests/test_composicion.py", "500.0", "500000.0")
rep("tests/test_composicion.py", "120.0", "120000.0")
rep("tests/test_composicion.py", "1033.6", "1033600.0")

rep("tests/test_tienda.py", "100.0", "100000.0")
rep("tests/test_tienda.py", "200.0", "200000.0")
rep("tests/test_tienda.py", "150)", "150000)")

print("Script fix ran")
