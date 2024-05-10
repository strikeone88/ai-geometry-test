import numpy as np
import cv2, os

# Crear carpeta de salida.
if not os.path.exists('training/numpy'):
    os.makedirs('training/numpy')

# Vectores de salida (Y)
output = {
    'C': (1.0, 0.0, 0.0),
    'R': (0.0, 1.0, 0.0),
    'T': (0.0, 0.0, 1.0)
}

# Obtener los archivos que vamos a procesar.
input_path = "training/set"
files = [
    os.path.join(input_path,f) for f in os.listdir(input_path) 
    if os.path.isfile(os.path.join(input_path, f))
]

# Convertir los archivos de imagen a vectores RGB normalizados (X).
for i in range(0, len(files)):
    print('🧪 Procesando ', i+1, '/', len(files), '...', end='\r')

    # Obtener tipo de figura (C, R, T), eso lo indica el 
    # carácter en la posición 5 desde el final del nombre del archivo.
    type = files[i][-5]

    # Leer imagen de entrada.
    input = cv2.imread(files[i], cv2.IMREAD_COLOR)

    # Cambiar tamaño a 128x128
    input = cv2.resize(input, (128, 128), interpolation=cv2.INTER_AREA)

    # Normalizar a valores entre [0, 1]
    input = input / 255.0

    # Guardar vector de entrada (X) y salida (Y).
    np.save('training/numpy/X'+str(i).zfill(4)+'.npy', input)
    np.save('training/numpy/Y'+str(i).zfill(4)+'.npy', output[type])

print('')
print('✨ Finalizado')
