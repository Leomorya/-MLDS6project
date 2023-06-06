
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
ruta_train="https://www.mediafire.com/file/7r6ddufr53xfbkq/train.csv/file"

# descargando el archivo
driver.get(ruta_train)

botom=driver.find_element(By.ID,"downloadButton")
#ahora click
botom.click()

# ruta local
archivo="/home/leomorya/Descargas/train.csv" 

# espera a descarga de los datos
time.sleep(10)

#carga en un dataframe

df_train=pd.read_csv(archivo)
display(df_train.head(5))

# ruta del archivo a descargar
ruta_test="https://www.mediafire.com/file/vtm76e3r9cguff9/test.csv/file"

# descargando el archivo
driver.get(ruta_test)

botom2 = driver.find_element(By.ID,"downloadButton")
#ahora click
botom2.click()

# ruta local
archivo2="/home/leomorya/Descargas/test.csv" 

# espera a descarga de los datos
time.sleep(10)

df_test=pd.read_csv(archivo2)
display(df_test.head(5))

