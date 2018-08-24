from libraries.database import MyDB
import json

# TODO I forgot to add user id
class Recipes:
    def __init__(self):
        self.db = MyDB()

    def getAllRecipesByUserId(self, user_id):
        sql = """SELECT * FROM recipe WHERE user_id = %s"""
        data = self.db.select(sql, user_id)

        if data:
            recipes = list()
            for recipe in data:
                recipes.append({
                    "id": recipe[0],
                    "name": recipe[1],
                    "amount": recipe[2],
                    "desired_strength": recipe[3],
                    "pg": recipe[4],
                    "vg": recipe[5],
                    "nicotine_strength": recipe[6],
                    "nicotine_pg": recipe[7],
                    "nicotine_vg": recipe[8],
                    "wvpga": recipe[9],
                    "sleep_time": recipe[10],
                    "vape_ready": recipe[11],
                    "comment": recipe[12]
                })
            return recipes
        else:
            return False

# ALTER TABLE `recipe`
# 	ADD COLUMN `user_id` INT(11) NOT NULL COMMENT 'Id of recipe owner' AFTER `comment`;
