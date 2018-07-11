from models.recipe import Recipe as RecipeModel


class Recipe:
    def __init__(self):
        pass

    def save(self, args):

        recipe = RecipeModel(
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

        # TODO Add recipe controller!

        # print(recipe.data())

        return recipe.save()