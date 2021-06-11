{
  "data": {
    "attributes": {
      "delegate_descriptor_id": "core::events::click",
      "name": "My Example Click Event"
     
    },
    "relationships": {
      "extension": {
        "data": {
          "id": "EXc26c6bcee0764457bea1fa8581f9928c",
          "type": "extensions"
        }
      },
      "rules": {
        "data": [
          {
            "id": "RL8ade93b528144b0685df3ca658831bfc",
            "type": "rules"
          }
        ]
      }
    },
    "type": "rule_components"
  }
} 




{
  "data": {
    "attributes": {
      "delegate_descriptor_id": "core::events::tab-blur",
      "name": "My Example var2"
     
    },
    "relationships": {
      "extension": {
        "data": {
          "id": "EXc26c6bcee0764457bea1fa8581f9928c",
          "type": "extensions"
        }
      },
      "rules": {
        "data": [
          {
            "id": "RL8ade93b528144b0685df3ca658831bfc",
            "type": "rules"
          }
        ]
      }
    },
    "type": "rule_components"
  }
} 


#Above json can create a event component of rule"""


{
  "data": {
    "attributes": {
      "delegate_descriptor_id": "core::conditions::value-comparison",
      "name": "My Example Value Comparison"
    },
    "settings":{
      "comparison":{
        "operator":"equals"
      },
      "leftOperand":"%Page Title%",
      "rightOperand":"testing"
    },
    "relationships": {
      "extension": {
        "data": {
          "id": "EXc26c6bcee0764457bea1fa8581f9928c",
          "type": "extensions"
        }
      },
      "rules": {
        "data": [
          {
            "id": "RL8ade93b528144b0685df3ca658831bfc",
            "type": "rules"
          }
        ]
      }
    },
    "type": "rule_components"
  }
}


r"""{
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


#it can create a condition

{
	"data": {
			
			"attributes": {
			"delegate_descriptor_id": "core::actions::custom-code",
			"name": "Core - Custom Code",
			"settings": "{\"source\": \"console\",\"language\":\"html\"}"
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
}
#It can create a action



    post_body = r"""{
	"data": {
			
			"attributes": {
			"delegate_descriptor_id":"""+json.dumps(descriptor)+r""",
			"name": "Core - Landing Page",
			"settings": "{\"page\":"""+json.dumps(page1)+r"""}\"
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


def createComponentAction(config, access_token):
    # https://experience.adobe.com/#/@accenture-partner/data-collection/client/companies/CO268e14e0982744c98e52417ad4ed6833/properties/PR23e1ae6d96634c5dab7e01c113397dac/rules/RL8ade93b528144b0685df3ca658831bfc
    # https://experience.adobe.com/#/@accenture-partner/data-collection/client/companies/CO268e14e0982744c98e52417ad4ed6833/properties/PR23e1ae6d96634c5dab7e01c113397dac/extensions/EXc26c6bcee0764457bea1fa8581f9928c
    propertyId = getPropertyId(config, access_token, _companyId)
    print(propertyId)
    post_body = r"""{
	"data": {
			
			"attributes": {
			"delegate_descriptor_id": "core::actions::custom-code",
			"name": "Core - Custom Code",
			"settings": "{\"source\": \"console\",\"language\":\"html\"}"
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
 

