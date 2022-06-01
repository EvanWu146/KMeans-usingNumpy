import numpy as np
import matplotlib.pyplot as plt
from math import floor

f = open('cluster.dat', 'r')
src_data = f.readlines()
data = []
for d in src_data:
    temp = d.strip('\n').split(' ')
    data.append(
        [float(temp[0]), float(temp[1])]
    )
data = np.array(data)
# print(data)

def getDistance(A, B):
    return np.sum(((np.array(A) - np.array(B)) ** 2), axis=0) ** 0.5

def randomCenter(data, k):
    index = randomInteger(low=0, high=len(data), length=k)
    val = []
    for i in index:
        val.append(data[i])

    return np.array(val)

def randomInteger(low, high, length):
    index = np.random.randint(low=low, high=high, size=(length,), dtype=int)
    realLen = len(list(set(index)))
    index = list(index)
    while realLen < length:
        add = np.random.randint(low=low, high=high, size=(length - realLen,), dtype=int)
        index = index + list(add)
        realLen = len(list(set(index)))
    return np.array(index)

# print(randomCenter(data, 7))

def newCenter(typeList, data, K):
    new_center = []
    for k in range(K):
        temp = [0, 0, 0]  # X, Y, count
        for t in range(len(typeList)):
            if typeList[t] == k + 1:
                temp[0] += data[k+1][0]
                temp[1] += data[k+1][1]
                temp[2] += 1
        if temp[2] == 0:
            temp[2] = 1
        new_center.append([temp[0]/temp[2], temp[1]/temp[2]])
    return new_center


def KMeans(data, K):
    typeList = [0]*len(data)
    center = randomCenter(data, K)

    while True:
        for i in range(len(data)):
            distanceList = [getDistance(data[i], center[k]) for k in range(K)]
            index = distanceList.index(min(distanceList))
            typeList[i] = index + 1

        new_center = newCenter(typeList, data, K)
        validCenter = 0
        for k in range(K):
            delta = getDistance(center[k], new_center[k])
            if delta < 1:
                validCenter += 1
            if validCenter == K:
                break
        center = new_center
        if validCenter == K:
            break

    return typeList, center

def drawPoint(data, label, center):
    plt.scatter(data[:, 0], data[:, 1], marker='o', c=label)
    for i in range(len(center)):
        plt.scatter(center[i, 0], center[i, 1], s=300, marker='*')
    plt.show()

def fit_predict(data, K, ratio=4):
    index = randomInteger(low=0, high=1001, length=floor(len(data) * (ratio / (1 + ratio))))
    trainSet, testSet = [], []
    for i in range(len(data)):
        if i in index:
            trainSet.append(data[i])
        else:
            testSet.append(list(data[i]))

    label, center = KMeans(np.array(trainSet), K)
    drawPoint(np.array(trainSet), label, np.array(center))

    testLabel = []
    for t in testSet:
        distance = []
        for c in center:
            distance.append(getDistance(t, c))
        testLabel.append(distance.index(min(distance)) + 1)
    print(testSet)
    print(testLabel)
    drawPoint(np.array(testSet), testLabel, np.array(center))


# 方法1
#label, center = KMeans(data, 100)
# drawPoint(data, label, np.array(center))

# 附加题
fit_predict(data, 10)

