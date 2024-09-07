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
│   ├── model/
│   │   └── modelos.pkl                 # Modelos já treinados
├── notebooks/
│   ├── EDA.ipynb                       # Análise Exploratória de Dados e tratamento inicial
│   ├── data_preprocessing.ipynb        # Pré-processamento e modelagem dos dados
├── tests/                              # Testes unitários
│   └── test_model_SVM.py               # Arquivo de testes unitários para validação do código
├── LICENSE                             # Licença do projeto
├── README.md                           # Este arquivo
└── requirements.txt                    # Lista de dependências para o projeto de Detecção de Cogumelos
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
- **Melhor acurácia com KNN**: 0.999
- **Melhor acurácia com Regressão Logística**: 0.876
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

# 🏆 O SVM foi o Melhor Modelo para Classificação de Cogumelos

## 1. Separação de Margem Máxima
O **SVM** se destacou por sua capacidade de encontrar a **margem de separação máxima** entre as classes, o que é essencial em dados onde as variáveis têm sobreposição, como no conjunto de cogumelos.
Com o uso do **kernel radial (RBF)**, o SVM conseguiu mapear os dados em um espaço de maior dimensão, tornando a separação entre cogumelos comestíveis e venenosos mais clara, mesmo que os dados não fossem linearmente separáveis.

## 2. Controle de Variância e Estabilidade
A variância do **SVM** foi de **1.458388e-07**, uma variância moderada, que indica que o modelo conseguiu capturar padrões complexos sem superajustar aos dados de treino.

### Comparado com outros modelos:
- **Árvore de Decisão** teve uma variância muito menor (**2.022212e-09**), sugerindo maior estabilidade, mas foi menos eficaz em capturar a complexidade dos dados.
- **Random Forest** também apresentou variância baixa (**2.453148e-09**), mas assim como a Árvore de Decisão, foi superado em termos de precisão.
- **KNN** e **Rede Neural** apresentaram variâncias maiores do que o SVM, indicando maior instabilidade nos resultados.

O coeficiente de variação do **SVM** foi **0.0383%**, mostrando um controle razoável de variação em relação ao desempenho, sendo maior que o de modelos como a **Árvore de Decisão** (0.0045%) e **Random Forest** (0.0049%), mas ainda assim eficiente.

## 3. Teste de Normalidade dos Resíduos (Shapiro-Wilk)
O p-value do **SVM** no teste de **Shapiro-Wilk** foi **0.411**, o que indica que os resíduos do modelo se aproximam de uma distribuição normal, o que é um sinal positivo para a robustez e adequação do modelo aos dados.

### Comparado com outros modelos:
- **Árvore de Decisão** e **Random Forest** apresentaram p-values extremamente baixos (**7.766e-12** e **4.247e-11**, respectivamente), sugerindo que os resíduos se afastam significativamente da normalidade, o que pode impactar a generalização dos modelos.
- **Rede Neural** também apresentou um p-value muito baixo (**4.164e-09**), o que, embora tenha dado bons resultados, indica resíduos não normais.
- **KNN** também não teve resíduos próximos à normalidade (p-value de **3.195e-08**).

## 4. Flexibilidade com Hiperparâmetros
O **SVM** se beneficiou da flexibilidade no ajuste de seus hiperparâmetros, como o valor de **C** (regularização) e o tipo de **kernel** utilizado. Esses ajustes permitiram ao modelo equilibrar precisão e generalização, o que foi essencial para seu desempenho superior.

## 5. Comparação com Outros Modelos
- **Árvore de Decisão** e **Random Forest** apresentaram baixa variância e foram muito estáveis, mas não conseguiram capturar a complexidade dos dados tão bem quanto o **SVM**.
- A **Rede Neural**, embora também tenha sido eficaz em lidar com a complexidade, teve resíduos significativamente afastados da normalidade, o que indica que seu desempenho pode ser menos consistente em dados não vistos.

---

# 🥈 Melhor Alternativa: Regressão Logística

## 1. Baixa Variância e Alta Estabilidade
A **Regressão Logística** apresentou a menor variância entre todos os modelos, com um valor de **3.325033e-12** e o menor coeficiente de variação de **0.000208%**.
Isso indica que a **Regressão Logística** é extremamente estável em suas previsões, sendo uma excelente alternativa para situações onde a simplicidade e a estabilidade são mais importantes do que a capacidade de capturar padrões não lineares.

## 2. Normalidade dos Resíduos
No teste de **Shapiro-Wilk**, a **Regressão Logística** apresentou um p-value de **0.2440**, indicando que seus resíduos também se aproximam da normalidade, embora não tanto quanto o **SVM**.
Isso mostra que, apesar de sua simplicidade, a **Regressão Logística** ainda se comporta de maneira robusta em relação à adequação aos dados.

## 3. Limitação em Dados Não Lineares
O desempenho inferior da **Regressão Logística** em comparação ao **SVM** pode ser explicado por sua incapacidade de lidar com dados não lineares. O conjunto de dados de cogumelos contém variáveis com relações complexas, o que favorece o uso de modelos como o **SVM** que podem lidar com essa não linearidade.


## 📝 Licença
Este projeto está licenciado sob os termos do Repositório de Aprendizado de Máquina da UCI. Consulte o arquivo `dataset_info.md` para mais detalhes.

Este projeto é distribuído sob a licença [MIT](LICENSE).

## 🤝 Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request.


## ✨ Agradecimentos
- UCI Machine Learning Repository pela disponibilização do dataset.