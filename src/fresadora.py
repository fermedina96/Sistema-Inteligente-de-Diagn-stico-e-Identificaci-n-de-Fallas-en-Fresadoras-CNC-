from src.sensor import Sensor
import pandas as pd

class Fresadora:
    """
    Representa una fresadora industrial.
    Contiene sensores y métodos para generar lecturas, evaluar estado y registrar datos.
    """
    def __init__(self, id_fresadora):
        self.id = id_fresadora
        self.sensores = {
            "temperatura": Sensor("Temperatura", 320, 10),
            "torque": Sensor("Torque", 40, 8),
            "velocidad": Sensor("Velocidad", 1500, 100)
        }
        self.estado = "NORMAL"
        self.color = "green"
        self.recomendacion = "Funcionamiento estable"

    def generar_lecturas(self):
        """Lee todos los sensores y actualiza los valores."""
        datos = {nombre: sensor.leer() for nombre, sensor in self.sensores.items()}
        self._evaluar_estado(datos)
        return datos

    def _evaluar_estado(self, datos):
        """Evalúa el estado de la máquina según umbrales físicos."""
        if datos["temperatura"] > 350 or datos["torque"] > 55:
            self.estado, self.color, self.recomendacion = "FALLA", "red", "Detener máquina y revisar herramienta"
        elif datos["temperatura"] > 340 or datos["torque"] > 48:
            self.estado, self.color, self.recomendacion = "ALERTA", "yellow", "Revisar refrigeración y torque"
        else:
            self.estado, self.color, self.recomendacion = "NORMAL", "green", "Funcionamiento estable"

    def __repr__(self):
        return f"Fresadora {self.id}: {self.estado}"
