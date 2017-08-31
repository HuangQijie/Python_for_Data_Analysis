# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 11:29:48 2017
This py file is for import csv file with column SN,dataset,dataname,datavalue, then plot by differen SN and dataset
@author: andy.huang
"""


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import csv
import pandas

#%%
'''
Protected Class section

'''
class SN_DataSet_DataName_DataValue_Dict(dict):


    def _init_(self):
        self.SNList=self.keys()

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

''' Class end here'''
#%%
SN_Index=0
DataSet_Index=5
DataName_Index=9
DataValue_Index=10

#SN_Index=0
#DataSet_Index=1
#DataName_Index=2
#DataValue_Index=3

data=np.genfromtxt('C:\\Users\\Andy.Huang\\Desktop\\ER_Gen2.csv',dtype='U75', skip_header=True, delimiter=',')

dt=SN_DataSet_DataName_DataValue_Dict()

for row in data:
    #%%
    '''
    Modify the data in below
    '''
#    if str.isnumeric(row[DataName_Index][len(row[DataName_Index])-4:len(row[DataName_Index])-1]):
#        chan=row[DataName_Index][len(row[DataName_Index])-4:len(row[DataName_Index])-1]
    #chan=row[DataName_Index].split('-')[1]
    #%%
    '''
        Data is transfered into nested dict
    '''
    dt.append_DataName_DataValue_data(row[SN_Index],row[DataSet_Index],row[DataName_Index],float(row[DataValue_Index]))
    #dt.append_DataName_DataValue_data(row[SN_Index],row[DataSet_Index],float(chan),float(row[DataValue_Index]))

#%% Start plotting
for SN in dt:
#    print(SN)
    for DataSet in dt[SN]:
#        print('\t'+DataSet)
        plotdata={}
        #plotdata_sorted={}
        for DataName in dt[SN][DataSet]:
#            print('\t\t'+DataName,end='\t')
#            print(dt[SN][DataSet][DataName])
            plotdata[DataName]=dt[SN][DataSet][DataName]
#%%Sort the Dataname , because dataname is string type and usually not sorted
        Name=[]
        Value=[]
        for k in sorted(plotdata.keys()):# Sort by keys
            Name.append(k)
            Value.append(plotdata[k])
#%%Sort end here
        #for item
        #print (plotdata.items())

        plt.plot(Name,Value,label=SN+'_'+DataSet)
        plt.legend(loc='upper left',bbox_to_anchor=(1,1))


plt.grid()
plt.xlabel('Channel')
plt.ylabel('Frequency Delta (GHz)')
#plt.autoscale(True,True,True)




