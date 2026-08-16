import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
from core.granulometria import processar_granulometria
from core.pdf import gerar_pdf_granulometria

def render():
    st.subheader("Análise Granulométrica (NBR 17054 / NBR 7211)")

    col1, col2 = st.columns(2)
    with col1:
        massa_inicial = st.number_input("Massa Inicial Seca (g)", value=500.0, step=50.0)
    with col2:
        massa_fundo = st.number_input("Fundo Receptor (g)", value=2.0, step=0.1)

    PENEIRAS = [
        {"abertura": 9.5, "astm": '3/8"', "serie": "Normal"},
        {"abertura": 4.75, "astm": "Nº 4", "serie": "Normal"},
        {"abertura": 2.36, "astm": "Nº 8", "serie": "Normal"},
        {"abertura": 1.18, "astm": "Nº 16", "serie": "Normal"},
        {"abertura": 0.60, "astm": "Nº 30", "serie": "Normal"},
        {"abertura": 0.30, "astm": "Nº 50", "serie": "Normal"},
        {"abertura": 0.15, "astm": "Nº 100", "serie": "Normal"},
    ]

    df_base = pd.DataFrame({
        "Abertura (mm)": [p["abertura"] for p in PENEIRAS],
        "ASTM": [p["astm"] for p in PENEIRAS],
        "Série": [p["serie"] for p in PENEIRAS],
        "Massa Retida (g)": [0.0, 15.0, 45.0, 110.0, 180.0, 115.0, 33.0],
    })

    df_editado = st.data_editor(df_base, use_container_width=True, hide_index=True)

    if st.button("📊 Processar Granulometria", use_container_width=True):
        res = processar_granulometria(massa_inicial, df_editado, massa_fundo)

        m1, m2, m3 = st.columns(3)
        m1.metric("Massa Recuperada", f"{res['massa_rec']:.1f} g")
        m2.metric("Erro de Perda", f"{res['erro']:.2f}%", delta="Aprovado" if res["erro"] <= 1.0 else "Reprovado")
        m3.metric("Módulo de Finura (MF)", f"{res['mf']:.2f}", f"DMC: {res['dmc']} mm")

        # Gráfico com Limites NBR 7211
        fig, ax = plt.subplots(figsize=(8, 3.5))
        ax.plot(res["df"]["Abertura (mm)"], res["df"]["Passante (%)"], marker="o", color="#005580", label="Amostra")
        
        # Limites Normativos
        peneiras_mm = [9.5, 4.75, 2.36, 1.18, 0.60, 0.30, 0.15]
        lim_inf = [100, 95, 80, 50, 20, 10, 0]
        lim_sup = [100, 100, 100, 85, 60, 30, 10]
        ax.plot(peneiras_mm, lim_inf, 'r--', alpha=0.6, label="Limite Inf. (NBR 7211)")
        ax.plot(peneiras_mm, lim_sup, 'g--', alpha=0.6, label="Limite Sup. (NBR 7211)")

        ax.set_xscale("log")
        ax.invert_xaxis()
        ax.set_title("Curva Granulométrica e Zonas da NBR 7211")
        ax.grid(True, which="both", linestyle="--", alpha=0.5)
        ax.legend()
        st.pyplot(fig)

        # Botão para Download em PDF
        pdf_bytes = gerar_pdf_granulometria("Obra Residencial A", "Eng. Silva", res)
        st.download_button(
            label="📄 Baixar Laudo Técnico em PDF",
            data=pdf_bytes,
            file_name="Laudo_Granulometria.pdf",
            mime="application/pdf",
        )