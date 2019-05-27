# -*- coding: utf-8 -*- #文件也为UTF-8
#!/usr/bin/env python
from PIL import Image, ImageDraw, ImageFont

import numpy as np

class DataReader:
    def __init__(self, inputFileName, vocabulary_file, maxlength, hanstart, hanend):
        self.char2id = dict()
        self.id2char = dict()
        self.hanstart = hanstart
        self.hanend = hanend
        self.inputFileName = inputFileName
        self.vocabulary_file = vocabulary_file
        self.ReadVocab()

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
        width,height = im.size
        im = im.convert("L")
        im = im.point(binaryzation(145), '1')
        data = im.getdata()
        data = np.matrix(data)//255
        new_data = np.reshape(data,(height,width))
        return new_data
    #     new_im = Image.fromarray(new_data)
    #     # 显示图片
    #     new_im.show()
    def MatrixToImage(data):
        data = data*255
        new_im = Image.fromarray(data.astype(np.uint8))
        #new_im.show()
        return new_im


    def ReadVocab(self):
        
        with open(self.vocabulary_file, 'r', encoding="utf-8") as f:
            c = f.readline().strip()
            cid = 0
            while c:
                self.char2id[c] = cid
                self.id2char[cid] = c
                cid += 1
                c = f.readline().strip()

    def CharMatrix(self):
        font = ImageFont.truetype('simkai.ttf', size=40)
        im = Image.new('RGB',(40,40),(255,255,255))
        
        for i in range(self.hanstart,self.hanend):
            c = self.id2char(i)
            draw = ImageDraw.Draw(im)
            draw.text((0, 0), c, (0,0,0),font=font)
            width,height = im.size
            im = im.convert("L")
            im = im.point(binaryzation(), '1')
            data = im.getdata()
            data = np.matrix(data)//255
            new_data = np.reshape(data,(height,width))


