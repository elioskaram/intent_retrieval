# Project Name

This project interacts with the "Conversational Language Understanding" API to retrieve intent predictions.
The model have been trained to detect coocking recepies based on words present in the prompts

## Setup

1. Obtain an API key from Azure for the "Conversational Language Understanding" service.
2. **Create a `config.py` file:** 
Create a `config.py` file in your project directory to store sensitive configuration variables such as the API key (`subscription_key`). This file should not be committed to version control to keep your API key secure.

    Example `config.py` file:
    ```python
    # config.py
    subscription_key = "your_subscription_key_here"
    ```

3. add this file to .gitignore
4. make sure you have downloaded pytest
```bash
    pip install pytest
```
5. Run tests using pytest: `python -m pytest tests`.

## Usage

Example usage:

```python
# Import the necessary modules
from your_package import clu_instance

# Define the text input and project/deployment names
text = "Find me a recipe for spaghetti carbonara"
project_name = "CookingRecipes"
deployment_name = "DeployCooking"

# Use the CLU instance to get the intent for the given text
intent = clu_instance.get_intent(text, project_name, deployment_name)