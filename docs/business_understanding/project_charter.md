# Project Charter - Entendimiento del Negocio
---

# Proyecto Predicción de endeudamiento de buenos clientes
---

## 1. Objetivo del Proyecto
---

El objetivo del proyecto es generar un modelo que prediga que clientes aceptaran un credito de libre inversión para su posterior despliege. Para este fin se utiliza una serie de datos de los clientes y variables economicas

### 1.1 Objetivos del negocio
---

El objetivo del negocio aumentar su rentabilidad en cuento a creditos, con este fin se tiene el siguiente objetivo

Aumentar la tasa de exito al ofrecer creditos a clientes del banco se debe tener en cuenta que estos clientes en general son buenos clientes o clientes que potencialmente pagaran su credito, es decir ya tienen un primer filtro y lo que intereza en conocer que tipos de clientes tomaran un credito al realizar el banco campañas para nuevos creditos, es decir predecir si el cliente tomora o no un credito teniendo en cuenta ciertas caracteristicas del cliente y del mercado.

### 1.2 Metas del proyecto de machine learning o deep learning
---

En este proyecto de machine learning se cuenta con un conjunto de datos historico del banco de clientes que han aceptado y que no han aceptado el credito con caracteristicas dadas por el banco, teniendo los datos y el objetivo del negocio se proponen los siguientes objetivos:

* Realizar un analisis exploratorio de los datos para identificar las caracteristicas mas relevantes, ademas, evitar posibles sesgos en modelos debido a correlaciones y desbalanceo de los mismos.
* Generar un modelo de machine learning que puedad predecir si un cliente nuevo tomara el credito o no
* Evaluar el modelo generado con diferentes metricas acordes al problema presente

## 2. Alcance del Proyecto
---

Para el desarrollo de este proyecto se utilizaron datos proporcionados por un banco que se utilizan como un examen para el cargo de cientifico de datos, estos estan disponible en [link](https://www.mediafire.com/folder/xzpcnokbul9ea/data) en formato CSV, ademas, de separados en train 23100 datos y tests 9869, que contienen datos de los clientes como monbre, educación, etc y algunas varibles economicas.  

* Descripción de los resultados esperados:
Para este proyecto se espera que se despliege un modelo en producción que haga inferencias sobre los clientes del banco, para crear de esta manera campañas de creditos a los resultados positivos de la inferencia, en cuento a tomar un credito.


## 3. Metodología
---
La metodología que se llevara a cabo en este proyecto es la CRISP-DM, que son las siglas de Cross-Industry Standard Process for Data Mining. La cual puede llevar varia iteraciociones de las siguintes etapas:
* Entendimiento del negocio, en esta etapa se plantea el objetivo del negocio y del proyecto de machine learning
* Entendicmiento del los datos, en esta etapa se realizar el análisis exploratorio de los datos, haciendo una ingenieria de caracteristicas y preperando los datos para el modelado
* Contrucción de diferentes modelos de meachine learning con los datos preparados 
* Evaluación de diferentes modelos de machine learning con metricas de desempeño teniendo en cuenta el objetivo del modelado, para este caso, metricas como accuracy, f1_score, precisión, etc, ya que es un modelo de clasificación 
* desplegado del modelo en producción
## 4. Cronograma
---
Las actividades desarrolladas en este proyecto son las siguientes:


|Paso|Actividad|Tiempo en semanas|
|:---:|:---|:---|
|1|Entendimiendo del negocio|1|
|2|Obtención de los datos|1|
|3|Preprocesamiento y analisis exploratorio de los datos|3|
|4|Selección de caracteristicas y modelamiento |2|
|5|Metricas de evaluación y selección del mejor modelo |1|
|6|Entrenamiento final del modelo |1/4|
|7|Despliege del modelo y creación de scrips de entrada de datos|1|
|8|Evaluación del modelo en producción y entrega final|3|

En total el proyecto solo toma 12 1/4 de semanas.

## 5. Equipo del Proyecto
---
Lider del proyecto
Jose Leonardo Sánchez - cientifico de datos

## 6. Presupuesto
---
|Item|Actividad|costo en pesos|
|:---:|:---|:---|
|1|Tecnicos del negocio|3.000.000|
|2|Tecnicos de datos y software|150.000.000|
|3|Software y hardware|30.000.000|
|4|Otros |10.000.000|

En total el proyecto tiene un costo aproximado de 
193.000.000 millones de pesos
## 7. Stakeholders
---
|Nombre|Cargo|Relación|Expectativa|
|:---:|:---|:---|:---|
|XXX|Gerente del banco|Contratación y definicion de necesidades|Aumento de creditos dados| 
|XXX|Asesor de credito|Entendicmiento del negocio y solución|Aumento de creditos dados|
|XXX|Asesor de credito|Entendicmiento del negocio y solución|Aumento de creditos dados|
|XXX|Analista financiero|Entendicmiento del negocio y solución|Aumento de creditos dados|
|XXX|Desarrollador del banco|Facilidades del despliege|Facil acceso a correr el modelo|
## 8. Aprobaciones
---
**Proyecto aprobado por el gerente del banco nombre XXX** 
- Firma XXX

**Fecha de aprobación** 
- 6 junio de 2023


