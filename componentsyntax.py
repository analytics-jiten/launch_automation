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
""" Above json can create a event component of rule"""



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



{
	"data": {
		"attributes": {
			"delegate_descriptor_id": "core::conditions::landing-page",
			"name": "My Example Value Comparison",
			"settings": [{"page":"testing rule component"}]
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