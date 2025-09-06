###Explore environmental data using Pandas

##Llamar a "pandas"

import pandas as pd


##Importar datos de calidad de aire
 
CO2Data = pd.read_csv("C:/Users/goliv/Documents/GitHub datos/Terminos_lagoon_TA_DIC_2023_RawData.csv")


##Visializar/Mostrar 

print(CO2Data.info())

#<class 'pandas.core.frame.DataFrame'>
#RangeIndex: 106 entries, 0 to 105
#Data columns (total 21 columns):
# #   Column                   Non-Null Count  Dtype
#---  ------                   --------------  -----
#0   sample                   106 non-null    object
#1   date                     106 non-null    object
#2   estuary                  106 non-null    object
#3   area                     106 non-null    object
#4   station                  106 non-null    object
#5   layer_depth              106 non-null    object
#6   season                   106 non-null    object
#7   chlorophy_microg_l       106 non-null    float64
#8   cond_microsiemens_cm     106 non-null    float64
#9   depth_m                  106 non-null    float64
#10  do_percent_sat           106 non-null    float64
#11  do_mg_l                  106 non-null    float64
#12  sal_psu                  106 non-null    float64
#13  sp_cond_microsiemens_cm  106 non-null    float64
#14  turbidity_fnu            106 non-null    float64
#15  temp_c                   106 non-null    float64
#16  latitude                 106 non-null    float64
#17  longitude                106 non-null    float64
#18  dic_micromol_kg          106 non-null    int64
#19  ta_micromol_kg           106 non-null    int64
#20  dummy_data               99 non-null     float64
#types: float64(12), int64(2), object(7)
#memory usage: 17.5+ KB
#None

_________________________________________________________

#Verificar si MatPlot esta instalado

#python --version Python 3.13.7
#pip --version pip 25.2 from C:

python -m pip install matplotlib



#import matplotlib.pyplot as plt

print("Matplotlib está listo para usar ✅")


#Llamar a MatPlot

import matplotlib.pyplot as plt



#Seleccionar la columna de sal_data (salinidad)

sal_data = CO2Data["sal_psu"]


#Crear un histograma. En intervalos de 10, y nombres en los ejes "x" ("Salinity (PSU)") y "y"("Probabilidad"). Y muestralo

plt.hist(sal_data, bins=10)
plt.xlabel("Salinity (PSU)")
plt.ylabel("Probablity")
plt.show()


#Histograma muestra la frecuencia absoluta de los datos para la variable salinidad
#EJE Y: Valores que caen en ese intervalo

________________________________________________________________________________
###Normalizar nuestras entradas por el número total de conteos

#Plotear el histograma con la densidad (normalizada)
#Seleccionar los datos de sal_data

data = CO2Data["sal_psu"]


#Plotear el histograma, se agrega la función density =TRUE

plt.hist(data, bins=10, density=True)
plt.xlabel("Salinity (PSU)")
plt.ylabel("Probablity")
plt.show()


#Histograma normalizado. Área total bajo las barras de cada rango = 1 (100%)
#EJE Y: Densidad de probabilidad o proporción relativa de los datos

___________________________________________________________________________
###Demostración del grafico de cajas y bigotes (boxplot)

##Creando el plot

#Seleccionar la variable do_mg (oxigeno disuelto)

do_data = CO2Data["do_mg_l"]


#Crear el boxplot. Llama a la función regresando el diccionario de MatPlot

plt.boxplot(do_data)

#{'whiskers': [<matplotlib.lines.Line2D object at 0x000001E25BC9B890>, <matplotlib.lines.Line2D object at 0x000001E25BC9B9D0>], 'caps': [<matplotlib.lines.Line2D object at 
#0x000001E25BC9BB10>, <matplotlib.lines.Line2D object at 0x000001E25BC9BC50>], 'boxes': [<matplotlib.lines.Line2D object at 0x000001E25A497750>], 'medians': [<matplotlib.lines.Line2D 
#object at 0x000001E25BC9BD90>], 'fliers': [<matplotlib.lines.Line2D object at 0x000001E25BC9BED0>], 'means': []}


#Asignarle etiquetas al boxplot. 

plt.xlabel("DO (mg/L)")
plt.ylabel("Concentration")
plt.title("Boxplot of DO Concentration")

#Text(0.5, 1.0, 'Boxplot of DO Concentration')


# Mostrar el plot (boxplot
plt.show()

_____________________________________________________________________________

#Plotear un boxplot con los datos de salinidad

#Seleccionar la columna de salinidad sal_psu

data = CO2Data["sal_psu"]
 


#Con plt.subplot crear subfiguras
#Crear una figura (fig2) y ejes (ax2)

fig2, ax2 = plt.subplots()



#Crear el boxplot. Agregar el titulo (set_title) y con muescas (notch = TRUE)

ax2.set_title('Notched boxes')
ax2.boxplot(data, notch=True)

plt.ylabel('Salinity ($PSU$)', fontsize = 12)
plt.show()

#{'whiskers': [<matplotlib.lines.Line2D object at 0x000001E25BD30E10>, <matplotlib.lines.Line2D object at 0x000001E25BD30F50>], 'caps': [<matplotlib.lines.Line2D object at 
#0x000001E25BD31090>, <matplotlib.lines.Line2D object at 0x000001E25BD311D0>], 'boxes': [<matplotlib.lines.Line2D object at 0x000001E25BD30CD0>], 'medians': [<matplotlib.lines.Line2D 
#object at 0x000001E25BD31310>], 'fliers': [<matplotlib.lines.Line2D object at 0x000001E25BD31450>], 'means': []}


#Agregar etiqueta en el eje y

plt.ylabel('Salinity ($PSU$)', fontsize = 12)


#Mostrar el plot

plt.show()

___________________________________________________________________________________

###Demostración del grafico de cajas y bigotes (boxplot) 2
##Plotear un boxplot para los datos de TA

#Crear un subconjunto de datos con un diccionario (dict) de propiedades y llamarlo green_diamond
# markerfacecolor en g , relleno color verde
# marker d, en forma de diamante
# crear una subfigura con plt.subplots (fig3) y ejes (ax3) donde se dibujará el boxplot


green_diamond = dict(markerfacecolor='g', marker='D')
fig3, ax3 = plt.subplots()



#Titulo del boxplot (ax3)

ax3.set_title('Changed Outlier Symbols')

#Text(0.5, 1.0, 'Changed Outlier Symbols')


#Crear boplot con las indicaciones de verde y diamante usando flierpropos (solo para outliers)

ax3.boxplot(data, flierprops=green_diamond)

#{'whiskers': [<matplotlib.lines.Line2D object at 0x000001E25B8C0F50>, <matplotlib.lines.Line2D object at 0x000001E25B8C1090>], 'caps': [<matplotlib.lines.Line2D object at 
#0x000001E25B79ED50>, <matplotlib.lines.Line2D object at 0x000001E25B79E210>], 'boxes': [<matplotlib.lines.Line2D object at 0x000001E25B8C1310>], 'medians': [<matplotlib.lines.Line2D 
#object at 0x000001E25B844F50>], 'fliers': [<matplotlib.lines.Line2D object at 0x000001E25B844A50>], 'means': []}


#Etiqueta del eje y

plt.ylabel('TA ($\mu mol  \; kg^{-1}$)', fontsize = 12)

#<python-input-17>:1: SyntaxWarning: invalid escape sequence '\m'
#Text(0, 0.5, 'TA ($\\mu mol  \\; kg^{-1}$)')


#Mostrar el grafico

plt.show()


______________________________________________________________________________________________________________

### Exercise. Plot histogram of DIC and TA

# Seleccionar las columnas con los datos de DIC y TA

DIC_data = CO2Data["dic_micromol_kg"]

TA_data = CO2Data["ta_micromol_kg"]


#Crear la figura como subplots. 1 fila y 2 columnas


fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14,7))


#Crear cada histograma

#Histograma de DIC. Ambos serán normalizados usando la función density
# Intervalos de 10
# cada figura con su eje ax1 y ax2
# etiquetas de los ejes x y y , y su titulo

ax1.hist(DIC_data, bins=10, density=True, color='royalblue', edgecolor='black')
ax1.set_xlabel('DIC (µmol kg⁻¹)')
ax1.set_ylabel('Probability')
ax1.set_title('Histogram of DIC')

#Text(0.5, 1.0, 'Histogram of DIC')



#Histograma de TA

ax2.hist(TA_data, bins=10, density=True, color='salmon', edgecolor='black')
ax2.set_xlabel('TA (µmol kg⁻¹)')
ax2.set_ylabel('Probability')
ax2.set_title('Histogram of TA')

#Text(0.5, 1.0, 'Histogram of TA')


#Ya que son dos gráficos lado a lado, se usa la función  plt.tigh_layout() para ajustar el espacio entre las subfiguras evitando el sobrealapamiento de las figuras y títulos

plt.tight_layout()


# Mostrar plot

plt.show()
