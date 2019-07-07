import numpy as np
import matplotlib.pyplot as plt

x = np.load('img_data.npy')
# y = np.load('char2vec.npy')
trainX = x.reshape([x.shape[0],40,40,1])

plt.imshow(trainX[20][: , :,0])
plt.show()

img = np.load("decoder_vec.npy")
#trainX = img.reshape(img.shape[0], [40, 40, 1])
plt.imshow(img[20][:, :, 0])
plt.show()
