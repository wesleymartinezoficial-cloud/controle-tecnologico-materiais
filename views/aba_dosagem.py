import streamlit as st
from core.dosagem import simular_traco_abcp

def render():
    st.subheader("Dosagem de Traço de Concreto (Método ABCP)")
    d1, d2, d3 = st.columns(3)
    with d1:
        fck_desejado = st.number_input("fck de Projeto (MPa)", value=30.0)
    with d2:
        slump_alvo = st.number_input("Slump Alvo (cm)", value=12.0)
    with d3:
        dmc_brita = st.selectbox("DMC da Brita (mm)", [9.5, 19.0, 25.0, 37.5], index=1)

    if st.button("🧮 Simular Traço Nominal", use_container_width=True):
        res = simular_traco_abcp(fck_desejado, dmc_brita)
        st.success("Traço em Massa Calculado (1 : a : b : a/c):")
        st.markdown(f"### **1 : {res['m_areia']:.2f} : {res['m_brita']:.2f} / a/c = {res['rel_ac']:.2f}**")
        
        t1, t2, t3 = st.columns(3)
        t1.metric("Consumo de Cimento", f"{res['massa_cimento']:.1f} kg/m³")
        t2.metric("Consumo de Água", f"{res['agua_m3']:.0f} L/m³")
        t3.metric("Resistência de Dosagem (fc28)", f"{res['fc28']:.1f} MPa")
