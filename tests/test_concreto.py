import pandas as pd
from core.concreto import calcular_fck_estimado

def test_calcular_fck_estimado():
    df = pd.DataFrame({"CP": ["CP1", "CP2"], "Carga (kN)": [240.0, 250.0]})
    res = calcular_fck_estimado(df, 10.0)
    assert res is not None
    assert res["fck_est"] > 0
    assert res["area_cm2"] > 0
