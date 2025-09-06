### Estadística no paramétrica. Test de Mann-Whitney U

# Función: Importa archivo csv. 

def import_csv(file):
    # Read the file into a DataFrame: df
    import pandas as pd
    return pd.read_csv(file)
 

# Via 

path = "C:/Users/goliv/Documents/GitHub datos/Terminos_lagoon_TA_DIC_2023_RawData.csv"


# Importar el archivo

co2_data = import_csv(path)

_____________________________________________________________________________________________________________________________
## Prueba de Mann-Whitmey U


# Llamar la función de prueba Mann-Whitney Udesde scipy.stats

from scipy.stats import mannwhitneyu



### Se define la función en base a 3 argumentos. data1 y data2 los grupos a analizar (teóricamente pareados) y el alpha indica el nivel de significancia con un 0.05 (5%) por defecto.
## Se adjunta un docstring debajo de la función (explica la función)
# resultado de la prueba. Argumento "two-sided" para indicar bilateral, es decir, son distintos (en ambas direcciones) los grupos de datos comparados. Puede usar "less" (primer grupo menor al segundo) o "greater" (primer grupo es mayor al segundo) indicando unilateral (izquierda y derecha, respectivamente). 

## Mostrar los resultados de la prueba
# f-sting en este caso permite agregar variables
# Toma de decisión usando el p.value


def mann_whitney_test(data1, data2, alpha=0.05):
    """
    Performs the Mann-Whitney U test and prints U statistic, p-value, and result.
    """
    result = mannwhitneyu(data1, data2, alternative='two-sided')
    
    print(f"U statistic = {result.statistic}")
    print(f"p-value = {result.pvalue}")

    if result.pvalue < alpha:
        print("The difference is statistically significant.")
    else:
        print("The difference is not statistically significant.")


_____________________________________________________________________________________________________________________

## Plotear el boxplot por de TA por estación
# Llamar las librerías de grafico


import seaborn as sns

import matplotlib.pyplot as plt



## Crear un boxplot
#sns.boxplot() función del diagrama
# variable x es "season" y variable y "ta" 

sns.boxplot(x='season', y='ta_micromol_kg', data=co2_data)

#sns.swarmplot(x='season', y='sal_psu', data=co2_data, color=".25")
#* waeplot seria un segunda grafico de puntos en dispersión sobre el boxplot



# Agregar etiquetas y título

plt.xlabel('Season')

plt.ylabel('TA (μmol/kg)')

plt.title('Box Plot of TA by Season')



# Mostrar el plot

plt.show()

______________________________________________________________________________________________________________

## Plotear un boxplot de salinidad por estación

# Llamar librerías de gráficos

import seaborn as sns

import matplotlib.pyplot as plt


# Crear el boxplot con variables x como "season", y como "sal". 
# En este caso si se agregar el warplot. Cada punto refleja una observación 
# Quartiles en boxplot y observaciones reales en puntos dispersos
# .25 indica un color "gris" en particular

sns.boxplot(x='season', y='sal_psu', data=co2_data)


# Agregar etiquetas y título

plt.xlabel('Season')

plt.ylabel('Salinity (PSU)')

plt.title('Box Plot of Salinity by Season')


# Mostrar el plot

plt.show()

_______________________________________________________________________________________________________________

## Filtrar los datos de salinidad por estación 

# sal_dry: valores de salinidad solo para la estación seca (Dry)
# sal_rainy: valores de salinidad solo para la estación seca (Rainy)
# .loc después del dataframe se una como "accesor" en pandas para seleccionar filas y columnas con etiquetas 
# Se producen dos series de datos, una para cada estación las cuales se pueden comparar

sal_dry = co2_data.loc[co2_data["season"] == "Dry", "sal_psu"]
sal_rainy = co2_data.loc[co2_data["season"] == "Rainy", "sal_psu"]



# Realizar la prueba de Mann-Whitney u para la salinidad comparando las estaciones seca y lluviosa

mann_whitney_test(sal_dry, sal_rainy)

#U statistic = 1660.0
#p-value = 0.003199701027350606
#The difference is statistically significant.

_________________________________________________________________________________________________________________

## Crear un Boxplot en forma de violin 

# Llamar las librerías de gráficos 

import seaborn as sns

import matplotlib.pyplot as plt


# Crear un Boxplot, variable x con "season", variable y con "sal"
# sns.violinplot forma de violin en el boxplot

sns.violinplot(x='season', y='sal_psu', data=co2_data)


# Agregar etiquetas y título

plt.title('Salinity Distribution by Season')

plt.xlabel('Season')

plt.ylabel('Salinity (PSU)')


# Mostrar el plot

plt.show()

_____________________________________________________________________________________________
###EXERSICE

## Evaluate the Mann-Whitney U test for DIC and temperatura. Create boxplots and violin plots for these analyses

## Evalúa la prueba U de Mann-Whitney para DIC y temperatura. Crea diagramas de caja (boxplots) y de violín (violin plots) para estos análisis

## Se realizará nuevamente por estación para cada variable

# Filtrar los datos por season (dry y rainy) para DIC y ta


#dic

dic_dry = co2_data.loc[co2_data['season'] == 'Dry', 'dic_micromol_kg']

dic_rainy = co2_data.loc[co2_data['season'] == 'Rainy', 'dic_micromol_kg']


#temperature

temp_dry = co2_data.loc[co2_data['season'] == 'Dry', 'temp_c']  

temp_rainy = co2_data.loc[co2_data['season'] == 'Rainy', 'temp_c']





# Aplicar prueba Mann-Whitney U para DIC y ta

#dic

mann_whitney_test(dic_dry, dic_rainy)

#U statistic = 1942.5
#p-value = 1.1746695070093671e-06
#The difference is statistically significant.



# ta

mann_whitney_test(temp_dry, temp_rainy)

#U statistic = 551.0
#p-value = 5.317160670684041e-06
#The difference is statistically significant.

___________________________________________________________________________________

### Crear Boxplots clásicos y en forma de violin de DIC y ta
_________________________________________________________________________________

# Plotear Boxplot para DIC y ta


# Llamar librerías de gráficos

import seaborn as sns

import matplotlib.pyplot as plt



# Plotear boxplot de DIC

sns.boxplot(x='season', y='dic_micromol_kg', data=co2_data)


# Agregar etiquetas y título

plt.xlabel('Season')

plt.ylabel('DIC')

plt.title('Boxplot of DIC_micromol_kg by Season')



# Mostrar plot

plt.show()


______________________


# Plotear boxplot de DIC

sns.boxplot(x='season', y='temp_c', data=co2_data)


# Agregar etiquetas y título

plt.xlabel('Season')

plt.ylabel('Temperature')

plt.title('Boxplot of Temperature by Season')



# Mostrar plot

plt.show()

_________________________________________________________________________________

## Plotear Boxplot en forma de violin para DIC y ta


# Plotear Boxplot en forma de violin para DIC

sns.violinplot(x='season', y='dic_micromol_kg', data=co2_data)



# Agregar etiquetas y título

plt.xlabel('Season')


plt.ylabel('DIC')


plt.title('Violin plot of DIC_micromol_kg by Season')



# Mostrar plot

plt.show()


_______________


# Plotear Boxplot en forma de violin para ta

sns.violinplot(x='season', y='temp_c', data=co2_data)



# Agregar etiquetas y título

plt.xlabel('Season')

plt.ylabel('Temperature')

plt.title('Violin plot of Temperature by Season')



# Mostrar plot

plt.show()


