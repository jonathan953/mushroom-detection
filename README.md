# 🍄 Mushroom Detection

## 📄 Descrição do Projeto
Este projeto realiza a classificação de cogumelos como comestíveis ou venenosos com base em diversas características físicas e ambientais. Usando um conjunto de dados detalhado das espécies **Agaricus** e **Lepiota**, aplicamos técnicas de Análise Exploratória de Dados (EDA), pré-processamento e modelagem de Machine Learning para treinar modelos capazes de prever a classe dos cogumelos.


## 📂 Estrutura do Projeto
A estrutura do projeto está organizada em pastas para facilitar a navegação e entendimento:

```bash
├── data/
│   ├── processed/
│   │   └── dados_processados.pkl       # Dados já processados e prontos para modelagem
│   ├── raw/
│   │   └── dataset_info.md             # Informações detalhadas sobre o conjunto de dados
├── notebooks/
│   ├── EDA.ipynb                       # Análise Exploratória de Dados e tratamento inicial
│   ├── data_preprocessing.ipynb        # Pré-processamento e modelagem dos dados
└── README.md                           # Este arquivo
```


## 📊 Análise Exploratória de Dados (EDA)
O notebook `EDA.ipynb` abrange:

- Carregamento e compreensão dos dados.
- Visualização de distribuições e correlações entre variáveis.
- Tratamento de dados ausentes e categóricos.
- Geração de insights iniciais sobre os atributos mais relevantes.


## 🛠️ Pré-processamento e Modelagem
O notebook `data_preprocessing.ipynb` aborda:

- Carregamento dos dados processados.
- Seleção das principais features para o modelo.
- Divisão do conjunto de dados em treino e teste.
- Implementação e avaliação de modelos de Machine Learning, como KNN, Decision Tree, Random Forest, Logistic Regression, SVM e Redes Neurais.
- Ajuste de hiperparâmetros utilizando `GridSearchCV`.
- Validação cruzada para assegurar a robustez dos modelos.


## 📁 Dados
- **Processed**: Contém o arquivo `dados_processados.pkl`, que é o conjunto de dados após o tratamento e pronto para ser usado na modelagem.
- **Raw**: Contém o arquivo `dataset_info.md` com as informações detalhadas sobre o conjunto de dados, incluindo a descrição dos atributos, fonte e citação.


## 📈 Resultados
Os modelos foram avaliados utilizando métricas como acurácia, e foi realizada uma busca de hiperparâmetros para otimizar o desempenho dos modelos. A seguir estão alguns dos resultados alcançados:

- **Melhor acurácia com Árvore de Decisão**: 1.0
- **Melhor acurácia com Random Forest**: 1.0
- **Melhor acurácia com KNN**: 0.99
- **Melhor acurácia com Regressão Logística**: 0.87
- **Melhor acurácia com SVM**: 0.995
- **Melhor acurácia com Redes Neurais**: 1.0



## 🖥️ Execução
Para executar este projeto localmente, siga os passos abaixo:

1. Clone o repositório:
```bash
   git clone https://github.com/jonathan953/mushroom-detection.git
```

2. Navegue até o diretório do projeto
```bash
  cd mushroom-detection
```

3. Instale as dependências necessárias
```bash
pip install -r requirements.txt
```
4. Execute os notebooks na sequência EDA.ipynb e data_preprocessing.ipynb para replicar a análise e os resultados.


## 📝 Licença
Este projeto está licenciado sob os termos do Repositório de Aprendizado de Máquina da UCI. Consulte o arquivo `dataset_info.md` para mais detalhes.


## 🤝 Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request.


## ✨ Agradecimentos
- UCI Machine Learning Repository pela disponibilização do dataset.