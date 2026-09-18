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

# 5. Transformación de datos: Promedio y Aprobados
df['promedio'] = df[['math score', 'reading score', 'writing score']].mean(axis=1)

# Se considera aprobado si la nota es >= 60 en todas las materias
df['aprobado'] = (df['math score'] >= 60) & (df['reading score'] >= 60) & (df['writing score'] >= 60)

print("\n--- DATASET CON PROMEDIO Y ESTATUS ---")
print(df[['math score', 'reading score', 'writing score', 'promedio', 'aprobado']].head())

# 6. Agrupaciones y comparativas
print("\n--- PROMEDIO POR GÉNERO ---")
print(df.groupby('gender')[['math score', 'reading score', 'writing score', 'promedio']].mean())

print("\n--- IMPACTO DEL CURSO DE PREPARACIÓN ---")
print(df.groupby('test preparation course')['promedio'].mean())