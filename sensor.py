import random
import numpy as np

class Sensor:
    """
    Clase que representa un sensor físico (temperatura, torque, velocidad).
    Genera lecturas aleatorias basadas en una distribución normal controlada.
    """
    def __init__(self, nombre, media, desviacion):
        self.nombre = nombre
        self.media = media
        self.desviacion = desviacion
        self.valor_actual = None

    def leer(self):
        """Genera una lectura simulada del sensor."""
        self.valor_actual = round(np.random.normal(self.media, self.desviacion), 2)
        return self.valor_actual

    def __repr__(self):
        return f"{self.nombre}: {self.valor_actual}"
