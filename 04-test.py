from keras.models import load_model
import numpy as np
import cv2, os

model = load_model('model.keras')
print('')

for filename in [file for file in os.listdir('training/test') if file.endswith('.png')]:
    input = cv2.imread(f'training/test/{filename}', cv2.IMREAD_COLOR)
    input = cv2.resize(input, (128, 128), interpolation=cv2.INTER_AREA)
    input = input / 255.0

    output = model.predict(np.array([input]), verbose=0)
    print("🧪 " + filename)
    print("Circulo: %.2f, Rectangulo: %.2f, Triangulo: %.2f\n" % (output[0][0], output[0][1], output[0][2]))
