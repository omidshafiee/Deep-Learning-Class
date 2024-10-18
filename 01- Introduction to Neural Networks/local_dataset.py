import numpy as np
import os

import tensorflow as tf
from tensorflow import keras
from keras import Sequential
from keras.layers import Input, Dense
from keras.datasets import mnist

import cv2

def load_minst(img_size :int, flatten=False, label_encode=True):
    """
    x_train, y_train, x_test, y_test = load_minst(img_size int)
    
    """
    # load mnist dataset
    (x_train_org, y_train_org), (x_test_org, y_test_org) = mnist.load_data(path='../datasets/mnist.npz')
    x_train_conv = [cv2.resize(img, dsize=(img_size, img_size)) for img in x_train_org]
    x_test_conv = [cv2.resize(img, dsize=(img_size, img_size)) for img in x_test_org]

    # Faltten Image (convert matrix to vector)
    # Model acceptable shape (number of samples, number of features)
    if flatten:
        x_train = np.reshape(x_train_conv, [-1, img_size**2])
        x_test = np.reshape(x_test_conv, [-1, img_size**2])
        print('Date layer flatten image.')
    else:
        x_train = np.reshape(x_train_conv, [-1, img_size, img_size])
        x_test = np.reshape(x_test_conv, [-1, img_size, img_size])
        print('No image flattening.')
        

    # Normalize data
    # use data type = float32 / may study on mixed precison
    x_train = x_train.astype('float32') 
    x_test = x_test.astype('float32') 

    x_train/= 255
    x_test/= 255
    
    if label_encode:
    # One hot labels to use by model [based on soft max]
        y_train = keras.utils.to_categorical(y_train_org, num_classes=10)
        y_test = keras.utils.to_categorical(y_test_org, num_classes=10)
        print('Label converted by One Hot Encoder.')
    else:
        y_train = y_train_org
        y_test  = y_test_org
        
        y_train = y_train.reshape(-1,1)
        y_test = y_test.reshape(-1,1)
        
        print('No label encoding.')
    

    return x_train, y_train, x_test, y_test





