import json
from os import cpu_count

from numpy import equal, nan
import pandas as pd
from createComponent import *



fileObj = pd.read_csv('file1.csv')
a = len(fileObj['rule'])
i = 0
while(i<a):
    #print(str(i)+" "+str(a))
    print("rule is : "+fileObj['rule'][i])

    print("Component: Conditions are: ")
    Condition = fileObj['delegate_descriptor_condition_settings'][i]
    if Condition is not nan:
        data = list(Condition.split("+"))
        print(len(data))    
        print(data)    

    i = i + 1



