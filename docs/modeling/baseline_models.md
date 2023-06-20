# Reporte del Modelo Baseline

Este documento contiene los resultados del modelo baseline.

## Descripción del modelo

Teniendo en cuenta que se desea realizar una clasificación binaria, el modelo base que se utilizara será uno de regresión logística de sklearn, teniendo en cuenta que la clase positiva (1) se encuentra desbalanceada, en la variación de hiperparametros se tendra el atributo class_weigth. Para ejecutar el algoritmo de variación de hiperparametros se utilizara gridsearch de sklearn debido a su facilidad de implementación.    

## Variables de entrada

Las variables de entrada utilizadas en el modelo conocida como exogenas o independientes son las siguientes:
Edad, Tipo_Trabajo, Estado_Civil, Educacion, mora, Vivienda, Consumo, Contacto, Mes, Dia, Campana, Dias_Ultima_Camp, No_Contactos, Resultado_Anterior, cons_price_idx, cons_conf_idx, nueva_característica 	
Siendo la nueva característica la aplicación de PCA a una compone3nte, a las tres variables que presentan un alto grado de correlación emp_var_rate,euribor3m y nr_employed. Para una mejor descrippción de las variables vease [link](https://github.com/Leomorya/-MLDS6project/blob/master/docs/data/data_dictionary.md)


## Variable objetivo

La variable objetivo simplemente se denota como y, la cual, es la aceptación del crédito (1) o la no aceptación (0), por parte del cliente. Esta presenta un fuerte desbalanceo.

## Evaluación del modelo

Para la evaluación de este modelo se utiliza principalmente la métrica F1_score,ya que combina las métricas precisión y recall, y nos da una idea que que tan bueno fue el clasificador para clasificar la clase positiva y sus errores de Falsos positivos y Falsos negativos.

Sin embargo se vera la matriz de confusión y las métricas accuracy, precisión y recall.

### Métricas de evaluación

Las métricas que se utilizaron para evaluar el modelo, fueron  precisión, recall y f1_score, siendo esta ultima la que, mostro mejores resultados. 

### Resultados de evaluación

|modelo base|clase|precisión|recall|f1_score|
|:---:|:---|:---|:---|:---|
|regresión logistica|positiva:1|0.33|0.64|0.44|
|regresión logistica|negativa:0|0.95|0.84|0.89| 

## Análisis de los resultados
De la métrica f1_score se desprende la probabilidad de que al escojer un cliente que el modelo escoja o prediga en la clase positiva (1), tiene una probabilidad de 33% de pertenecer a dichas clase, lo que estas, un 22% mas alto que la probabilidad aleatoria la cual, es de 11%.  


## Conclusiones

Del modelamiento base se obtuvieron las siguientes conclusiones:

* La metrica de evaluacion que obtiene mejor desempeño es la f1_score, esto es debido al fuerte desbalanceo de clases

* La probabilidad aleatoria de que se contacte a un cliente y este acepte el credito es de p = 855/7623 = 0.11 osea del 11%, mientras que, con el modelo aumenta a p(m)= 544/1599 = 0.34 entonces, es del 33%, lo que es, una notable mejora.

* Probar mas modelos a ver si se encuentra una m,ejora notable, tales como, arboles de decisión, maquinas de soporte y/o redes neuronales. 
## Referencias

El notebook con el modelo base se encuentra en el siguinte link [modelo_base](https://github.com/Leomorya/-MLDS6project/blob/entrega_tres/scripts/training/modelo_linea_base.ipynb) 
