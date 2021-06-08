import time
import jwt
import json 
import time
import datetime
import requests

config = {
"apiKey":"f41462b5e5724dbbbb84bfbff9b504bf",#client id
"technicalAccountId":"C088169960B8B8070A495F93@techacct.adobe.com",
"orgId":"0CEB60F754C7E06B0A4C98A2@AdobeOrg",
"secret":"p8e-sBXHxAtfKM-iL2NqBsg7DFi307n93F3f",

"key":"""
-----BEGIN PRIVATE KEY-----
MIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQCj+GNQV2hblhzzk6HrYOv/Pz5O
IQX8GtkRZB6CA+Q0tpJMHEeG9PCpY+8Yisthw0G7Y4+ifT9gU7wXlcgPGh2u5QjNRB83YeVqdkDp
sDl+Ns3tBSPGvvEu/t39ZNhThmzL7tbFmTM9U+zH3M1hhswFcr7IN6AK4effXf2yL8kmCGSe3j9B
1OrYnaxD3J9z9AaQJoL5f4Ip4imtjZEhGCPK81BrBCgm56u6Qpoz7WQkMm+O8kgi+0zcGDuu8QeB
Sh465Ln+ASvWZX91yspuYbRaRH8EMW6kUwmUxjYm/+ZBsGi1v0/pMOwbdFfFxmk7R928AjK7pR+v
k8D9b4ugAUsJAgMBAAECggEAbrGZwjwv7Fxr0RgiYHe++kLkufPbSXWKgw4W9mjQH7H9E7qnovkq
mwAnAmd4o9ggQPQWnHh3V31P5pAsTd2wmkhuZ7yMYmQJb5TDf7+DIKy42kD1BRAUXEic7pqs275N
JmNnxGAHUmic2dQ7JpLMmwT6vMmolpApbAbU5P0Ti0Nb+z+q5xuvgsAmZW8EiXecotp8f4EChYb4
o4wOyQi5aLh4NTnbZkBZE+dch1f0VF7eAGHjv42jALLU1OnigsRrLQawoQEJ+788IGVNFQJ+U/Kn
nI5F9515eE++U+ig+lbIVsiTt3qZWPLtOOXsh7XLhe499gc6mq4gPJNcYxExDQKBgQDbZ2lgJjfT
2I54g/QPHFIE4JZBSRPekfbWcXn9XbRPcPGzPwKT07HrgVVgWhzjEImMsFvAMEwnLrfPE3GHtmkl
DSkLmto0gDgqV2cggnIImhYrEwV0uNv4ra62nhxXAWMOuGwUAwdpeqnSbk/NcfISTuR2cQoXcQHa
HNxkOlUf2wKBgQC/UfKpxwtmkeRACUUFqTk6oBcmGzPLyA1P/cuYOVDq5GPwkJOBIC7FUY5buaDx
fV38tZZiuP5GwVKe+9icQ0L7FGnTURhm/SecU34pcsB/5+pC44u/MLNVua4lCMyqBLkHffcKBX+f
M/244W3i31OikMQ2Lrh99EJNHaUdU5836wKBgEM0F7jVu//tsyYC9Pyz5gOMbzmsEqP3/a2NsJoE
27gBlmcbA8UX8MV8JhSPRY3fgOJRGqlxocHWs4KAKCQzoV0x/MKLOg8evxVpFDOHATrVR7kF6IPq
I6a2PG+/WlrkF91oa+JtUxXh9qZ4F4WMQ2OMOrp0wWyQtsqCUJd6rpxFAoGAKzJIdNbRFyaHf4HY
SK/tkPQGZf8sUa1ofBAUgNkoEPDiM7Wg6D2o8bo5RzKBSSUCLIWfX8je+IC7s9OvE5EINYJlZmXf
+Zjc8anUSW10Uyy8sr+HlPJc+1UCIbB77UNFt5BUT7nwF7T4a17Sna/IxWKkOouP8jhNI/Y2iomP
4GMCgYAJ3tHW+m0T07n7WPwpNKn/sdEbgqhpr/VDnLx0Vth7/dxFF+YVp3PidqkeWRhaYE61XVDz
dOjYu67Sfkk+Ka1QaoszjS83KcDRznp8fXHXJzl03ZV1ySJ7JXaQWtJ4utPKEf5CDa3s1uT/9VYO
CKd39ZY2uE52Z5Pec6z5jsXZRw==
-----END PRIVATE KEY-----
""",   
"metascopes":"ent_reactor_sdk",
"imsHost":"ims-na1.adobelogin.com",  
"imsExchange":"https://ims-na1.adobelogin.com/ims/exchange/jwt/",
"activityURL":"https://analytics.adobe.io/discovery/me"
}

def get_jwt_token(config):
    return jwt.encode({
        "exp": datetime.datetime.utcnow() + datetime.timedelta(seconds=30),
        "iss": config["orgId"],
        "sub": config["technicalAccountId"],
        "https://{}/s/{}".format(config["imsHost"], config["metascopes"]): True,
        "aud": "https://{}/c/{}".format(config["imsHost"], config["apiKey"])
    }, config["key"], algorithm='RS256')

def get_access_token(config, jwt_token):
    post_body = {
        "client_id": config["apiKey"],
        "client_secret": config["secret"],
        "jwt_token": jwt_token
    }
    response = requests.post(config["imsExchange"], data=post_body, verify=False)
    #return response.json()["access_token"]
    #print(response.json())
    return response.json()['access_token']

jwt_token = get_jwt_token(config)
access_token = get_access_token(config, jwt_token)
#print("JWT Token:", jwt_token)
#print()
#print("Access Token:", access_token)