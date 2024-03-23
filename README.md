# Project Name

This project interacts with the "Conversational Language Understanding" API to retrieve intent predictions.

## Setup

1. Obtain an API key from Azure for the "Conversational Language Understanding" service.
2. Install dependencies by running `pip install -r requirements.txt`.
3. Update `api/conversational_language_understanding.py` with your API key and API endpoint.
4. Run tests using pytest: `pytest tests/`.

## Usage

Example usage:

```python
from api.conversational_language_understanding import ConversationalLanguageUnderstanding

clf = ConversationalLanguageUnderstanding(api_key="your_api_key_here", base_url="https://your-api-endpoint.com")
text = "How do I make spaghetti carbonara?"
intent = clf.get_intent(text)
print("Intent:", intent)
