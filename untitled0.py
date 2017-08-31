# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 11:29:48 2017

@author: andy.huang
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import csv
#import SN_DataSet_DataName_DataValue_Dict
#with open('C:\\Users\\Andy.Huang\\Desktop\\bbb.csv') as csvfile:
#    reader = csv.DictReader(csvfile)
##    print(reader.fieldnames)
#    for row in reader:
#        print(row[''])

#
#    a = np.array([[1,2,3],[4,5,6],[0,0,1]])
#    a_arg = np.argsort(a[:,1])  #按第'1'列排序
#    a = a[a_arg]

class SN_DataSet_DataName_DataValue_Dict(dict):


#    def _init_(self,a_SN='',a_DataSet='',a_DataName='',a_DataValue=''):
#        self[a_SN]={a_DataSet:{a_DataName:a_DataValue}}
#        DataName_DataValue_Dict={}
#        DataSet_DataName_DataValu_Dict={}
#        DataName_DataValue_Dict['1']='1'
#        DataSet_DataName_DataValu_Dict['1']=DataName_DataValue_Dict
#        self['1']=DataSet_DataName_DataValu_Dict

    def append_SN_data(self,a_SN,a_DataSet_DataName_DataValue={}):
        if a_SN in self:
             self[a_SN]=a_DataSet_DataName_DataValue
        else:
            self.update({a_SN:a_DataSet_DataName_DataValue})
    def append_DataSet_data(self,a_SN,a_DataSet,a_DataName_DataValue={}):
        if a_SN in self:
            if a_DataSet in self[a_SN]:
                self[a_SN][a_DataSet]=a_DataName_DataValue
            else:
               self[a_SN].update({a_DataSet:a_DataName_DataValue})
        else:
            self.update({a_SN:{a_DataSet:a_DataName_DataValue}})
    def append_DataName_DataValue_data(self,a_SN,a_DataSet,a_DataName,a_DataValue):
        if a_SN in self:
            if a_DataSet in self[a_SN]:
                self[a_SN][a_DataSet][a_DataName]=a_DataValue

            else:
                self[a_SN].update({a_DataSet:{a_DataName:a_DataValue}})
        else:
            self.update({a_SN:{a_DataSet:{a_DataName:a_DataValue}}})




SN_Index=0
DataSet_Index=5
DataName_Index=8
DataValue_Index=9
data=np.genfromtxt('C:\\Users\\Andy.Huang\\Desktop\\tttt.csv',dtype='U75', skip_header=True, delimiter=',')
#print(data[1][1])

#data=str(data)
#data=data[np.argsort(data[:,0])]
#length=1
#for i in range(0,len(data)-1):
#    tempSN=data[i][Index_SN]
#
#    if tempSN==data[i+1][Index_SN]:
#        length=length+1
#    else:
#        Name_Value=data[(i-length+1):i][Index_DataName:Index_Value]
#        print(Name_Value)
#        length=1
dt=SN_DataSet_DataName_DataValue_Dict()
#dt.__init__()
for row in data:
    if str.isnumeric(row[DataName_Index][len(row[DataName_Index])-4:len(row[DataName_Index])-1]):
        chan=row[DataName_Index][len(row[DataName_Index])-4:len(row[DataName_Index])-1]
        dt.append_DataName_DataValue_data(row[SN_Index],row[DataSet_Index],chan,row[DataValue_Index])
for SN in dt:
#    print(SN)
    for DataSet in dt[SN]:
#        print('\t'+DataSet)
        plotdata={}
        for DataName in dt[SN][DataSet]:
#            print('\t\t'+DataName,end='\t')
#            print(dt[SN][DataSet][DataName])
            plotdata[DataName]=dt[SN][DataSet][DataName]
            #plt.scatter(DataName,dt[SN][DataSet][DataName])
        [(k,plotdata[k]) for k in sorted(plotdata.keys())]# Sort by keys
        #for item
        #print (plotdata.items())

        plt.plot(list(plotdata.keys()),list(plotdata.values()),label=SN+'_'+DataSet)
        plt.legend()
plt.xlabel('Channel')
plt.ylabel('Frequency Delta (GHz)')




