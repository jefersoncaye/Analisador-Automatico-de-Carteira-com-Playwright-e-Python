# Analisador Automático de Carteira com Playwright e Python

Este projeto demonstra o uso do **Playwright com Python** para raspagem de dados financeiros em tempo real, processamento de informações e geração de relatórios automáticos a partir de uma carteira de investimentos.

O objetivo é mostrar que o Playwright pode ser utilizado não apenas para testes automatizados, mas também como uma ferramenta robusta de automação web aplicada a problemas reais.

---

## Funcionalidades

- Raspagem automática de preços de ativos no Google Finance
- Cálculo automático de:
  - valor investido
  - valor atual
  - lucro ou prejuízo
  - percentual de ganho ou perda
- Organização da carteira por classe de ativo:
  - Criptomoedas
  - Ações
  - FIIs
- Resumo consolidado por classe de investimento
- Cálculo do total geral da carteira
- Identificação do melhor e do pior ativo com base no percentual de retorno

---

## Tecnologias Utilizadas

- Python 3.9 ou superior
- Playwright (API síncrona)
- Chromium (navegador controlado pelo Playwright)

---

## Requisitos

- Python 3.9 ou superior
- pip
- Windows, Linux ou macOS

---

## Instalação

### Clonar o repositório

git clone https://github.com/jefersoncaye/Analisador-Autom-tico-de-Carteira-com-Playwright-e-Python

cd seu-repositorio

### Criar ambiente virtual (opcional)

python -m venv venv

Windows:  
venv\Scripts\activate

Linux/macOS:  
source venv/bin/activate

### Instalar dependências

pip install playwright

### Instalar navegadores

playwright install

---

## Execução

python main.py

---

## Estrutura da Carteira

CARTEIRA = [
    {"ativo": "BTC-BRL", "quantidade": 0.05, "preco_compra": 135000, "classe": "Cripto"},
    {"ativo": "PETR4:BVMF", "quantidade": 150, "preco_compra": 34.20, "classe": "Ação"},
    {"ativo": "MXRF11:BVMF", "quantidade": 200, "preco_compra": 10.20, "classe": "FII"},
]

---

## Observações

Projeto educacional. Mudanças no Google Finance podem exigir ajustes nos locators.

---
