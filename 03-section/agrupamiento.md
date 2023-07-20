# Agrupación

El agrupamiento es la tarea de dividir la población o los puntos de datos en varios grupos, de modo que los puntos de datos en los mismos grupos sean más similares a otros puntos de datos en el mismo grupo que a los de otros grupos. En palabras simples, el objetivo es segregar grupos con rasgos similares y asignarlos en grupos.

![](https://static.javatpoint.com/tutorial/machine-learning/images/k-means-clustering-algorithm-in-machine-learning.png)

## El algoritmo k-means
K-means es un algoritmo de clasificación no supervisada (clusterización) que agrupa objetos en k grupos basándose en sus características. El agrupamiento se realiza minimizando la suma de distancias entre cada objeto y el centroide de su grupo o cluster. Se suele usar la distancia cuadrática.

El algoritmo consta de tres pasos:

    Inicialización: una vez escogido el número de grupos, k, se establecen k centroides en el espacio de los datos, por ejemplo, escogiéndolos aleatoriamente.
    Asignación objetos a los centroides: cada objeto de los datos es asignado a su centroide más cercano.
    Actualización centroides: se actualiza la posición del centroide de cada grupo tomando como nuevo centroide la posición del promedio de los objetos pertenecientes a dicho grupo.

Se repiten los pasos 2 y 3 hasta que los centroides no se mueven, o se mueven por debajo de una distancia umbral en cada paso.

![](https://www.unioviedo.es/compnum/laboratorios_py/new/d1.png)


## Aplicaciones
La agrupación en clústeres de K-Means es el algoritmo de aprendizaje automático no supervisado más común. Es ampliamente utilizado para muchas aplicaciones que incluyen:

        Segmentación de imagen

        Segmentación de clientes

        Agrupación de especies

        Detección de anomalías

        Lenguajes de agrupamiento

## Intuición de agrupamiento de K-Means

La agrupación en clústeres de K-Means se utiliza para encontrar grupos intrínsecos dentro del conjunto de datos sin etiquetar y extraer inferencias de ellos. Se basa en el agrupamiento basado en el centroide.

**Centroide:** un centroide es un punto de datos en el centro de un clúster. En el agrupamiento basado en centroide, los clústeres se representan mediante un centroide. Es un algoritmo iterativo en el que la noción de similitud se deriva de lo cerca que está un punto de datos del centroide del grupo. El agrupamiento de K-Means funciona de la siguiente manera: El algoritmo de agrupamiento de K-Means utiliza un procedimiento iterativo para entregar un resultado final. El algoritmo requiere el número de grupos K y el conjunto de datos como entrada. El conjunto de datos es una colección de características para cada punto de datos.


## Elegir el valor de K

El algoritmo K-Means depende de encontrar la cantidad de grupos y etiquetas de datos para un valor predefinido de K. Para encontrar la cantidad de grupos en los datos, necesitamos ejecutar el algoritmo de agrupación en clústeres K-Means para diferentes valores de K y comparar los resultados. Entonces, el rendimiento del algoritmo K-Means depende del valor de K. Debemos elegir el valor óptimo de K que nos brinde el mejor rendimiento. Hay diferentes técnicas disponibles para encontrar el valor óptimo de K. La técnica más común es el método del codo que se describe a continuación.

## El método elbow (codo)

Método elbow (codo) en K-Means

Podemos ver que si K aumenta, la distorsión promedio disminuirá. Luego, cada clúster tendrá menos instancias constituyentes y las instancias estarán más cerca de sus respectivos centroides. Sin embargo, las mejoras en la distorsión promedio disminuirán a medida que aumente K. El valor de K en el que la mejora en la distorsión disminuye más se denomina **codo**, en el que debemos dejar de dividir los datos en grupos adicionales.