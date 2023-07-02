# ruta de la transformación que se va a guardar one hot

ruta_guarda = r"./Modelos_utilizados_preprocesamiento"
# datos para guardar el modelo one hot

# preprocesamiento
import pandas as pd
import numpy as np

#Carga de datos
# ruta de los datos
ruta=r"../../../../data/datos_train_prep_selec.csv"

# cargando los datos 
df_train_prep_selec=pd.read_csv(ruta)

# aplica PCA sobre los datos de train y guarda el modelo
def one_hot_train(df_prep):
    """
    Parametros: dataframe preprocesado y con selcción de caracteristicas solo train 
    
    Aplica la transfromación one hot a los datos de entrenamiento y guarda el modelo de 
    la transformación 
    
    Retorna: Guarda el modelo entrenado one hot con los datos 
    de train 
    
    """
    #toma las caracteristicas categoricas 
    categoricas=df_prep.select_dtypes('object').columns
    df_cat= df_prep[categoricas]

    import joblib
    from sklearn.preprocessing import OneHotEncoder
    # crea el objeto one hot 
    one_hot = OneHotEncoder(handle_unknown='ignore')
    modelo_one_hot_entrenado = one_hot.fit(df_cat)
    
    # Guardar el modelo en un archivo
    joblib.dump(modelo_one_hot_entrenado, f'{ruta_guarda}/modelo_one_hot.pkl')
    
    pass 
    
one_hot_train(df_train_prep_selec)
