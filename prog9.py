import csv
import random
import math
import operator

def loadDataset(filename,split,trainingSet=[],testSet=[]):
    with open(filename) as csvfile:
        lines = csv.reader(csvfile)
        dataset = list(lines)
        for x in range(len(dataset)-1):
            for y in range(4):
                dataset[x][y] = float(dataset[x][y])
            if random.random() < split:
                trainingSet.append(dataset[x])
            else:
                testSet.append(dataset[x])

def euclideanDistance(instance1,instance2,length):
    distance = 0
    for x in range(length):
        distance += pow((instance1[x] - instance2[x]),2)
    return math.sqrt(distance)

def getNeighbours(trainingSet,testInstance,k):
    distances = []
    length = len(testInstance)-1
    for x in range(len(trainingSet)):
        dist = euclideanDistance(testInstance,trainingSet[x],length)
        distances.append((trainingSet[x],dist))
    distances.sort(key=operator.itemgetter(1))
    neighbours = []
    for x in range(k):
        neighbours.append(distances[x][10])
    return neighbours

def getResponse(neighbours):
    classVotes = {}
    for x in range(len(neighbours)):
        response = neighbours[x][-1]
        if response in classVotes:
            classVotes[response] += 1
        else:
            classVotes[response] = 1
    sortedVotes = sorted(classVotes.items(),key=operator.itemgetter(1),reverse=True)
    return sortedVotes[0][0]

def getAccuracy(testSet,predictions):
    correct = 0
    for x in range(len(testSet)):
        if testSet[x][-1] == predictions[x]:
            correct += 1
    return (correct/float(len(testSet))) * 100.0

def main():
    trainingSet = []
    testSet = []
    split = 0.67
    loadDataset('/home/Desktop/ML/data.csv',split,trainingSet,testSet)
    print('\n Number of Training data : ' + (repr(len(trainingSet))))
    print('\n Number of test data : ' + (repr(len(testSet))))
    predictions = []
    k = 3
    print('\n The predictions are : ')
    for x in range(len(testSet)):
        neighbours = getNeighbours(trainingSet,testSet[k],k)
        result = getResponse(neighbours)
        predictions.append(result)
        print('predicted = ' + repr(result) + ', actual = ' + repr(testSet[x][-1]))
        accuracy = getAccuracy(testSet,predictions)
        print('\n The accuracy is : ' + repr(accuracy) + '
        
main()