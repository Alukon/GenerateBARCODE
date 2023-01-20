# pip install python-barcode
# pip install "python-barcode[images]"
# settings in project install pillow
from barcode.writer import ImageWriter
import barcode

ean = barcode.get('ean13', '123456789101', writer=ImageWriter())
filename = ean.save('ean13')


