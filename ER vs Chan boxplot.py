# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 22:30:57 2017

@author: Administrator
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import csv
import pandas as pd
from pandas import Series, DataFrame
import re

SN_Index=0
Chan_Index=9
ER_Index=10
#DataValue_Index=3

#data_read=pd.read_csv('D:\\GitHub_data\\Python_for_Data_Analysis\\bbb.csv')
data_read=pd.read_csv('C:\\Users\\Andy.Huang\\Desktop\\TSFP Negative chirp.csv')

Column_Name=data_read.columns
SN_Name=Column_Name[SN_Index]
Chan_Name=Column_Name[Chan_Index]
ER_Name=Column_Name[ER_Index]


data=pd.DataFrame(data_read,columns=[Chan_Name,ER_Name])
Chan_Series=data.drop_duplicates(Chan_Name)[Chan_Name]
Chan_Series=Chan_Series.sort_values()

ER_dataframe=DataFrame()
for chan in Chan_Series:
    ER_Series=data[data[Chan_Name]==chan][ER_Name]
    #ER_Series=ER_Series.rename(columns={ER_Name:str(chan)})
    #ER_dataframe=ER_dataframe.assign(chan=ER_Series.values,ignore_index=True)
    ER_dataframe=pd.concat([ER_dataframe,pd.DataFrame({chan:ER_Series})],axis=1)


ER_dataframe.boxplot()
plt.xlabel('Channel')
plt.ylabel('ER(dB)')
plt.title('TSFP Negative chirp ER distribution')
