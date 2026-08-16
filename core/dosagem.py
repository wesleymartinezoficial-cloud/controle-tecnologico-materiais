def simular_traco_abcp(fck_desejado: float, dmc_brita: float) -> dict:
    fc28 = fck_desejado + (1.65 * 4.0)
    rel_ac = round(0.58 - (fc28 - 20) * 0.012, 2)
    agua_m3 = 200.0 if dmc_brita == 19.0 else 190.0
    massa_cimento = agua_m3 / rel_ac
    
    return {
        "fc28": fc28,
        "rel_ac": rel_ac,
        "agua_m3": agua_m3,
        "massa_cimento": massa_cimento,
        "m_areia": 2.1,
        "m_brita": 2.8
    }
