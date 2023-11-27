# Apertura de llave de paso en Control Difuso.

En este repositorio se diseña un controlador difuso para controlar y automatizar el nivel de humedad que requieren la gran mayoría de plantas frutales en Colombia.

## EL problema planteado es el siguiente:

¡Imagina que tienes una huerta en tu casa! Te gusta sembrar tu propia comida y plantas de decoración y como eres un buen ingeniero/a, quieres controlar y automatizar el nivel de humedad que requieren tus plantas. Tu tarea es implementar en Python un controlador difuso. 

1. Variables de entrada: 
- Porcentaje de humedad en el suelo. 
- Temperatura en el ambiente. 

2. Variable de salida: 
- porcentaje de apertura de la llave de paso.

## Diseñe un controlador difuso que cumpla los siguientes criterios: 

1. El diseño debe cumplir que a una temperatura de 25°C y un porcentaje de humedad del 50%, la apertura de la llave de paso debe estar aproximadamente en 5%. 
2. la mayoría de plantas prospera cuando el porcentaje de humedad se encuentra entre el 50% y 75%. 
3. Consulta cuales son los rangos de temperatura normales en la región y ubícalos como tu universo de discurso. 
4. Las variables de entrada deben tener como mínimo 4 funciones de membresía cada una.

# Sistema Apertura de llave de paso con Lógica Difusa.

Este sistema de apertura de la llave de paso en Python utiliza lógica difusa para determinar el porcentaje de apertura de acuerdo con las mediciones proporcionadas por los sensores.

## Descripción de contenido.  

1. El código fuente se encuentra en la carpeta "notebooks".

2. las imágenes dadas en simulación se encuentran en la carpeta"Images".

## Descripción.

El sistema de apertura de la llave de paso utiliza lógica difusa para tomar decisiones basadas en dos variables de entrada: Porcentaje de humedad en el suelo y Temperatura en el ambiente. En función de estas variables, el sistema asigna una porcentaje de apertura.

## Requisitos.

Asegúrate de tener Python y las bibliotecas necesarias instaladas. Puedes instalar las bibliotecas requeridas ejecutando en la terminal el siguiente comando: 

pip install numpy scikit-fuzzy matplotlib

Se recomienda simular el código en Visual Studio Code.

## Detalles del Código.

El código se divide en tres partes principales:

1. Definición de las Variables de Entrada y Salida.

Porcentaje de humedad en el suelo y Temperatura en el ambiente son variables de entrada que representan el porcentaje de humedad y temperatura en el ambiente y porcentaje de apertura de la llave de paso es la variable de salida que representa el porcentaje de apertura adecuado.

2. Funciones de Membresía.

Las funciones de membresía definen cómo se relacionan las entradas y la salida, estas están diseñadas en ciertos niveles para proporcionar mayor precisión en la segmentación.

3. Reglas Difusas.

El sistema utiliza reglas difusas para tomar decisiones basadas en las variables de entrada. Las reglas se definen para diferentes combinaciones y niveles de humedad y temperatura.