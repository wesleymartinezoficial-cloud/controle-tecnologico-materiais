import pandas as pd
import plotly.graph_objects as go
import streamlit as st
from core.granulometria import calcular_material_pulverulento, processar_granulometria

LIMITES_MASSA = {
    "Areia (Agregado Miúdo)": {"massa_min": 300.0},
    "Brita 0 (Pedrisco)": {"massa_min": 1000.0},
    "Brita 1": {"massa_min": 5000.0},
    "Brita 2": {"massa_min": 10000.0},
}

PENEIRAS = [
    {"abertura": 37.5, "astm": '1 1/2"', "serie_normal": True},
    {"abertura": 19.0, "astm": '3/4"', "serie_normal": True},
    {"abertura": 9.5, "astm": '3/8"', "serie_normal": True},
    {"abertura": 4.75, "astm": "Nº 4", "serie_normal": True},
    {"abertura": 2.36, "astm": "Nº 8", "serie_normal": True},
    {"abertura": 1.18, "astm": "Nº 16", "serie_normal": False},
    {"abertura": 0.60, "astm": "Nº 30", "serie_normal": True},
    {"abertura": 0.30, "astm": "Nº 50", "serie_normal": True},
    {"abertura": 0.15, "astm": "Nº 100", "serie_normal": True},
]

def render():
    st.subheader("Análise Granulométrica e Material Pulverulento")
    c1, c2 = st.columns(2)
    with c1:
        tipo = st.selectbox("Tipo de Agregado", list(LIMITES_MASSA.keys()))
    with c2:
        m_min = LIMITES_MASSA[tipo]["massa_min"]
        massa_inicial = st.number_input("Massa Inicial Seca (g)", value=m_min, step=100.0)

    st.markdown("---")
    st.write("**1.1 Material Pulverulento (< 0,075 mm - Peneira Nº 200 - NBR NM 46)**")
    col_p1, col_p2 = st.columns(2)
    with col_p1:
        m_seca_lavada = st.number_input("Massa da amostra seca APÓS lavagem na #200 (g)", value=massa_inicial * 0.97)
    with col_p2:
        if massa_inicial > 0:
            mat_p = calcular_material_pulverulento(massa_inicial, m_seca_lavada)
            st.metric("Teor de Material Pulverulento", f"{mat_p:.2f}%")

    st.markdown("---")
    st.write("**1.2 Ensaio de Peneiramento Granulométrico (NBR 17054)**")
    df_base = pd.DataFrame({
        "Abertura (mm)": [p["abertura"] for p in PENEIRAS],
        "ASTM": [p["astm"] for p in PENEIRAS],
        "Série": ["Normal" if p["serie_normal"] else "Intermediária" for p in PENEIRAS],
        "Massa Retida (g)": [0.0] * len(PENEIRAS),
    })

    col_tab, col_fundo = st.columns([3, 1])
    with col_tab:
        df_editado = st.data_editor(df_base, use_container_width=True, hide_index=True)
    with col_fundo:
        massa_fundo = st.number_input("Fundo Receptor (g)", value=0.0)
        btn_calc_1 = st.button("📊 Processar Granulometria", use_container_width=True)

    if btn_calc_1 and massa_inicial > 0:
        res = processar_granulometria(massa_inicial, df_editado, massa_fundo)
        m1, m2, m3 = st.columns(3)
        m1.metric("Massa Recuperada", f"{res['massa_rec']:.1f} g")
        m2.metric("Erro de Perda", f"{res['erro']:.2f}%", delta="✓ Aprovado" if res["erro"] <= 1.0 else "❌ Reprovado (>1%)")
        m3.metric("Módulo de Finura (MF)", f"{res['mf']:.2f}", f"DMC: {res['dmc'] if res['dmc'] else 'N/I'} mm")

        # ----------------------------------------------------------------------
        # GRÁFICO INTERATIVO COM PLOTLY
        # ----------------------------------------------------------------------
        df_res = res["df_resultado"]
        fig = go.Figure()

        # Curva de Ensaio
        fig.add_trace(go.Scatter(
            x=df_res["Abertura (mm)"],
            y=df_res["Passante (%)"],
            mode='lines+markers',
            name='Amostra Ensaiada',
            line=dict(color='#005580', width=3),
            marker=dict(size=8)
        ))

        # Ajustes Visuais e Escala Logarítmica Granulométrica
        fig.update_layout(
            title=f"Curva Granulométrica Interativa - {tipo}",
            xaxis=dict(
                title="Abertura das Peneiras (mm) [Escala Log]",
                type="log",
                autorange="reversed"  # Inverte o eixo conforme convenção de solos/agregados
            ),
            yaxis=dict(title="Porcentagem Passante Acumulada (%)", range=[0, 105]),
            template="plotly_white",
            hovermode="x unified",
            margin=dict(l=40, r=40, t=50, b=40)
        )

        st.plotly_chart(fig, use_container_width=True)
