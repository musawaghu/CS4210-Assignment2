# -------------------------------------------------------------------------
# AUTHOR: Musa Waghu
# FILENAME: title of the source file
# SPECIFICATION: description of the program
# FOR: CS 4210- Assignment #2
# TIME SPENT: how long it took you to complete the assignment
# -----------------------------------------------------------*/

# IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard vectors and arrays

# importing some Python libraries
from sklearn.neighbors import KNeighborsClassifier
import csv

db = []

# reading the data in a csv file
with open('binary_points.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for i, row in enumerate(reader):
        if i > 0:  # skipping the header
            db.append(row)

error_rate = 0
# loop your data to allow each instance to be your test set
for a in range(len(db)):

    # add the training features to the 2D array X removing the instance that will be used for testing in this iteration. For instance, X = [[1, 3], [2, 1,], ...]]. Convert each feature value to
    # float to avoid warning messages
    X = []
    for b in range(len(db)):
        if a != b:
            X.append([float(db[b][0]), float(db[b][1])])
    # X =

    # transform the original training classes to numbers and add to the vector Y removing the instance that will be used for testing in this iteration. For instance, Y = [1, 2, ,...]. Convert each
    #  feature value to float to avoid warning messages
    Y = []
    for b in range(len(db)):
        if a != b:
            if db[b][2] == '+':
                Y.append(1)
            else:
                Y.append(0)

    # Y =

    # store the test sample of this iteration in the vector testSample
    testSample = [float(db[a][0]), float(db[a][1])]
    # testSample =

    # fitting the knn to the data
    clf = KNeighborsClassifier(n_neighbors=1, p=2)
    clf = clf.fit(X, Y)

    # use your test sample in this iteration to make the class prediction. For instance:
    # class_predicted = clf.predict([[1, 2]])[0]
    class_predicted = clf.predict([testSample])[0]

    # compare the prediction with the true label of the test instance to start calculating the error rate.
    if db[a][2] == '+' and class_predicted == 0:
        error_rate += 1
    elif db[a][2] == '-' and class_predicted == 1:
        error_rate += 1

# print the error rate
print("Error rate for 1NN: ", error_rate / len(db))
