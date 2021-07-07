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



def fetchRuleComponent(config, access_token):
    propertyId = getPropertyId(config, access_token, _companyId)
    print("Property Id: "+propertyId)
    #https://reactor.adobe.io/rule_components/RC9ab25fbc35634e00b9395356a85a51b0/notes?sort=-updated_at&page[size]=1


    response = requests.get("https://reactor.adobe.io/rule_components/RC2b45a1dac2e04b52893cc876d7824533",  headers=_header, verify=False)

    if(response.status_code == 200):
          print("Congratulations! Your Rule component is Fetched Successfully")
    else:
          print("Oops! Error Occured. Please check the error here:", response)

    
    jsonResponse = response.json()
    print("Entire JSON response")
    print(jsonResponse)

fetchRuleComponent(config.config, config.access_token)




"""


core::conditions::landing-page, page +core::conditions::landing-page, page
core::conditions::landing-page,page +core::conditions::landing-page, page
core::conditions::landing-page, page +core::conditions::landing-page, page+core::conditions::landing-page, page +core::conditions::landing-page, page
core::conditions::landing-page, page +core::conditions::landing-page, page

"""