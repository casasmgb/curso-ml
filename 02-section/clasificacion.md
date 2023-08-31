# Clasificacion
![](https://miro.medium.com/v2/resize:fit:720/format:webp/1*UgYbimgPXf6XXxMy2yqRLw.png)


Permite clasificar respuestas en base a datos de entrada, en el ejemplo de Predicción de insuficiencia cardíaca, vimos que la salida estaba dada con 1 en caso de que se sufra una amenaza de muerte y 0 en caso contrario.


## Problema
Las respuestas de un modelo de regresión lineal pueden entregar resultados como este:

    0.4    0.499    0.5    0.6

estos resultados podrían tener consecuencias ya que no se tendría una posición certera.


De este ejemplo, se puede inferir que la regresión lineal no es adecuada para el problema de clasificación. La regresión lineal no tiene límites, y esto nos lleva a la regresión logística. Su valor oscila estrictamente entre 0 y 1.

## Tipos de regresion logistica

1. Regresión logística binaria

    La respuesta categórica tiene solo dos 2 resultados posibles. Ejemplo: 0,1

2. Regresión logística multinomial

    Tres o más categorías sin ordenar. Ejemplo: predecir qué alimento se prefiere más (vegetales, cereales, carnes)

3. Regresión logística ordinal

    Tres o más categorías con orden. Ejemplo: calificación de película de 1 a 5


## Límite de decisión

Para predecir a qué clase pertenece un dato, se puede establecer un umbral. En base a este umbral, la probabilidad estimada obtenida se clasifica en clases.

Digamos, si **valor_predicho ≥ 0.5**, entonces clasifique la respuesta como 1 y no como 0.

El límite de decisión puede ser lineal o no lineal. El orden polinomial se puede aumentar para obtener un límite de decisión complejo.

## Funcion de costo

![](https://miro.medium.com/v2/resize:fit:640/format:webp/1*TqZ9myxIdLuKNmt8orCeew.png)
