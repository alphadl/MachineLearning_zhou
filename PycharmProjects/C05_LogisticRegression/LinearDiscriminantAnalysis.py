#-*-coding:utf-8-*-#
from numpy import *
import numpy as np
import matplotlib.pyplot as plt
dataMat=matrix([[0.697,0.460],[0.774,0.376],[0.634,0.264],
               [0.608,0.318],[0.556,0.215],[0.403,0.237],
               [0.4801,.149],[0.437,0.211],[0.666,0.091],
               [0.243,0.267],[0.245,0.057],[0.343,0.099],
               [0.639,0.161],[0.657,0.198],[0.360,0.370],
               [0.593,0.042],[0.719,0.103]])
labelMat=matrix([[1],[1],[1],[1],[1],[1],[1],[1],[0],[0],[0],[0],[0],[0],[0],[0],[0]])

def cal_w():
    data1=dataMat[0:7,:];data2=dataMat[8:-1,:];
    mean1=array([mean(data1[:,0]),mean(data1[:,1])]);mean2=array([mean(data2[:,0]),mean(data2[:,1])]);
    m1=shape(data1)[0]
    sw=zeros(shape=(2,2))
    for i in range(m1):
        xsmean=mat(data1[i,:]-mean1) #de-centralization
        sw+=xsmean.transpose()*xsmean
    m2=shape(data2)[0]
    for i in range(m2):
        xsmean = mat(data2[i, :] - mean2)  # de-centralization
        sw += xsmean.transpose() * xsmean
    w=(mean2-mean1)*mat(sw).I
    return w,mean1,mean2
def plot(w):
    dataArr=array(dataMat)
    m=shape(dataArr)[0]
    x1=[];y1=[];x2=[];y2=[];
    for i in range(m):
        if int(labelMat[i])==1:x1.append(dataArr[i,0]);y1.append(dataArr[i,1])
        else:x2.append(dataArr[i,0]);y2.append(dataArr[i,1])
    plt.figure()
    ax=plt.subplot(111)
    ax.scatter(x1,y1,s=30,c='red',marker='s')
    ax.scatter(x2,y2,s=30,c='green')
    x = arange(0, 1, 0.01)
    y = array((-w[0,0]*x)/w[0,1])
    ax.plot(x, y)
    plt.xlabel('x1');
    plt.ylabel('x2');
    plt.show()
def prediction(x1,x2,mean1,mean2):
    w=array((-0.30976863,-0.77101574))
    new_x=array((x1,x2))
    k=sum(w * new_x)
    print "新来的点距离种类1种类2分别为",fabs(k-sum(w*mean1)),fabs(k-sum(w*mean2))
    if fabs(k-sum(w*mean1))>fabs(k-sum(w*mean2)):return "bad melon"
    else:return "good melon"
# w=cal_w()
# print w
# plot(w)
print prediction(0.719,0.107,cal_w()[1],cal_w()[2])