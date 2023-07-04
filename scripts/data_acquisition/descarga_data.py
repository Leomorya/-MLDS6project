import time
import re
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome("chromedriver", options=chrome_options)
import os
#ruta de la carpeta descargas
carpeta_descargas = os.path.expanduser("~/Descargas")

#crea la carpeta data
carpeta_data = os.path.join(carpeta_descargas, "data")
os.makedirs(carpeta_data, exist_ok=True)

# ruta del archivo a descargar
ruta_train="https://www.mediafire.com/file/il2ma0ez6wnr1ag/train.csv/file"

# descargando el archivo
driver.get(ruta_train)

botom=driver.find_element(By.ID,"downloadButton")
#ahora click
botom.click()

# ruta local
archivo="./Descargas/data/train.csv" 

# espera a descarga de los datos
time.sleep(10)



#carga en un dataframe

#df_train=pd.read_csv(archivo)
#display(df_train.head(5))

# ruta del archivo a descargar
ruta_produccion="https://www.mediafire.com/file/zzp8uyl29ox5hhz/produccion.csv/file"

# descargando el archivo
driver.get(ruta_produccion)

botom2 = driver.find_element(By.ID,"downloadButton")
#ahora click
botom2.click()

# ruta local
#archivo2="./Descargas/data/test.csv" 

# espera a descarga de los datos
time.sleep(10)

#df_test=pd.read_csv(archivo2)
#display(df_produccion.head(5))

# cambia los archivos descargados a la carpeta data 

ruta_archivo_descargado = os.path.join(carpeta_descargas, "train.csv") # Ruta del archivo descargado
ruta_destino = os.path.join(carpeta_data, "train.csv")  # Ruta de destino en la carpeta "data"

os.rename(ruta_archivo_descargado, ruta_destino) # guarda el archivo train.csv en la carpeta data

ruta_archivo_descargado = os.path.join(carpeta_descargas, "produccion.csv")  
ruta_destino = os.path.join(carpeta_data, "produccion.csv")  

os.rename(ruta_archivo_descargado, ruta_destino) # guarda el archivo produccion.csv en la carpeta data

# Cerrar el navegador
driver.quit()

