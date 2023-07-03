
import time
import re
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome("chromedriver", options=chrome_options)

# ruta del archivo a descargar
ruta_train="https://www.mediafire.com/file/il2ma0ez6wnr1ag/train.csv/file"

# descargando el archivo
driver.get(ruta_train)

botom=driver.find_element(By.ID,"downloadButton")
#ahora click
botom.click()

# ruta local
archivo="./Descargas/train.csv" 

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
archivo2="./Descargas/test.csv" 

# espera a descarga de los datos
time.sleep(10)

#df_test=pd.read_csv(archivo2)
#display(df_produccion.head(5))
