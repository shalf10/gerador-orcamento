import csv
import os

CAMINHO_ARQUIVO = "data/orcamentos.csv"

def salvar_orcamento(dados):
    arquivo_existe = os.path.exists(CAMINHO_ARQUIVO)

    with open(CAMINHO_ARQUIVO, mode='a', newline='', encoding="utf-8") as csvfile:
        campos = ['cliente', 'servico', 'valor', 'prazo', 'data']
        writer = csv.DictWriter(csvfile, fieldnames=campos)

        # Escreve o cabeçalho apenas se o arquivo não existir
        if not arquivo_existe or os.stat(CAMINHO_ARQUIVO).st_size == 0:
            writer.writeheader()

        writer.writerow(dados)

def formatar_valor(valor):
    return f"R$ {valor:,.2f}".replace('.', 'X').replace(',', '.').replace("X", ",")