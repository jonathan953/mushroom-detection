import unittest
import joblib
import os
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

class TestMushroomDetection(unittest.TestCase):

    def setUp(self):
        # Caminho para o arquivo de dados processados (.pkl salvo com joblib)
        self.data_path = './data/processed/dados_processados.pkl'
        
        # Tenta carregar o arquivo .pkl com joblib
        try:
            self.data = joblib.load(self.data_path)  # Carrega o dataset pré-processado
        except FileNotFoundError:
            # Se o arquivo de dados não for encontrado, o teste falha
            self.fail(f"Arquivo não encontrado: {self.data_path}")
        except Exception as e:
            # Se houver qualquer outro erro durante o carregamento, o teste falha
            self.fail(f"Erro ao carregar arquivo: {e}")
        
        # Definir a coluna alvo (variável dependente) que contém a classe de cogumelos
        target_column = 'classe'
        
        # Verificar se a coluna alvo está presente e dividir os dados em X (features) e y (target)
        try:
            self.X = self.data.drop(target_column, axis=1)  # Remove a coluna alvo dos dados
            self.y = self.data[target_column]  # Extrai a coluna alvo
        except KeyError:
            # Se a coluna 'classe' não estiver nos dados, o teste falha
            self.fail(f"A coluna '{target_column}' não foi encontrada nos dados.")

        # Divide os dados em treino (80%) e teste (20%)
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            self.X, self.y, test_size=0.2, random_state=42  # random_state garante a reprodutibilidade
        )
        
        # Criar e treinar o modelo SVM com os melhores hiperparâmetros encontrados
        self.model_svm = SVC(C=1.0, kernel='rbf', tol=0.001)
        self.model_svm.fit(self.X_train, self.y_train)
    
    def test_svm_accuracy(self):
        # Testa o modelo SVM e verifica sua acurácia
        try:
            predictions = self.model_svm.predict(self.X_test)  # Faz previsões no conjunto de teste
            accuracy = accuracy_score(self.y_test, predictions)  # Calcula a acurácia das previsões

            # Verifica se a acurácia é maior ou igual a 90%. Se não, o teste falha.
            self.assertGreaterEqual(accuracy, 0.9, "Acurácia do SVM é inferior ao esperado.")
        except Exception as e:
            # Se houver qualquer erro durante a previsão, o teste falha
            self.fail(f"Falha ao fazer previsões ou calcular acurácia: {e}")

    def test_data_integrity(self):
        # Verifica se os dados foram carregados corretamente
        self.assertIsNotNone(self.data, "Falha ao carregar o dataset.")  # Verifica se o dataset foi carregado
        self.assertGreater(len(self.data), 0, "O dataset está vazio.")  # Verifica se o dataset não está vazio
        self.assertIn('classe', self.data.columns, "Coluna 'classe' não está presente nos dados.")  # Verifica se a coluna 'classe' existe

    def test_model_loading(self):
        # Verifica se o modelo salvo pode ser carregado corretamente
        model_path = './data/model/modelo_svm.pkl'  # Caminho para o arquivo do modelo salvo
        if os.path.exists(model_path):
            try:
                # Carrega o modelo SVM salvo
                model_svm = joblib.load(model_path)
                self.assertIsNotNone(model_svm, "O modelo SVM não foi carregado corretamente.")
            except Exception as e:
                # Se houver erro ao carregar o modelo, o teste falha
                self.fail(f"Falha ao carregar o modelo: {e}")
        else:
            # Pula o teste se o modelo salvo não for encontrado
            self.skipTest(f"Modelo salvo não encontrado no caminho: {model_path}")

if __name__ == '__main__':
    unittest.main()
