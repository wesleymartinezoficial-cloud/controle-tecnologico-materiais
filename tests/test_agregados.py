import pytest
from core.agregados import calcular_agregado_miudo, calcular_massa_unitaria

def test_calcular_agregado_miudo():
    res = calcular_agregado_miudo(490.0, 500.0, 1300.0, 1610.0)
    assert round(res["massa_especifica"], 2) == 2.58
    assert round(res["absorcao"], 2) == 2.04

def test_calcular_massa_unitaria():
    res = calcular_massa_unitaria(15.0, 4000.0, 25000.0, 2.65)
    assert round(res["massa_unitaria_kg_dm3"], 2) == 1.40
