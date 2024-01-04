#! recgen\Scripts\python.exe

import google.generativeai as palm
import os                                                                                                                                                                                                          
from dotenv import load_dotenv, find_dotenv
from pathlib import Path


load_dotenv(Path(r"recgen\.env"))
palm.configure(api_key=os.getenv("Key"))

def generate_recipe_suggestion(vegetables, cuisine, message, flag=0):
  """Generates a recipe suggestion based on the given vegetables and cuisine.

  Args:
    vegetables: A list of vegetables.
    cuisine: The cuisine type.

  Returns:
    A dictionary containing the following information:
      * cooking_steps: A list of cooking steps.
      * nutritional_information: A dictionary containing the nutritional information of the recipe.
      * estimated_time_to_cook: The estimated time to cook the recipe in minutes.
  """

  
  response = palm.chat(context="You are a great indian chef capable of writing the recipes of the given food items and giving the nutritional values of the dishes.",
                       messages=f"this is the list of ingredients/vegetables: {vegetables}. I want to make a delicious and royal dish of the {cuisine} cuisine. For generating the nice recipes from llm models like you, give a descriptive prompt that will first have the title of recipe in more attractive and mouth watery. then the incredients section where you will mention the list of incredients and the quantity need. next section would be the stepwise instruction in detailed manner. and the last section would be the nutritional values of that dish. the cuisine and the main incredients list will be the input to the model.",
                       temperature=1.0)
  if flag==1:
    response = response.reply(message)
  
  return response.last

# print(generate_recipe_suggestion(["Potato, Cauliflower, Carrot, Beans, Capsicum", "Tomato (Chopped)", "Onion (Chopped)", "Ginger-Garlic Paste"],"Indian- Maharashtrian"))