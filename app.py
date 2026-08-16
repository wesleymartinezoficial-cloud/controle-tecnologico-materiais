import streamlit as st
from views import aba_concreto, aba_dicas, aba_granulometria

st.set_page_config(
    page_title="Controle Tecnológico - ABNT",
    layout="wide",
    page_icon="🏗️",
)

st.title("🏗️ Sistema Integrado de Controle Tecnológico")
st.caption("Automação de ensaios laboratoriais segundo normas ABNT.")

tab1, tab2, tab3 = st.tabs([
    "📊 Granulometria",
    "💥 Resistência do Concreto",
    "🎓 Dicas Acadêmicas",
])

with tab1:
    aba_granulometria.render()

with tab2:
    aba_concreto.render()

with tab3:
    aba_dicas.render()