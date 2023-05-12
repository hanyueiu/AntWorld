import cv2
from PIL import Image, ImageDraw

img = Image.new("RGBA", (200, 30), (0, 0, 0, 0))
Draw = ImageDraw.Draw(img)
Draw.text(xy=(20, 10), text='Randint', fill='white')
Draw.text(xy=(80, 10), text='Randint', fill='white')
Draw.text(xy=(140, 10), text='Randint', fill='white')
img.save("bg.png")
img.show()
