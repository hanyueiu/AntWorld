import cv2
from PIL import Image, ImageDraw, ImageFont

# YYH PIL.ImageDraw创建图像并绘制线，多边形，圆，椭圆 https://blog.csdn.net/JBY2020/article/details/125381667
img = Image.new("RGBA", (300, 30), (0, 0, 0, 0))

Draw = ImageDraw.Draw(img)

Draw.text(xy=(30, 10), text='Randint', fill='white')
Draw.text(xy=(130, 10), text='Randint', fill='white')
Draw.text(xy=(230, 10), text='Randint', fill='white')
Draw.line((0, 20, 300, 20), fill="white", width=3)

img1 = Image.open("img001.png")
rgba_channel = img1.split()
# Draw.bitmap((10, 0), rgba_channel[0], fill=(255, 255, 255))
# Draw.bitmap((10, 0), rgba_channel[1], fill=(0, 255, 0))
# Draw.bitmap((10, 0), rgba_channel[2], fill=(0, 0, 255))
# img.paste(img, (50, 0), img1)
#
#
# # 从PIL.Image.Image对象获取图片的二维坐标
# x, y = img.size
# #
# for i in range(x):
#     # if 50 < i < 255:
#     #     continue
#     for k in range(y):
#         # 获取图片的颜色
#         color = img.getpixel((i, k))
#
#         color = color[:-1] + (0,)
#         # 在对应的坐标设置图片的颜色
#         img.putpixel((i, k), color)
img.save("img002.png")
img.show()
