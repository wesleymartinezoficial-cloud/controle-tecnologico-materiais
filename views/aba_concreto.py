import pandas as pd
import streamlit as st
from core.concreto import calcular_fck_estimado

def render():
    st.subheader("Resistência à Compressão e Validação de Lote (fck,est)")
    c_cp1, c_cp2, c_cp3 = st.columns(3)
    with c_cp1:
        d = st.number_input("Diâmetro do CP (cm)", value=10.0)
    with c_cp2:
        h = st.number_input("Altura do CP (cm)", value=20.0)
    with c_cp3:
        idade = st.text_input("Idade (dias)", value="28")

    st.write("**Resultados de Ruptura dos CPs:**")
    df_cps = pd.DataFrame({"CP": ["CP-01", "CP-02", "CP-03", "CP-04", "CP-05"], "Carga (kN)": [240.0, 255.0, 248.0, 260.0, 242.0]})
    df_cps_edit = st.data_editor(df_cps, num_rows="dynamic", use_container_width=True, hide_index=True)

    if st.button("💥 Processar Lote e Calcular fck,est", use_container_width=True):
        res = calcular_fck_estimado(df_cps_edit, d)
        if res:
            st.dataframe(res["df_resultado"], use_container_width=True)
            k1, k2, k3 = st.columns(3)
            k1.metric("Resistência Média (fc,m)", f"{res['fc_m']:.2f} MPa")
            k2.metric("fck Estimado (NBR 12655)", f"{res['fck_est']:.2f} MPa")
            k3.metric("Menor Valor (f1)", f"{res['f1']:.2f} MPa")
