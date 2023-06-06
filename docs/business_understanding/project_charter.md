{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "e8b4723f",
   "metadata": {},
   "source": [
    "# Project Charter - Entendimiento del Negocio\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "76548201",
   "metadata": {},
   "source": [
    "# Proyecto Predicción de endeudamiento de buenos clientes  "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "5cdcdb42",
   "metadata": {},
   "source": [
    "## 1. Objetivo del Proyecto\n",
    "\n",
    "El objetivo del proyecto es generar un modelo que prediga que clientes aceptaran un credito de libre inversión. Para este fin se utiliza una serie de datos de los clientes y variables economicas\n",
    "\n",
    "### 1.1 Objetivos del negocio\n",
    "\n",
    "El objetivo del negocio aumentar su rentabilidad en cuento a creditos, con este fin se tiene el siguiente objetivo\n",
    "\n",
    "Aumentar la tasa de exito al ofrecer creditos a clientes del banco se debe tener en cuenta que estos clientes en general son buenos clientes o clientes que potencialmente pagaran su credito, es decir ya tienen un primer filtro y lo que intereza en conocer que tipos de clientes tomaran un credito al realizar el banco campañas para nuevos creditos, es decir predecir si el cliente tomora o no un credito teniendo en cuenta ciertas caracteristicas del cliente y del mercado.\n",
    "\n",
    "### 1.2 Metas del proyecto de machine learning o deep learning\n",
    "\n",
    "En este proyecto de machine learning se cuenta con un conjunto de datos historico del banco de clientes que han aceptado y que no han aceptado el credito con caracteristicas dadas por el banco, teniendo los datos y el objetivo del negocio se proponen los siguientes objetivos:\n",
    "\n",
    "* Realizar un analisis exploratorio de los datos para identificar las caracteristicas mas relevantes, ademas, evitar posibles sesgos en modelos debido a correlaciones y desbalanceo de los mismos.\n",
    "* Generar un modelo de machine learning que puedad predecir si un cliente nuevo tomara el credito o no\n",
    "* Evaluar el modelo generado con diferentes metricas acordes al problema presente\n",
    "\n",
    "## 2. Alcance del Proyecto\n",
    "Los alcances son:\n",
    "* Realizar un análisis exploratorio de los datos\n",
    "* Procesar los datos de manera que puedan utilizarce para entrenar un modelo de machine learning y evaluarlo\n",
    "* construir un modelo predictivo que machine learning que prediga si un cliente tomara o no un credito\n",
    "* Desplegar el modelo de tal manera, que puede ser usado en producción por los asesores de creditos del banco\n",
    "* Evaluación en producción de modelo \n",
    "\n",
    "\n",
    "## 3. Metodología\n",
    "La metodología que se llevara a cabo en este proyecto es la CRISP-DM, que son las siglas de Cross-Industry Standard Process for Data Mining. La cual puede llevar varia iteraciociones de las siguintes etapas:\n",
    "* Entendicmiento del negocio, en esta etapa se plantea el objetivo del negocio y del proyecto de machine learning\n",
    "* Entendicmiento del los datos, en esta etapa se realizar el análisis exploratorio de los datos, haciendo una ingenieria de caracteristicas y preperando los datos para el modelado\n",
    "* Contrucción de diferentes modelos de meachine learning con los datos preparados \n",
    "* Evaluación de diferentes modelos de machine learning con metricas de desempeño teniendo en cuenta el objetivo del modelado, para este caso, metricas como accuracy, f1_score, precisión, etc, ya que es un modelo de clasificación \n",
    "* desplegado del modelo en producción\n",
    "## 4. Cronograma\n",
    "Las actividades desarrolladas en este proyecto son las siguientes:\n",
    "\n",
    "\n",
    "|Paso|Actividad|Tiempo en semanas|\n",
    "|:---:|:---|:---|\n",
    "|1|Entendimiendo del negocio|1|\n",
    "|2|Obtención de los datos|1|\n",
    "|3|Preprocesamiento y analisis exploratorio de los datos|3|\n",
    "|4|Selección de caracteristicas y modelamiento |2|\n",
    "|5|Metricas de evaluación y selección del mejor modelo |1|\n",
    "|6|Entrenamiento final del modelo |1/4|\n",
    "|7|Despliege del modelo y creación de scrips de entrada de datos|1|\n",
    "|8|Evaluación del modelo en producción y entrega final|3|\n",
    "\n",
    "En total el proyecto solo toma 12 1/4 de semanas.\n",
    "\n",
    "## 5. Equipo del Proyecto\n",
    "Lider del proyecto\n",
    "Jose Leonardo Sánchez - cientifico de datos\n",
    "\n",
    "## 6. Presupuesto\n",
    "|Item|Actividad|costo en pesos|\n",
    "|:---:|:---|:---|\n",
    "|1|Tecnicos del negocio|3.000.000|\n",
    "|2|Tecnicos de datos y software|150.000.000|\n",
    "|3|Software y hardware|30.000.000|\n",
    "|4|Otros |10.000.000|\n",
    "\n",
    "En total el proyecto tiene un costo aproximado de \n",
    "193.000.000 millones de pesos\n",
    "## 7. Stakeholders\n",
    "|Nombre|Cargo|Relación|Expectativa|\n",
    "|:---:|:---|:---|:---|\n",
    "|XXX|Gerente del banco|Contratación y definicion de necesidades|Aumento de creditos dados| \n",
    "|XXX|Asesor de credito|Entendicmiento del negocio y solución|Aumento de creditos dados|\n",
    "|XXX|Asesor de credito|Entendicmiento del negocio y solución|Aumento de creditos dados|\n",
    "|XXX|Analista financiero|Entendicmiento del negocio y solución|Aumento de creditos dados|\n",
    "|XXX|Desarrollador del banco|Facilidades del despliege|Facil acceso a correr el modelo|\n",
    "## 8. Aprobaciones\n",
    "**Proyecto aprobado por el gerente del banco nombre XXX** \n",
    "- Firma XXX\n",
    "\n",
    "**Fecha de aprobación** \n",
    "- 6 junio de 2023\n",
    "\n",
    "\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
