# 🍄 Mushroom Detection

&nbsp;

## 📄 Descrição do Projeto
Este projeto realiza a classificação de cogumelos como comestíveis ou venenosos com base em diversas características físicas e ambientais. Usando um conjunto de dados detalhado das espécies **Agaricus** e **Lepiota**, aplicamos técnicas de Análise Exploratória de Dados (EDA), pré-processamento e modelagem de Machine Learning para treinar modelos capazes de prever a classe dos cogumelos.

---
  
## 📂 Estrutura do Projeto
A estrutura do projeto está organizada em pastas para facilitar a navegação e entendimento:

```bash
├── .vscode/
│   └── extensions.json                # Recomendação de extensões para o projeto
├── data/
│   ├── model/
│   │   └── modelo_rf.pkl              # Modelo Random Forest já treinado
│   ├── processed/
│   │   └── dados_processados.pkl       # Dados já processados e prontos para modelagem
│   ├── raw/
│   │   └── dataset_info.md             # Informações detalhadas sobre o conjunto de dados
├── docs/
│   ├── LICENSE                         # Licença do projeto
│   ├── README.md                       # Este arquivo
├── notebooks/
│   ├── EDA.ipynb                       # Análise Exploratória de Dados e tratamento inicial
│   ├── data_preprocessing.ipynb        # Pré-processamento e modelagem dos dados
├── tests/                              # Testes unitários
│   └── test_model_RF.py               # Arquivo de testes unitários para validação do código
├── .gitignore                          # Ignora alguns downloads ao baixar o projeto
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

O notebook `data_preprocessing.ipynb` conduz um fluxo completo de preparação e modelagem dos dados, com foco em desempenho e reprodutibilidade. As etapas incluem:

1. **🔄 Carregamento de Dados Otimizado**  
   O conjunto de dados limpo e tratado é carregado diretamente do arquivo `dados_processados.pkl`, reduzindo o tempo de execução e evitando retrabalho em etapas anteriores.

2. **🎯 Seleção de Variáveis Relevantes**  
   São selecionadas as features com maior poder preditivo para o modelo. Essa etapa reduz dimensionalidade e melhora a performance, garantindo modelos mais simples e eficientes.

3. **📊 Divisão dos Dados**  
   Utiliza-se `train_test_split` com `random_state` para separar os dados de forma estratificada entre treino e teste, preservando a proporção das classes e prevenindo o overfitting.

4. **🤖 Treinamento de Modelos Diversos**  
   Foram avaliados diversos algoritmos de classificação, incluindo:
   - **KNN**
   - **Decision Tree**
   - **Random Forest**
   - **Logistic Regression**
   - **SVM**
   - **Redes Neurais (MLPClassifier)**  
   Após comparação, o **Random Forest** se destacou como o modelo com melhor desempenho e estabilidade.

5. **🔍 Otimização com Grid Search**  
   O `GridSearchCV` foi empregado para testar diferentes combinações de hiperparâmetros, buscando maximizar a acurácia e garantir uma configuração ideal para cada modelo avaliado.

6. **📚 Validação Cruzada Estratificada**  
   A robustez dos modelos foi testada com validação cruzada K-Fold estratificada. Isso assegura que o desempenho não está enviesado por uma divisão específica dos dados.

7. **💾 Salvamento do Modelo Final**  
   O modelo Random Forest treinado é salvo em `modelo_rf.pkl` e utilizado posteriormente para predições e testes automatizados com `unittest`.

---

## 📁 Estrutura dos Dados

- **Processed**: Contém o arquivo `dados_processados.pkl`, que é o conjunto de dados após o pré-processamento. Isso inclui tratamento de valores ausentes, codificação de variáveis categóricas e normalização, deixando os dados prontos para a modelagem.
- **Raw**: Contém o arquivo `dataset_info.md`, que fornece informações detalhadas sobre o conjunto de dados original, incluindo descrições dos atributos, a fonte dos dados e as referências para citação. Este arquivo é útil para compreender a estrutura dos dados antes do pré-processamento.
- **Model**: Contém o modelo Random Forest treinado e otimizado, incluído no arquivo `modelo_rf.pkl`,  para uso futuro. O modelo podem ser facilmente carregado para fazer previsões sem a necessidade de re-treinar o algoritmo.

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

## 📝 Licença
Este projeto está licenciado sob os termos do Repositório de Aprendizado de Máquina da UCI. Consulte o arquivo `dataset_info.md` para mais detalhes.

Este projeto é distribuído sob a licença [MIT](LICENSE).


## 🤝 Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request.


## ✨ Agradecimentos
- UCI Machine Learning Repository pela disponibilização do dataset.
