## BD3 - Grupo 4

**_Integrantes:_**

- Salazar Alva, Rodrigo Gabriel
- Sara Junco, Juan Sebastian 
- Ponce Contreras, Luis Eduardo
- Lapa Carhuamaca, Arleth Ivhy

---
# Proyecto 3 | Bases de Datos Multimedia

## Introducción

El objetivo de este proyecto es aplicar algoritmos de búsqueda y recuperación de la información eficiente de imágenes, para ello se implementa un servicio web de reconocimiento facial para personas a partir de una colección grande de imágenes de rostros humanos. El proceso de generar dicha aplicación  contempla tres pasos, los cuales son: Extracción de características, Indexación de vectores característicos para búsquedas eficientes y aplicación del algoritmo de búsqueda KNN.  Estos procedimientos forman el backend, mientras que, para una interacción con los usuarios se realizó el frontend, en el cual puede realizar una consulta con una foto externa y retorna el top-k de las imágenes más parecidas.


### Algoritmo de búsqueda KNN

#### KNN-Secuencial
Es importante denotar, para el KNN Secuencial, que está implementado en memoria principal. El procedimiento es el siguiente: se indexa las caras conocidas hasta "n" y llevamos un contador. Una vez que hemos llegado a "n", cerramos la indexación en memoria y se pasa esta información en un bucle for a la función de la librería Face Recognition face_distance. Agregaremos las distancias correspondientes a una estructura heap queue, con la cual finalmente retornaremos los K resultados más cercanos a nuestra query. Lo más notorio al realizar la búsqueda secuencial de esta manera, es que la gran mayoría del tiempo utilizado es la primera parte, indexar. Calcular, guardar y retornar los resultados resulta mucho más rápido, como se podrá apreciar en la experimentación realizada.

#### KNN-Rtree
En primer lugar, se usa el índice Rtree guardado, y se asignan los valores necesarios correspondientes. Luego se realiza el encoder de la query a procesar Finalmente, para cada elemento en la lista del query (ya que es posible que existan varias caras), se agrega a la variable que recibe la función de la librería Rtree.

#### KNN-HighD
Para esta implementación, se ha utilizado la estructura del KDTree, la cual consiste en ser una estructura de datos espacial para organizar ciertos puntos en un espacio de K - Dimensiones. Precisamente utilizamos esta estructura, ya que sus propiedades son óptimas para realizar una búsqueda de clave multidimensional, ya sea una búsqueda por rango o una búsqueda de vecinos más cercanos y a su vez este crea una gran nube de puntos. Para este caso, explicaremos el paso a paso de como funciona el algoritmo de búsqueda KNN en el KDTree. En primer lugar, debemos entender que cada nivel del KDTree tiene un eje que representa a los nodos, por ejemplo la raíz representa la partición en el eje X y sus hijos representan la partición en el eje Y. Dicha propiedad será aprovechada para el desarrollo de este algoritmo. Ahora, este algoritmo se ejecuta desde la raíz del árbol, básicamente se mueve recursivamente hacia abajo del árbol, simulando la inserción de un punto en el KDTree. Una vez que se llega un nodo hoja, este se verifica con respecto a su distancia hacia la query y la "mejor distancia actual", si este es menor se actualiza la mejor distancia con la del nodo hoja, caso contrario se sigue evaluando. Sin embargo, este algoritmo no solo se enfoca en evaluar el cuadrante en donde se encuentra la query, sino que este puede evaluar otras particiones del cuadrante contrario y conforme sea la distancia de la query con las regiones o sus puntos, se evaluara si se actualiza la mejor distancia. De esta forma, conseguimos los K vecinos más cercanos.

#### Range Search HighD
La búsqueda por rango en un KDTree es muy particular, ya que esta aprovecha las propiedades dimensionales de la estructura. Por ende, este algoritmo se realizará primero tomando la región que empieza desde la raíz y verificar si esta intersecta con el rango de evaluación, si la respuesta es afirmativa, entonces se procede a acceder a sus hijos, las cuales tendrán una región diferente de partición y de nuevo se verificará si alguno de sus hijos intersecta con el rango, de no ser posible con uno de sus hijos, ya no se sigue bajando con ese respectivo nodo. El objetivo de este algoritmo, es poder llegar a las hojas en donde se encontrarán los puntos de evaluación y poder obtener los que se encuentran dentro del rango a través de verificaciones con sus regiones de partición.

### Análisis de la maldición de la dimensionalidad 

Dentro de Machine Learning a medida que se tiene un conjunto de datos con muchas dimensiones, es decir datos con múltiples características provoca dos principales errores, estos son:
La distancia entre los datos aumenta cuando el número de dimensiones aumenta. 
La variabilidad disminuye exponencialmente con el número de dimensiones.

Para esto, existen algunas soluciones óptimas para poder afrontar esta problemática, estas son las siguientes: 
Reducir o disminuir el número de dimensiones.
Aumentar el número de datos.

#### Técnicas de reducción de dimensionalidad

##### Principal Component Analysis (PCA) 

Consiste en mantener solo las características dimensionales que tienen la mayor parte de la varianza y descartar las dimensiones que contienen una varianza casi nula, capturando de esta manera la dirección de máxima varianza, dándose así esta reducción de dimensionalidad de las características de datos. Devuelve P componentes principales en un rango de 1 a N características originales, ordenadas en base a  cuáles características representan mayor varianza.
  
##### Linear Discriminant Analysis (LDA) 
Consiste en explícitamente intentar modelar la diferencia entre las clases de datos. Cada componente busca maximizar la separabilidad entre las diferentes clases, minimizando a su vez la distancia entre elementos de una misma clase. Devuelve L ejes en un rango de 1 a C-1 clases, ordenadas en base a cuanta separabilidad representan.
   
   
## Experimentación

Se realizaron 3 pruebas, cada una con un respectivo algoritmo KNN-RTree, KNN-secuencial y el KNN-HighD sobre una colección de objetos de tamaño N y el valor constante de k = 8. Se comparó los resultados en la siguiente tabla:


|           | KNN-Secuencial | KNN-RTree | KNN-HighD |
|-----------|----------------|-----------|-----------|
| N = 100   |                |           |           |
| N = 200   |                |           |           |
| N = 400   |                |           |           |
| N = 800   |                |           |           |
| N = 1600  |                |           |           |
| N = 3200  |                |           |           |
| N = 6400  |                |           |           |
| N = 12800 |                |           |           |


#### Aplicación web
Para visualizar los resultados implementamos una pequeña aplicación web usando Flask para el servidor y React para el frontend. A continuación se muestra la interfaz.

///INSERTAR FOTO DE LA APP

