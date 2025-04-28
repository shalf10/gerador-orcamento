from fpdf import FPDF
import os

def gerar_pdf(dados):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt="Orçamento", ln=True, align='C')
    pdf.ln(10)

    for chave, valor in dados.items():
        pdf.cell(200, 10, txt=f"{chave.capitalize()}: {valor}", ln=True)

    # Salvar PDF com nome do cliente
    nome_arquivo = f"data/orcamento_{dados['cliente'].replace(' ', '_')}.pdf"
    pdf.output(nome_arquivo)