#!/usr/bin/python
#
# CIS 472/572 -- Programming Homework #1
#
# Starter code provided by Daniel Lowd, 1/25/2018
#
#
from __future__ import division
import sys
import re
# Node class for the decision tree
import node

#for entropy calcs
import math

train=None
varnames=None
test=None
testvarnames=None
root=None

# Helper function computes entropy of Bernoulli distribution with
# parameter p
def entropy(p):
        lf = p
        rh = 1 - p
        res = -(rh * math.log(rh, 2)) - (lf*math.log(lf, 2))
        return res;

# Compute information gain for a particular split, given the counts
# py_pxi : number of occurences of y=1 with x_i=1 for all i=1 to n
# pxi : number of occurrences of x_i=1
# py : number of ocurrences of y=1
# total : total length of the data
def infogain(py_pxi, pxi, py, total):
	# >>>> YOUR CODE GOES HERE <<<<
    # For now, always return "0":
	return 0;

# OTHER SUGGESTED HELPER FUNCTIONS:
# - collect counts for each variable value with each class label
# - find the best variable to split on, according to mutual information
# - partition data based on a given variable	

def getBest(data, names):
    #given data, find the most successful attribute
    #that is to say, the attribute that leads to a result of 1
    #the most frequently

    #entropy check
    tot = 0
    pas = 0
    for item in data:
        tot += 1
        if item[-1] == 1:
            pas +=1

    entsucc = entropy(pas/tot)
    print pas
    print entsucc

    gsuc = 0
    ndex = 0
    for i in range(0, len(names)-1):
        suc = 0
        print "testing " + names[i] + "..."
        for item in data:
            if item[i] == 1:
                if item[-1] == 1:
                    suc += 1

        if suc > gsuc:
            gsuc = suc
            ndex = i
    print str(names[ndex]) + " is the best attribute, with " + str(gsuc) + " entries out of " + str(len(data)) + " passing with it."

# Load data from a file
def read_data(filename):
    f = open(filename, 'r')
    p = re.compile(',')
    data = []
    header = f.readline().strip()
    varnames = p.split(header)
    namehash = {}
    for l in f:
        data.append([int(x) for x in p.split(l.strip())])
    return (data, varnames)

# Saves the model to a file.  Most of the work here is done in the
# node class.  This should work as-is with no changes needed.
def print_model(root, modelfile):
    f = open(modelfile, 'w+')
    root.write(f, 0)

# Build tree in a top-down manner, selecting splits until we hit a
# pure leaf or all splits look bad.
def build_tree(data, varnames):
    # >>>> YOUR CODE GOES HERE <<<<
    # For now, always return a leaf predicting "1":
    return node.Leaf(varnames, 1)


# "varnames" is a list of names, one for each variable
# "train" and "test" are lists of examples.
# Each example is a list of attribute values, where the last element in
# the list is the class value.
def loadAndTrain(trainS,testS,modelS):
	global train
	global varnames
	global test
	global testvarnames
	global root
	(train, varnames) = read_data(trainS)
	(test, testvarnames) = read_data(testS)
	modelfile = modelS
	
	# build_tree is the main function you'll have to implement, along with
    # any helper functions needed.  It should return the root node of the
    # decision tree.
        getBest(test, varnames)
	root = build_tree(train, varnames)
	print_model(root, modelfile)
	
def runTest():
	correct = 0
	# The position of the class label is the last element in the list.
	yi = len(test[0]) - 1
	for x in test:
		# Classification is done recursively by the node class.
        # This should work as-is.
		pred = root.classify(x)
		if pred == x[yi]:
			correct += 1
	acc = float(correct)/len(test)
	return acc	
	
	
# Load train and test data.  Learn model.  Report accuracy.
def main(argv):
    if (len(argv) != 3):
                print entropy(0.8571428571428)
		print 'Usage: id3.py <train> <test> <model>'
		sys.exit(2)
    loadAndTrain(argv[0],argv[1],argv[2]) 
                    
    acc = runTest()             
    print "Accuracy: ",acc                      

if __name__ == "__main__":
    main(sys.argv[1:])
