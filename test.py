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

# normalization or standardization
#  
from sklearn.preprocessing import StandardScaler, MinMaxScaler

vec = np.load("latent_vec.npy")
s_scaler = MinMaxScaler(feature_range=(-1,1))
#s_scaler = StandardScaler()
standard_vec = s_scaler.fit_transform(vec)

print(standard_vec)
print(np.max(standard_vec), np.min(standard_vec))