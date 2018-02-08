from __future__ import division
import math
import random

def genData(dims):
#Given a dimension, spawns 100 entries with dims attributes of either 0 or 1
    res = []
    for i in range(0,50):
        bas = []
        bas.append(0)
        for i in range(1, dims):
            bas.append(random.randint(0,1))
        res.append(bas)

    for i in range(0,50):
        bas = []
        bas.append(1)
        for i in range(1, dims):
            bas.append(random.randint(0,1))
        res.append(bas)

    return res

def nn(train, entry):
#Given a data entry, predicts whether its first label will be 0 or 1
    dist = len(entry)
    pred = 2
    for item in train:
        tdist = 0
        for i in range(0, len(item)):
            if item[i] != entry[i]:
                tdist += 1
        if dist >= tdist:
            pred = item[0]
            dist = tdist
    return pred

def training(train, test):
#for every item in the test data, if the first label matches the prediction,
#increment a counter by one
    succount = 0
    for i in range(0, len(test)):
        if nn(train,test[i]) == test[i][0]:
            succount += 1

    return succount

def trainrep(dim):
#trains a given dimension three times and averages the results
    sumr = 0
    print "Testing with a dimension of " + str(dim) + "..."
    for i in range(0,3):
        train = genData(dim)
        test = genData(dim)
        sumr += training(train, test)
    return sumr / 3

def main():
    print "Average accuracy for dimension of 5 = " + str(trainrep(5)) + "%"
    print "Average accuracy for dimension of 10 = " + str(trainrep(10)) + "%"
    print "Average accuracy for dimension of 20 = " + str(trainrep(20)) + "%"
    print "Average accuracy for dimension of 50 = " + str(trainrep(50)) + "%"
    print "Average accuracy for dimension of 100 = " + str(trainrep(100)) + "%"


main()
