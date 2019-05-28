from PIL import Image, ImageDraw, ImageFont

import numpy as np
import pickle

def binaryzation(threshold=145):           #降噪，图片二值化
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(255)
    
    return table

def ReadVocab(vocabulary_file,hanstart, hanend, char2id_file, id2char_file):
    """Read vocabulary file into dictionary char2id and id2char

    Args:
    hanstart, hanend: The number of the first and last Chinese characters in vocabulary
    """    
    char2id = dict()
    id2char =dict()
    with open(vocabulary_file, 'r', encoding="utf-8") as f:
        
        for i in range(hanstart):
            c = f.readline().strip()

        for cid in range(hanstart, hanend+1):
            c = f.readline().strip()
            char2id[c] = cid
            id2char[cid] = c
    
    with open(char2id_file, 'wb') as f:
        pickle.dump(char2id, f)
    with open(id2char_file, 'wb') as f:
        pickle.dump(id2char, f)



def CharMatrix(hanstart, hanend, id2char_file,
outputfile, charid2idx_file):
    """
    Convert every Chinese character to 2-value array, and save them in outputfile.

    Args:
    hanstart, hanend: The number of the first and last Chinese characters in vocabulary.
    outputfile: the saved 2-value arrays file.
    charid2idx_file: Map the number of Chinese characters in vacabulary file to index in the saved 2-valued arrays.
    id2char_file: a pickle file that saved id2char dict.
    """

    font = ImageFont.truetype('simkai.ttf', size=40)
    im = Image.new('RGB',(40,40),(255,255,255))
    result = list()
    id = 0
    charid2vecid = dict()

    with open(id2char_file, 'rb') as f:
        id2char = pickle.load(f)

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
        charid2vecid[i] = id
        id += 1
    with open(charid2idx_file, 'wb') as f:
        pickle.dump(charid2vecid, f)

    m = np.array(result)
    np.save(outputfile, m)


#ReadVocab('vocab.txt',671,8102,'char2id_file.txt','id2char_file.txt')
#CharMatrix(671,8102,'id2char_file.txt','img_data.npy', 'charid2idx_file.txt')


#     new_im = Image.fromarray(new_data)
#     # 显示图片
#     new_im.show()
def MatrixToImage(data):
    data = data*255
    new_im = Image.fromarray(data.astype(np.uint8))
    #new_im.show()
    return new_im

with open('char2id_file.txt', 'rb') as f:
    char2id = pickle.load(f)

with open('charid2idx_file.txt', 'rb') as f:
    charid2idx = pickle.load(f)

ch = '年'
charid = char2id[ch]
idx = charid2idx[charid]
imgdata = np.load('img_data.npy')
d = imgdata[idx]
im = MatrixToImage(d)
im.show()