from bert_embedding import BertEmbedding
from keras.models import Sequential
from keras.preprocessing import sequence
from keras.layers import  Bidirectional
from keras.layers import Dense, Dropout, Embedding
from keras.layers import LSTM, Activation, Input
import tensorflow as tf
import keras
import csv
import numpy as np
import pickle
from sklearn.preprocessing import MinMaxScaler
import sys
import os
from collections import namedtuple
from keras_bert import load_vocabulary, load_trained_model_from_checkpoint, Tokenizer

print('This demo demonstrates how to load the pre-trained model and extract word embeddings')

def get_checkpoint_paths(model_path):
    CheckpointPaths = namedtuple('CheckpointPaths', ['config', 'checkpoint', 'vocab'])
    config_path = os.path.join(model_path, 'bert_config.json')
    checkpoint_path = os.path.join(model_path, 'model.ckpt-0')
    vocab_path = os.path.join(model_path, 'vocab.txt')
    return CheckpointPaths(config_path, checkpoint_path, vocab_path)

model_path = '../myBert/output'

classes = 2
maxlen = 50
train_file = '../myBert/dataset/train.tsv'
test_file = '../myBert/dataset/test.tsv'
AddImgFeature = True

paths = get_checkpoint_paths(model_path)

model = load_trained_model_from_checkpoint(paths.config, paths.checkpoint, seq_len=maxlen)
model.summary(line_length=120)

token_dict = load_vocabulary(paths.vocab)

tokenizer = Tokenizer(token_dict)

#loaded_embedding = BertEmbedding(model="bert_12_768_12", dataset_name='wiki_cn', params_path='../myBert/bert_12_768_12_wiki_cn-885ebb9a.params', max_seq_length=maxlen)

def read_tsv(input_file, quotechar=None):
    """Reads a tab separated value file."""
    with tf.gfile.Open(input_file, "r") as f:
        reader = csv.reader(f, delimiter="\t", quotechar=quotechar)
        lines = []
        for line in reader:
            lines.append(line)
        return lines
#load image feature and normalize into [-1, 1]
img_feature = np.load("latent_vec.npy")
s_scaler = MinMaxScaler(feature_range=(-1,1))
standard_img_feature = s_scaler.fit_transform(img_feature)

with open("char2id_file.txt", 'rb') as f:
    char2id = pickle.load(f)

def char_embedding(input_file, max_word=50, classes=2):
    """Return char embedding given a Chinese doc, shape:(maxlen, 768)."""
    lines = read_tsv(input_file)
    x = list()
    y = list()
    sentences = list()
    for line in lines:
        sentences.append(line[0])
        y.append(line[1])
    #对于文档中的每个句子调用Bert的嵌入
    #result = loaded_embedding(sentences)
    #将每个句子嵌入截断或补足max_word个，不足的用最后一个embedding补足
    # for r in result:
    #     if(AddImgFeature):
    #         for i, c in enumerate(r[0]):
    #             if c in char2id.keys():
    #                 id = char2id[c] - 671               
    #                 r[1][i] = np.sum([standard_img_feature[id], r[1][i]], axis=0)/2

    #     temp = r[1]
    #     l = len(r[1])
    #     temp = temp[:max_word] + [temp[-1]] * (max_word - l)
    #     x.append(temp)
    for s in sentences:
        tokens = tokenizer.tokenize(s)
        indices, segments = tokenizer.encode(first=s, max_len=maxlen)
        predicts = model.predict([np.array([indices]), np.array([segments])])[0]
        for i, token in enumerate(tokens):
            if token in char2id.keys():
                id = indices[i]-671
                temp = np.sum(standard_img_feature[id],predicts[i])
            x.append(temp)
    
    y = keras.utils.to_categorical(y,num_classes=2)
    assert(len(x)==len(y))
    return np.array(x), np.array(y)

LSTM_Model = Sequential()
LSTM_Model.add(Bidirectional(LSTM(256),input_shape=(maxlen,768,)))
LSTM_Model.add(Dropout(0.5))
LSTM_Model.add(Dense(classes))
LSTM_Model.add(Activation('sigmoid'))

LSTM_Model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

x, y = char_embedding(train_file)
xt, yt = char_embedding(test_file)

history = LSTM_Model.fit(x, y, batch_size=256, epochs=10)
score, acc = LSTM_Model.evaluate(xt, yt,
                            batch_size=256)
print('Test score:', score)
print('Test accuracy:', acc)

with open("test_result"+str(AddImgFeature)+".txt", 'w') as f:
        f.writelines('Test score:'+str(score))
        f.writelines('Test accuracy:'+str(acc))
