import pandas as pd

def calcular_material_pulverulento(massa_inicial: float, massa_seca_lavada: float) -> float:
    if massa_inicial <= 0:
        raise ValueError("A massa inicial deve ser maior que zero.")
    return ((massa_inicial - massa_seca_lavada) / massa_inicial) * 100.0

def processar_granulometria(massa_inicial: float, df_peneiras: pd.DataFrame, massa_fundo: float) -> dict:
    if massa_inicial <= 0:
        raise ValueError("A massa inicial deve ser maior que zero.")

    massa_rec = df_peneiras["Massa Retida (g)"].sum() + massa_fundo
    erro = (abs(massa_inicial - massa_rec) / massa_inicial) * 100.0

    acumulado, soma_pa_norm, dmc = 0.0, 0.0, None
    retida_simples, retida_acumulada, passante = [], [], []

    for _, row in df_peneiras.iterrows():
        pr = (row["Massa Retida (g)"] / massa_inicial) * 100.0
        acumulado += pr
        pp = 100.0 - acumulado

        retida_simples.append(round(pr, 2))
        retida_acumulada.append(round(acumulado, 2))
        passante.append(round(pp, 2))

        if row["Série"] == "Normal":
            soma_pa_norm += acumulado
        if acumulado <= 5.0:
            dmc = row["Abertura (mm)"]

    mf = soma_pa_norm / 100.0
    df_res = df_peneiras.copy()
    df_res["Retida Simples (%)"] = retida_simples
    df_res["Retida Acum. (%)"] = retida_acumulada
    df_res["Passante (%)"] = passante

    return {
        "massa_rec": massa_rec,
        "erro": erro,
        "mf": mf,
        "dmc": dmc,
        "df_resultado": df_res
    }
