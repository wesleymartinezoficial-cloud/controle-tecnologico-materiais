import streamlit as st

def render():
    st.markdown("""
    ### Fórmulas e Referências Normativas
    * **NBR 12655:** $f_{ck,est} = 2 \\cdot \\frac{\\sum f_i}{m} - f_m$
    * **NBR 5739:** $f_c = \\frac{F}{A \\cdot 10}$ (com $F$ em N e $A$ em cm²).
    * **NBR NM 46:** $Pulverulento (\\%) = \\frac{M_{seca} - M_{lavada}}{M_{seca}} \\times 100$.
    * **NBR 15270:** $f_b = \\frac{F}{A_{bruta} \\cdot 10}$.
    """)
