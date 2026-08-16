from core.blocos import calcular_resistencia_bloco

def test_calcular_resistencia_bloco():
    res = calcular_resistencia_bloco(14.0, 39.0, 180.0)
    assert res["area_bruta"] == 546.0
    assert round(res["f_b"], 2) == 3.30
