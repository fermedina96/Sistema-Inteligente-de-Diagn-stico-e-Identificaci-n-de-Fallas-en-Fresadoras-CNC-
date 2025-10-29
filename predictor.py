from src.predictor import PredictiveModel
modelo = PredictiveModel()
modelo.entrenar("data/ai4i2020.csv")

from sklearn.metrics import classification_report
print(classification_report(y_test, y_pred))
