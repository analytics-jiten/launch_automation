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


def createRule(config, access_token):
    propertyId = getPropertyId(config, access_token, _companyId)
    post_body = """
        {
      "data": {
    "attributes": {
      "name": "First Yash Testing via API"
    },
    "type": "rules"
    }
    }
    """
    to_python = json.loads(post_body)
    response = requests.post("https://reactor.adobe.io/properties/"+propertyId +
                             "/rules", data=json.dumps(to_python), headers=_header, verify=False)
    if(response.status_code == 201):
        print("Congratulations! Your Rule is Created Successfully")
    else:
        print("Oops! Error Occured. Please check the error here:", response)


createRule(config.config, config.access_token)


