
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense
from keras.utils import np_utils

"""
load data from keras 
not needed to have the mnist data as file 
mnist data is stored in datasets of keras

"""
(X_train, y_train), (X_test, y_test) = mnist.load_data()
#calculating the amount of pixels
PixelCount = X_train.shape[1] * X_train.shape[2]
#make train set
X_train = X_train.reshape(X_train.shape[0], PixelCount).astype('float32') / 255
#make test set
X_test = X_test.reshape(X_test.shape[0], PixelCount).astype('float32') / 255

"train catagory"
y_train = np_utils.to_categorical(y_train)
"test catagory"
y_test = np_utils.to_categorical(y_test)
num_classes = y_test.shape[1]


def base_model():
	#empty model
    model = Sequential()
	#add layer
    model.add(Dense(PixelCount, input_dim=PixelCount, kernel_initializer='normal', activation='relu'))
	#ad layer
    model.add(Dense(num_classes, kernel_initializer='normal', activation='softmax'))
	#make model
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model

#get base model for iris
model = base_model()
"""
train model
train sets
amount of iterations :20
size of train set    :100
"""
model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=20, batch_size=100, verbose=2)

"""
validate model with testsets
"""
scores = model.evaluate(X_test, y_test, verbose=0)
#print score
print("Error amount: %.2f%%" % (100-scores[1]*100))
