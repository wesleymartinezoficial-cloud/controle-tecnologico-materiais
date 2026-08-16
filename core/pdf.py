from fpdf import FPDF

class PDFLaudo(FPDF):
    def header(self):
        self.set_font("Arial", "B", 14)
        self.cell(0, 10, "LAUDO DE CONTROLE TECNOLÓGICO - ABNT", border=True, ln=True, align="C")
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 8)
        self.cell(0, 10, f"Página {self.page_no()}", align="C")

def gerar_pdf_granulometria(obra: str, responsavel: str, res: dict) -> bytes:
    pdf = PDFLaudo()
    pdf.add_page()
    pdf.set_font("Arial", "", 10)

    # Identificação
    pdf.cell(0, 8, f"Obra / Projeto: {obra}", ln=True)
    pdf.cell(0, 8, f"Responsável Técnico: {responsavel}", ln=True)
    pdf.ln(5)

    # Resultados Sintéticos
    pdf.set_font("Arial", "B", 11)
    pdf.cell(0, 8, "Resultados Ensaio de Granulometria:", ln=True)
    pdf.set_font("Arial", "", 10)
    pdf.cell(0, 6, f"- Módulo de Finura (MF): {res['mf']:.2f}", ln=True)
    pdf.cell(0, 6, f"- Dimensão Máxima Característica (DMC): {res['dmc']} mm", ln=True)
    pdf.cell(0, 6, f"- Erro de Perda: {res['erro']:.2f}%", ln=True)
    pdf.ln(5)

    # Retorna o arquivo como bytes para o Streamlit fazer o download
    return bytes(pdf.output())
