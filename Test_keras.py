from keras.models import Sequential
from keras.layers import Dense
from sklearn.metrics import accuracy_score

import numpy
# fix random seed for reproducibility
numpy.random.seed(100)
# load pima indians dataset
dataset = numpy.loadtxt("All_matchdata.txt", delimiter=",")
dataset2 = numpy.loadtxt("match8_final.txt", delimiter=",")
# split into input (X) and output (Y) variables
X_training = dataset[0:,0:38]
Y_training = dataset[0:,38]
X_testing= dataset2[0:,0:38]
Y_testing = dataset2[:,38]
X_sureTest = []
Y_sureTest = []

# create model
model = Sequential()
model.add(Dense(12, input_dim=38, activation='relu'))
model.add(Dense(10, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
# Compile model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
# Fit the model
model.fit(X_training, Y_training, epochs=50, batch_size=1)
# evaluate the model

print(X_testing.shape)

'''
for x in range(0, 90):
    #print(x)
    score = model.predict(numpy.array(X_testing[x], ndmin = 2))
    if score > 0.3 and score < 0.7:
        X_sureTest.append(X_testing[x])
        Y_sureTest.append(Y_testing[x])
'''

#scores = model.evaluate(X_testing, Y_testing)
#scores = model.evaluate(numpy.asarray(X_sureTest), numpy.asarray(Y_sureTest))
#print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))
#print(numpy.asarray(X_sureTest).shape)
pred = model.predict_classes(X_testing)
print("\nACC:")
print(accuracy_score(pred, Y_testing))