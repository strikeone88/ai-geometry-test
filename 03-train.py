import tensorflow as tf
import numpy as np
import os

from keras.layers import Dense, Convolution2D, MaxPooling2D, Flatten
from keras.models import Sequential

NUM_SAMPLES = 200
NUM_CLASSES = 3

X = np.zeros(shape=(128,128,3), dtype='float64')
Y = np.zeros(shape=(3), dtype='float64')

# ******************************
# Arquitectura de red.

# Inicia con 128x128x3
model = Sequential([
	Convolution2D(32, (5,5), activation='relu'),    # 124x124x32
	MaxPooling2D((4, 4)),                           # 28x28x32
	Flatten(),                                      # 25,088
	Dense(256, activation='relu'),                  # 256
	Dense(Y.shape[-1])                              # 3
])

model.compile(optimizer='adam', loss='mean_squared_error', metrics=['accuracy'])

# Cargar datos de entrenamiento.
print('🧪 Cargando datos ...', end='')
samples = [
    file[1:-4] for file in os.listdir('training/numpy/')
    if file.startswith('X') and file.endswith('.npy')
]
print('\r🧪 Cargando datos ... ' + str(len(samples)))

X = []
Y = []
for id in samples:
    X.append(np.load('training/numpy/X'+id+'.npy'))
    Y.append(np.load('training/numpy/Y'+id+'.npy'))

X = np.array(X)
Y = np.array(Y)

print('🧪 Entrenando ...')
model.fit(x=X, y=Y, batch_size=32, epochs=15, verbose=1)

print('\n\n')
model.summary()
model.save('model.keras')
