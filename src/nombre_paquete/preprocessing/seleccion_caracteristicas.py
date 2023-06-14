
# transformación de los datos con PCA, min max escaler y one hot
# este script transforma los datos preprocesados en listos para 
# entrenar el modelo 


def seleccion_caracteristicas(df_prep,cadena=""):
    """
    parametros: dataframe con los datos preprocesados
                cadena: string con valor "train" para datos 
                de entrenamiento o ninguno para datos en producción 
                sin etiqueta
        (transforma con PCA las caracteristicas 
        "emp_var_rate","euribor3m","nr_employed", en una sola ya que
        presentan un alto grado de correlación)
        (la varianza explicada en esta transformación en una 
        componente es de 99%)
    
    returno: un dataframe con una caracteristica nueva que 
        reemplaza a "emp_var_rate","euribor3m","nr_employed",
        eliminando estas del dataframe 
    
    """
    
    
    
    from sklearn.decomposition import PCA
    df_seleccion = df_prep.copy(deep=True)
    #caracteristicas correlacionedas, tres caracteristicas 
    caract_corr=["emp_var_rate","euribor3m","nr_employed"]
    #aplica pca
    pca = PCA(n_components=1)
    nueva_caracteristica = pca.fit(df_seleccion[caract_corr])
    # crea la nueva caracteristica
    df_seleccion["nueva_caracteristica"]=pca.transform(
                                df_seleccion[caract_corr])
    
    df_seleccion.drop(caract_corr,inplace=True,axis=1)
    
    if cadena == "train":
        #reordenando
        ultima_columna = df_seleccion.columns[-1]
        penultima_columna = df_seleccion.columns[-2]
        df_seleccion = df_seleccion[[*df_seleccion.columns[:-2], 
                                 ultima_columna, penultima_columna]]
    
    return df_seleccion
