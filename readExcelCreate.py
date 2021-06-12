from abc import abstractproperty
import json
from numpy import equal, nan
import pandas as pd
from createComponent import *
from main import *


file1 = pd.read_csv("file1.csv")
condition_data = (file1['delegate_descriptor_condition_settings'][0])
event_data = (file1['delegate_descriptor_event_settings'][0])
action_data = (file1['delegate_descriptor_action_settings'][0])



def createR(fileObj):
    a = len(fileObj['rule'])
    i = 0
    while(i<a):
        #print(str(i)+" "+str(a))
        print("rule is : "+fileObj['rule'][i])
        ruleId = createRule(config.config,config.access_token,fileObj['rule'][i])
        print("Creating Component Conditions: ")
        Condition = fileObj['delegate_descriptor_condition_settings'][i]
        if Condition is not nan:
            data = list(Condition.split("+"))    
            for d in data:
                print(d)
                createComponentCondition(config.config, config.access_token,str(d),ruleId)
        print("Creating Component Event: ")
        Event = fileObj['delegate_descriptor_event_settings'][i]
        if Event is not nan:
            data = list(Event.split("+"))    
            for d in data:
                createComponentEvent(config.config, config.access_token,str(d),ruleId)
        print("Creating Component Action: ")
        Action = fileObj['delegate_descriptor_action_settings'][i]
        if Action is not nan:
            data = list(Action.split("+"))    
            for d in data:
                print(d)
                createComponentAction(config.config, config.access_token,str(d),ruleId)
        
        #Moving to next rule        
        i = i + 1


# createCondition(file1)
# createEvent(file1)
# createAction(file1)
createR(file1)





# def createCondition(fileObj):
#     i = 0
#     fi = fileObj
#     data = "test"
#     a = len(file1['delegate_descriptor_condition_settings'])
#     while(i<a):
#         data = fi['delegate_descriptor_condition_settings'][i]
#         i = i+1
#         if(data is nan):
#             break
#         createComponentCondition(config.config, config.access_token,str(data))

# def createAction(fileObj):
#     i = 0
#     fi = fileObj
#     data = "test"
#     a = len(file1['delegate_descriptor_action_settings'])
#     while(i<a):
#         data = fi['delegate_descriptor_action_settings'][i]
#         i = i+1
#         if(data is nan):
#             break
#         createComponentAction(config.config, config.access_token,data)
        

# def createEvent(fileObj):
#     i = 0
#     fi = fileObj
#     data = "test"
#     a = len(file1['delegate_descriptor_event_settings'])
#     while(i<a):
#         data = fi['delegate_descriptor_event_settings'][i]
#         i = i+1
#         if(data is nan):
#             break
#         createComponentEvent(config.config, config.access_token,data)
        

