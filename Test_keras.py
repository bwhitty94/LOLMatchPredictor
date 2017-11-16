from keras.models import Sequential
from keras.layers import Dense
import numpy
# fix random seed for reproducibility
numpy.random.seed(7)
# load pima indians dataset
dataset = numpy.loadtxt("newfile.txt", delimiter=",")
# split into input (X) and output (Y) variables
X_training = dataset[0:175,0:10]
Y_training = dataset[0:175,10]
X_testing= dataset[175:,0:10]
Y_testing = dataset[175:,10]

# create model
model = Sequential()
model.add(Dense(12, input_dim=10, activation='relu'))
model.add(Dense(10, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
# Compile model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
# Fit the model
model.fit(X_training, Y_training, epochs=10, batch_size=5)
# evaluate the model
scores = model.evaluate(X_testing, Y_testing)
print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))