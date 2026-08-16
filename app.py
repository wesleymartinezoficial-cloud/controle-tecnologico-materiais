import streamlit as st
from views import (
    aba_agregados,
    aba_blocos,
    aba_concreto,
    aba_dosagem,
    aba_granulometria,
    aba_memoria,
    aba_slump,
)

st.set_page_config(
    page_title="Sistema de Controle Tecnológico - ABNT",
    layout="wide",
    page_icon="🏗️",
)

st.sidebar.image("https://img.icons8.com/color/96/worker-with-roadblock.png", width=60)
st.sidebar.title("Informações do Laudo")

obra = st.sidebar.text_input("Obra / Empreendimento", value="Residencial Unifamiliar")
cliente = st.sidebar.text_input("Cliente / Contratante", value="Construtora X")
responsavel = st.sidebar.text_input("Engenheiro Responsável / CREA", value="Eng. Silvério Medeiros")
data_ensaio = st.sidebar.date_input("Data do Ensaio")

st.sidebar.markdown("---")
st.sidebar.caption("Normas: NBR 17054 | 16916 | 16917 | 16972 | 5739 | 12655 | NM 46 | 16889 | 15270")

st.title("🏗️ Sistema Integrado de Controle Tecnológico e Dosagem")
st.caption(f"**Obra:** {obra} | **Responsável:** {responsavel} | **Data:** {data_ensaio.strftime('%d/%m/%Y')}")

tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs([
    "📊 Granulometria & Pulverulento",
    "🏖️ Agregados (Físico)",
    "💥 Compressão & fck (NBR 12655)",
    "🧱 Blocos / Alvenaria",
    "📐 Slump Test (Concreto)",
    "🧮 Dosagem / Traço (ABCP)",
    "📚 Memória de Cálculo",
])

with tab1:
    aba_granulometria.render()
with tab2:
    aba_agregados.render()
with tab3:
    aba_concreto.render()
with tab4:
    aba_blocos.render()
with tab5:
    aba_slump.render()
with tab6:
    aba_dosagem.render()
with tab7:
    aba_memoria.render()
