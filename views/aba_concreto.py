import pandas as pd
import streamlit as st
from core.concreto import calcular_fck_estimado

def render():
    st.subheader("Avaliação Estatística da Resistência do Concreto (NBR 12655)")

    col1, col2 = st.columns(2)
    with col1:
        d_cp = st.number_input("Diâmetro do CP (cm)", value=10.0)
    with col2:
        h_cp = st.number_input("Altura do CP (cm)", value=20.0)

    df_cps = pd.DataFrame({"CP": ["CP-1", "CP-2", "CP-3", "CP-4"], "Carga (kN)": [245.0, 252.0, 238.0, 260.0]})
    df_edit = st.data_editor(df_cps, num_rows="dynamic", use_container_width=True, hide_index=True)

    if st.button("💥 Calcular fck Estimado", use_container_width=True):
        cargas = df_edit["Carga (kN)"].tolist()
        res = calcular_fck_estimado(cargas, d_cp)

        if res:
            r1, r2, r3 = st.columns(3)
            r1.metric("Resistência Média (fc,m)", f"{res['fc_m']:.2f} MPa")
            r2.metric("fck Estimado", f"{res['fck_est']:.2f} MPa")
            r3.metric("Área da Seção", f"{res['area_cm2']:.2f} cm²")
