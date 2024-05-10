## Configuración del Proyecto

1.- Crear una virtual environment de Python
```sh
python -m venv .venv
```

2.- Activar la virtual environment
```sh
.venv\Scripts\activate
```

3.- Instalar las dependencias, vamos usar OpenCV, Keras, Tensorflow, Numpy y Pillow.
```sh
pip install -r requirements.txt
```

<br/>

## Creación de Imágenes de Entrenamiento

Para entrenar la red se deben tener muchas imágenes de muestra de figuras como triangulos, rectangulos y circulos en diferentes posiciones. Se pueden obtener de internet, o dibujarlas a mano, pero como se necesitan bastantes -digamos unas 100+ de cada figura- vamos a generarlas. Ejecutar el comando:

```sh
python 01-generate.py
```

Se van a generar 200 imágenes aleatorias de triangulos, rectangulos y circulos en la carpeta `training\set`, los archivos tienen nombre XXXX_Z.png donde "XXXX" es un número desde 0001 hasta 0200 y el "Z" nos indica que tipo de figura es: C=Circulo, R=Rectángulo, T=Triángulo.

<br/>

## Convertir Imágenes a Vectores

Ahora debemos convertir todas las imágenes a arreglos de NumPy (vectores) porque asi vamos a poder procesarlos. Para eso se debe ejecutar:

```sh
python 02-convert.py
```

Al realizar esto se van a convertir todas las imágenes de la carpeta `training\set` en vectores que se guardan en la carpeta `training\numpy` junto con su vector de salida (ver `02-convert.py` para más información). Al final deben quedar 600 archivos con nombre `Xnnnn.npy` y `Ynnnn.npy` donde "nnnn" es un numero desde 0000 hasta 0599.

<br/>

## Entrenamiento

El entrenamiento puede tardar varios minutos. Se debe contar con suficientes recursos de procesamiento para completar este paso. En caso de no poder realizar este paso se puede utilizar el modelo ya pre-entrenado usando el archivo `pretrained_model.keras`.

Para iniciar el entrenamiento ejecutar:

```sh
python 03-train.py
```

El entrenamiento tomará 10 épocas, y la arquitectura de la red neuronal es:

- Capa de Convolución de 5x5 y 8 filtros (ReLU)
- Capa de Pooling 4x4
- Capa de Aplanamiento
- Capa Densa n=256 (ReLU)
- Capa Densa n=3

La entrada es un arreglo de 128x128x3 que representa la imagen, y la salida es un vector 1x3 que representa la clase de la figura:

 - (1, 0, 0) → Círculo
 - (0, 1, 0) → Rectángulo
 - (0, 0, 1) → Triángulo

Al haber finalizado el entrenamiento el archivo `model.keras` será creado en la misma carpeta.

<br/>

## Prueba

Teniendo el modelo entrado vamos a realizar una prueba rápida. Primeramente debemos copiar algunas imágenes de `training/set` a la carpeta `training/test`, o bien podemos hacer nuestras propias imágenes de prueba.

En caso de querer utilizar el modelo pre-entrenado cambiarle el nombre al archivo `pretrained_model.keras` a `model.keras`. 

Para realizar la prueba vamos a ejecutar:

```sh
python 04-test.py
```

Este script tomará las imágenes de la carpeta `training\test` y va a mostrar el vector de salida que la red neuronal predijo. Algo como:

```sh
🧪 0001_R.png
Circulo: -0.06, Rectangulo: 1.02, Triangulo: 0.03

🧪 0008_R.png
Circulo: -0.02, Rectangulo: 1.02, Triangulo: -0.02

🧪 0018_C.png
Circulo: 0.98, Rectangulo: -0.00, Triangulo: 0.02

🧪 0035_C.png
Circulo: 0.96, Rectangulo: -0.01, Triangulo: 0.04

🧪 0046_R.png
Circulo: 0.01, Rectangulo: 1.03, Triangulo: -0.07

🧪 0058_R.png
Circulo: -0.00, Rectangulo: 1.02, Triangulo: -0.00

🧪 0071_R.png
Circulo: -0.01, Rectangulo: 1.02, Triangulo: -0.01

🧪 0088_T.png
Circulo: 0.01, Rectangulo: -0.01, Triangulo: 0.97
```

<br/>

## Prueba Final

Es hora de la prueba final! Para eso vamos a utilizar la imagen "prueba.png" que está en la carpeta de inicio. Esta imagen contiene varias figuras geométricas y vamos a probar si el modelo logra detectarlas de manera correcta.

```sh
python 05-final.py
```
