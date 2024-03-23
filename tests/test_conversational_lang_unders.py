import pytest
from tests.config import subscription_key
from api.conversational_lang_unders import ConversationalLanguageUnderstanding

@pytest.fixture
def clu_instance():
    return ConversationalLanguageUnderstanding(
        endpoint="https://cooking102.cognitiveservices.azure.com/",
        api_version="2023-04-01",
        subscription_key=subscription_key
    )

def test_intent_recipe_search(clu_instance):
    text = "Find me a recipe for spaghetti carbonara"
    project_name = "CookingRecipes"
    deployment_name = "DeployCooking"
    intent = clu_instance.get_intent(text, project_name, deployment_name)
    assert intent == "searchRecipe"

def test_intent_recipe_ingredients(clu_instance):
    text = "What's the best way to cook pasta?"
    project_name = "CookingRecipes"
    deployment_name = "DeployCooking"
    intent = clu_instance.get_intent(text, project_name, deployment_name)
    assert intent == "searchRecipe"

def test_intent_recipe_instructions(clu_instance):
    text = "I want to make lasagna for dinner tonight. Do you have a recipe?"
    project_name = "CookingRecipes"
    deployment_name = "DeployCooking"
    intent = clu_instance.get_intent(text, project_name, deployment_name)
    assert intent == "searchRecipe"