### Spearman's Correlation Matrix
### Matriz de correlación de Spearman


# Leer los datos del archivo csv
# Llamar a pandas

import pandas as pd

CO2Data = pd.read_csv("C:/Users/goliv/Documents/GitHub datos/Terminos_lagoon_TA_DIC_2023_RawData.csv")


# Seleccionar columnas de "ta" y "DIC"

ta_sal_dic_df = CO2Data[['sal_psu', 'ta_micromol_kg', 'dic_micromol_kg']]



# Mostrar las 5 primeras filas de cada variable

print(ta_sal_dic_df.head())



# Calcular la matriz de correlación de Spearman 

corr_matrix = ta_sal_dic_df.corr(method='spearman')



# Plotear la matriz de correlación de Sperman
# Llamar libererias de gráficos y estadístico 

import matplotlib.pyplot as plt

import seaborn as sns

# Plotear  un grafico de calot
# Definir aspectos de la figura
 
plt.figure(figsize=(8, 6))
sns.set(style="white", font_scale=1.2)
sns.heatmap(corr_matrix, 
            annot=True, 
            fmt=".2f", 
            cmap='cividis', 
            square=True, 
            linewidths=0.5, 
            linecolor='gray',
            cbar_kws={'shrink': 0.8})

# Leyenda del título y ajustar los margenes
plt.title('Spearman Correlation Matrix', fontsize=14, weight='bold')
plt.tight_layout()


#Mostrar el gráfico 
plt.show()




