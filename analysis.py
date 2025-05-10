import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Cargar el CSV
df = pd.read_csv("International_Education_Costs.csv")

# Mostrar las primeras filas
head = df.head()
print(head)

# Verificar si hay valores nulos
sum_null_data = df.isnull().sum()
print("Cantidad de valores nulos por columna")
print(sum_null_data)


# Convertir columnas numéricas a tipo float o int
numeric_cols = ['Tuition_USD', 'Living_Cost_Index', 'Rent_USD', 'Visa_Fee_USD', 'Insurance_USD']
for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Rellenar valores nulos con 0 o con la media
df[numeric_cols] = df[numeric_cols].fillna(0)

# Resumen estadístico
statistic_summary = df.describe()
print(statistic_summary)

# Gráfics

plt.figure(figsize=(10,6))

# Histograma de matrículas
sns.histplot(df['Tuition_USD'], bins=30, kde=True)
plt.title('Distribución de Matrículas')
plt.xlabel('Matrícula (USD)')
plt.ylabel('Frecuencia')
plt.show()

## PREGUNTAS CLAVE