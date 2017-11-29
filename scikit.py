from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import numpy

numpy.random.seed(7)
numpy.random.seed(7)
# load pima indians dataset
dataset = numpy.loadtxt("All_matchdata.txt", delimiter=",")
# split into input (X) and output (Y) variables
X_training = dataset[0:500,0:38]
Y_training = dataset[0:500,38]
X_testing= dataset[500:,0:38]
Y_testing = dataset[500:,38]
X_sureTest = []
Y_sureTest = []

knn = KNeighborsClassifier(n_neighbors=100)
knn.fit(X_training, Y_training)

#pred = knn.predict(numpy.array(X_testing, ndmin = 2))

for i in range(0, len(X_testing) - 1):
    score = knn.predict_proba(numpy.array(X_testing[i], ndmin = 2))
    print(score[0,0])
    if score[0,0] < 0.45 or score[0,0] > 0.55:
        X_sureTest.append(X_testing[i])
        Y_sureTest.append(Y_testing[i])

pred = knn.predict(numpy.asarray(X_sureTest))
print(len(pred))
print(accuracy_score(Y_sureTest, pred))
'''        
print(knn.predict_proba(numpy.array(X_testing[0], ndmin = 2)))
print(accuracy_score(Y_testing, pred))
print(knn.predict(numpy.array(X_testing[0] ,ndmin = 2)))
'''