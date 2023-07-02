# ruta de la transformación que se va a guardar min max
ruta_guarda = r"./Modelos_utilizados_preprocesamiento"

# datos para guardar el modelo min max

# preprocesamiento
import pandas as pd
import numpy as np

#Carga de datos
# ruta de los datos
ruta=r"../../../../data/datos_train_prep_selec.csv"

# cargando los datos 
df_train_prep_selec=pd.read_csv(ruta)

# aplica PCA sobre los datos de train y guarda el modelo
def min_max_train(df_prep):
    """
    Parametros: dataframe preprocesado y con selección de caracteristicas solo train 
    
    Aplica la transfromación min max escaler a los datos de entrenamiento y guarda 
    el modelo de la transformación 
    
    Retorna: Guarda el modelo entrenado min max escaler con los datos 
    de train 
    
    """
    
    #toma las caracteristicas categoricas 
    numeric = df_prep._get_numeric_data().columns[:-1]
    
    df_num = df_prep[numeric]
    df_num = df_num.drop("ID",axis=1)
       
    import joblib
    from sklearn.preprocessing import MinMaxScaler
    # crea el objeto min_max
    min_max = MinMaxScaler()
    modelo_min_max_entrenado = min_max.fit(df_num)
    
    # Guardar el modelo en un archivo
    joblib.dump(modelo_min_max_entrenado, f'{ruta_guarda}/modelo_min_max.pkl')
    
    pass 
    
min_max_train(df_train_prep_selec)
