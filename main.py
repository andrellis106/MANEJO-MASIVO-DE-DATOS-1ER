import pandas as pd
import matplotlib.pyplot as plt

# 1. Cargar el dataset
df = pd.read_csv('StudentsPerformance.csv')

# 2. Ver las primeras filas
print("--- PRIMERAS FILAS DEL DATASET ---")
print(df.head())

# 3. Información general de las columnas y tipos de datos
print("\n--- INFORMACIÓN DEL DATASET ---")
print(df.info())

# 4. Estadísticas descriptivas de las puntuaciones
print("\n--- ESTADÍSTICAS DESCRIPTIVAS ---")
print(df.describe())