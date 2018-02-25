import numpy as np
import tflearn

#from tflearn.data_utils import to_categorical, pad_sequences, load_

# NOTE: Preprocessing for the dataset already accomplished in the previous files

'''
train, test, _ = imdb.load_dat(path = 'imdb.pkl', n_words= 10000, valid_portion= .1) #10% validation set, pkl for a bytestream

trainX, trainY = train
testX, testY = test

#Data preprocessing vectorize
#Sequence padding
trainX= pad_sequences(trainX, maxlen=100, value=0.)
testX = pad_sequences(testX, maxlen=100, value=0.)
'''
data, target = tflearn.data_utils.load_csv('final.csv', target_column=4,has_header=True)
'''
def preprocess(tweets, columns_to_delete):
    # Sort by descending id and delete columns
    for column_to_delete in sorted(columns_to_delete, reverse=True):
        [tweet.pop(column_to_delete) for tweet in tweets]
    return np.array(tweets, dtype=np.float32)

to_ignore=[3]
'''
#data = preprocess(data, to_ignore)
target = np.reshape(target, (10320,1))



# Build deep neural network
net = tflearn.input_data(shape=[None, 4])
net = tflearn.fully_connected(net, 32)
net = tflearn.fully_connected(net, 32)
net = tflearn.fully_connected(net, 1, activation='linear')
net = tflearn.regression(net, optimizer='adam', learning_rate=0.01,loss='mean_square', name='target')


model = tflearn.DNN(net)
# Start training (apply gradient descent algorithm)
model.fit(data, target, show_metric=True, n_epoch=5, batch_size=16, validation_set=0.1)

'''
trainY = to_catagorical(trainY, nb_classes=2)
testY = to_categorical(testY , nb_classes=2)

#Network building
net = tflearn.input_data([None, 100]) #input layer
net = tflearn.embedding(net, input_dim = 10000, output_dim= 128) #embedding layer
net = tflearn.lstm(net, 128, dropout=0.8)
net = tflearn.fully_connected(net , 2, activation='softmax') #squish to output the probability
net = tflearn.regression(net, optimizer='adam', learning_rate=0.0001, loss='catagorical_crossentropy')

#Training
model = tflearn.DNN(net, tensorboard_verbose=0)
model.fit(trainX, trainY, validation_set(testX, testY), show_metric=True, batch_size=32)
'''

# Testing Phase

bad = [ 2000, .67, .55, 2]
good = [ 100000, -.65, .35, 3]

pred = model.predict([bad, good])
print("Tweet 1 difference value:", pred[0][0])
print("Tweet 2 difference value:", pred[1][0])
