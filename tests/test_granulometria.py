import pandas as pd
import pytest
from core.granulometria import calcular_material_pulverulento, processar_granulometria

def test_calcular_material_pulverulento():
    assert round(calcular_material_pulverulento(500.0, 485.0), 2) == 3.0

def test_calcular_material_pulverulento_invalido():
    with pytest.raises(ValueError):
        calcular_material_pulverulento(0.0, 100.0)

def test_processar_granulometria_sucesso():
    df = pd.DataFrame({
        "Abertura (mm)": [9.5, 4.75, 2.36],
        "Série": ["Normal", "Normal", "Normal"],
        "Massa Retida (g)": [0.0, 50.0, 450.0]
    })
    res = processar_granulometria(500.0, df, 0.0)
    assert res["massa_rec"] == 500.0
    assert res["erro"] == 0.0
    assert res["dmc"] == 4.75
