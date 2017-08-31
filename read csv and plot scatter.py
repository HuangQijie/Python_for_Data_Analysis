#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import csv

SN=[]
Chan=[]
Value=[]
v=[]
vv=[]

with open('C:\\Users\\Andy.Huang\\Desktop\\bbb.csv', 'r') as csvfile:
    for item in csvfile:
        v=item.strip('\n').split(',')
        #print (v[2])

        vv=v[2].split('-')
        v_Chan=vv[1]
        #print (v_Chan)
        #if v_Chan[0]=='t' and (v_Chan[21] not in ('m','r')):
        v_SN=v[0]
        v_Value=v[3]
        SN.append(v_SN)
        Chan.append(v_Chan)
        Value.append(v_Value)

#
    """SN.pop(0)
    Chan.pop(0)
    Value.pop(0)    """
    #print(SN,Chan,Value)
    #plt.plot(0,0)
    length=1
    for i in range(len(SN)-1):
        tempSN=SN[i]

        #print(i,tempSN,SN[i+1])
        if tempSN==SN[i+1]:
            length=length+1
        else:
            #print(length,i)

            #print(Chan[(i-length+1):i],Value[(i-length+1):i])
            #subValue=Value[(i-length+1):i]
            #subValue=[ float(item) for item in subValue]
            #revalue=[]
            #for item in subValue:

                #print (float(item),float(min(subValue)))
                #revalue.append(float(item)-float(min(subValue)))
            #print (Chan[(i-length+1):i],revalue)

            if SN[i]=='RW1703L01-08':
                handle=plt.scatter(Chan[(i-length+1):i],Value[(i-length+1):i],color='r',label=SN[i])
                plt.legend(handles=[handle])

            else:
                plt.scatter(Chan[(i-length+1):i],Value[(i-length+1):i])


            length=1
plt.title('iRatio0')
plt.xlabel('Chan')
plt.ylabel('iRatio0')
#plt.show()

#plt.legend()
#csvfile.close()
