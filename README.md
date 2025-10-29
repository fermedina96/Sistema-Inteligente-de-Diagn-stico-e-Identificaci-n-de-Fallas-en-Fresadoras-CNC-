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

