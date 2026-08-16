import streamlit as st

def render():
    st.subheader("Ensaio de Abatimento do Tronco de Cone (Slump Test)")
    slump = st.number_input("Abatimento Medido (cm)", value=10.0, step=0.5)
    
    if slump < 5.0:
        classe = "S10 (Concreto Seco - Extrusão/Pisos)"
    elif 5.0 <= slump < 10.0:
        classe = "S50 (Elementos Pré-moldados / Pavlov)"
    elif 10.0 <= slump < 16.0:
        classe = "S100 (Vigas, Pilares e Lajes com densidade média de armadura)"
    elif 16.0 <= slump < 22.0:
        classe = "S160 (Concreto Bombeável / Paredes de Concreto)"
    else:
        classe = "S220 (Concreto Fluido / Fundações Profundas)"

    st.info(f"📌 **Classe de Consistência:** {classe}")
