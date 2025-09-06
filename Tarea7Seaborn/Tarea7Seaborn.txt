###Seaborn: statistical data visualization

##LLamar a pandas

import pandas as pd


#Importar los datos

CO2Data = pd.read_csv("C:/Users/goliv/Documents/GitHub datos/Terminos_lagoon_TA_DIC_2023_RawData.csv")


#Visializar/Mostrar

print(CO2Data.info())

#<class 'pandas.core.frame.DataFrame'>
#RangeIndex: 106 entries, 0 to 105
#Data columns (total 21 columns):
# #   Column                   Non-Null Count  Dtype
#---  ------                   --------------  -----
# 0   sample                   106 non-null    object
# 1   date                     106 non-null    object
# 2   estuary                  106 non-null    object
# 3   area                     106 non-null    object
# 4   station                  106 non-null    object
# 5   layer_depth              106 non-null    object
# 6   season                   106 non-null    object
# 7   chlorophy_microg_l       106 non-null    float64
# 8   cond_microsiemens_cm     106 non-null    float64
# 9   depth_m                  106 non-null    float64
# 10  do_percent_sat           106 non-null    float64
# 11  do_mg_l                  106 non-null    float64
# 12  sal_psu                  106 non-null    float64
# 13  sp_cond_microsiemens_cm  106 non-null    float64
# 14  turbidity_fnu            106 non-null    float64
# 15  temp_c                   106 non-null    float64
# 16  latitude                 106 non-null    float64
# 17  longitude                106 non-null    float64
# 18  dic_micromol_kg          106 non-null    int64
# 19  ta_micromol_kg           106 non-null    int64
# 20  dummy_data               99 non-null     float64
#dtypes: float64(12), int64(2), object(7)
#memory usage: 17.5+ KB
#None

_____________________________________________________


## Cargar las librerías y configurar la figura a crear

import seaborn as sns
import matplotlib.pyplot as plt 


#Crear una lista de colores similar a viridis, "verde" y "azul"

my_colors = ["#5ec962", "#3b528b"]


#Agregar la lista de colores a una "paleta"
# snt.set() Dejar una configuración general prederminad a los graficos en adelante
# font_scale Escala de la fuente en títulos y ejes
# ticks estilo con marcas
# aplicar la plaeta que determinamos con los colores de viridis

sns.set(font_scale=2, style="ticks", palette= my_colors)

____________________________________________________________________________

###Graficar un boxplot con la función CatPlot usando Seaborn

##Funcion

# sns.catplot() Funcion Seaborn para boxplot categóricos
#  Usar area como variable x
# Usar los valores de Ta como variable y
# Colorear los boxplots de acuerdo con la estación ("season")
# Dividir el grafico en columnas de acuerdo a cada estuario (subfiguras)
# Tipo caja (box)


ax = sns.catplot(data=CO2Data,
                 x="area", y="ta_micromol_kg",
                hue="season", col="estuary",
                kind="box", 
                height=7, aspect=1)



# Etiquetas
#Eliminar la etiqueta de x, y en y mostrar una personal

ax.set(xlabel='', ylabel=' TA ($\mu mol \; kg^{-1}$)')

#<python-input-24>:1: SyntaxWarning: invalid escape sequence '\m'
#<seaborn.axisgrid.FacetGrid object at 0x000002B2B32D2E40>



# Títulos de las columnas
# col_template nombre de la columna original
# row_template nombre de la fila original

ax.set_titles(col_template="{col_name}", row_template="{row_name}")


#Ajustar tamaño de la fuente
#plot.set especifico para objetos de Matplotlib

plt.setp(ax._legend.get_title(), fontsize=20)



#Ajustes del grafico
#sns.despine() Eliminar líneas de bordes
# Agregar FALSE para indicar cuales ignorar con sns.despine


sns.despine(top=False,right=False)


#Mostrar plot

plt.show()

___________________________________________________________________________________

### Graficar un diagrama tipo violín con Catplot en Seaborn

#Se modifica principalmente el tipo de grafico de box a violin

ax = sns.catplot(data=CO2Data, 
                x="area", y="ta_micromol_kg",
                hue="season", col="estuary", 
                kind="violin", 
                height=7, aspect=1)


# Se elimina la etiqueta del eje x

ax.set(xlabel='', ylabel=' TA ($\mu mol \; kg^{-1}$)')

#<python-input-31>:1: SyntaxWarning: invalid escape sequence '\m'
#<seaborn.axisgrid.FacetGrid object at 0x000002B2B3D7D450>



#Titulos de las columnas

ax.set_titles(col_template="{col_name}", row_template="{row_name}")

#<seaborn.axisgrid.FacetGrid object at 0x000002B2B3D7D450>


#Tamaño del titulo

plt.setp(ax._legend.get_title(), fontsize=20)



#Eliminar líneas externas expecto la superior y la derecha

sns.despine(top=False, right=False)


#Mostrar el plot

plt.show()

______________________________________________________________________________

### Plotear un ANOVA de 3 vías
# Funcion pointplot
# tipo pointplot Los puntos representan la media de los datos por categoría
                 Barras indican un intervalo de eror (por defecto estal 95%)
#capsize Resalta el error de las barras
#errorbar="se" Utiliza el error estándar de los intervalos de confianza


ax = sns.catplot(
    data=CO2Data, x="season", 
    y="ta_micromol_kg", hue="estuary", col="area",
    capsize=.2, palette="YlGnBu_d", errorbar="se",
    kind="point", height=6, aspect=.75,
)


#Ajustar columnas
#Eliminar la columna izquierda

ax.despine(left=True)

#<seaborn.axisgrid.FacetGrid object at 0x000002B2B7032490>



#Ajustar eitquetas. Eliminar etiqueta del eje x y renombrar el eje y

ax.set(xlabel='', ylabel=' TA ($\mu mol \; kg^{-1}$)')

#<python-input-39>:1: SyntaxWarning: invalid escape sequence '\m'
#<seaborn.axisgrid.FacetGrid object at 0x000002B2B7032490>


#Agregar los nimbres de las areas

ax.set_titles(col_template="{col_name}", row_template="{row_name}")

#<seaborn.axisgrid.FacetGrid object at 0x000002B2B7032490>


#Definir tamaño del titulo

plt.setp(ax._legend.get_title(), fontsize=20)



#Eliminar las líneas excepto la superior y derecha

sns.despine(top=False,right=False)


#Mostrar el plot

plt.show()

___________________________________________________________________________________

###Diagramas de dispersion (regresión lineal): "DIC vs Salinity" en cada estuario
#Se usa la funcion sns.lmplot. Crear un grafico de dispersion con una regresion lineal ajustada 

ax = sns.lmplot(x="sal_psu", y="ta_micromol_kg",
                hue="season",col="estuary",
                data=CO2Data, 
                height=7, aspect=1)



#Ajustar los nombres de los ejes (*CORRECCION ES TA NO DIC)

ax.set(xlabel='Salinity (PSU)', ylabel=' TA ($\mu mol \; kg^{-1}$)')

#<python-input-45>:1: SyntaxWarning: invalid escape sequence '\m'
#<seaborn.axisgrid.FacetGrid object at 0x000002B2B8B49090>



#Aignar títulos a cada subgrafico (en este caso los estuarios)

ax.set_titles(col_template="{col_name}", row_template="{row_name}")

#<seaborn.axisgrid.FacetGrid object at 0x000002B2B8B49090>



#Ajustar tamaño de la leyenda

plt.setp(ax._legend.get_title(), fontsize=20)



#Eliminar líneas del marco excepto superior y derecho

sns.despine(top=False,right=False)



#Mostrar plot

plt.show()

___________________________________________________________________________

###Exercise. How can you modify the units of the figures?


#Se pueden utilizar varios argumentos dentro de la función principal para modificar las unidades de los objetos en Matplotlib y Seaborn

#Asumiendo la misma base de los datos y la función general para un grafico de boxplot categorico. #Tambien aplica en lmplot

#sns.catplot(
#    data=CO2Data, x="area", y="ta_micromol_kg",
#    kind="box",

#Se pueden agregar indicaciones

# 1) height= cambia la altura (pulgadas)
# 2) aspect= modifica la relación entre el ancho vs alto

sns.catplot(
    data=CO2Data, x="area", y="ta_micromol_kg",
    kind="box",
    height=10,    
    aspect=1.5   
)
 

#Dentro de los subfiguras de MatPlotlib se puede asignar valores sobre el default de ancho y alto
#usando figsize= ( , )
#El primer sera ancho (12) y luego el alto (6)

fig, ax = plt.subplots(figsize=(12, 6))  
sns.boxplot(data=CO2Data, x="area", y="ta_micromol_kg", ax=ax)
plt.show()



___________________________________________________________________________________________
___________________________________________________________________________________________

###Check the examples at https://seaborn.pydata.org/ and create your own figures. If possible, use your own data.

###HEATPLOT de abundancias


##Llamar a las librerias

import pandas as pd

import seaborn as sns

import matplotlib.pyplot as plt

#matplotlib.pyplot permite realizar plots mas ordenes mas directas 




## Importar bases de datos

#Base 1. Grafico de lineplot . Abundancias de especies (individual y abundancia total) a traves del tiempo (age, años calibrados antes del presente (~1950))

base1 = pd.read_csv("C:/Users/goliv/Documents/GitHub datos/base1.csv")




#Verificar/Mostrar

print(base1.info())

#<class 'pandas.core.frame.DataFrame'>
#RangeIndex: 97 entries, 0 to 96
#Data columns (total 20 columns):
# #   Column                 Non-Null Count  Dtype
#---  ------                 --------------  -----
# 0   age                    97 non-null     int64
# 1   Leberis                97 non-null     int64
# 2   A_intermedia           97 non-null     int64
# 3   Chydorus               97 non-null     int64
# 4   A_excisa               97 non-null     int64
# 5   A_ossiani              97 non-null     int64
# 6   A_verucosa_pectinata   97 non-null     int64
# 7   A_verrucosa_verrucosa  97 non-null     int64
# 8   Ephemeroporus          97 non-null     int64
# 9   Karualona              97 non-null     int64
# 10  Kurzia                 97 non-null     int64
# 11  Dunhevedia_americana   97 non-null     int64
# 12  Graptoleberis          97 non-null     int64
# 13  Magnospina_dentifera   97 non-null     int64
# 14  Camptocercus           97 non-null     int64
# 15  Pleuxorus              97 non-null     int64
# 16  Euryalona              97 non-null     int64
# 17  Bosmina_sp             97 non-null     int64
# 18  Liederobosmina_sp      97 non-null     int64
# 19  Total_abundance        97 non-null     int64
#dtypes: int64(20)
#memory usage: 15.3 KB
#None



#Mostrar las cabeceras de las columnas

print(base1.head())

#   age  Leberis  A_intermedia  Chydorus  ...  Euryalona  Bosmina_sp  Liederobosmina_sp  Total_abundance
#0  290        0             5         0  ...          0           0                  0               25
#1  344        5            20        15  ...          0           0                  0              125
#2  399        0             5         5  ...          0           0                  0               30
#3  449        0             5         5  ...          0           0                  0               40
#4  501        0             5        10  ...          0           0                  0               20




________________________________________________________________________________________

###Heatplot

# Se seleccionan las especies
#difference deja fuera las columnas de "age" y "Total_abundance"

species_cols = base1.columns.difference(['age', 'Total_abundance'])



#Dado que la edad va de lo mas viejo a lo mas joven, se da el argumento de ordenar con la función "sort" y la indicación de ascendente (ascending) la tabla por edad con lo mas viejo al fondo 
#set_index convierte la columna de edad en un índice de todo el dataframe. Edad como filas y abundancias como columnas


heatmap_data = base1.sort_values('age', ascending=True).set_index('age')[species_cols]



#Funcion
#tamaño
#heatmap como argumento del plot
#cmpap como color
#cbar con eituqeta para las abundancias de las especies
#linewidths = 0, no muestra ningún margen entre las celdas de cada fila o columna


plt.figure(figsize=(12,8))
sns.heatmap(
    heatmap_data,
    cmap='viridis',
    cbar_kws={'label':'Abundancia total'},
    linewidths=0  # sin bordes entre celdas
)


#Etiquetas y título 

plt.ylabel('Edad (años cal. AP)')

plt.xlabel('Especies')

plt.title('Abundancia de todas las especies de cladoceros vs Edad (años cal. AP)')



#Mostrar grafico

plt.show()



