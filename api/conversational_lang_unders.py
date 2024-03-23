import requests

class ConversationalLanguageUnderstanding:
    def __init__(self, endpoint, api_version, subscription_key):
        self.endpoint = endpoint
        self.api_version = api_version
        self.subscription_key = subscription_key

    def get_intent(self, text, project_name, deployment_name):
        request_url = f"{self.endpoint}/language/:analyze-conversations?api-version={self.api_version}"
        headers = {
            "Ocp-Apim-Subscription-Key": self.subscription_key,
            "Content-Type": "application/json"
        }
        request_body = {
            "kind": "Conversation",
            "analysisInput": {
                "conversationItem": {
                    "id": "1",
                    "participantId": "1",
                    "text": text
                }
            },
            "parameters": {
                "projectName": project_name,
                "deploymentName": deployment_name,
                "stringIndexType": "TextElement_V8"
            }
        }
        response = requests.post(request_url, headers=headers, json=request_body)
        if response.status_code == 200:
            response_json = response.json()
            top_intent = response_json["result"]["prediction"]["topIntent"]
            return top_intent
        else:
            return None
