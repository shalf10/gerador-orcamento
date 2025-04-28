from utils.pdf_generator import gerar_pdf
from utils.data_handler import salvar_orcamento

def criar_orcamento(dados):
    """
    Função para criar um orçamento e salvar em um arquivo PDF.
    
    Parâmetros:
    dados (dict): Dicionário contendo os dados do orçamento.
    """
    # Salvar os dados do orçamento em um arquivo
    salvar_orcamento(dados)
    
    # Gerar o PDF do orçamento
    gerar_pdf(dados)
    # Aqui você pode adicionar mais funcionalidades, como enviar o orçamento por e-mail ou armazená-lo em um banco de dados.