
from models.recipes import Recipes as RecipesModel
from libraries.token import Token


class Recipes:
    def __init__(self):
        self.RecipesModel = RecipesModel
    # Return all recipes of this user
    def return_user_recipes(self, user_id):

        recipes = RecipesModel.getAllRecipesByUserId(self, user_id)
        return recipes, 200
