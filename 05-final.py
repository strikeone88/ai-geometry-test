from keras.models import load_model
import numpy as np
import cv2

def containsPoint(rect, x, y):
    return rect[0] <= x and x <= rect[0]+rect[2] and rect[1] <= y and y <= rect[1]+rect[3]

def containsRect(rect, i):
    return rect != i and containsPoint(rect, i[0], i[1]) and containsPoint(rect, i[0]+i[2], i[1]) and containsPoint(rect, i[0], i[1]+i[3]) and containsPoint(rect, i[0]+i[2], i[1]+i[3])

model = load_model('model.keras')

# Cargar imagen de prueba, convertir a escapa de grises y aplicar umbral adaptativo
original = cv2.imread("prueba.png", cv2.IMREAD_COLOR)
img = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
threshold = cv2.adaptiveThreshold (img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 15, 10)

# Detectar contornos para segmentación
contours, hierarchy = cv2.findContours(threshold, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_TC89_KCOS)
rects = [cv2.boundingRect(i) for i in contours]

# Aislar segmentos dentro del maximo de area y que no contengan otros segmentos
max_area = img.shape[0]*img.shape[1]*0.98
rects = [i for i in rects if i[2]*i[3] < max_area]
rects = [i for i in rects if sum(containsRect(j,i) for j in rects) == 0]

# Iniciar etiquetado de los segmentos
labels = {
    0: "Circulo",
    1: "Rectangulo",
    2: "Triangulo"
}

for rect in rects:
    x1 = rect[0]
    y1 = rect[1]
    x2 = x1 + rect[2]
    y2 = y1 + rect[3]

    # Obtener segmento de la imagen original, redimensionar a 128x128 y normalizar
    input = original[y1:y2, x1:x2]
    input = (255 - input)
    input = cv2.resize(input, (128, 128), interpolation=cv2.INTER_AREA)
    input = input / 255.0

    # Obtener etiqueta del segmento con mayor probabilidad
    output = model.predict(np.array([input]))

    # Marcar el segmento y mostrar la etiqueta
    cv2.rectangle(original, rect, (255,0,0), 1)
    label = labels[np.argmax(output)]
    size = cv2.getTextSize(label, cv2.FONT_HERSHEY_COMPLEX_SMALL, 1.0, 1)
    cv2.putText(original, label, (int((x1+x2-size[0][0])/2), int((y1+y2-size[0][1])/2)), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1.0, (0,0,0))

cv2.imshow("original", original)
cv2.waitKey(0)
cv2.destroyAllWindows()
