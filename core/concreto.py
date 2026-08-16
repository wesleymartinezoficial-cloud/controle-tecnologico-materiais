import math
import pandas as pd

def calcular_fck_estimado(df_cps: pd.DataFrame, diametro_cm: float) -> dict:
    if diametro_cm <= 0:
        raise ValueError("O diâmetro deve ser positivo.")
    
    cargas = df_cps["Carga (kN)"].tolist()
    n = len(cargas)
    if n < 2:
        return None

    area_cm2 = (math.pi * (diametro_cm**2)) / 4.0
    fcs = [(carga * 1000.0 / area_cm2) / 10.0 for carga in cargas]
    fcs_ordenados = sorted(fcs)
    fc_m = sum(fcs) / n

    m = math.floor(n / 2)
    soma_menores = sum(fcs_ordenados[:m])
    fck_est_1 = (2 * (soma_menores / m)) - fcs_ordenados[m]
    fck_est_2 = 0.85 * fc_m
    fck_est = max(fck_est_1, fck_est_2)

    df_res = df_cps.copy()
    df_res["fc (MPa)"] = [round(x, 2) for x in fcs]

    return {
        "df_resultado": df_res,
        "fc_m": fc_m,
        "fck_est": fck_est,
        "f1": fcs_ordenados[0],
        "area_cm2": area_cm2
    }
