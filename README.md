# international_education_cost_practice

Built just for academic purposes

# Cost of International Education

[Link al dataset](https://www.kaggle.com/datasets/adilshamim8/cost-of-international-education)

## About this file

This file, Cost of International Education, provides a structured overview of the key financial components international students incur when studying abroad. It captures geographic details (country, city, university) alongside program-specific information (program name, degree level, duration) and a comprehensive breakdown of direct and ancillary costs—tuition, living expenses, accommodation, visa fees, insurance, and exchange rates. By standardizing all monetary values to U.S. dollars and including a living-cost index, this dataset enables clear, apples-to-apples comparisons across varied locations and programs.

## Column Descriptions

### Country
Name of the nation where the institution is located (e.g., “Germany”, “Canada”). Used to group and filter cost data by national context.

### City
Urban area or municipality hosting the university (e.g., “Munich”, “Toronto”). Helps analyze cost variations within a country.

### University
Full, official name of the higher-education institution (e.g., “Technical University of Munich”, “University of Toronto”). Enables benchmarking across specific schools.

### Program
Title of the academic course or field of study (e.g., “Master of Computer Science”, “MBA”). Distinguishes costs by discipline and curriculum.

### Level
Degree classification: e.g., “Undergraduate”, “Master’s”, “PhD”, or other certification levels. Facilitates analysis of cost differences by academic tier.

### Duration_Years
Program length in years (integer). Indicates total study time for prorating annual costs or comparing shorter vs. longer programs.

### Tuition_USD
Total academic tuition fee for the entire program, converted into U.S. dollars. Tuition refers to fees charged by institutions for instruction and services.

### Living_Cost_Index
Normalized index reflecting relative day-to- day living expenses (food, transport, utilities), with New York City as the baseline (100). Sourced from global cost-of-living databases.

### Rent_USD
Average monthly cost of student accommodation, in U.S. dollars. Derived from crowdsourced housing-price datasets for consistency.

### Visa_Fee_USD
One-time application fee required for an international student visa, in U.S. dollars. Fees vary by country but generally cover processing and issuance.

### Insurance_USD
Annual health or student insurance cost, in U.S. dollars. Health insurance covers part or all medical expenses during study abroad.

### Exchange_Rate
Number of local currency units per one U.S. dollar at data collection time. Exchange rates are essential for converting local costs into USD for consistent comparison.

Ahora vamos al proyecto.

## Herramientas Necesarias

- Jupyter Notebook  o Google Colab (gratis)
- Librerías básicas: pandas, matplotlib, seaborn
- El archivo .csv cargado localmente

### 1. Introducción al Dataset

```py
import pandas as pd

# Cargar el CSV
df = pd.read_csv("International_Education_Costs.csv")

# Mostrar las primeras filas
df.head()
```

### 2. Limpieza Básica de Datos


```py
# Verificar si hay valores nulos
df.isnull().sum()

# Convertir columnas numéricas a tipo float o int
numeric_cols = ['Tuition_USD', 'Living_Cost_Index', 'Rent_USD', 'Visa_Fee_USD', 'Insurance_USD']
for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Rellenar valores nulos con 0 o con la media
df[numeric_cols] = df[numeric_cols].fillna(0)
```

### 3. Estadística Descriptiva


```py
# Resumen estadístico
df.describe()
```

**Preguntas clave:**

- ¿Cuántos países están representados?
- ¿Qué nivel académico es más común?
- ¿Cuál es el promedio de matrícula?
     

### 4. Visualización Básica

```py
import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(10,6))

# Histograma de matrículas
sns.histplot(df['Tuition_USD'], bins=30, kde=True)
plt.title('Distribución de Matrículas')
plt.xlabel('Matrícula (USD)')
plt.ylabel('Frecuencia')
plt.show()
```

```py
# Boxplot por nivel académico
sns.boxplot(x='Level', y='Tuition_USD', data=df)
plt.title('Matrícula por Nivel Académico')
plt.xlabel('Nivel')
plt.ylabel('Matrícula (USD)')
plt.xticks(rotation=45)
plt.show()
```

## Preguntas clave

### 1- ¿Cuáles son los 5 países con la matrícula promedio más alta?
### 2- ¿Cómo se distribuye la matrícula entre los distintos niveles académicos?
### 3- ¿Qué relación hay entre el índice de costo de vida y la matrícula?
### 4- ¿Cuál es el promedio de alquiler mensual por país?
### 5- ¿Qué programas son los más comunes en el dataset?
### 6- ¿Cuál es el costo total anual promedio por país?
### 7- ¿Qué nivel académico tiene menor duración promedio?
### 8- ¿Cuánto varía el costo de la matrícula dentro de un mismo país?
### 9- ¿Cuál es la correlación entre el tipo de cambio y otros costos?
### 10- ¿Cuál es el costo acumulado para un programa completo

## Conceptos básicos

###  ¿Qué es un Dataset? 

Un dataset  (conjunto de datos) es una colección organizada de información o registros, generalmente dispuesta en filas y columnas. 

- Filas : Representan observaciones individuales (por ejemplo, cada fila podría ser un programa universitario).
- Columnas : Representan características o variables de esas observaciones (por ejemplo, país, universidad, costo de matrícula, etc.).
     
### ¿Qué es un DataFrame? 

En Python (usando la librería pandas), un DataFrame es una estructura de datos bidimensional similar a una tabla de Excel o una base de datos. 

### Valores Null 

Los valores null  representan datos faltantes o ausentes  en el conjunto de datos. 

**¿Por qué importan?**

- Pueden afectar cálculos como promedios o gráficos.
- Se pueden manejar eliminándolos o rellenándolos con valores razonables (como la media).

### Valores Atípicos (Outliers) 

Son valores que se desvían mucho del resto. Por ejemplo, una matrícula de $60,000 cuando el promedio es $10,000. 

**¿Cómo detectarlos?** 

- Usando boxplots
- Calculando percentiles (ej. más allá del 99%)
     

### Tipos de Datos  

- Numéricos : Edad, precio, cantidad (se pueden sumar, promediar, etc.)
- Categóricos : País, nivel académico, programa (representan categorías)

### Conversión de datos

**Variables:**
| Descripción                          | Sintaxis                              | Ejemplo                                                   |
| ------------------------------------ | ------------------------------------- | --------------------------------------------------------- |
| Convertir a entero                   | int(x)                                | numero_float = 3.14159                                    |
|                                      |                                       | numero_entero = int(numero_float)                         |
|                                      |                                       | print(f"Entero: {numero_entero}")                         |
| Convertir a número de punto flotante | float(x)                              | numero_string = "123.45"                                  |
|                                      |                                       | numero_float = float(numero_string)                       |
|                                      |                                       | print(f"Flotante: {numero_float}")                        |
| Convertir a cadena de texto          | str(x)                                | numero_int = 100                                          |
|                                      |                                       | numero_string = str(numero_int)                           |
|                                      |                                       | print(f"Cadena: {numero_string}")                         |
| Convertir a número complejo          | complex(real, imag) o complex(string) | parte_real = 5                                            |
|                                      |                                       | parte_imaginaria = 2                                      |
|                                      |                                       | numero_complejo_1 = complex(parte_real, parte_imaginaria) |
|                                      |                                       | print(f"Complejo 1: {numero_complejo_1}")                 |
|                                      |                                       | string_complejo = "3+4j"                                  |
|                                      |                                       | numero_complejo_2 = complex(string_complejo)              |
|                                      |                                       | print(f"Complejo 2: {numero_complejo_2}")                 |
| Convertir a booleano                 | bool(x)                               | numero_cero = 0                                           |
|                                      |                                       | booleano_cero = bool(numero_cero)                         |
|                                      |                                       | print(f"Booleano de 0: {booleano_cero}")                  |
|                                      |                                       | numero_positivo = 15                                      |
|                                      |                                       | booleano_positivo = bool(numero_positivo)                 |
|                                      |                                       | print(f"Booleano de 15: {booleano_positivo}")             |
| Convertir a hexadecimal (cadena)     | hex(x)                                | numero_decimal = 255                                      |
|                                      |                                       | hexadecimal = hex(numero_decimal)                         |
|                                      |                                       | print(f"Hexadecimal: {hexadecimal}")                      |
| Convertir a binario (cadena)         | bin(x)                                | numero_decimal = 10                                       |
|                                      |                                       | binario = bin(numero_decimal)                             |
|                                      |                                       | print(f"Binario: {binario}")                              |
| Convertir a octal (cadena)           | oct(x)                                | numero_decimal = 64                                       |
|                                      |                                       | octal = oct(numero_decimal)                               |
|                                      |                                       | print(f"Octal: {octal}")                                  |
| Convertir desde hexadecimal (entero) | int(string, 16)                       | hex_string = "0xff"                                       |
|                                      |                                       | decimal_hex = int(hex_string, 16)                         |
|                                      |                                       | print(f"Decimal desde Hex: {decimal_hex}")                |
| Convertir desde binario (entero)     | int(string, 2)                        | bin_string = "0b1010"                                     |
|                                      |                                       | decimal_bin = int(bin_string, 2)                          |
|                                      |                                       | print(f"Decimal desde Bin: {decimal_bin}")                |
| Convertir desde octal (entero)       | int(string, 8)                        | oct_string = "0o100"                                      |
|                                      |                                       | decimal_oct = int(oct_string, 8)                          |
|                                      |                                       | print(f"Decimal desde Oct: {decimal_oct}")                |


**Columnas en *dataframe***

```py
import pandas as pd

# Supongamos que tienes un DataFrame llamado 'df' y una columna llamada 'nombre_columna'

df['nombre_columna'] = df['nombre_columna'].astype(nuevo_tipo)
```
Donde `nuevo_tipo` puede ser:

- `int`: para convertir a entero.
- `float`: para convertir a número de punto flotante.
- `str`: para convertir a cadena de texto.
- `bool`: para convertir a booleano.
- `category`: para convertir a tipo categórico (útil para datos repetitivos).
- `datetime64`: para convertir a formato de fecha y hora.

###  Estadística Descriptiva con .describe() 

La función `describe()` en pandas genera un resumen estadístico rápido de las columnas numéricas. 

**¿Qué muestra?**

| Métrica | Significado |
| ------  | ------      |
| count |	Cantidad de datos no nulos |
| mean |	Promedio |
| std |	Desviación estándar (cómo se dispersan los datos) |
| min / max |	Valor mínimo y máximo |
| 25%, 50%, 75%	 |Cuartiles (valores que dividen los datos en porcentajes) |

### Nociones para Visualización Básica 

Visualizar datos ayuda a entender patrones, tendencias y anomalías. 

**Tipos comunes de gráficos:** 

| Gráfico | Uso |
| ----    | ----|
| Histograma |	Mostrar la distribución de una variable (ej. costo de matrícula) |
| Gráfico de barras |	Comparar categorías (ej. costo promedio por país) |
| Boxplo |t	Ver dispersión y outliers (valores extremos) |
| Scatter plot |	Ver relación entre dos variables (ej. costo vs índice de vida) |