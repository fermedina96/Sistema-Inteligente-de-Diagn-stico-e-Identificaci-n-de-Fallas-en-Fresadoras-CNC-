import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from imblearn.combine import SMOTETomek
import joblib


class PredictiveModel:
    """
    Modelo predictivo de mantenimiento para fresadoras CNC.
    Entrena y guarda un modelo supervisado para clasificación de fallas.
    """
    def __init__(self):
        self.model = None
        self.scaler = StandardScaler()

    def entrenar(self, ruta_dataset):
        df = pd.read_csv(ruta_dataset)
        X = df[['Air temperature [K]', 'Process temperature [K]', 'Torque [Nm]', 'Tool wear [min]']]
        y = df['Machine failure']

        # Normalización y balanceo
        X_scaled = self.scaler.fit_transform(X)
        smt = SMOTETomek(random_state=42)
        X_res, y_res = smt.fit_resample(X_scaled, y)

        X_train, X_test, y_train, y_test = train_test_split(X_res, y_res, test_size=0.2, random_state=42)
        self.model = RandomForestClassifier(class_weight='balanced', random_state=42)
        self.model.fit(X_train, y_train)
        joblib.dump(self.model, 'modelo_fresadora.pkl')

    def predecir(self, datos):
        """Recibe un diccionario con lecturas de sensores y predice falla."""
        if not self.model:
            self.model = joblib.load('modelo_fresadora.pkl')

        X = pd.DataFrame([datos])
        X_scaled = self.scaler.transform(X)
        pred = self.model.predict(X_scaled)[0]
        return int(pred)
