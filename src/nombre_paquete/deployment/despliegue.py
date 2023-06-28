from fastapi import FastAPI,UploadFile, File
import joblib
import numpy as np
import pandas as pd
from io import StringIO
import sys


# colocamos la ruta de los paquetes a python 
sys.path.append('/home/leomorya/proyecto_final_metodologias/tdsp_template/src/nombre_paquete/')

#cargamos el modelo 
ruta_1 = "/home/leomorya/proyecto_final_metodologias/tdsp_template/src"
ruta_2 = "/nombre_paquete/models"
ruta_guarda = f"{ruta_1}{ruta_2}"
modelo=joblib.load(f'{ruta_guarda}/modelo_random_forest.pkl')


#importamos lo paquetes creados de preprocesmaiento
from preprocessing.funcion_de_preprocesamiento import preprocesamiento
from preprocessing.seleccion_caracteristicas import seleccion_caracteristicas
from preprocessing.transformaciones_datos import transformaciones

app = FastAPI()

#Alive function
@app.get("/")
def alive():
    return ('Alive')

@app.post("/inferencias")
async def cargar_archivo(file: UploadFile = File(...)):
    # Leer el contenido del archivo
    contenido = await file.read()


    # Convertir los datos en un DataFrame
    datos_df = pd.read_csv(StringIO(contenido.decode('utf-8'))) 
    
    #procesmaiento de los datos
    datos_preprocesados = preprocesamiento(datos_df)
    datos_features=seleccion_caracteristicas(datos_preprocesados)
    datos_tranformados=transformaciones(datos_features)
    
    #sirve para imprmir los datos preprocesadso en consola
    #print(datos_tranformados.tolist())
    
    
    # Realizar la inferencia utilizando el modelo cargado
    resultado = modelo.predict(datos_tranformados)

    # Devolver el resultado
    return {"resultado": resultado.tolist()}