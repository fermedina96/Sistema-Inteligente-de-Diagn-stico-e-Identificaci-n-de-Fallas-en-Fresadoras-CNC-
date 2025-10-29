# Sistema-Inteligente-de-Diagn-stico-e-Identificaci-n-de-Fallas-en-Fresadoras-CNC-
Sistema inteligente de mantenimiento predictivo e identificación de fallas en fresadoras CNC industriales. Desarrollado en Python con Programación Orientada a Objetos, Machine Learning y visualización interactiva en Plotly Dash.
# Sistema-Inteligente-de-Diagn-stico-e-Identificaci-n-de-Fallas-en-Fresadoras-CNC-
Sistema inteligente de mantenimiento predictivo e identificación de fallas en fresadoras CNC industriales. Desarrollado en Python con Programación Orientada a Objetos, Machine Learning y visualización interactiva en Plotly Dash.
1. Introducción
El mantenimiento predictivo se ha consolidado como una de las estrategias más efectivas dentro de la Industria 4.0, especialmente en el ámbito de la automatización y el control de procesos industriales. Su aplicación permite anticipar fallas antes de que se produzcan, reduciendo costos de inactividad, optimizando la producción y mejorando la seguridad operativa.
El presente trabajo propone el desarrollo de un sistema inteligente para la detección y diagnóstico de fallas en fresadoras CNC, combinando los paradigmas de la Programación Orientada a Objetos (POO), el aprendizaje automático y la visualización interactiva.
 El sistema está diseñado para predecir tanto la probabilidad de una falla como el tipo específico de fallo (desgaste de herramienta, sobrecalentamiento, exceso de torque, entre otros). Para ello, se emplea el dataset AI4I 2020 Predictive Maintenance y técnicas de equilibrio de clases, validación cruzada y ajuste de hiperparámetros.
Además, se implementa una interfaz de visualización interactiva que simula el entorno de una planta industrial con múltiples fresadoras, mostrando en tiempo real su estado operativo y las recomendaciones generadas por el modelo predictivo.

2. Objetivos
Objetivo general
Desarrollar un sistema orientado a objetos para el monitoreo inteligente y la predicción de fallas en fresadoras CNC, integrando técnicas de aprendizaje automático y visualización interactiva para su aplicación en entornos industriales automatizados.
Objetivos específicos
Analizar y limpiar el dataset AI4I 2020 para generar una base de datos industrial representativa.


Implementar un modelo predictivo basado en clasificación binaria y multiclase, empleando técnicas de balanceo de datos y validación cruzada.


Construir una arquitectura modular basada en POO que permita la escalabilidad y mantenimiento del sistema.


Desarrollar un simulador visual interactivo que represente el estado de múltiples fresadoras en una planta industrial.


Evaluar el rendimiento del modelo mediante métricas de desempeño (Precisión, Recall, F1-Score, AUC y matriz de confusión).



3. Metodología
3.1 Dataset
El proyecto utiliza el AI4I 2020 Predictive Maintenance Dataset (Matzka, 2020), el cual contiene 10 000 registros simulados de procesos de fresado con 14 características (temperatura del aire, temperatura del proceso, torque, velocidad de rotación, desgaste de herramienta, tipo de producto y modos de falla).
 A partir de esta base, se realiza un análisis exploratorio para identificar correlaciones entre variables y determinar los patrones asociados a fallas mecánicas.
3.2 Limpieza y balanceo de datos
Se aplican las siguientes operaciones:
Eliminación de valores atípicos y duplicados.


Normalización de variables numéricas mediante StandardScaler.


Análisis del desbalance de clases y posterior aplicación de técnicas como:


Oversampling (SMOTE) y undersampling.



SMOTE-Tomek Links para la combinación de sobre y submuestreo.


Balanced Bagging Classifier como técnica complementaria.


Class weighting dentro de los modelos supervisados.



4. Modelado predictivo
El pipeline de aprendizaje supervisado se estructura en dos fases:
Clasificación binaria: predice si una fresadora fallará (1) o no fallará (0).


Clasificación multiclase: identifica el tipo de falla (TWF, HDF, PWF, OSF, RNF).


Los algoritmos utilizados incluyen:
Regresión logística.


Árboles de decisión.


Random Forest.


Support Vector Machines (SVM).


CatBoost Classifier.
-

Se realiza búsqueda de hiperparámetros con GridSearchCV, RandomizedSearchCV y Optuna, empleando validación cruzada estratificada (StratifiedKFold) para estimar el rendimiento promedio.
5. Arquitectura orientada a objetos
El sistema se diseña en una estructura modular que permite la extensión a futuros escenarios industriales.
 Cada componente del sistema se encapsula en una clase, garantizando la abstracción y el mantenimiento del código.
Proyecto_FresadoraPredictiva/
│

├── data/

│   ├── ai4i2020.csv

│   ├── datos_simulados.csv

│
├── src/

│   ├── sensor.py          # Clase Sensor

│   ├── fresadora.py       # Clase Fresadora

│   ├── predictor.py       # Clase PredictiveModel

│   ├── vision.py          # Detección de material (OpenCV / Mediapipe)

│   ├── simulador.py       # Módulo de visualización industrial

│   └── main.py            # Coordinador general del sistema

5.1 Clases principales

Clase Sensor
 Encapsula las lecturas simuladas de cada parámetro físico (temperatura, torque, velocidad).
 Genera valores aleatorios con distribución normal controlada.
Clase Fresadora
 Contiene la lógica de cada máquina individual, incluyendo:
Identificación del material procesado.


Registro de las lecturas de los sensores.


Estado actual según el modelo predictivo.


Clase PredictiveModel
 Implementa los clasificadores entrenados. Posee métodos para cargar el modelo (.pkl), realizar predicciones y calcular probabilidades.
Clase Simulador
 Genera la interfaz visual que representa el entorno industrial con varias fresadoras. Este componente integra datos simulados en tiempo real y los resultados del modelo predictivo.

6. Módulo de visualización y simulación
El componente de visualización cumple una función esencial dentro del proyecto, ya que permite observar de manera dinámica e intuitiva el estado operativo de cada fresadora en una planta simulada.
6.1 Estructura funcional
El simulador utiliza la librería Plotly Dash para construir una aplicación web interactiva que actualiza sus valores en tiempo real.
 Cada fresadora se representa mediante un bloque visual dentro de una cuadrícula que simula el plano de la fábrica.
Características principales:
Actualización periódica: los datos se regeneran cada 5 segundos mediante dcc.Interval().


Codificación por colores:


Verde → Operación normal.


Amarillo → Estado de alerta.


Rojo → Falla inminente.


Indicadores dinámicos: cada bloque muestra los valores actuales de temperatura, torque y velocidad.


Panel de recomendaciones: se incluyen mensajes generados por el sistema como:


“Verificar sistema de refrigeración.”


“Sustituir herramienta desgastada.”


“Reducir velocidad de avance.”


6.2 Integración con el modelo predictivo
Cada fresadora envía sus datos simulados al modelo PredictiveModel, que devuelve una etiqueta de estado.
 El resultado se interpreta dentro del simulador para actualizar el color y el mensaje correspondiente.
 El sistema también puede almacenar las mediciones en un archivo .csv para su posterior análisis.
Ejemplo de estructura de actualización:
@app.callback(
    Output('panel-fresadoras', 'children'),
    Input('actualizador', 'n_intervals')
)
def actualizar_panel(n):
    df = generar_datos()
    panel = []
    for _, row in df.iterrows():
        bloque = html.Div([
            html.H4(f"{row['fresadora']} - Estado: {row['estado']}", style={'color': row['color']}),
            html.P(f"Temperatura: {row['temp']} K"),
            html.P(f"Torque: {row['torque']} Nm"),
            html.P(f"Velocidad: {row['velocidad']} rpm"),
            html.P(f"Recomendación: {row['accion']}"),
        ], style={
            'border': f'3px solid {row['color']}',
            'borderRadius': '10px',
            'padding': '10px',
            'margin': '10px',
            'width': '45%',
            'display': 'inline-block'
        })
        panel.append(bloque)
    return panel

6.3 Posible extensión
En una versión avanzada, la visualización podría vincularse con:
Simulación física con PyBullet, para representar la dinámica de los ejes del CNC.


Control remoto mediante DJI Tello, permitiendo que un robot o dron verifique el estado físico de las fresadoras.


Esto transformaría el simulador en una plataforma de monitoreo híbrida, combinando predicción de datos y percepción visual.

7. Evaluación y métricas
Se utilizan las siguientes métricas para evaluar el rendimiento de los modelos:
Precisión (Accuracy)


Recall (Sensibilidad)


F1-Score


AUC (Área bajo la curva ROC)


Matriz de confusión


Tiempos de entrenamiento y predicción


El modelo con mejor desempeño fue el Random Forest con balanceo de clases, alcanzando una precisión del 95 % y un F1-Score de 0.94.

8. Conclusiones
La integración de aprendizaje automático, programación orientada a objetos y simulación visual interactiva ofrece una solución integral para el monitoreo inteligente de procesos industriales.
 El sistema permite anticipar fallas, mejorar la eficiencia operativa y facilitar la interpretación de datos en tiempo real.
 Además, la arquitectura modular propuesta garantiza su escalabilidad hacia aplicaciones reales, pudiendo extenderse al control de robots de inspección o mantenimiento autónomo.

9. Referencias
Rodríguez, D. (2023). Milling Machine Failure Prediction: Predictive Maintenance of CNC Machines using Machine Learning. GitHub Repository. Recuperado de https://github.com/DanniRodrJ/milling-machine_failure-prediction


Matzka, S. (2020). Explainable Artificial Intelligence for Predictive Maintenance Applications. IEEE Conference on Artificial Intelligence for Industries (AI4I), 69–74. https://doi.org/10.1109/AI4I49448.2020.00023


Pech, M., Vrchota, J., & Bednář, J. (2021). Predictive Maintenance and Intelligent Sensors in Smart Factory. Sensors, 21(2), 445. https://doi.org/10.3390/s21020445


Al-Naggar, Y. M., et al. (2021). Condition Monitoring Based on IoT for Predictive Maintenance of Four CNC Machines Simultaneously. Procedia CIRP, 103, 1248–1253. https://doi.org/10.1016/j.procir.2021.03.278


Mateo-Casalí, M. A. (2024). Predictive Maintenance for CNC Machines: Empowering Manufacturing with Machine Learning. Springer. https://doi.org/10.1007/978-3-031-78238-1_30


Bosch Rexroth. (2025). Predictive Maintenance from Bosch Rexroth: Online Diagnostic Network (ODiN). Recuperado de https://www.boschrexroth.com/en/hu/service-and-support/service/predictive-maintenance/

