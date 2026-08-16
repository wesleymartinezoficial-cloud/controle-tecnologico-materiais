import streamlit as st
from core.blocos import calcular_resistencia_bloco

def render():
    st.subheader("Resistência à Compressão de Blocos de Alvenaria")
    cb1, cb2, cb3 = st.columns(3)
    with cb1:
        largura = st.number_input("Largura do Bloco (cm)", value=14.0)
    with cb2:
        comprimento = st.number_input("Comprimento do Bloco (cm)", value=39.0)
    with cb3:
        carga_bloco = st.number_input("Carga de Ruptura (kN)", value=180.0)

    if st.button("🧱 Calcular Resistência do Bloco", use_container_width=True):
        res = calcular_resistencia_bloco(largura, comprimento, carga_bloco)
        b1, b2 = st.columns(2)
        b1.metric("Área Bruta da Face", f"{res['area_bruta']:.1f} cm²")
        b2.metric("Resistência Bruta (fb)", f"{res['f_b']:.2f} MPa")
