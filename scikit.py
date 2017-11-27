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

knn = KNeighborsClassifier(n_neighbors=100)
knn.fit(X_training, Y_training)

pred = knn.predict(numpy.array(X_testing, ndmin = 2))
print(accuracy_score(Y_testing, pred))
print(knn.predict(numpy.array(X_testing[0] ,ndmin = 2)))