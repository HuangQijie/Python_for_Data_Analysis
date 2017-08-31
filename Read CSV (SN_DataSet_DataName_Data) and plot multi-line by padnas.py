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
import pandas as pd


#%%
SN_Index=0
DataSet_Index=5
DataName_Index=8
DataValue_Index=9


data_read=pd.read_csv('C:\\Users\\Andy.Huang\\Desktop\\tttt.csv')

Column_Name=data_read.columns
SN_Name=Column_Name[SN_Index]
DataSet_Name=Column_Name[DataSet_Index]
DataName_Name=Column_Name[DataName_Index]
DataValue_Name=Column_Name[DataValue_Index]


data_read=data_read.set_index([SN_Name,DataSet_Name])

data=pd.DataFrame(data_read,columns=[ DataName_Name,DataValue_Name])

DataName_frame=data[DataName_Name]

DataName_frame.str.

#DataName_Series=data[DataName_Name]


#dt=SN_DataSet_DataName_DataValue_Dict()

#for row in data:
#    print(row)



#    #%%
#    '''
#    Modify the data in below
#    '''
##    if str.isnumeric(row[DataName_Index][len(row[DataName_Index])-4:len(row[DataName_Index])-1]):
##        chan=row[DataName_Index][len(row[DataName_Index])-4:len(row[DataName_Index])-1]
#    #chan=row[DataName_Index].split('-')[1]
#    #%%
#    '''
#        Data is transfered into nested dict
#    '''
#    dt.append_DataName_DataValue_data(row[SN_Index],row[DataSet_Index],row[DataName_Index],float(row[DataValue_Index]))
#    #dt.append_DataName_DataValue_data(row[SN_Index],row[DataSet_Index],float(chan),float(row[DataValue_Index]))

#%% Start plotting
#for SN in dt:
##    print(SN)
#    for DataSet in dt[SN]:
##        print('\t'+DataSet)
#        plotdata={}
#        #plotdata_sorted={}
#        for DataName in dt[SN][DataSet]:
##            print('\t\t'+DataName,end='\t')
##            print(dt[SN][DataSet][DataName])
#            plotdata[DataName]=dt[SN][DataSet][DataName]
##%%Sort the Dataname , because dataname is string type and usually not sorted
#        Name=[]
#        Value=[]
#        for k in sorted(plotdata.keys()):# Sort by keys
#            Name.append(k)
#            Value.append(plotdata[k])
##%%Sort end here
#        #for item
#        #print (plotdata.items())
#
#        plt.plot(Name,Value,label=SN+'_'+DataSet)
#        plt.legend(loc='upper left',bbox_to_anchor=(1,1))
#
#
#plt.grid()
#plt.xlabel('Channel')
#plt.ylabel('Frequency Delta (GHz)')
#plt.autoscale(True,True,True)




