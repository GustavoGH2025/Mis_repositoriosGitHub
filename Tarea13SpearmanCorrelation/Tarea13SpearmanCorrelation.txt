### Spearman's Correlation
### Correlación de Spearman


# Importar el archivo con pandas

import pandas as pd


# Cargar directamente de la via 

CO2Data = pd.read_csv("C:/Users/goliv/Documents/GitHub datos/Terminos_lagoon_TA_DIC_2023_RawData.csv")


# Importar stats de scipy

from scipy import stats


### Definir la función: 
## Prueba de Sperman con dos variables númericas a comparar
## alpha por default de 0.05
# if len: analiza que ambas muestras tengan la misma cantidad de observaciones
# rho es el coeficiente de correlación (-1 a 1)
# pval valor p asociado a la prueba de hipótesis 
# Test de decisión con el alfa: Relación es o no significante, correlación positiva o negativa  


def test_spearman(x, y, alpha=0.05):
    if len(x) != len(y):
        raise ValueError("Las variables deben tener la misma longitud.")

    rho, pval = stats.spearmanr(x, y)

    print(f"Spearman's correlation coefficient (rho): {rho:.3f}")
    print(f"p-value: {pval:.4f}")

    if pval < alpha:
        print(f"✔️ Significant relationship (p < {alpha:.3f})")
    else:
        print(f"⚠️ No significant relationship (p ≥ {alpha:.3f})")

    if rho > 0:
        print("📈 Positive correlation")
    else:
        print("📉 Negative correlation")


### Si el p.value no es significante se puede asumir una correlación nula



# Llamar la función y aplicarla a dos variables (ta y DIC) del dataframe

test_spearman(CO2Data["ta_micromol_kg"], CO2Data["dic_micromol_kg"])


##Spearman's correlation coefficient (rho): 0.838
#Correlación fuerte  y positiva

##p-value: 0.0000
# El valor es tan bajo que la probabilidad de que obtener esta correlación por azar es prácticamente nula

##✔️ Significant relationship (p < 0.050)
# Se rechaza la HO 

##?? Positive correlation
# Relación en una misma dirección (positiva) para ambas variables

_____________________________________________________________________________________________________________
_____________________________________________________________________________________________________________


### Exercise: Create a function to compute the Pearson correlation
              Crear una función para calcular la correlación de Pearson


# Importar stats

from scipy import stats



# Definir la función 

def test_pearson(x, y, alpha=0.05):
    if len(x) != len(y):
        raise ValueError("Las variables deben tener la misma longitud.")
    
    r, pval = stats.pearsonr(x, y)
    
    print(f"Pearson correlation coefficient (r): {r:.3f}")
    print(f"p-value: {pval:.4f}")
    
    if pval < alpha:
        print(f"✔️ Significant relationship (p < {alpha:.3f})")
    else:
        print(f"⚠️ No significant relationship (p ≥ {alpha:.3f})")
    
    if r > 0:
        print("📈 Positive correlation")
    else:
        print("📉 Negative correlation")



## Llamar la función para analizar la correlación ente el oxigeno disuelto y la turbidez

test_pearson(CO2Data["do_mg_l"], CO2Data["turbidity_fnu"])


## Pearson correlation coefficient (r): -0.084
# La correlación es muy débil y negativa

##p-value: 0.3939
# Muy superior al 0.05 indicando no significancia

⚠️ No significant relationship (p ≥ 0.050)
# No se rechaza la HO, la relación podría ser nula

?? Negative correlation
# Correlación negativa, van en direcciones opuestas, aunque sin un efecto significativo una sobre la otra 



