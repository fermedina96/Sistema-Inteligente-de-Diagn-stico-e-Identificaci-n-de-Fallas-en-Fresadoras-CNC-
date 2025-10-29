from src.predictor import PredictiveModel
from src.simulador import iniciar

def main():
    print("Entrenando modelo predictivo...")
    modelo = PredictiveModel()
    modelo.entrenar("data/ai4i2020.csv")
    print("Modelo entrenado y guardado.")
    iniciar()

if __name__ == "__main__":
    main()
