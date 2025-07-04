import os
import joblib
import unittest
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd

# Caminhos relativos ao diretório do projeto
CAMINHO_DADOS = os.path.join("..", "data", "processed", "dados_processados.pkl")
CAMINHO_MODELO = os.path.join("..", "data", "model", "modelo_rf.pkl")

class TestRandomForestMushroomDetection(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Carregar dados processados
        if not os.path.exists(CAMINHO_DADOS):
            raise FileNotFoundError(f"Arquivo de dados não encontrado: {CAMINHO_DADOS}")
        cls.data = joblib.load(CAMINHO_DADOS)

        if 'classe' not in cls.data.columns:
            raise KeyError("A coluna 'classe' não foi encontrada nos dados.")

        # Separar X e y
        cls.X = cls.data.drop("classe", axis=1)
        cls.y = cls.data["classe"]

        # Dividir treino/teste
        cls.X_train, cls.X_test, cls.y_train, cls.y_test = train_test_split(
            cls.X, cls.y, test_size=0.2, random_state=42
        )

        # Treinar modelo
        cls.modelo_rf = RandomForestClassifier(n_estimators=100, random_state=42)
        cls.modelo_rf.fit(cls.X_train, cls.y_train)

        # Salvar modelo treinado
        joblib.dump(cls.modelo_rf, CAMINHO_MODELO)

    def test_accuracy_minima(self):
        """✅ Teste se a acurácia é maior ou igual a 0.95"""
        preds = self.modelo_rf.predict(self.X_test)
        acc = accuracy_score(self.y_test, preds)
        self.assertGreaterEqual(acc, 0.95, f"Acurácia abaixo do esperado: {acc:.2f}")

    def test_modelo_salvo_e_carregado(self):
        """✅ Teste se o modelo salvo pode ser carregado corretamente"""
        self.assertTrue(os.path.exists(CAMINHO_MODELO), "Arquivo do modelo salvo não existe.")
        modelo_carregado = joblib.load(CAMINHO_MODELO)

        # Verifica se as previsões são iguais
        preds_original = self.modelo_rf.predict(self.X_test[:5])
        preds_carregado = modelo_carregado.predict(self.X_test[:5])
        np.testing.assert_array_equal(preds_original, preds_carregado, "Predições do modelo carregado não batem com o original.")

    def test_input_de_predicao_realista(self):
        """✅ Teste com uma amostra realista usando a própria base de dados"""
        # Usa uma linha real dos dados como amostra de input
        amostra_real = self.X_test.iloc[[0]]
        pred = self.modelo_rf.predict(amostra_real)
        self.assertIn(pred[0], [0, 1], "Predição fora do esperado (0 ou 1).")

    def test_dados_integridade(self):
        """✅ Verifica se os dados carregados têm integridade"""
        self.assertIsNotNone(self.data, "Dados não carregados.")
        self.assertGreater(len(self.data), 0, "Dataset está vazio.")
        self.assertIn("classe", self.data.columns, "Coluna 'classe' não encontrada.")

if __name__ == "__main__":
    unittest.main()
