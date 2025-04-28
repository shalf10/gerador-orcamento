Um projeto simples em Python para gerar orçamentos automaticamente!
Este sistema coleta informações do cliente, salva os dados em um arquivo .csv e gera um orçamento em PDF formatado.
🚀 Funcionalidades

    Coleta informações básicas de orçamento:

        Nome do cliente

        Serviço ou produto

        Valor (formatado em R$)

        Prazo de entrega

    Salva todos os orçamentos no arquivo orcamentos.csv

    Gera um PDF personalizado para cada orçamento

📂 Estrutura de Pastas

gerador_orcamento/
├── main.py
├── orcamento.py
├── utils/
│   ├── pdf_generator.py
│   ├── data_handler.py
├── data/
│   ├── orcamentos.csv
├── README.md
├── requirements.txt

🛠️ Tecnologias usadas

    Python 3.8+

    fpdf2 – para criação de PDFs

    Bibliotecas padrão do Python:

        csv

        os

        datetime

📥 Instalação e uso

    Clone o repositório:

git clone https://github.com/seu-usuario/gerador-orcamento.git
cd gerador_orcamento

    Instale as dependências:

pip install -r requirements.txt

    Rode o programa:

python main.py

📝 Exemplo de Uso

Quando rodar o programa, você verá:

=== Gerador de Orçamentos ===

Nome do cliente: João Silva
Serviço/Produto: Criação de Site
Valor (R$): 2500
Prazo de entrega (ex: 7 dias): 10 dias

Orçamento criado com sucesso!

    O sistema salva no data/orcamentos.csv.

    Gera um PDF em data/orcamento_Joao_Silva.pdf.

✨ Melhorias futuras (opcionais)

    Adicionar campos como telefone e e-mail do cliente

    Criar uma interface gráfica (ex: com Streamlit ou Tkinter)

    Melhorar o design dos PDFs

    Enviar orçamentos por e-mail automaticamente

🧠 Autor

Desenvolvido como projeto de estudo para portfólio de Python.
Feito com foco em prática e aprendizado contínuo! 🚀