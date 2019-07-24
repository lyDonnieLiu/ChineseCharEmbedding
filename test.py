import numpy as np
import matplotlib.pyplot as plt
import pickle

# x = np.load('img_data.npy')
# y = np.load('char2vec.npy')
# trainX = x.reshape([x.shape[0],40,40,1])

# plt.imshow(trainX[3][: , :,0])
# plt.show()

# img = np.load("decoder_vec.npy")
# trainX = img.reshape(img.shape[0], [40, 40, 1])
# plt.imshow(img[3][:, :, 0])
# plt.show()


with open("char2id_file.txt", 'rb') as f:
    char2id = pickle.load(f)

print(len(char2id))