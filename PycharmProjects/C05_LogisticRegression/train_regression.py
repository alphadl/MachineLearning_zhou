from numpy import *
import matplotlib.pyplot as plt
dataMat=matrix([[1,0.697,0.460],[1,0.774,0.376],[1,0.634,0.264],
               [1,0.608,0.318],[1,0.556,0.215],[1,0.403,0.237],
               [1,0.481,0.149],[1,0.437,0.211],[1,0.666,0.091],
               [1,0.243,0.267],[1,0.245,0.057],[1,0.343,0.099],
               [1,0.639,0.161],[1,0.657,0.198],[1,0.360,0.370],
               [1,0.593,0.042],[1,0.719,0.103]])
labelMat=matrix([[1],[1],[1],[1],[1],[1],[1],[1],[0],[0],[0],[0],[0],[0],[0],[0],[0]])
def sigmoid(inX):
    return 1.0/(1+exp(-inX))
def gradAscent(dataMat,labelMat):
    labelMat=labelMat.transpose()
    m,n=shape(dataMat)
    alpha=0.001
    maxCycle=500
    weight=ones((n,1))
    for k in range(maxCycle):
        h=sigmoid((dataMat*weight))
        error=labelMat-h
        weight=weight+alpha*dataMat.transpose()*error
    return weight
def stoGradAscent0(dataMat,labelMat):
    m,n=shape(dataMat)
    alpha=0.01
    weight=ones(n)
    for i in range(m):
        h=sigmoid(dataMat[i]*weight)
        error=int(labelMat[i])-h
        weight=weight+alpha*error*dataMat[i]
    return weight
def stoGradAscent1(dataMat,labelMat,numIter):
    m,n=shape(dataMat)
    weight=ones(n)
    for j in range(numIter):
        dataIndex=range(m)
        for i in range(m):
            alpha=4/(1.0+i+j)+0.01
            randIndex=int(random.uniform(0,len(dataIndex)))
            h=sigmoid(sum(dataMat[randIndex]*weight))
            error=int(labelMat[randIndex])-h
            weight=weight+alpha*error*dataMat[randIndex]
            del(dataIndex[randIndex])
    return weight
def plotBestFit(weight,dataMat,labelMat):
    dataArr=array(dataMat)
    m=shape(dataArr)[0]
    x1=[];y1=[]
    x2=[];y2=[]
    for i in range(m):
        if int(labelMat[i])==1: x1.append(dataMat[i,1]);y1.append(dataMat[i,2])
        else :x2.append(dataMat[i,1]);y2.append(dataMat[i,2])
    fig=plt.figure()
    ax=fig.add_subplot(111)
    ax.scatter(x1,y1,s=30,c='red',marker='s')
    ax.scatter(x2,y2,s=30,c='green')
    x=arange(0,1,0.01)
    y=array(-(weight[0]+weight[1]*x)/weight[2]).transpose()
    ax.plot(x,y)
    plt.xlabel('x1');plt.ylabel('x2');
    plt.show()
def prediction(x1,x2):
    weight=array([ -5.67897117,5.49008639,19.46581541])
    new_x=array([1,x1,x2])
    if sigmoid(sum(new_x*weight)) >0.5:return 'good watermalen'
    else:return 'bad watermalen'
# print gradAscent(dataMat,labelMat.transpose())
# print stoGradAscent0(array(dataMat),labelMat)
# print stoGradAscent1(array(dataMat),labelMat,100000)
# plotBestFit(stoGradAscent1(array(dataMat),labelMat,100000),dataMat,labelMat)
print prediction(0.429,0.460)
