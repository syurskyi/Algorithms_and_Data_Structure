import qrcode
from PIL import Image

img = qrcode.make("https://www.thu.edu.tw")
img.show()

img.save("D:/THU_QRcode.jpg")

