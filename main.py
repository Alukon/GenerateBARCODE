# pip install python-barcode
# pip install "python-barcode[images]"
# settings in project install pillow
from barcode.writer import ImageWriter
import barcode

# ean = barcode.get('ean13', '123456789101', writer=ImageWriter())
# filename = ean.save('ean13')
# генератор штрихкода------------------------------

# pip install pyzbar
from pyzbar.pyzbar import decode
from PIL import Image

image = Image.open('Кот.png')
decoded = decode(image)
print(decoded[0].data.decode('utf-8'))
# считыватель штрихкода------------------------------


