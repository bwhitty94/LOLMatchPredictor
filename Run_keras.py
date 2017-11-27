from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Flatten
import numpy
# fix random seed for reproducibility
def runKeras():
    numpy.random.seed(100)
    # load pima indians dataset
    dataSet = numpy.loadtxt("All_matchdata.txt", delimiter=",")
    dataTest = numpy.loadtxt("match8_final.txt", delimiter=",")
    testmatch = numpy.loadtxt("test_matches.txt", delimiter = ",")
    # split into input (X) and output (Y) variables
    X_training = dataSet[0:,0:38]
    Y_training = dataSet[0:,38]

    X_testing = dataTest[50:,0:38]
    Y_testing = dataTest[50:,38]
    # X_testing = testmatch[:,0:38]
    # Y_testing = testmatch[:,38]
    print(X_testing)
    # create model
    model = Sequential()
    model.add(Dense(64, input_dim=38, activation='relu'))
    model.add(Dense(38, activation='relu'))
    model.add(Dense(1, activation='sigmoid'))
    # Compile model
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    # Fit the model
    model.fit(X_training, Y_training, epochs=200, batch_size=10)
    # evaluate the model
    # scores = model.evaluate(X_testing, Y_testing)
    # print(scores)
    # predictions = model.predict(numpy.array([[0.9300,0.9581,0.8649,0.7080,0.6215,0.1300,0.0581,0.0649,0.0080,0.0215]]))
    predictions = model.predict(numpy.array(X_testing, ndmin = 2))
    print (predictions)

    totalCorrect = 0
    rounded = [round(x[0]) for x in predictions]
    for i in range(0,len(predictions)):
        rounded[i] = 1 - rounded[i]
        if(rounded[i] == Y_testing[i]):
            totalCorrect = totalCorrect + 1

    print("totalcorrecct: " + str(totalCorrect) + " out of " +str(len(predictions)) + " %: " + str(totalCorrect/len(predictions)))


    # print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1] * 100))

if __name__ == "__main__":
    runKeras()