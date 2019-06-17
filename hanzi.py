# -*- coding: utf-8 -*- #文件也为UTF-8
#!/usr/bin/env python
from PIL import Image, ImageDraw, ImageFont

import numpy as np
# import scipy
import matplotlib.pyplot as plt

<<<<<<< HEAD
font = ImageFont.truetype('Songti.ttc', size=32)
img = Image.new('RGB', (40, 40), (255, 255, 255))
draw = ImageDraw.Draw(img)
c = '一'
draw.text((0, 0), c, (0, 0, 0), font=font)
=======
font = ImageFont.truetype('simkai.ttf', size=40)
img = Image.new('RGB', (40, 40), (255, 255, 255))
draw = ImageDraw.Draw(img)
draw.text((0, 0), u'耄', (0, 0, 0), font=font)
>>>>>>> 7053f3bcb7d89d1d2051e3751ba7548716a5b3a2
#draw.text((0,60),unicode('你好','utf-8'),(0,0,0),font=font)

img.show()
img.save('ni.jpg')
thred = 145

def binaryzation(threshold=145):           #降噪，图片二值化
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(255)
 
    return table

def ImageToMatrix(filename):
    # 读取图片
    im = Image.open(filename)
    # 显示图片
#     im.show()  
    width, height = im.size
    im = im.convert("L")
    im = im.point(binaryzation(145), '1')
    data = im.getdata()
    data = np.matrix(data)//255
    new_data = np.reshape(data, (height, width))
    return new_data
#     new_im = Image.fromarray(new_data)
#     # 显示图片
#     new_im.show()
def MatrixToImage(data):
    data = data*255
    new_im = Image.fromarray(data.astype(np.uint8))
    #new_im.show()
    return new_im



x = ImageToMatrix("ni.jpg")
print("形状:{0}\n数据:{1}".format( x.shape, x))

new_im = MatrixToImage(x)
new_im.show()