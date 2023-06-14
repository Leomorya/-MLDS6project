# ruta del modelo que se va a guardar PCA
ruta_1 = "/home/leomorya/proyecto_final_metodologias/tdsp_template/scripts"
ruta_2 = "/preprocessing/Modelos_utilizados_preprocesamiento"
ruta_guarda = f"{ruta_1}{ruta_2}"

# datos para guardar el modelo PCA 

# preprocesamiento
import pandas as pd
import numpy as np

#Carga de datos
# ruta de los datos
ruta=r"/home/leomorya/proyecto_final_metodologias/data/datos_preprocesados_train.csv"

# cargando los datos 
df_train_prep=pd.read_csv(ruta)

# aplica PCA sobre los datos de train y guarda el modelo
def PCA_train(df_prep):
    """
    Parametros: dataframe preprocesado solo train 
    
    (transforma con PCA las caracteristicas 
        "emp_var_rate","euribor3m","nr_employed", en una sola ya que
        presentan un alto grado de correlación)
        (la varianza explicada en esta transformación en una 
        componente es de 99%)
    
    Retorna: Guarda el modelo entrenado PCA con los datos 
    de train 
    
    """
    
    
    import joblib
    from sklearn.decomposition import PCA
    # crea el objeto pca 
    pca = PCA(n_components=1)
    caract_corr=["emp_var_rate","euribor3m","nr_employed"]
    modelo_pca_entrenado = pca.fit(df_prep[caract_corr])
    
    # Guardar el modelo en un archivo
    joblib.dump(modelo_pca_entrenado, f'{ruta_guarda}/modelo_pca.pkl')
    
    pass 
    
PCA_train(df_train_prep)
    
