###IMPORTAR Y EXPLORAR


def import_csv(file):
    # Read the file into a DataFrame: df
    import pandas as pd
    return pd.read_csv(file)

path = "C:/Users/goliv/Documents/GitHub datos/Terminos_lagoon_TA_DIC_2023_RawData.csv"

CO2Data = import_csv(path)

##EXPLORAR 5 PRIMERAS FILAS

print(CO2Data.head())


#   sample      date     estuary   area station  ...  latitude #longitude  dic_micromol_kg  ta_micromol_kg  dummy_data
#0  CDL01S  5/3/2020  Candelaria  River   CDL01  ... 18.55736 -91.25012             3915            3863      3685.0
#1  CDL01F  5/3/2020  Candelaria  River   CDL01  ...  18.55722 -91.24990             3698            3685         NaN
#2  CDL02S  5/3/2020  Candelaria  River   CDL02  ...  18.61007 -91.24410             3724            3708      3708.0
#3  CDL02F  5/3/2020  Candelaria  River   CDL02  ...  18.61005 -91.24403             3667            3992      3992.0
#4  CDL03S  5/3/2020  Candelaria  River   CDL03  ...  18.63166 -91.29359             2928            3023      3023.0


##AGRUPAR POR COLUMNAS CATEGÓRICAS (SEASON Y ESTUARY)
##CALCULAR LA MEDIA Y DESVIACIÓN ESTÁNDAR DE VARIABLES NUMÉRICAS


##DEFINIR VARIABLES A  ANALIZAR. EN ESTE CASO SERÁN "DIC, TA, SAL"

variables = ['dic_micromol_kg', 'ta_micromol_kg', 'sal_psu']



##CALCULAR LA MEDIA Y LA DESVIACIÓN ESTÁNDAR USANDO LA FUNCION DE AGRUPAMIENTO groupby POR SEASON Y ESTUARY

result = CO2Data.groupby(['season', 'estuary'])[variables].agg(['mean', 'std']).reset_index()



#RENOMBRAR LAS COLUMNAS PARA MAYOR CLARIDAD (JUNTAT LOS TERMINOS MEAN Y SD A LOS VARIABLES)

result.columns = ['_'.join(col).strip() if isinstance(col, tuple) else col for col in result.columns]


##VERIFICAR/MOSTRAR

print(result)

# season_    estuary_  dic_micromol_kg_mean  ...  ta_micromol_kg_std  sal_psu_mean  sal_psu_std
#0    Dry  Candelaria           2917.055556  ...          556.680114     23.633889    12.121592
#1     Dry    Palizada           2968.194444  ...          323.177154     16.392500    13.830189
#2   Rainy  Candelaria           2474.125000  ...          192.848635     15.165000    13.937384
#3   Rainy    Palizada           2507.277778  ...          260.962923      8.533333     9.940109

#[4 rows x 8 columns]


______________________________________________________________________________________________
#INSTALAR SI FALTAN "pandas" Y "tabulate"

import pandas as pd
from tabulate import tabulate



#USAR EL DATAFRAME DE CO2Data PREVIAMENTE CARGARDO (EJERCISIO ANTERIOR)

#CO2Data = pd.read_csv('tu_archivo.csv')# Ejemplo si proviene de un CSV


#DEFINIR LAS COLUMNAS A ANALIZAR
 
variables = ['dic_micromol_kg', 'ta_micromol_kg', 'sal_psu']



##CALCULAR LA MEDIA Y LA DESVIACIÓN ESTÁNDAR AGRUPANDO POR SEASON Y ESTUARY
##INDEX QUITAR EL INDICE JERARQUICO PARA SEASON Y ESTUARY

result = CO2Data.groupby(['season', 'estuary'])[variables].agg(['mean', 'std']).reset_index()

print(result)
#   season     estuary dic_micromol_kg             ta_micromol_kg                sal_psu
                                mean         std           mean         std       mean        std
#0    Dry  Candelaria     2917.055556  630.585893    3076.777778  556.680114  23.633889  12.121592
#1    Dry    Palizada     2968.194444  391.242257    3107.888889  323.177154  16.392500  13.830189
#2  Rainy  Candelaria     2474.125000  306.407980    2537.062500  192.848635  15.165000  13.937384
#3  Rainy    Palizada     2507.277778  216.751092    2529.333333  260.962923   8.533333   9.940109



##Asignar nombres de columnas adecuados
result.columns = ['season', 'estuary'] + [f"{var}_{stat}" for var in variables for stat in ['mean', 'std']]

print(result)

#  season     estuary  dic_micromol_kg_mean  ...  ta_micromol_kg_std  sal_psu_mean  sal_psu_std
#0    Dry  Candelaria           2917.055556  ...          556.680114     23.633889    12.121592
#1    Dry    Palizada           2968.194444  ...          323.177154     16.392500    13.830189
#2  Rainy  Candelaria           2474.125000  ...          192.848635     15.165000    13.937384
#3  Rainy    Palizada           2507.277778  ...          260.962923      8.533333     9.940109

#[4 rows x 8 columns]


##FORMATEAR LOS VALORES PARA MOSTRAR "MEDIA ± DESVIACIÓN ESTÁNDAR". SIN NOTACIÓN CIENTÍFICA Y CON DOS CIFRAS DECIMALES
#CREAR UNA FUNCION


for var in variables:
    mean_col = f"{var}_mean"
    std_col = f"{var}_std"
    result[f"{var}_formatted"] = result.apply(lambda row: f"{row[mean_col]:,.2f} ± {row[std_col]:,.2f}", axis=1)


#CREAR UN NUEVO DATA FRAME DONDE SE SELECCIONES SOLO LAS COLUMNAS FORMATEADAS JUNTO CON LOS ÍNDICES

formatted_result = result[['season', 'estuary'] + [f"{var}_formatted" for var in variables]]


##MOSTRAR LA TABLA CON LOS RESULTADOS FORMATEADOS USANDO LA FUNCION TABULATE

table = tabulate(formatted_result, headers='keys', tablefmt='pretty', showindex=False)
print(table)


+--------+------------+---------------------------+--------------------------+-------------------+
| season |  estuary   | dic_micromol_kg_formatted | ta_micromol_kg_formatted | sal_psu_formatted |
+--------+------------+---------------------------+--------------------------+-------------------+
|  Dry   | Candelaria |     2,917.06 ± 630.59     |    3,076.78 ± 556.68     |   23.63 ± 12.12   |
|  Dry   |  Palizada  |     2,968.19 ± 391.24     |    3,107.89 ± 323.18     |   16.39 ± 13.83   |
| Rainy  | Candelaria |     2,474.12 ± 306.41     |    2,537.06 ± 192.85     |   15.16 ± 13.94   |
| Rainy  |  Palizada  |     2,507.28 ± 216.75     |    2,529.33 ± 260.96     |    8.53 ± 9.94    |
+--------+------------+---------------------------+--------------------------+-------------------+


##GUARDAR LA TABLA EN UN ARCHIVO CSV

formatted_result.to_csv("resultados_agrupados.csv", index=False)


##MOSTRAR DONDE ESTA GUARDADO EL EXCEL

import os
print(os.getcwd())
