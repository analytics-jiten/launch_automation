import json
import pandas as pd


file1 = pd.read_csv("file1.csv")
condition_data = (file1['delegate_descriptor_condition_settings'][0])

descriptor, page1 = list(condition_data.split(","))


dic = {}

dic['data'] = {}

dic['data']['attributes'] = {
    'delegate_descriptor_id': descriptor,
    'name': 'Core - Landing Page',
    'settings': {'page':page1}
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
        'id': 'RL8ade93b528144b0685df3ca658831bfc',
        'type': 'rules'
    }]
}

dic['data']['type'] = 'rule_components'


s = json.dumps(dic)

print(s) 
