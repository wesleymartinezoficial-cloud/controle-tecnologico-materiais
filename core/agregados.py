def calcular_agregado_miudo(m_seco: float, m_sss: float, m_pic_agua: float, m_pic_am_ag: float) -> dict:
    den = m_pic_agua + m_sss - m_pic_am_ag
    if den <= 0:
        raise ValueError("Valores de massa incompatíveis para o ensaio de picnômetro.")
    
    massa_especifica = m_seco / den
    absorcao = ((m_sss - m_seco) / m_seco) * 100.0
    return {"massa_especifica": massa_especifica, "absorcao": absorcao}

def calcular_massa_unitaria(v_rec: float, m_rec: float, m_rec_am: float, gamma_esp: float) -> dict:
    if v_rec <= 0 or gamma_esp <= 0:
        raise ValueError("Volume e massa específica devem ser maiores que zero.")
    
    m_am = m_rec_am - m_rec
    gamma_u = (m_am / 1000.0) / v_rec
    vazios = (1.0 - (gamma_u / gamma_esp)) * 100.0
    return {"massa_unitaria_kg_dm3": gamma_u, "vazios_percent": vazios}
