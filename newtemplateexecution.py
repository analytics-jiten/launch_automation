from numpy import nan
from requests.api import request
from requests.models import Response
import config
import pandas as pd
import httplib2
import requests
import json
from pandas.io.json import json_normalize

_header = {"Accept": "application/vnd.api+json;revision=1",
           "Content-Type": "application/vnd.api+json;revision=1",
           "Authorization": "Bearer " + config.access_token,
           "X-Api-Key": config.config['apiKey'],
           'X-Gw-Ims-Org-Id': config.config["orgId"]
           }

_companyId = requests.get(
    'https://reactor.adobe.io/companies?filter[name]=CONTAINS PLC', headers=_header, verify=False).json()['data'][0]['id']


def getPropertyId(config, access_token, companyId):
    response = requests.get("https://reactor.adobe.io/companies/"+str(companyId) +
                            "/properties?filter[name]=CONTAINS sky", headers=_header, verify=False)
    return response.json()['data'][0]['id']


def execute1(config, access_token):
    propertyId = getPropertyId(config, access_token, _companyId)
    
    fileObj = pd.read_csv('template.csv')
    a = len(fileObj['Rule Name'])
    i = 0
    while(i<a):
        rule_name = fileObj['Rule Name'][i]
        if i!=0 : 
            rule_name_prev = fileObj['Rule Name'][i-1] 
        else: 
            rule_name_prev = "" 
        if rule_name is not nan and rule_name is not rule_name_prev:
            dic = {}
            dic['data']={}
            dic['data']['attributes'] = {
                'name' : rule_name
            }
            dic['data']['type'] = 'rules'

            #dumps the above json
            to_python = json.dumps(dic)
            #network call to creates this rule
            response = requests.post("https://reactor.adobe.io/properties/"+propertyId +"/rules", data=to_python, headers=_header, verify=False)
            print(response)
            print("hello")
            if(response.status_code == 201):
                entirejson = response.json()
                print("Congratulations! Your Rule is Created Successfully")
                ruleId = entirejson['data']['id']
            else:
                print("Oops! Error Occured. Please check the error here:", response)
            entirejson = response.json()
            ruleId = entirejson['data']['id']
            print("Your rule id is : "+ruleId)
    
        #creating components - Event of this rule
        event_name = fileObj['Event Name'][i]    
        event_type = fileObj['Event Type'][i]
        event_extension = fileObj['Event Extension'][i]
        #delegate descriptor id
        desc_id = event_extension+"::events::"+event_type
        
        dic['data']['attributes'] = {
            'delegate_descriptor_id':desc_id,
            'name': event_name,
        }    
        dic['data']['relationships'] = {}
        dic['data']['relationships']['extension'] = {
            'data': {
                'id': 'EXc26c6bcee0764457bea1fa8581f9928c',
                 'type': 'extensions'
             }
           }

        dic['data']['relationships']['rules'] = {
            'data': [{
                'id': ruleId,
                'type': 'rules'
            }]
        }
        dic['data']['type'] = 'rule_components'

        to_python = json.dumps(dic)
        #network call to create this component
        response = requests.post("https://reactor.adobe.io/properties/"+propertyId +"/rule_components",data=to_python, headers=_header, verify=False)
        if(response.status_code):
            print("Congratulations! Your Rule component is Created Successfully")
            jsonResponse = response.json()
            print("Entire JSON response")
            print(jsonResponse)
            
        #creating Conditions - Event of this rule
        condition_name = fileObj['Condition Name'][i]    
        condition = fileObj['Condition Type'][i]
        condition_extension = fileObj['Condition Extension'][i]

        #Splitting combined values of conditions 
        condition_type = list(condition.split(","))
        #delegate descriptor id
        desc_id = condition_extension+"::conditions::"+str(condition_type[0])
        print(condition_type)

        dic['data']['attributes'] = {
        'delegate_descriptor_id': desc_id,
        'name': condition_name,
        'settings': json.dumps({'source':str(condition_type[1]),'language': str(condition_type[2])})
        }

        to_python = json.dumps(dic)
        response = requests.post("https://reactor.adobe.io/properties/"+propertyId +"/rule_components", data= to_python, headers=_header, verify=False)
        if(response.status_code == 201):
            print("Congratulations! Your Rule component is Created Successfully")
        else:
            print("Oops! Error Occured. Please check the error here:", response.json)
        jsonResponse = response.json()
        print("Entire JSON response")
        print(jsonResponse)
        #increment the counter to next rule
        i = i + 1


execute1(config.config,config.access_token)