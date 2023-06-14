# trasnformación de los datos 
# a los datos numericos se les realizara una transformacion min max
# tomando el intervalos [0,1] para que los modelos no se sesge debido 
# a las magnitudes 

# a los datos catgoricos se les realizara 
#una transformación one - hot

import numpy as np
import pandas as pd


def transformaciones(df_prep_selec):
    df_transform = df_prep_selec.copy(deep=True)
    
    # transformación columnas numericas 
    # obtengo las columnas numericas y el dataframe numerico
    numeric = df_transform._get_numeric_data().columns
         
    # ruta para cargar modelo min_max_escaler 
    ruta_1 = "/home/leomorya/proyecto_final_metodologias/tdsp_template/scripts"
    ruta_2 = "/preprocessing/Modelos_utilizados_preprocesamiento"
    ruta_carga = f"{ruta_1}{ruta_2}"
    
    import joblib
    # carga el modelo min_max
    min_max = joblib.load(f"{ruta_carga}/modelo_min_max.pkl")    
               
    # obtiene la matriz min_max sin el ID
    matrix_numeric = min_max.transform(df_transform[numeric[1:]])
    
    #trasnformación de las columnas categoricas
    categoricas=df_transform.select_dtypes('object').columns
    
    
    # carga el modelo one_hot_escaler
    one_hot = joblib.load(f"{ruta_carga}/modelo_one_hot.pkl") 
    
    
    # obtiene la matriz one_hot_escaler
    matrix_categ = one_hot.transform(df_transform[categoricas]).toarray()
    
    matrix_final = np.concatenate([matrix_categ,matrix_numeric],axis=1)      
    
    return matrix_final
