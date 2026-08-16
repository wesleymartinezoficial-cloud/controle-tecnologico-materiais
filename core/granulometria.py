import pandas as pd

def processar_granulometria(massa_inicial: float, df_peneiras: pd.DataFrame, massa_fundo: float) -> dict:
    """
    Calcula retida simples, acumulada, passante, módulo de finura, DMC e erro (NBR 17054 / NBR 7211).
    """
    massa_rec = df_peneiras["Massa Retida (g)"].sum() + massa_fundo
    erro_percentual = (abs(massa_inicial - massa_rec) / massa_inicial) * 100

    acumulado, soma_pa_norm, dmc = 0.0, 0.0, None
    retida_simples, retida_acumulada, passante = [], [], []

    for _, row in df_peneiras.iterrows():
        pr = (row["Massa Retida (g)"] / massa_inicial) * 100
        acumulado += pr
        pp = 100.0 - acumulado

        retida_simples.append(round(pr, 2))
        retida_acumulada.append(round(acumulado, 2))
        passante.append(round(pp, 2))

        if row.get("Série") == "Normal":
            soma_pa_norm += acumulado
        if acumulado <= 5.0:
            dmc = row["Abertura (mm)"]

    modulo_finura = soma_pa_norm / 100.0

    df_resultado = df_peneiras.copy()
    df_resultado["Retida Simples (%)"] = retida_simples
    df_resultado["Retida Acum. (%)"] = retida_acumulada
    df_resultado["Passante (%)"] = passante

    return {
        "massa_rec": massa_rec,
        "erro": erro_percentual,
        "mf": modulo_finura,
        "dmc": dmc,
        "df": df_resultado,
    }
