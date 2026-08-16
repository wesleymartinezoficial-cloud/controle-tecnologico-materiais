from core.dosagem import simular_traco_abcp

def test_simular_traco_abcp():
    res = simular_traco_abcp(30.0, 19.0)
    assert res["fc28"] == 36.6
    assert res["agua_m3"] == 200.0
