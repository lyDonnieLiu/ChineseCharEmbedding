from PIL import Image, ImageDraw, ImageFont

import numpy as np

def binaryzation(threshold=145):           #降噪，图片二值化
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(255)
    
    return table

def ReadVocab(vocabulary_file,hanstart, hanend):
        
    with open(vocabulary_file, 'r', encoding="utf-8") as f:
        
        for i in range(hanstart):
            c = f.readline().strip()

        for cid in range(hanstart, hanend+1):
            c = f.readline().strip()
            char2id[c] = cid
            id2char[cid] = c
           


def CharMatrix(hanstart, hanend, outputfile, charid2idx_file):
    font = ImageFont.truetype('simkai.ttf', size=40)
    im = Image.new('RGB',(40,40),(255,255,255))
    result = list()
    id = 0
    charid2vecid = list()    
    for i in range(hanstart,hanend+1):
        c = id2char[i]
        draw = ImageDraw.Draw(im)
        draw.text((0, 0), c ,font=font)
        width,height = im.size
        im = im.convert("L")
        im = im.point(binaryzation(), '1')
        data = im.getdata()
        data = np.matrix(data)//255
        new_data = np.reshape(data,(height,width))
        result.append(new_data)
        charid2vecid.append([i,id])
        id += 1
    
    m = np.array(result)
    n = np.array(charid2vecid)
    np.save(outputfile, m)
    np.save(charid2idx_file, n)


char2id = dict()
id2char = dict()
ReadVocab('vocab.txt',671,8102)
CharMatrix(671,8102,'img_data.npy', 'char2vec.npy')


