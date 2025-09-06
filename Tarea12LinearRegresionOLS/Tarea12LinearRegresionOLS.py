### Linear regresion and least squares (OLS) regression
### Regresión lineal y regresión por mínimos cuadrados (OLS)


# Import library and read data with pandas 
# Importar la librería y leer los datos con pandas

import pandas as pd


#Via

CO2Data = pd.read_csv("C:/Users/goliv/Documents/GitHub datos/Terminos_lagoon_TA_DIC_2023_RawData.csv")


##Scatter plot with linear regretion = scipy.stats.linregress
##Gráfico de dispersión con regresión lineal = scipy.stats.linregress
# Regresión lineal para dos variables (pendiente e independiente). Calcula la pendiente, la intersección, R cuadrado, valor p, error estándar. 



## Llamar librerías grafica (matplotlib) y estadística (scipy.stats)
 
import matplotlib.pyplot as plt
from scipy import stats


# Definir variables "x" y "y"

x = CO2Data['ta_micromol_kg']
y = CO2Data['dic_micromol_kg']



# Plotear gráfico de dispersión

plt.scatter(x, y, label='original data')



# Agregar etiquetas a los ejes

plt.xlabel('TA ($\mu mol  \; kg^{-1}$)', fontsize = 12, )

plt.ylabel('DIC ($\mu mol  \; kg^{-1}$)', fontsize = 12)



# Calcular la linea de regresión lineal

slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)



# Plotear la regresión lineal 

plt.plot(x, intercept + slope*x, 'r', label='fitted line')


# Ajustar tamaño de la figura

plt.gcf().set_size_inches(6, 4)



# Guardar el grafico como PDF 
# Funcion import, os para carpetas
# Directorio 
# os.makedirs crea la carpeta si no existe
 
import os
output_dir = '../output_files'
os.makedirs(output_dir, exist_ok=True)
plt.savefig(os.path.join(output_dir, 'DIC_TA_pH.pdf'), dpi=300, bbox_inches='tight')


#*Veridicar donde guardo el archivo

import os
print(os.path.abspath(output_dir))
# "C:\Users\goliv\AppData\Local\Programs\Python\output_files"


#Mostrar el plot
plt.show()


# Mostrar el valor de la pendiente en la consola
print('Slope:', slope)
# Slope: 0.9329743239047245


#Muestra el valor de R cuadrado, valor p, pendiente, e intercepto

print("r-squared:", r_value**2)
# r-squared: 0.7784247010713174

print("p_value:", p_value)
# p_value: 8.179416835110045e-36

print("slope:", slope)
# slope: 0.9329743239047245

print("intercept:", intercept)
# intercept: 80.30614134209554


_________________________________________________________________________

### Perform least squares (OLS) regression: scipy.stats.linregress
### Realizar la regresión de mínimos cuadrados ordinarios (OLS): scipy.stats.linregress

## Regresión lineal simples o multiple
# Incluye valores p, intervalos de confianza y pruebas de diagnostico, 


# Llamar paquetes. starmodels y numpy para estadística para 

import statsmodels.api as sm

import numpy as np



# Definir las variables pendiente e independiente (x y y)

x = CO2Data['ta_micromol_kg']

y = CO2Data['dic_micromol_kg']


# Agregar una contante para incluir un intercepto al modelo
# Es OBLIGATORIO ingresar el valor, ya que de lo contratio el modelo asume que la linea de regresión pasa por el origen (intercepto = 0) 

x = sm.add_constant(x)



#  Ajustar el modelo de regresión lineal de minimos cuadrados ordinarios (OLS)

model = sm.OLS(y, x).fit()


# Mostrar el resumen del modelo

print(model.summary())



#                            OLS Regression Results
#==============================================================================
#Dep. Variable:        dic_micromol_kg   R-squared:                       0.778
#Model:                            OLS   Adj. R-squared:                  0.776
#Method:                 Least Squares   F-statistic:                     365.4
#Date:                Wed, 03 Sep 2025   Prob (F-statistic):           8.18e-36
#Time:                        17:04:40   Log-Likelihood:                -728.75
#No. Observations:                 106   AIC:                             1462.
#Df Residuals:                     104   BIC:                             1467.
#Df Model:                           1
#Covariance Type:            nonrobust
#==================================================================================
#                     coef    std err          t      P>|t|      [0.025      0.975]
#----------------------------------------------------------------------------------
#const             80.3061    144.021      0.558      0.578    -205.292     365.905
#ta_micromol_kg     0.9330      0.049     19.115      0.000       0.836       1.030
#==============================================================================
#Omnibus:                       62.113   Durbin-Watson:                   1.542
#Prob(Omnibus):                  0.000   Jarque-Bera (JB):              263.618
#Skew:                          -2.001   Prob(JB):                     5.70e-58
#Kurtosis:                       9.608   Cond. No.                     1.85e+04
#==============================================================================
#
#Notes:
#[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
#[2] The condition number is large, 1.85e+04. This might indicate that there are
#strong multicollinearity or other numerical problems.

# Valores de F estadístico y probabilidad muy significativos


_____________________________________________________________

#Post procesador. Modelo OLS

# Mostrar la interpretación del modelo 

print("\n=== MODEL INTERPRETATION ===\n")


##Evaluar: Calidad del ajuste y el R cuadrado
# ≥ 0.7 → Buen ajuste
# 0.4–0.7 → Ajuste moderado
# < 0.4 → Ajuste débil


r2 = model.rsquared
fit_quality = (
    "✔️ Good model fit: Explains most of the variance." if r2 >= 0.7 else
    "⚠️ Moderate model fit: Explains part of the variance." if r2 >= 0.4 else
    "❌ Weak model fit: Explains little variance. Review your model."
)

print(f"R² = {r2:.3f}\n{fit_quality}")

#R² = 0.778
#✔️ Good model fit: Explains most of the variance.

______________________________________________________________

# Coeficientes y valores p. Tabla de valores.

results = model.summary2().tables[1]

slope_var = results.index.drop('const')[0]  


# Mostrar los coeficientes
print("\nCoefficients:")
for var, row in results.iterrows():
    coef, pval = row['Coef.'], row['P>|t|']
    significance = "✔️ Significant (p < 0.05)" if pval < 0.05 else "⚠️ Not significant (p ≥ 0.05)"
    print(f"- {var}: Coef = {coef:.4f}, p = {pval:.4f} → {significance}")


#Coefficients:
#- const: Coef = 80.3061, p = 0.5783 → ⚠️ Not significant (p ≥ 0.05)
#- ta_micromol_kg: Coef = 0.9330, p = 0.0000 → ✔️ Significant (p < 0.05)
_________________________________________________________________

# Interpretación de la pendiente (Slope)
# calcular pendiente

slope_coef, slope_pval = results.loc[slope_var, ['Coef.', 'P>|t|']]


# Mostrar valor de la pendiente

print(f"\nSlope ({slope_var}): {slope_coef:.4f}, p = {slope_pval:.4f} → "
      f"{'✔️ Significant' if slope_pval < 0.05 else '⚠️ Not significant'}")

#Slope (ta_micromol_kg): 0.9330, p = 0.0000 → ✔️ Significant

__________________________________________________________________________

# Error estandar. Mostrar

print(f"\nStandard Error of the model: {np.sqrt(model.scale):.4f}")

# Standard Error of the model: 236.4180

______________________________________________________________________________________________________________
_____________________________________________________________________________________________________________


### Exercises: perform linear regressions of salinity vs temperature and dec vs salinity.
               realizar regresiones lineales de salinidad vs temperatura y DIC vs salinidad.



## Llamar librerías (grafico y estadístico) 

import matplotlib.pyplot as plt
from scipy import stats

____________________________________________________________________________

## Salinidad vs Temperatura

# Definir variables

x = CO2Data['sal_psu']

y = CO2Data['temp_c']



# Grafico de dispersión

plt.scatter(x, y, label='Original data')



# Agregar etiquetas

plt.xlabel('Salinity (psu)', fontsize=12)

plt.ylabel('Temperature (°C)', fontsize=12)


# Calcular la regresión 

slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)



# Plotear la linea de regresión 

plt.plot(x, intercept + slope*x, 'r', label='Fitted line')


# Ajustar la figura

plt.gcf().set_size_inches(6, 4)



# Mostrar la leyenda de la grafica y asignar título
# Mostrar grafico en la consola

plt.legend()
plt.title("Salinity vs Temperature")
plt.show()

#Mostrar, "Titulo", pendiente, intercepto, R2, y p.value

print("=== Salinity vs Temperature ===")
# === Salinity vs Temperature ===

print("Slope:", slope)
#Slope: -0.028458717486946162

print("Intercept:", intercept)
# Intercept: 27.25200067150795

print("R-squared:", r_value**2)
# R-squared: 0.17749929096684752

print("p-value:", p_value)
p-value: 6.879907520531155e-06

________________________________________________________________________________________


# ## Salinidad vs DIC


# Definir variables

x = CO2Data['sal_psu']

y = CO2Data['dic_micromol_kg']



# Grafico de dispersión

plt.scatter(x, y, label='Original data')



# Agregar etiquetas

plt.xlabel('Salinity (psu)', fontsize=12)

plt.ylabel('DIC ($\mu mol \; kg^{-1}$)', fontsize=12)



# Calcular la regresión 

slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)



# Plotear la linea de regresión 

plt.plot(x, intercept + slope*x, 'r', label='Fitted line')



# Ajustar la figura


plt.gcf().set_size_inches(6, 4)


# Mostrar la leyenda de la grafica y asignar título
# Mostrar grafico en la consola

plt.legend()
plt.title("DIC vs Salinity")
plt.show()


#Mostrar, "Titulo", pendiente, intercepto, R2, y p.value

print("=== DIC vs Salinity ===")
# === DIC vs Salinity ===

print("Slope:", slope)
# Slope: -21.053197646779633

print("Intercept:", intercept)
# Intercept: 3162.874756459312

print("R-squared:", r_value**2)
# R-squared: 0.32710473310227767

print("p-value:", p_value)
# p-value: 1.51441040237653e-10





