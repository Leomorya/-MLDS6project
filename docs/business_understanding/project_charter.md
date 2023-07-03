# Project Charter - Entendimiento del Negocio

# Proyecto Predicción de endeudamiento de buenos clientes

## 1. Objetivo del Proyecto

El objetivo del proyecto es generar un modelo que prediga que clientes aceptaran un crédito de libre inversión para su posterior despliegue. Para este fin se utiliza una serie de datos de los clientes y variables económicas

### 1.1 Objetivos del negocio

El objetivo del negocio aumentar su rentabilidad en cuento a créditos, con este fin se tiene el siguiente objetivo

Aumentar la tasa de éxito al ofrecer créditos a clientes del banco se debe tener en cuenta que estos clientes en general son buenos clientes o clientes que potencialmente pagaran su crédito, es decir ya tienen un primer filtro y lo que interesá en conocer que tipos de clientes tomaran un crédito al realizar el banco campañas para nuevos créditos, es decir predecir si el cliente tomara o no un crédito teniendo en cuenta ciertas características del cliente y del mercado.

### 1.2 Metas del proyecto de machine learning o deep learning

En este proyecto de machine learning se cuenta con un conjunto de datos historico del banco de clientes que han aceptado y que no han aceptado el crédito con características dadas por el banco, teniendo los datos y el objetivo del negocio se proponen los siguientes objetivos:

* Realizar un análisis exploratorio de los datos para identificar las características mas relevantes, ademas, evitar posibles sesgos en modelos debido a correlaciones y desbalanceo de los mismos.
* Generar un modelo de machine learning que pueda predecir si un cliente nuevo tomara el crédito o no
* Evaluar el modelo generado con diferentes metricas acordes al problema presente

## 2. Alcance del Proyecto

Para el desarrollo de este proyecto se utilizaron datos proporcionados por un banco que se utilizan como un examen para el cargo de científico de datos, estos están disponible en [link](https://www.mediafire.com/folder/xzpcnokbul9ea/data) en formato CSV, ademas, de separados en train 23100 datos y producción 9869, que contienen datos de los clientes como nombre, educación, etc y algunas variables económicas.  

* Descripción de los resultados esperados:
Para este proyecto se espera que se despliegue un modelo en producción que haga inferencias sobre los clientes del banco, para crear de esta manera campañas de créditos a los resultados positivos de la inferencia, en cuento a tomar un crédito.


## 3. Metodología
La metodología que se llevara a cabo en este proyecto es la CRISP-DM, que son las siglas de Cross-Industry Standard Process for Data Mining. La cual puede llevar varia iteraciones de las siguientes etapas:
* Entendimiento del negocio, en esta etapa se plantea el objetivo del negocio y del proyecto de machine learning
* Entendimiento del los datos, en esta etapa se realizar el análisis exploratorio de los datos, haciendo una ingeniería de características y preparando los datos para el modelado
* Construcción de diferentes modelos de meachine learning con los datos preparados 
* Evaluación de diferentes modelos de machine learning con métricas de desempeño teniendo en cuenta el objetivo del modelado, para este caso, métricas como accuracy, f1_score, precisión, etc, ya que es un modelo de clasificación 
* desplegado del modelo en producción
## 4. Cronograma
Las actividades desarrolladas en este proyecto son las siguientes:


|Paso|Actividad|Tiempo en semanas|
|:---:|:---|:---|
|1|Entendimiento del negocio|1|
|2|Obtención de los datos|1|
|3|Preprocesamiento y análisis exploratorio de los datos|3|
|4|Selección de características y modelamiento |2|
|5|Métricas de evaluación y selección del mejor modelo |1|
|6|Entrenamiento final del modelo |1/4|
|7|Despliegue del modelo y creación de scripts de entrada de datos|1|
|8|Evaluación del modelo en producción y entrega final|3|

En total el proyecto solo toma 12 1/4 de semanas.

## 5. Equipo del Proyecto
Líder del proyecto
Jose Leonardo Sánchez - científico de datos

## 6. Presupuesto
|Item|Actividad|costo en pesos|
|:---:|:---|:---|
|1|Técnicos del negocio|3.000.000|
|2|Técnicos de datos y software|150.000.000|
|3|Software y hardware|30.000.000|
|4|Otros |10.000.000|

En total el proyecto tiene un costo aproximado de 
193.000.000 millones de pesos
## 7. Stakeholders
|Nombre|Cargo|Relación|Expectativa|
|:---:|:---|:---|:---|
|XXX|Gerente del banco|Contratación y definición de necesidades|Aumento de créditos dados| 
|XXX|Asesor de crédito|Entendimiento del negocio y solución|Aumento de créditos dados|
|XXX|Asesor de crédito|Entendimiento del negocio y solución|Aumento de créditos dados|
|XXX|Analista financiero|Entendimiento del negocio y solución|Aumento de créditos dados|
|XXX|Desarrollador del banco|Facilidades del despliegue|Fácil acceso a correr el modelo|
## 8. Aprobaciones
**Proyecto aprobado por el gerente del banco nombre XXX** 
- Firma XXX

**Fecha de aprobación** 
- 6 junio de 2023


