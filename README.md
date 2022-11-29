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

## Implementación


### Librerías utilizadas

Face Recognition: Se realiza el uso de las funciones face_encodings y face_distance.
Rtree: Métodos de indexación espacial para Python.

### Dataset
Se usará una colección de 13 mil imágenes de rostros de personas aproximadamente extraídas de Labeled Faces in the Wild.

### Construccion del indice Rtree
Para construir el índice Rtree, se usó la librería Rtree de python para aplicar los métodos de indexación para los vectores característicos.

### Algoritmo de búsqueda KNN

#### KNN-Secuencial
Es importante denotar, para el KNN Secuencial, que está implementado en memoria principal. El procedimiento es el siguiente: se indexa las caras conocidas hasta "n" y llevamos un contador. Una vez que hemos llegado a "n", cerramos la indexación en memoria y se pasa esta información en un bucle for a la función de la librería Face Recognition face_distance. Agregaremos las distancias correspondientes a una estructura heap queue, con la cual finalmente retornaremos los K resultados más cercanos a nuestra query. Lo más notorio al realizar la búsqueda secuencial de esta manera, es que la gran mayoría del tiempo utilizado es la primera parte, indexar. Calcular, guardar y retornar los resultados resulta mucho más rápido, como se podrá apreciar en la experimentación realizada.

#### KNN-Rtree
En primer lugar, se usa el índice Rtree guardado, y se asignan los valores necesarios correspondientes. Luego se realiza el encoder de la query a procesar Finalmente, para cada elemento en la lista del query (ya que es posible que existan varias caras), se agrega a la variable que recibe la función de la librería Rtree.

#### KNN-HighD


### Algoritmo de búsqueda por Rango


### Análisis de la maldición de la dimensionalidad 

## Experimentación
