{
    'data': {
        'id': 'RC63e6c0f00e474d85ba0453614e56bb42', 'type': 'rule_components', 'attributes': { 'created_at': '2021-07-06T18:49:01.149Z', 'delegate_descriptor_id': 'adobe-analytics::actions::set-variables', 'deleted_at': None, 'dirty': False, 'name': 'Adobe Analytics - Set Variables', 'negate': False, 'order': 0, 'rule_order': 50.0, 'timeout': 2000, 'delay_next': True, 'published': False, 'published_at': None, 'revision_number': 0, 'updated_at': '2021-07-06T18:49:01.149Z', 'settings': '{"trackerProperties":{"eVars":[{"name":"eVar1","type":"value","value":"1"}],"props":[{"name":"prop1","type":"value","value":"1"}]}}' }, 'relationships': {
            'updated_with_extension_package': { 'links': { 'related': 'https://reactor.adobe.io/rule_components/RC63e6c0f00e474d85ba0453614e56bb42/updated_with_extension_package' }, 'data': { 'id': 'EPbde2f7ca14e540399dcc1f8208860b7b', 'type': 'extension_packages' } }, 'updated_with_extension': {
                'links': { 'related': 'https://reactor.adobe.io/rule_components/RC63e6c0f00e474d85ba0453614e56bb42/updated_with_extension' }, 'data': {
                    'id': 'EX303a2dfe95444427a905bce603c71dfe',
                        'type': 'extensions'
                }
            }, 'extension': { 'links': { 'related': 'https://reactor.adobe.io/rule_components/RC63e6c0f00e474d85ba0453614e56bb42/extension' }, 'data': { 'id': 'EX075d5e58920a4f9086cad021775bfd19', 'type': 'extensions' } }, 'notes': { 'links': { 'related': 'https://reactor.adobe.io/rule_components/RC63e6c0f00e474d85ba0453614e56bb42/notes' } }, 'origin': { 'links': { 'related': 'https://reactor.adobe.io/rule_components/RC63e6c0f00e474d85ba0453614e56bb42/origin' }, 'data': { 'id': 'RC63e6c0f00e474d85ba0453614e56bb42', 'type': 'rule_components' } }, 'property': { 'links': { 'related': 'https://reactor.adobe.io/properties/PRbea6633fe0604c21a125ac20a3ecf53d' }, 'data': { 'id': 'PRbea6633fe0604c21a125ac20a3ecf53d', 'type': 'properties' } }, 'rules': { 'links': { 'related': 'https://reactor.adobe.io/rule_components/RC63e6c0f00e474d85ba0453614e56bb42/rules' } }
        }, 'links': { 'extension': 'https://reactor.adobe.io/extensions/EX075d5e58920a4f9086cad021775bfd19', 'origin': 'https://reactor.adobe.io/rule_components/RC63e6c0f00e474d85ba0453614e56bb42', 'rules': 'https://reactor.adobe.io/rule_components/RC63e6c0f00e474d85ba0453614e56bb42/rules', 'self': 'https://reactor.adobe.io/rule_components/RC63e6c0f00e474d85ba0453614e56bb42' }, 'meta': { 'latest_revision_number': 1 }
    }
}

dic = {}
    dic['data'] = {}
    dic['data']['attributes'] = {
        'delegate_descriptor_id': 'adobe-analytics::actions::set-variables',
        'name': 'AA - Set Var'
    }
    dic['data']['attributes']['settings'] = {}
    dic['data']['attributes']['settings']['trackerProperties'] = json.dumps({
        'eVars':[{
            'name':'eVar1','type':'value','value':'1'
        }]
    })
    
    dic['data']['attributes']['settings']['trackerProperties'] = json.dumps({
        'props':[{
            'name':'prop1','type':'value','value':'1'
        }]
    })
    
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