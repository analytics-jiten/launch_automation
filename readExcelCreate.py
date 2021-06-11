import json
from numpy import equal, nan
import pandas as pd
from createComponent import *


file1 = pd.read_csv("file1.csv")
condition_data = (file1['delegate_descriptor_condition_settings'][0])
event_data = (file1['delegate_descriptor_event_settings'][0])
action_data = (file1['delegate_descriptor_action_settings'][0])



def createCondition(fileObj):
    i = 0
    fi = fileObj
    data = "test"
    a = len(file1['delegate_descriptor_condition_settings'])
    while(i<a):
        data = fi['delegate_descriptor_condition_settings'][i]
        i = i+1
        if(data is nan):
            break
        createComponentCondition(config.config, config.access_token,str(data))

def createAction(fileObj):
    i = 0
    fi = fileObj
    data = "test"
    a = len(file1['delegate_descriptor_action_settings'])
    while(i<a):
        data = fi['delegate_descriptor_action_settings'][i]
        i = i+1
        if(data is nan):
            break
        createComponentAction(config.config, config.access_token,data)
        

def createEvent(fileObj):
    i = 0
    fi = fileObj
    data = "test"
    a = len(file1['delegate_descriptor_event_settings'])
    while(i<a):
        data = fi['delegate_descriptor_event_settings'][i]
        i = i+1
        if(data is nan):
            break
        createComponentEvent(config.config, config.access_token,data)
        

createCondition(file1)
createEvent(file1)
createAction(file1)