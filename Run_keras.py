from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Flatten
import numpy
# fix random seed for reproducibility

def categorizePrediction(score):
    if (score < .20):
        return 1
    if(score < .40):
        return 2
    if(score < .60):
        return 3
    if(score < .80):
        return 4
    if(score < 1):
        return 5
    return 0

def runKeras():
    numpy.random.seed(100)
    # load pima indians dataset
    dataSet = numpy.loadtxt("All_matchdata.txt", delimiter=",")
    match= numpy.loadtxt("currentmatchfile.txt", delimiter = ",")
    match_data = match[5,0:38]
    # split into input (X) and output (Y) variables
    X_training = dataSet[0:,0:38]
    Y_training = dataSet[0:,38]

    model = Sequential()
    model.add(Dense(64, input_dim=38, activation='relu'))
    model.add(Dense(38, activation='relu'))
    model.add(Dense(1, activation='sigmoid'))
    # Compile model
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    # Fit the model
    model.fit(X_training, Y_training, epochs=200, batch_size=10)
    prediction = model.predict(numpy.array(match_data, ndmin = 2))

    bensValue = categorizePrediction(prediction)
    return bensValue

# if __name__ == "__main__":
    # runKeras()