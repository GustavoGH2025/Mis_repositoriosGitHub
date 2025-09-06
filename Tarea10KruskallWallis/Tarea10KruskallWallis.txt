### Estadística No paramétrica. Test de Kruskall-Wallis

# Importar la función

def import_csv(file):
    # Read the file into a DataFrame: df
    import pandas as pd
    return pd.read_csv(file)



# Via 

path = "C:/Users/goliv/Documents/GitHub datos/Terminos_lagoon_TA_DIC_2023_RawData.csv"


# Importar archivo

co2_data = import_csv(path)

_____________________________________________________________________________

### Test de Kruskall-Wallis para muestras independientes


# Importar la función kruskal desde scipy.stats

from scipy.stats import kruskal



# Definir toda la función

def kruskal_wallis_test(*groups, alpha=0.05):
    """
    Performs the Kruskal-Wallis H-test for independent samples.
    Accepts multiple groups as arguments.
    Prints the H statistic, p-value, and interpretation.
    """
    result = kruskal(*groups)
    
    print(f"H statistic = {result.statistic}")
    print(f"p-value = {result.pvalue}")
    
    if result.pvalue < alpha:
        print("The difference between groups is statistically significant.")
    else:
        print("No statistically significant difference between groups.")



# Importar la función scikit_posthocs (pruebas post-hocs para pruebas no paramétricas) 
#* You need to install the scikit-posthocs package: conda install -c conda-forge scikit-posthocs

import scikit_posthocs as sp



# Definir la función 

def dunn_posthoc(data, group_col, value_col, p_adjust='bonferroni'):
    """
    Runs Dunn's post-hoc test after Kruskal-Wallis.
    """
    result = sp.posthoc_dunn(data, val_col=value_col, group_col=group_col, p_adjust=p_adjust)
    print(result)
    return result
___________________________________________________________________________________________________________

## Plotear los valores de ta (alkalinidad total) por cada area de la laguna usando Seaborn 
___________________________________________________________________________________________________________


# Llamar librerías para graficar

import seaborn as sns

import matplotlib.pyplot as plt


# Crear un Boxplot con los datos de ta_micromol_kg

sns.boxplot(x='area', y='ta_micromol_kg', data=co2_data)



# Agregar etiquetas y título

plt.xlabel('Area of the lagoon')

plt.ylabel('Total Alkalinity (micromol/kg)')

plt.title('Total Alkalinity by Area of the Lagoon')



# Mostrar plot

plt.show()


_________________________________________________________________


# Seleccionar los datos de cada area de la laguna 
# Filtrar los datos de ta para "River", "Pluma", y "Coast"

ta_river = co2_data[co2_data['area'] == 'River']['ta_micromol_kg']

ta_plume = co2_data[co2_data['area'] == 'Plume']['ta_micromol_kg']

ta_coast= co2_data[co2_data['area'] == 'Coast']['ta_micromol_kg']



### Realizar la prueba de Kruskall-Wallis

kruskal_wallis_test(ta_river, ta_plume, ta_coast)

#H statistic = 23.340675555846637
#p-value = 8.543517259038796e-06
#The difference between groups is statistically significant.



### Realizar prueba post-hoc de Dunn sobre los datos filtrados de ta

dunn_posthoc(co2_data, 'area', 'ta_micromol_kg')

#          Coast     Plume     River
#Coast  1.000000  1.000000  0.000016
#Plume  1.000000  1.000000  0.000659
#River  0.000016  0.000659  1.000000

# Valores < 0.05 indican diferencias significativas entre las areas de la laguna para la variable ta 

____________________________________________________________________________________________________

Exercise: Perform Kruskal-Wallis test and plot a box plot for DIC and temperature data

         Realiza la prueba de Kruskal-Wallis y grafica un diagrama de caja (boxplot) para los datos de DIC y temperatura.



# Filtrar los datos por area ("River", "Pluma", "Coast") para DIC y temperatura

# DIC

dic_river = co2_data[co2_data['area'] == 'River']['dic_micromol_kg']

dic_plume = co2_data[co2_data['area'] == 'Plume']['dic_micromol_kg']

dic_coast = co2_data[co2_data['area'] == 'Coast']['dic_micromol_kg']



# Temperature

temp_river = co2_data[co2_data['area'] == 'River']['temp_c']

temp_plume = co2_data[co2_data['area'] == 'Plume']['temp_c']

temp_coast = co2_data[co2_data['area'] == 'Coast']['temp_c']




### Realizar prueba Kruskall-Walls a cada conjunto de datos (por estación)


# DIC

kruskal_wallis_test(dic_river, dic_plume, dic_coast)

#H statistic = 55.889669058187486
#p-value = 7.306553461098262e-13
#The difference between groups is statistically significant.



# Temperature

kruskal_wallis_test(temp_river, temp_plume, temp_coast)

#H statistic = 7.6996429549091365
#p-value = 0.021283535690208223
#The difference between groups is statistically significant.


_____________________________________________________________________________

### Boxplots con Seaborn

# Llamar librería para graficar

import seaborn as sns

import matplotlib.pyplot as plt



## Boxplot para DIC

sns.boxplot(x='area', y='dic_micromol_kg', data=co2_data)


# Agregamos etiquetas y título

plt.xlabel('Area of the Lagoon')

plt.ylabel('DIC (micromol/kg)')

plt.title('DIC by Area of the Lagoon')


# Mostrar plot

plt.show()




## Boxplot para Temperature

sns.boxplot(x='area', y='temp_c', data=co2_data)



# # Agregamos etiquetas y título

plt.xlabel('Area of the Lagoon')

plt.ylabel('Temperature (°C)')

plt.title('Temperature by Area of the Lagoon')


# Mostrar plot

plt.show()









