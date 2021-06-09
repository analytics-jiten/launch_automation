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



def createComponent(config, access_token):
    # https://experience.adobe.com/#/@accenture-partner/data-collection/client/companies/CO268e14e0982744c98e52417ad4ed6833/properties/PR23e1ae6d96634c5dab7e01c113397dac/rules/RL8ade93b528144b0685df3ca658831bfc
    # https://experience.adobe.com/#/@accenture-partner/data-collection/client/companies/CO268e14e0982744c98e52417ad4ed6833/properties/PR23e1ae6d96634c5dab7e01c113397dac/extensions/EXc26c6bcee0764457bea1fa8581f9928c
    propertyId = getPropertyId(config, access_token, _companyId)
    print(propertyId)
    post_body = r"""{
	"data": {
			
			"attributes": {
			"delegate_descriptor_id": "core::conditions::landing-page",
			"name": "Core - Landing Page",
			"settings": "{\"page\": \"test\"}"
		},
		"relationships": {
			"extension": {
				"data": {
					"id": "EXc26c6bcee0764457bea1fa8581f9928c",
					"type": "extensions"
				}
			},
			"rules": {
				"data": [{
					"id": "RL8ade93b528144b0685df3ca658831bfc",
					"type": "rules"
				}]
			}
		},
		"type": "rule_components"
	}
}"""
    to_python = json.loads(post_body)
    response = requests.post("https://reactor.adobe.io/properties/"+propertyId +"/rule_components", data=json.dumps(to_python), headers=_header, verify=False)

    if(response.status_code == 201):
          print("Congratulations! Your Rule component is Created Successfully")
    else:
          print("Oops! Error Occured. Please check the error here:", response.json)
    jsonResponse = response.json()
    print("Entire JSON response")
    print(jsonResponse)
            
createComponent(config.config, config.access_token)
