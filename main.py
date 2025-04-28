from orcamento import criar_orcamento
from datetime import datetime
from utils.data_handler import formatar_valor

def main():
    print("=== Gerador de Orçamento ===\n")

    cliente = input("Nome do cliente: ")
    servico = input("Serviço/Produto: ")
    valor = float(input("Valor (R$): "))
    valor_formatado = formatar_valor(valor)
    prazo = input("Prazo (dias): ")

    orcamento = {
        "cliente": cliente,
        "servico": servico,
        "valor": valor_formatado,
        "prazo": prazo,
        "data": datetime.today().strftime('%d/%m/%Y')
    }

    criar_orcamento(orcamento)
    print("\nOrçamento gerado com sucesso!")

if __name__ == "__main__":
    main()