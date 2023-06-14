
# De los resultados del analisis exploratorio se realiza 
## el siguiente preprocesamiento

# función de prepocesamiento

def preprocesamiento(df):
    """
    parametros: dataframe de los datos sin procesar 
    
    #realiza el preprocesamiento de las columnas Dias_Ultima_Camp,
    cons_price_idx,euribor3m y Estado_Civil
    
    
    retorna: un dataframe con los datos preprocesados 
    """
    
    
    #genera una copia del dataframe
    df_prep=df.copy(deep=True)
    #Asiga 0 si el cliente a sido contactado 1 de los contrario
    df_prep["Dias_Ultima_Camp"]=df_prep["Dias_Ultima_Camp"
           ].apply(lambda x: 1 if x==999 else 0)
    
    #columna cons_price_idx, el rango de esta columna
    # debe estar entre 90<x<100  
    fun=lambda x: x if len(str(int(x)))<3 else x/(10**(len(str(int(x)))-2))
    df_prep["cons_price_idx"]=df_prep["cons_price_idx"].apply(fun)
    
    # columna euribor3m, el rango de esta columna no debe 
    # superar el 10 ya que es una taza de interes 

    fun2=lambda x: x if x<10 else x/1000
    df_prep["euribor3m"]=df_prep["euribor3m"].apply(fun2)
    
    # columna estado civil se unne en una categoria 
    # single por soltero y divorced y divorciado 
    
    def transformar_estado_civil(valor):
        if valor == 'single':
            return 'soltero'
        elif valor == 'divorced':
            return 'divorciado'
        else:
            return valor
    
    df_prep["Estado_Civil"]=df_prep["Estado_Civil"].apply(transformar_estado_civil)
    
    
    return df_prep
