# Diccionario de datos
A continuación se presenta una descripción de los datos en bruto dados por el banco, para generar el clasificador.

El data set contiene las siguientes columnas de caracteristicas 

 | Nombre | descripción | Tipo de atributo |Tipo de dato  |rango de valores o numero de categorias|
 | :--- | :--- | :--- | :--- | :--- |
 |ID|codigo de identificacion unico|asignado al sujeto|numerico int64|rango [1,23099]|
 |Edad| Edad del cliente|propio del sujeto|numerico int64| rango [18,95]|
 |Tipo_trabajo|Trabajo del cliente|propio del sujeto| categorico object| string 12 categorias |
 |Estado_Civil|Estado civil del cliente| propio del sujeto| categorico  object| string 6 categorias |
 |Educacion| nivel de educacion del cliente| propio del sujeto|categorico object| string 8 categorias |
 |mora|a presentado mora el cliente en un prestamo|asignado al sujeto|categorico object| string 3 categorias |
 |Vivienda|Tiene prestamo de vivienda el cliente|estado del sujeto|categorico object| string 3 categorias |
 |Consumo|Tiene prestamo de Consumo el cliente|estado del sujeto|categorico object| string 3 categorias |
 |Contacto|Tipo de telefono de contacto del cliente|caracteristica del sujeto|categorico object| string 2 categorias|
 |Mes|Mes de ultimo contacto con el cliente|campaña de marketing|categorico object| string 10 categorias |
 |Dia|día del ultimo contacto con el cliente|campaña de marketing|categorico object| string 5 categorias |
 |Campana|numero de contactos realizados con el cliente durante la actual campaña|campaña de marketing |numerico int 64| rango [1,39] |
 | Dias_Ultima_Camp| numero de dias que ha pasado desde la ultima campaña sin contactar al cliente, si nunca a sido contactado 999|caracteristica de contacto del cliente|numerico int 64| rango [1,999]|
 | No_Contactos| numero de veces que ha sido contactado el cliente antes de esta campaña|caracteristica de contacto del cliente|numerico int 64| rango [0,7]|
 | Resultado_Anterior| resultado de la campaña de marketing sobre el cliente| propio de la campaña sobre el cliente|categorico object| string 3 categorias |
 | emp_var_rate| tasa de variacion de empleo, indicador trimestral|social economico |numerico float 64| rango [-3.40,1.4]|
 | cons_price_idx|indice de precios al consumidor, mide la variacion de la canasta familiar mes a mes |social economico |numerico float 64| rango [93.20,94767]|
 | cons_conf_idx|indice de confianza del consumidor, mide la confianza de consumidor sobre la ecomia nacional y personal  |social economico |numerico float 64| rango [-50.8,-26.9]|
 | euribor3m| tasa de prestamos a tres meses entre bancos europeos|social economico |numerico float 64| rango [0.634,5045]|
 |nr_employed	|numero de empleados |desconocido|numerico float 64| rango [7963,5228]|
 |y	|variable objetivo accede al credito o no, binaria |bancaria |numerico int 64| rango [0,1]|
