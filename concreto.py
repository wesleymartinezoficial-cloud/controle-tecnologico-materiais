import math
import pandas as pd

def calcular_fck_estimado(cargas_kn: list, diametro_cm: float) -> dict:
    """
    Calcula a resistência de ruptura e o fck estimado conforme NBR 12655 (Amostragem Parcial).
    """
    area_cm2 = (math.pi * (diametro_cm**2)) / 4.0
    fcs = [(carga * 1000.0 / area_cm2) / 10.0 for carga in cargas_kn]

    n = len(fcs)
    if n < 2:
        return None

    fcs_ordenados = sorted(fcs)
    fc_m = sum(fcs) / n

    m = math.floor(n / 2)
    soma_menores = sum(fcs_ordenados[:m])
    fck_est_1 = (2 * (soma_menores / m)) - fcs_ordenados[m]
    fck_est_2 = 0.85 * fc_m
    fck_est = max(fck_est_1, fck_est_2)

    return {
        "fcs": fcs,
        "fc_m": fc_m,
        "fck_est": fck_est,
        "area_cm2": area_cm2,
    }