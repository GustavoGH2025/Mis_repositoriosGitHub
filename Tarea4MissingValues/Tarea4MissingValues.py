###VERIFICAR SI ESTA INSTALADO EN POWERSHELL


#pandas y openpyxl 

pip install pandas
pip install openpyxl


###IMPORTAR CSV###

def import_csv(file):
    # Read the file into a DataFrame: df
    import pandas as pd
    return pd.read_csv(file)

# Path to the file to be imported
path = "C:/Users/goliv/Documents/GitHub datos/Terminos_lagoon_TA_DIC_2023_RawData.csv"



# Import the file
CO2Data = import_csv(path)


###EXPLOTAR LOS DATOS DEL CSV O DATAFRAME###

print(CO2Data.shape)

#(106,21)

#VERIFICAR

print(CO2Data.head())

#   sample      date     estuary   area station  ...  latitude longitude  dic_micromol_kg  ta_micromol_kg  dummy_data
#0  CDL01S  5/3/2020  Candelaria  River   CDL01  ...  18.55736 -91.25012             3915            3863      3685.0
#1  CDL01F  5/3/2020  Candelaria  River   CDL01  ...  18.55722 -91.24990             3698            3685         NaN
#2  CDL02S  5/3/2020  Candelaria  River   CDL02  ...  18.61007 -91.24410             3724            3708      3708.0
#3  CDL02F  5/3/2020  Candelaria  River   CDL02  ...  18.61005 -91.24403             3667            3992      3992.0
#4  CDL03S  5/3/2020  Candelaria  River   CDL03  ...  18.63166 -91.29359             2928            3023      3023.0

#[5 rows x 21 columns]


#INFORMACION DEL DATAFRAME

print(CO2Data.info())

#<class 'pandas.core.frame.DataFrame'>
#RangeIndex: 106 entries, 0 to 105
#Data columns (total 21 columns):
# #   Column                   Non-Null Count  Dtype
---  ------                   --------------  -----
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
# dtypes: float64(12), int64(2), object(7)
# memory usage: 17.5+ KB
# None


print(CO2Data.describe())

#       chlorophy_microg_l  cond_microsiemens_cm     depth_m  do_percent_sat  ...   longitude  dic_micromol_kg  ta_micromol_kg   dummy_data
#count          106.000000            106.000000  106.000000      106.000000  ...  106.000000       106.000000      106.000000    99.000000
#mean             6.545472          27895.183962    1.830160       89.515094  ...  -91.602783      2797.981132     2912.915094  2902.888889
#std             14.941262          20931.232513    2.038739       29.772291  ...    0.240359       499.852416      472.694346   473.698989
#min              0.360000             13.800000    0.105000        1.700000  ...  -91.902180      2152.000000     2357.000000  2357.000000
#25%              2.555000           1778.025000    0.428750       84.575000  ...  -91.809810      2452.250000     2585.500000  2561.500000
#50%              3.705000          33202.600000    0.638500       97.100000  ...  -91.786895      2646.500000     2823.000000  2814.000000
#75%              5.925000          47046.650000    2.883250      105.300000  ...  -91.367565      2963.250000     3053.750000  3029.000000
#max            150.900000          59988.600000    8.558000      174.100000  ...  -91.244000      4324.000000     4307.000000  4307.000000

#[8 rows x 14 columns]


#ANALIZAR EN BUSCA DE VALORES PERDIDOS (NAs) EN LAS COLUMNAS

print(CO2Data.isnull().sum())

#sample                     0
#date                       0
#estuary                    0
#area                       0
#station                    0
#layer_depth                0
#season                     0
#chlorophy_microg_l         0
#cond_microsiemens_cm       0
#depth_m                    0
#do_percent_sat             0
#do_mg_l                    0
#sal_psu                    0
#sp_cond_microsiemens_cm    0
#turbidity_fnu              0
#temp_c                     0
#latitude                   0
#longitude                  0
#dic_micromol_kg            0
#ta_micromol_kg             0
#dummy_data                 7
#dtype: int64



#RELLENAR LOS ESPACIOS VACIOS EN LAS COLUMNAS DONDE FALTEN DATOS
#CREAR UNA COPIA DEL DATAFRAME

CO2Data_fill = CO2Data.copy()
#Es necesario poner .copy para no modificar el archivo original

CO2Data_fill = CO2Data_fill.fillna(method="ffill")

___________________________________________________________
<python-input-12>:1: FutureWarning: DataFrame.fillna with 'method' is deprecated and will raise in a future version. Use obj.ffill() or obj.bfill() instead.
###* Advertencia, cambiar el código en futuros scrips, 1) Rellenar hacia adelante: CO2Data_fill = CO2Data_fill.ffill() 2) Rellenar hacia atrás: CO2Data_fill = CO2Data_fill.bfill() 
________________________________________________________


#RELLENAR LOS VACIOS, Y SUMARLOS. TRUE = 0 

print(CO2Data_fill.isnull().sum())

#sample                     0
#date                       0
#estuary                    0
#area                       0
#station                    0
#layer_depth                0
#season                     0
#chlorophy_microg_l         0
#cond_microsiemens_cm       0
#depth_m                    0
#do_percent_sat             0
#do_mg_l                    0
#sal_psu                    0
#sp_cond_microsiemens_cm    0
#turbidity_fnu              0
#temp_c                     0
#latitude                   0
#longitude                  0
#dic_micromol_kg            0
#ta_micromol_kg             0
#dummy_data                 0
#dtype: int64


#INTERPOLACION EN VALORES FALTANTES
#HACER UNA COPIA DEL PRIMER DATAFRAME

CO2Data_fill_linear = CO2Data.copy()


#INTERPOLAR DE MANERA LINEAL
#RELLENAR LOS DATOS FALTANTES

CO2Data_fill_linear = CO2Data_fill_linear.interpolate(method='linear')


print(CO2Data_fill_linear.isnull().sum())

#sample                     0
#date                       0
#estuary                    0
#area                       0
#station                    0
#layer_depth                0
#season                     0
#chlorophy_microg_l         0
#cond_microsiemens_cm       0
#depth_m                    0
#do_percent_sat             0
#do_mg_l                    0
#sal_psu                    0
#sp_cond_microsiemens_cm    0
#turbidity_fnu              0
#temp_c                     0
#latitude                   0
#longitude                  0
#dic_micromol_kg            0
#ta_micromol_kg             0
#dummy_data                 0
#dtype: int64

________________________________________________________________________________________________________________________
###Exercises:
_______________________________________________________________________________________________________________________
###Create a new column called "TA_DIC_ratio" that is the ratio of TA to DIC


#CON BASE EN EL DATAFRAME CO3DATA_fill SE USA UN DATAFRAME SIN DATOS FALTANTES
#SE CREA LA COLUMNA TA/TIC USANDO LOS NOMBRES DE LAS COLUMNAS CON TA "ta_micromol_kg" y DIC "'dic_micromol_kg"

CO2Data_fill['TA_DIC_ratio'] = CO2Data_fill['ta_micromol_kg'] / CO2Data_fill['dic_micromol_kg']


#Verificar

print(CO2Data_fill.columns)

#Index(['sample', 'date', 'estuary', 'area', 'station', 'layer_depth', 'season',
#       'chlorophy_microg_l', 'cond_microsiemens_cm', 'depth_m',
#       'do_percent_sat', 'do_mg_l', 'sal_psu', 'sp_cond_microsiemens_cm',
#       'turbidity_fnu', 'temp_c', 'latitude', 'longitude', 'dic_micromol_kg',
#       'ta_micromol_kg', 'dummy_data', 'TA_DIC_ratio'],
#      dtype='object')


print(CO2Data_fill[['ta_micromol_kg', 'dic_micromol_kg', 'TA_DIC_ratio']].head())

#   ta_micromol_kg  dic_micromol_kg  TA_DIC_ratio
#0            3863             3915      0.986718
#1            3685             3698      0.996485
#2            3708             3724      0.995704
#3            3992             3667      1.088628
#4            3023             2928      1.032445
___________________________________________________________________________________________________________________

###Calculate the mean and standard deviation of the "TA_DIC_ratio" for each season

#AGRUPAR LAS ESTACIONES CON LA FUNCION groupby Y CALCULAR MEDIA Y DESVIACION ESTANDAR

season_stats = CO2Data_fill.groupby('season')['TA_DIC_ratio'].agg(['mean','std'])


#VERIFICAR

print(season_stats)

#            mean       std
#season
#Dry     1.058558  0.086111
#Rainy   1.022350  0.100924


#TAMBIEN SE PUEDE CALCULAR CON las funciones .pivot_table y aggfunc

season_stats = CO2Data_fill.pivot_table(values='TA_DIC_ratio', index='season',
                                                      aggfunc=['mean','std'])

#VERIFICAR

print(season_stats)

#               mean          std
#       TA_DIC_ratio TA_DIC_ratio
#season
#Dry        1.058558     0.086111
#Rainy      1.022350     0.100924

___________________________________________________________________________________________________________________________

##Calculate the mean and standard deviation of the "TA_DIC_ratio" for each season and area

##NUEVAMENTE SE PUEDE USAR LA FUNCION groupby, Y AGRENDO "season" Y "area"

season_area_stats = CO2Data_fill.groupby(['season','area'])['TA_DIC_ratio'].agg(['mean','std'])


#VERIFICAR

print(season_area_stats)

#                  mean       std
#season area
#Dry    Coast  1.115766  0.115033
#       Plume  1.059687  0.035574
#       River  1.000221  0.037747
#Rainy  Coast  1.090127  0.129658
#       Plume  1.025544  0.049222
#       River  0.945217  0.025084

______________________________________________________________________________________________________________________________


##Save the results to an Excel file called "TA_DIC_Season_Areas.xlsx"

season_area_stats.to_excel('TA_DIC_Season_Areas.xlsx')

##CONOCER LA CARPETA DONDE SE GUARDO EL ARCHIVO EXCEL

import os
print(os.getcwd())


