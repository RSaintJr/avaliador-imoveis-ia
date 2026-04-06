# Avaliador Imobiliário Preditivo | Machine Learning

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)

## Sobre o Projeto
Este projeto consiste em uma aplicação web preditiva focada na avaliação de ativos imobiliários. A solução utiliza um pipeline de Machine Learning para estimar o valor de mercado de propriedades com base em variáveis geoespaciais, demográficas e estruturais. O objetivo principal é demonstrar a aplicação ponta a ponta de engenharia de dados e modelagem preditiva na resolução de problemas de precificação.

**Acesso à Aplicação em Produção:** https://avaliador-imoveis-ia.streamlit.app/

## Arquitetura e Pipeline de Dados
O desenvolvimento foi estruturado com foco em rigor estatístico e otimização para ambientes de produção:

* **Feature Engineering:** Tratamento de valores ausentes via imputação pela mediana e transformação de variáveis categóricas espaciais utilizando *One-Hot Encoding*, garantindo a integridade da representação vetorial para o algoritmo.
* **Modelagem e Validação:** Separação estrita entre conjuntos de treino e teste para prevenção de *Data Leakage*. A regressão foi construída utilizando o algoritmo **Random Forest Regressor**, selecionado por sua eficácia no mapeamento de correlações não lineares em dados tabulares.
* **Deploy e Compressão:** O modelo final foi ajustado (*pruning* de profundidade) e submetido à compressão nativa (zlib via `joblib`), assegurando a viabilidade de execução em servidores de nuvem com restrições de memória RAM.

## Resultados e Métricas
* **R² Score (Coeficiente de Determinação):** 0.82 (O modelo explica 82% da variância na precificação imobiliária dos dados de teste).
* **Mean Absolute Error (MAE):** ~$31.330 (Margem de erro absoluta média na estimativa financeira).

## Como Executar Localmente

Requisitos: Python 3.x instalado no ambiente.

```bash
# Clonar o repositório
git clone [https://github.com/roberto/avaliador-imoveis-ia.git](https://github.com/roberto/avaliador-imoveis-ia.git)

# Acessar o diretório
cd avaliador-imoveis-ia

# Instalar as dependências necessárias
pip install -r requirements.txt

# Inicializar o servidor web local
streamlit run app.py
