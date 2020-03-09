import tensorflow as tf
import numpy as np
import os
import boto3
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Flatten
from tensorflow.keras.layers import Embedding
from tensorflow.keras.layers import Conv1D
from tensorflow.keras.layers import GlobalMaxPool1D


print ("Entering model cnn file")

def keras_model_fn(_, config):

    embeddings_index = dict()
    file = open(config["embeddings_path"], encoding="utf-8") 
    for i in file:
        values = i.split()
        word = values[0]
        coefs = np.array(values[1:], dtype='float32')
        embeddings_index[word] = coefs
    file.close()

    vocab_size = config["embeddings_dictionary_size"]

    words_rows = len(embeddings_index.keys())
    columns = config['embeddings_vector_size']
    matrix_emb = np.zeros((words_rows,columns))

    for index, key in zip(range(0, words_rows), embeddings_index.keys()):
        matrix_emb[index] = embeddings_index[key]

    model = Sequential()
    model.add(Embedding(config['embeddings_dictionary_size'], config['embeddings_vector_size'], weights=[matrix_emb], name='embedding', input_length=config['padding_size'], trainable=True))
    model.add(Conv1D(filters = 100, kernel_size = 2,activation = 'relu', padding = 'valid', strides = 1,))
    # model.add(GlobalMaxPool1D )
    model.add(Conv1D(filters = 50, kernel_size = 3,activation = 'relu', padding = 'valid', strides = 1,))
    model.add(Conv1D(filters = 20, kernel_size = 2,activation = 'relu', padding = 'valid', strides = 1,))
    model.add(Flatten())
    model.add(Dense(100, activation = 'relu'))
    model.add(Dense(1, activation = 'sigmoid', name ='score'))
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    cnn_model = model
    return cnn_model


def load_embeddings(embeddings_path, embeddings_dictionary_size, embeddings_vector_size):

    s3_file = False

    if 's3://' in embeddings_path:
        s3_file =  True
        s3_client = boto3.client('s3')
        path_split = embeddings_path.replace('s3://', "").split('/')
        bucket = path_split.pop(0)
        key = '/'.join(path_split)

        data = s3_client.get_object(Bucket= bucket, Key = key)
        embeddings_file = data['Body'].iter_lines()

    else:
        embeddings_file = open(embeddings_path, 'r')

    # return matrix_emb

# def save_model(model, output):

#     model.save(output)
#     print("Model successfully saved_model at: {}".format(output))



def save_model(model, output):

    """
    Method to save a model in SaveModel format with signature to allow for serving

    """

    print("Saving model...")

    tf.saved_model.save(model, os.path.join(output, "1"))

    print("Model successfully saved at: {}".format(output))

