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
from pandas import Series, DataFrame
import re


#SN_Index=0
#DataSet_Index=5
#DataName_Index=8
#DataValue_Index=9


SN_Index=0
DataSet_Index=1
DataName_Index=2
DataValue_Index=3

data_read=pd.read_csv('D:\\GitHub_data\\Python_for_Data_Analysis\\bbb.csv')

Column_Name=data_read.columns
SN_Name=Column_Name[SN_Index]
DataSet_Name=Column_Name[DataSet_Index]
DataName_Name=Column_Name[DataName_Index]
DataValue_Name=Column_Name[DataValue_Index]


#data_read=data_read.set_index([SN_Name,DataSet_Name])

data=pd.DataFrame(data_read,columns=[ SN_Name,DataSet_Name,DataName_Name,DataValue_Name])

DataName_DataFrame=data[DataName_Name]
#pattern='[a-zA-Z_:\[\]]+([0-9]+)' # screen out the channel number
pattern='.+\-([0-9]+)'
DataName_DataFrame=DataName_DataFrame.str.extract(pattern,flags=re.IGNORECASE)


del data[DataName_Name]
data.insert(2,DataName_Name,DataName_DataFrame)
data=data.dropna()#delete row whose dataname is NA
#data=data.set_index([SN_Name,DataSet_Name])
 
SN_list=data.drop_duplicates([SN_Name])[SN_Name]#get SN list
DataSet_list=data.drop_duplicates([DataSet_Name])[DataSet_Name]#get dataname list

#for sn in SN_list:
#    for dataset in DataSet_list:
#        plotdata=data[data[DataSet_Name]==dataset][data[SN_Name]==sn]
#        plotdata.sort_index(by=DataName_Name)
#        pass
#        plt.plot(plotdata[DataName_Name],plotdata[DataValue_Name],label=sn+'_'+dataset)
#        plt.legend(loc='upper left',bbox_to_anchor=(1,1))


for sn in SN_list:
    plotdata=data[data[SN_Name]==sn]
    plotdata=plotdata.apply(pd.to_numeric, errors='ignore')
    plotdata=plotdata.sort_values(by=DataName_Name)
    pass
    plt.plot(plotdata[DataName_Name],plotdata[DataValue_Name],label=sn)
    plt.legend(loc='best',bbox_to_anchor=(1,1))

plt.grid()
plt.xlabel('Channel')
plt.ylabel('Frequency Delta (GHz)')
#plt.autoscale(True,True,True)




