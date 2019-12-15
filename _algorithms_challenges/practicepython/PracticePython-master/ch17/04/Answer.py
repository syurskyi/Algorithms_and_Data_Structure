## 搜尋 python image mirror
from PIL import Image
import matplotlib.pyplot as plt

img = Image.open("bird.jpg")
flip_img = img.transpose(Image.FLIP_LEFT_RIGHT)

flip_img.show()
