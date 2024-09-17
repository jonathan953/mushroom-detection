# 🍄 Mushroom Detection

&nbsp;

## 📄 Descrição do Projeto
Este projeto realiza a classificação de cogumelos como comestíveis ou venenosos com base em diversas características físicas e ambientais. Usando um conjunto de dados detalhado das espécies **Agaricus** e **Lepiota**, aplicamos técnicas de Análise Exploratória de Dados (EDA), pré-processamento e modelagem de Machine Learning para treinar modelos capazes de prever a classe dos cogumelos.

---
  
## 📂 Estrutura do Projeto
A estrutura do projeto está organizada em pastas para facilitar a navegação e entendimento:

```bash
├── data/
│   ├── processed/
│   │   └── dados_processados.pkl       # Dados já processados e prontos para modelagem
│   ├── raw/
│   │   └── dataset_info.md             # Informações detalhadas sobre o conjunto de dados
│   ├── model/
│   │   └── modelo_svm.pkl              # Modelo SVM já treinado
├── notebooks/
│   ├── EDA.ipynb                       # Análise Exploratória de Dados e tratamento inicial
│   ├── data_preprocessing.ipynb        # Pré-processamento e modelagem dos dados
├── tests/                              # Testes unitários
│   └── test_model_SVM.py               # Arquivo de testes unitários para validação do código
├── LICENSE                             # Licença do projeto
├── README.md                           # Este arquivo
└── requirements.txt                    # Lista de dependências para o projeto de Detecção de Cogumelos
```

---

## 📊 Análise Exploratória de Dados (EDA)
O notebook `EDA.ipynb` abrange:

- Carregamento e compreensão dos dados.
- Visualização de distribuições e correlações entre variáveis.
- Tratamento de dados ausentes e categóricos.
- Geração de insights iniciais sobre os atributos mais relevantes.

---

## 🛠️ Pré-processamento e Modelagem

O notebook `data_preprocessing.ipynb` executa as seguintes etapas essenciais:

1. **Carregamento dos Dados Processados**: Os dados limpos são carregados do arquivo `dados_processados.pkl` para otimizar o tempo de execução.

2. **Seleção de Features**: São escolhidas as variáveis mais relevantes para melhorar a performance dos modelos.

3. **Divisão Treino/Teste**: Os dados são divididos em conjuntos de treino e teste usando `train_test_split`, garantindo boa representatividade e evitando overfitting.

4. **Avaliação de Modelos**: São treinados e avaliados diversos modelos de Machine Learning, como KNN, Decision Tree, Random Forest, Logistic Regression, SVM e Redes Neurais, com o SVM apresentando o melhor desempenho.

5. **Ajuste de Hiperparâmetros**: O `GridSearchCV` é usado para otimizar hiperparâmetros e aumentar a precisão dos modelos.

6. **Validação Cruzada**: A validação cruzada é aplicada para assegurar a robustez dos modelos e a sua capacidade de generalização.

---

## 📁 Estrutura dos Dados

- **Processed**: Contém o arquivo `dados_processados.pkl`, que é o conjunto de dados após o pré-processamento. Isso inclui tratamento de valores ausentes, codificação de variáveis categóricas e normalização, deixando os dados prontos para a modelagem.
- **Raw**: Contém o arquivo `dataset_info.md`, que fornece informações detalhadas sobre o conjunto de dados original, incluindo descrições dos atributos, a fonte dos dados e as referências para citação. Este arquivo é útil para compreender a estrutura dos dados antes do pré-processamento.
- **Model**: Contém o modelo SVM treinado e otimizado, incluído no arquivo `modelo_svm.pkl`,  para uso futuro. O modelo podem ser facilmente carregado para fazer previsões sem a necessidade de re-treinar o algoritmo.

---

## 📈 Resultados Comparativos dos Modelos

Os modelos de Machine Learning foram avaliados utilizando **acurácia**, **variância** e o **teste de normalidade de Shapiro-Wilk** para medir a performance, estabilidade e adequação dos resíduos à normalidade. Abaixo, estão os principais resultados:

| Modelo                           | Acurácia | Variância         | Shapiro-Wilk (p-value)  | Comentários                                                                 |
|-----------------------------------|----------|-------------------|-------------------------|-----------------------------------------------------------------------------|
| **Support Vector Machine (SVM)**  | 0.992    | 1.275214e-06      | 0.3161                 | Excelente equilíbrio entre acurácia, baixa variância e resíduos relativamente próximos à normalidade. Ideal para dados não lineares e com margens de decisão bem definidas. |
| **Logistic Regression**           | 0.876    | 4.583502e-12      | 0.6069                  | Acurácia mais baixa comparada a outros modelos, porém com excelente estabilidade (baixa variância) e resíduos bastante próximos da normalidade. Indicado para dados lineares.        |
| **Decision Tree**                 | 1.0      | 0.000000e+00     | 1.0             | Acurácia perfeita e variância nula, mas resíduos extremamente longe da normalidade. Tendência ao overfitting, o que pode prejudicar a generalização do modelo.                                              |
| **Random Forest**                 | 1.0      | 3.904961e-09    | 4.4017            | Acurácia perfeita e boa robustez. No entanto, resíduos significativamente longe da normalidade, sugerindo problemas com a modelagem dos dados ou alta complexidade.                                       |
| **Neural Networks**               | 1.0      | 1.081776e-07      | 0.0014               | Acurácia muito alta, mas com maior variância e resíduos longe da normalidade, indicando possíveis ajustes a serem feitos, como tuning de hiperparâmetros ou regularização.                                         |
| **K-Nearest Neighbors (KNN)**     | 1.0   | 1.644531e-08    | 3.8155               | Acurácia próxima de 1.0, mas maior variação nos resultados. Resíduos longe da normalidade indicam que o modelo pode não estar capturando bem os padrões subjacentes.                       |

---

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

 ---

## 🏆 O SVM foi o Melhor Modelo para Classificação de Cogumelos

### 1. Separação de Margem Máxima
O **Support Vector Machine (SVM)** destacou-se por sua habilidade de encontrar a **margem de separação máxima** entre as classes. Isso é crucial em dados onde as variáveis têm sobreposição, como no conjunto de cogumelos. Utilizando o **kernel radial (RBF)**, o SVM conseguiu mapear os dados em um espaço de maior dimensão, facilitando a separação entre cogumelos comestíveis e venenosos, mesmo que os dados não fossem linearmente separáveis.

### 2. Controle de Variância e Estabilidade
A variância do **SVM** foi de **1.275214e-06**, um valor que indica um controle moderado da variação, capturando padrões complexos sem superajustar aos dados de treino.

#### Comparação com outros modelos:
- **Decision Tree** teve uma variância menor (**0.000000e+00**), sugerindo maior estabilidade, mas foi menos eficaz em capturar a complexidade dos dados, indicando overfitting.
- **Random Forest** também apresentou variância baixa (**3.904961e-09**), mas, como a Decision Tree, não superou o SVM em termos de precisão.
- **K-Nearest Neighbors (KNN)** e **Neural Networks** apresentaram variâncias maiores do que o SVM, mostrando maior instabilidade nos resultados.

O coeficiente de variação do **SVM** foi **0.0383%**, demonstrando um controle razoável de variação no desempenho. Ele foi mais elevado que os da **Decision Tree** (0.0045%) e da **Random Forest** (0.0049%), mas ainda eficiente, sendo superior em precisão.

### 3. Teste de Normalidade dos Resíduos (Shapiro-Wilk)
O p-value do **SVM** no teste de **Shapiro-Wilk** foi **0.2865**, sugerindo que os resíduos do modelo se aproximam de uma distribuição normal. Isso é um bom indicador da robustez e adequação do modelo aos dados.

#### Comparação com outros modelos:
- **Árvore de Decisão** e **Random Forest** apresentaram p-values muito baixos (**4.2396e-11** e **4.2432e-11**, respectivamente), indicando que seus resíduos estão muito distantes da normalidade, possivelmente devido ao overfitting.
- **Neural Networks** apresentou um p-value muito baixo (**0.0001**), o que, embora mostre boa acurácia, sugere problemas significativos de normalidade dos resíduos.
- **K-Nearest Neighbors (KNN)** também teve resíduos distantes da normalidade (p-value de **1.3457e-08**), o que indica que o modelo pode não estar capturando bem os padrões subjacentes.
- **Regressão Logística** teve um p-value de **0.1699**, indicando que os resíduos estão razoavelmente próximos da normalidade.


### 4. Flexibilidade com Hiperparâmetros
O **SVM** se beneficiou da flexibilidade no ajuste de hiperparâmetros como **C** (regularização) e o tipo de **kernel**. Esses ajustes permitiram ao modelo equilibrar precisão e generalização, sendo uma excelente escolha para dados com padrões não lineares, como no caso dos cogumelos.

### 5. Comparação com Outros Modelos
- **Decision Tree** e **Random Forest** apresentaram baixa variância e foram estáveis, mas não conseguiram capturar a complexidade dos dados tão bem quanto o **SVM**.
- **Neural Networks**, embora eficaz para lidar com a complexidade, teve resíduos significativamente afastados da normalidade, o que pode prejudicar sua consistência em dados desconhecidos.
- **K-Nearest Neighbors (KNN)** teve uma acurácia alta, mas sua maior variação nos resultados e resíduos fora da normalidade sugerem uma menor capacidade de generalização.

---

## 🥈 Melhor Alternativa: Logistic Regression

### 1. Baixa Variância e Alta Estabilidade
A **Logistic Regression** destacou-se pela menor variância entre todos os modelos, com um valor de **4.583502e-12**. Isso indica que o modelo é extremamente estável em suas previsões, sendo uma excelente escolha para cenários onde simplicidade e estabilidade são mais importantes que a capacidade de capturar padrões complexos ou não lineares.

### 2. Normalidade dos Resíduos
No teste de **Shapiro-Wilk**, a **Logistic Regression** apresentou um p-value de **0.1699**, indicando que seus resíduos estão próximos da normalidade. Isso demonstra que, apesar de sua simplicidade, o modelo é robusto e bem ajustado aos dados.

### 3. Limitação em Dados Não Lineares
O desempenho inferior da **Logistic Regression** em relação ao **SVM** pode ser explicado por sua limitação ao lidar com dados não lineares. Como o conjunto de dados de cogumelos contém variáveis com interações mais complexas, o **SVM** (com seu kernel RBF) consegue capturar essas relações não lineares com maior eficácia.


---

## Conclusão
O **SVM** foi o melhor modelo para a classificação de cogumelos, devido à sua alta acurácia, controle moderado de variância, normalidade dos resíduos e flexibilidade em ajustar hiperparâmetros. A **Logistic Regression**, embora menos precisa, é uma excelente alternativa pela sua estabilidade e simplicidade, sendo útil em casos onde não há tanta necessidade de capturar a complexidade não linear dos dados.

---

## 📝 Licença
Este projeto está licenciado sob os termos do Repositório de Aprendizado de Máquina da UCI. Consulte o arquivo `dataset_info.md` para mais detalhes.

Este projeto é distribuído sob a licença [MIT](LICENSE).


## 🤝 Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request.


## ✨ Agradecimentos
- UCI Machine Learning Repository pela disponibilização do dataset.