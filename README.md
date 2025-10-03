# Clean Code - Atv de Dependência

## Objetivo
Esta atividade consiste em uma refatoração de um código monolítico, com foco em reduzir dependências e melhorar a organização.

## Mudanças
- Código dividido em módulos (`user_service`, `email_service`, `external_api`, `main`).
- Uso da biblioteca [requests](https://pypi.org/project/requests/) para consumo de API externa.
- Inclusão da biblioteca [rich](https://pypi.org/project/rich/) para melhorar a saída de dados no terminal.
- Funções mais coesas e fáceis de testar, evitando efeitos colaterais desnecessários.

## Requisitos
- Python 3.9+
- Instalar dependências:
```bash
pip install -r requirements.txt
