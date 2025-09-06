### PRUEBA DE NORMALIDAD

# Función general. Importar el archivo como dataframe

def import_csv(file):
    # Read the file into a DataFrame: df
    import pandas as pd
    return pd.read_csv(file)

# Ruta del documento a importar

path = "C:/Users/goliv/Documents/GitHub datos/Terminos_lagoon_TA_DIC_2023_RawData.csv"


# Importar el archivo 

CO2Data = import_csv(path)

print(CO2Data.head())

#   sample      date     estuary   area station  ...  latitude longitude  dic_micromol_kg  #ta_micromol_kg  dummy_data
#0  CDL01S  5/3/2020  Candelaria  River   CDL01  ...  18.55736 -91.25012             3915            #3863      3685.0
#1  CDL01F  5/3/2020  Candelaria  River   CDL01  ...  18.55722 -91.24990             3698            #3685         NaN
#2  CDL02S  5/3/2020  Candelaria  River   CDL02  ...  18.61007 -91.24410             3724            #3708      3708.0
#3  CDL02F  5/3/2020  Candelaria  River   CDL02  ...  18.61005 -91.24403             3667            #3992      3992.0
#4  CDL03S  5/3/2020  Candelaria  River   CDL03  ...  18.63166 -91.29359             2928            #3023      3023.0

#[5 rows x 21 columns]

____________________________________________________________________________

##Prueba de normalidad de Shapiro
#Si el valor p de la prueba es mayor que α = 0.05, entonces se asume que los datos siguen una distribución normal.”

#Usando la librería de scipy.stats tae la función de Shapiro

from scipy.stats import shapiro


#  Se selecciona la columna de ta_micromol_kg

ta = CO2Data['ta_micromol_kg']


#Prueba de Shapiro en ta. Valor stat (prueba) y p (significancia)

stat, p = shapiro(ta)



# Mostrar el resultado
# f-sting se usa para indicar el numero de decimales para el estadístico y la significancia

print(f'Estadístico= {stat:.5f}, p-valor= {p:.5f}')

#Estadístico= 0.87971, p-valor= 0.00000



##Regla de decisión
#Si p> 0.05, no hay evidencia para rechazar la normalidad -> se asume como normal
#Si p≤ 0.05, hay evidencia para rechazar la normalidad -> no es normal

if p > 0.05:
    print("La distribución es normal (no se rechaza H0)")
else:
    print("La distribución NO es normal (se rechaza H0)")

#La distribución NO es normal (se rechaza H0)

____________________________________________________________________

#Importar la función Shapiro

from scipy.stats import shapiro 



#Seleccionat la columna ta

TA = CO2Data['ta_micromol_kg']


#Aplicar prueba de Shapiro en los datos de TA (renombrada con mayúsculas)

shapiro_results = shapiro(TA)



#***ESTA LINEA ESTA MAL PORQUE NO SE DEFINIO NI STAT NI P
print(f'Statistic= {stat:.5f}, p-value= {p:.5f}')



#COREGIR CON 

print(f'Statistic= {shapiro_results.statistic:.5f}, p-value= {shapiro_results.pvalue:.5f}')

#Statistic= 0.87971, p-value= 0.00000


##Prueba de decisión
#Si p < 0.05 → los datos no son normales (rechazas H₀).
#Si p ≥ 0.05 → los datos son normales (no rechazas H₀).


if shapiro_results.pvalue < 0.05:
    print("The data is not normally distributed (reject H₀).")

else:
    print("The data is normally distributed (fail to reject H₀).")


#The data is not normally distributed (reject H₀).


#Mostrar resultados de la prueba

print(shapiro_results)

#ShapiroResult(statistic=np.float64(0.8797113785286559), pvalue=np.float64(9.07143565709752e-08))


#***NOTAR QUE AMBAS > < EN LAS PRUEBAS DE DECISIÓN SE RESPETAN SOLO QUE ESTAN PLANTEADAS DE OTRA FORMA

_____________________________________________________________________________________________________________


#EXERCISE: Respond to the following question: When is it appropriate to use the Kolmogorov-Smirnov test instead of the Shapiro-Wilk test?

#          Responde a la siguiente pregunta: ¿Cuándo es apropiado usar la prueba de Kolmogorov-Smirnov en lugar de la prueba de Shapiro-Wilk?


#El test de Shapiro-Wilk esta diseñado específicamente para analizar un conjunto de datos y probar si son "normales". Esto significa realizar una prueba y obtener un valor de significancia p que nos indique si siguen una distribución normal. Entre los supuestos en los que se aplica la prueba es que se aplica generalmente a tamaños de muestra pequeños. 

#Por otro lado, el test de Kolmogorov-Smirnov mide a bondad del conjunto de datos. Esto quiere decir determinar como se comportan los datos respecto a una distribución teórica conocida. Por lo que no es exclusivo para medir si se distribuye de manera normal, sino también para distribuciones como la exponencial, Poisson, uniforme, etc. usando la prueba y un valor p entre la distribución de los datos y una distribución teórica. Además, la prueba es más fuerte en muestras de datos grandes. 

#En general, ambas pruebas te indicaran 1) Si no se distribuyen como tal distribución (de manera normal para Shapiro-Wilk, o se parecen a una distribución teórica en Kolmogorov-Smirnov) o que no hay suficiente evidencia para no decir que no se distribuyen a un tipo de distribución teórica. 

_________________________________________________________________________________________________________________________________________________________

# Based on the previous answer, perform the appropriate test to assess normality in the DIC (Dissolved Inorganic Carbon) and Salinity datasets.

# Basado en la respuesta anterior, realiza la prueba apropiada para evaluar la normalidad en los conjuntos de datos de DIC (Carbono Inorgánico Disuelto) y Salinidad.



#Importar shapiro

from scipy.stats import shapiro



# Seleccionar las columnas de DIC y ta

DIC = CO2Data['dic_micromol_kg']
Salinity = CO2Data['ta_micromol_kg']  


# Prueba de Shapiro para cada conjunto de datos

shapiro_DIC = shapiro(DIC)
shapiro_Salinity = shapiro(Salinity)

_____________________________________________________________________________________

# Mostrar resultado de la prueba en DIC

print(f"DIC -> Estadístico= {shapiro_DIC.statistic:.5f}, p-valor= {shapiro_DIC.pvalue:.5f}")

#DIC -> Estadístico= 0.85997, p-valor= 0.00000


#Prueba de decisión 

if shapiro_DIC.pvalue < 0.05:
    print("DIC: La distribución NO es normal (rechazamos H₀)")
else:
    print("DIC: La distribución es normal (no rechazamos H₀)")

#DIC: La distribución NO es normal (rechazamos H₀)

_______________________________________________________________________________________

# Mostrar resultado de la prueba en ta

print(f"\nSalinity -> Estadístico= {shapiro_Salinity.statistic:.5f}, p-valor= {shapiro_Salinity.pvalue:.5f}")

#Salinity -> Estadístico= 0.87971, p-valor= 0.00000


#Prueba de decisión 


if shapiro_Salinity.pvalue < 0.05:
    print("Salinity: La distribución NO es normal (rechazamos H₀)")
else:
    print("Salinity: La distribución es normal (no rechazamos H₀)")

#Salinity: La distribución NO es normal (rechazamos H₀)



###NINGUN CONJUNTO DE DATOS DE CARBONO INORGANICO DISUELTO (DIC) Y SALINIDAD SE DISTRIBUCYEN DE MANERA NORMAL  









