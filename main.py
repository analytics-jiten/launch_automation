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
                            "/properties?filter[name]=CONTAINS Yash_TrainingJun21", headers=_header, verify=False)
    return response.json()['data'][0]['id']


def createRule(config, access_token,rule):
    propertyId = getPropertyId(config, access_token, _companyId)
    # post_body = r"""
    #     {
    #   "data": {
    # "attributes": {
    #   "name": """+json.dumps(rule)+r"""
    # },
    # "type": "rules"
    # }
    # }
    # """
    dic = {}
    dic['data']={}
    dic['data']['attributes'] = {
        'name' : 'Hello World Rule'
    }
    dic['data']['type'] = 'rules'

    to_python = json.dumps(dic)
    response = requests.post("https://reactor.adobe.io/properties/"+propertyId +
                             "/rules", data=to_python, headers=_header, verify=False)
    if(response.status_code == 201):
        entirejson = response.json()
        print("Congratulations! Your Rule is Created Successfully")
        
    else:
        print("Oops! Error Occured. Please check the error here:", response)
    ruleId = entirejson['data']['id']


    #create Events

    dic ={}
    dic['data'] = {}
    dic['data']['attributes'] = {
        'delegate_descriptor_id':'core::events::click',
        'name': 'Test-final',
    }
    
    dic['data']['relationships'] = {}

    dic['data']['relationships']['extension'] = {
        'data': {
            'id': 'EXa0d885ebf6374e95a84af877c8db9528',
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
    response = requests.post("https://reactor.adobe.io/properties/"+propertyId +"/rule_components", data=to_python, headers=_header, verify=False)

    if(response.status_code == 201):
          print("Congratulations! Your Rule component is Created Successfully")
    else:
          print("Oops! Error Occured. Please check the error here:", response.json)
    jsonResponse = response.json()
    print("Entire JSON response")
    print(jsonResponse)

    #create Conditions
    dic = {}
    page1 = 'page'
    dic['data'] = {}

    dic['data']['attributes'] = {
        'delegate_descriptor_id': 'core::conditions::landing-page',
        'name': 'Core - Landing Page',
        'settings': json.dumps({'page': page1})
    }
    
    dic['data']['relationships'] = {}

    dic['data']['relationships']['extension'] = {
        'data': {
            'id': 'EXa0d885ebf6374e95a84af877c8db9528',
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
    response = requests.post("https://reactor.adobe.io/properties/"+propertyId +"/rule_components", data=to_python, headers=_header, verify=False)

    if(response.status_code == 201):
          print("Congratulations! Your Rule component is Created Successfully")
    else:
          print("Oops! Error Occured. Please check the error here:", response.json)
    jsonResponse = response.json()
    print("Entire JSON response")
    print(jsonResponse)

    
    #create Actions
    dic = {}
    dic['data'] = {}
    dic['data']['attributes'] = {
        'delegate_descriptor_id': 'adobe-analytics::actions::send-beacon',
        'name': 'AA - Send Beacon',
        'settings': json.dumps('{"type":"page"}')
    }

    #to make send beacon put 'settings': {'{"type":"page"}'}
    
    dic['data']['relationships'] = {}

    dic['data']['relationships']['extension'] = {
        'data': {
            'id': 'EX075d5e58920a4f9086cad021775bfd19',
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

    response = requests.post("https://reactor.adobe.io/properties/"+propertyId +"/rule_components", data= to_python, headers=_header, verify=False)

    if(response.status_code == 201):
          print("Congratulations! Your Rule component is Created Successfully")
    else:
          print("Oops! Error Occured. Please check the error here:", response.json)
    jsonResponse = response.json()
    print("Entire JSON response")
    print(jsonResponse)
 


createRule(config.config, config.access_token,"test rule components ")


