from models.recipe import Recipe as RecipeModel


class Recipe:
    def __init__(self):
        self.recipeModel = RecipeModel

    def save(self, args):

        # print(self)
        # return False

        return self.recipeModel.save(
            self,
            args['name'],
            args['amount'],
            args['base'],
            args['comment'],
            args['desired_strength'],
            args['flavor'],
            args['nicotine'],
            args['pg'],
            args['vg'],
            args['sleep_time'],
            args['vapeReady'],
            args['wvpga'],
        )

    def get(self, recipe_id):
        return self.recipeModel.get(self, recipe_id)