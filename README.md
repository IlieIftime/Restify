# Restify
# Restify

**Descrição**  
Restify é o repositório com o código-fonte do projeto associado ao relatório final EI1 (B23). Este README foca-se na execução, estrutura e utilização do código (não no conteúdo do relatório). O repositório contém scripts para treino, avaliação e inferência, notebooks de exploração e utilitários para reproduzir os experimentos.

---

## Índice
- [Funcionalidades](#funcionalidades)  
- [Pré-requisitos](#pré-requisitos)  
- [Instalação](#instalação)  

---

## Funcionalidades
- Scripts para **pré-processamento** de dados.  
- Pipelines de **treino** e **validação** de modelos.  
- Ferramentas para **avaliação** e geração de métricas/figuras.  
- Script de **inferência** para aplicar modelos a novos dados.  
- Notebooks de exploração e análise.

---

## Pré-requisitos
- **Python 3.8+**  
- `pip`  
- Recomendado: ambiente virtual (`venv`, `conda`)

---

## Instalação
```bash
# clonar repositório
git clone https://github.com/IlieIftime/Restify.git
cd Restify

# criar e ativar ambiente virtual (exemplo com venv)
python -m venv .venv
# Linux / macOS
source .venv/bin/activate
# Windows
.venv\Scripts\activate

# instalar dependências
pip install -r requirements.txt

/
├── src/               # Código-fonte (módulos e scripts)
├── data/              # Dados brutos e processados (não commitar dados sensíveis)
├── notebooks/         # Notebooks de exploração e experimentação
├── models/            # Modelos treinados e artefactos
├── docs/              # Documentação, figuras e relatórios auxiliares
├── tests/             # Testes unitários / de integração
├── requirements.txt   # Dependências do projeto
├── config/            # Ficheiros de configuração (yaml/json)
└── README.md          # Este ficheiro

# Exemplo genérico — ajustar flags conforme config do projeto
python src/train.py --config config/train.yaml --output models/
