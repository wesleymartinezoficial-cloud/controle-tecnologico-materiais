def calcular_resistencia_bloco(largura_cm: float, comprimento_cm: float, carga_kn: float) -> dict:
    if largura_cm <= 0 or comprimento_cm <= 0:
        raise ValueError("Dimensões do bloco devem ser maiores que zero.")
    
    area_bruta = largura_cm * comprimento_cm
    f_b = ((carga_kn * 1000.0) / area_bruta) / 10.0
    return {"area_bruta": area_bruta, "f_b": f_b}
