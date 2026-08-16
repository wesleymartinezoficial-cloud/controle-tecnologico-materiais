import streamlit as st
from core.agregados import calcular_agregado_miudo, calcular_massa_unitaria

def render():
    st.subheader("Caracterização Física de Agregados")
    col_a1, col_a2 = st.columns(2)
    with col_a1:
        st.markdown("**Agregado Miúdo (Areia)**")
        m_seco_m = st.number_input("Massa Seca (g)", value=490.0)
        m_sss_m = st.number_input("Massa SSS (g)", value=500.0)
        m_pic_agua = st.number_input("Massa Picnômetro + Água (g)", value=1300.0)
        m_pic_am_ag = st.number_input("Massa Picnômetro + Amostra + Água (g)", value=1610.0)
        
        if st.button("Calcular Miúdo"):
            res = calcular_agregado_miudo(m_seco_m, m_sss_m, m_pic_agua, m_pic_am_ag)
            st.success(f"Massa Específica Seca: {res['massa_especifica']:.3f} g/cm³ | Absorção: {res['absorcao']:.2f}%")

    with col_a2:
        st.markdown("**Massa Unitária Solta (NBR 16972)**")
        v_rec = st.number_input("Volume Recipiente (L)", value=15.0)
        m_rec = st.number_input("Massa Recipiente Vazio (g)", value=4000.0)
        m_rec_am = st.number_input("Massa Recipiente + Agregado (g)", value=25000.0)
        gamma_esp = st.number_input("Massa Específica Real (g/cm³)", value=2.65)
        
        if st.button("Calcular Unitária"):
            res = calcular_massa_unitaria(v_rec, m_rec, m_rec_am, gamma_esp)
            st.success(f"Massa Unitária: {res['massa_unitaria_kg_dm3']:.3f} kg/dm³ | Vazios: {res['vazios_percent']:.2f}%")
