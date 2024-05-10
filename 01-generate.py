from PIL import Image, ImageDraw
import random
import os

# Número de imagenes a generar por categoría.
N = 200

# Crear carpeta de entrenamiento.
if not os.path.exists('training/set'):
    os.makedirs('training/set')

# Generar triangulos.
print('')
for i in range(1, N+1):
    image = Image.new('RGBA', (256, 256))
    draw = ImageDraw.Draw(image)
    draw.rectangle((0, 0, 255, 255), fill=(0,0,0,255))
    p0 = (random.randint(0,256), random.randint(0,256))
    p1 = (random.randint(0,256), random.randint(0,256))
    p2 = (random.randint(0,256), random.randint(0,256))
    print('🧪 Creando triangulos ...', i, end='\r')
    draw.polygon([p0,p1,p2], fill=(random.randint(20,255),random.randint(20,255),random.randint(20,255),255))
    image.save('training/set/'+str(i).zfill(4)+'_T.png')
    del draw
    del image

# Generar circulos.
print('')
for i in range(1, N+1):
    image = Image.new('RGBA', (256, 256))
    draw = ImageDraw.Draw(image)
    draw.rectangle((0, 0, 255, 255), fill=(0,0,0,255))
    w = random.randint(10,250)
    h = random.randint(10,250)
    x = random.randint(0,256-w)
    y = random.randint(0,256-h)
    print('🧪 Creando circulos ...', i, end='\r')
    draw.ellipse((x, y, x+w, y+h), fill=(random.randint(20,255),random.randint(20,255),random.randint(20,255),255))
    image.save('training/set/'+str(i).zfill(4)+'_C.png')
    del draw
    del image

# Generar rectangulos.
print('')
for i in range(1, N+1):
    image = Image.new('RGBA', (256, 256))
    draw = ImageDraw.Draw(image)
    draw.rectangle((0, 0, 255, 255), fill=(0,0,0,255))
    w = random.randint(10,250)
    h = random.randint(10,250)
    x = random.randint(0,256-w)
    y = random.randint(0,256-h)
    print('🧪 Creando rectangulos ...', i, end='\r')
    draw.rectangle((x, y, x+w, y+h), fill=(random.randint(20,255),random.randint(20,255),random.randint(20,255),255))
    image.save('training/set/'+str(i).zfill(4)+'_R.png')
    del draw
    del image

print('\n✨ Finalizado')
