from libraries.database import MyDB
import json


# TODO Learn more about this!
# TODO THIS IS BULLSHIT! Do it right way!!
class Recipe:

    def __init__(self):
        self.db = MyDB()

    def save(self,
             name,
             amount,
             base,
             comment,
             desired_strength,
             flavor,
             nicotine,
             pg,
             vg,
             sleep_time,
             vape_ready,
             wvpqa):

        nicotine_obj = json.loads(nicotine)
        flavor_obj = json.loads(flavor)

        flavor = flavor_obj
        nicotine_pg = nicotine_obj["pg"]
        nicotine_vg = nicotine_obj["vg"]
        nicotine_strength = nicotine_obj["strength"]

        # recipe goes in recipe table and flavors goes in flavors table
        sql = """INSERT INTO `recipe` 
        (name, amount, desired_strength, pg, vg, nicotine_strength, nicotine_pg, nicotine_vg, wvpga, sleep_time, vape_ready, comment) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        recipe_id = self.db.insert(sql, (name,
                                         amount,
                                         desired_strength,
                                         pg,
                                         vg,
                                         nicotine_strength,
                                         nicotine_pg,
                                         nicotine_vg,
                                         wvpqa,
                                         sleep_time,
                                         vape_ready,
                                         comment))

        self.save_flavors(recipe_id)

        return recipe_id

    def save_flavors(self, recipe_id):
        for flavor in self.flavor:
            sql = """INSERT INTO `recipe_flavors`
            (recipe_id, name, amount, percentage, `type`, grams)
            VALUES (%s, %s, %s, %s, %s, %s)"""
            self.db.insert(sql, (recipe_id, flavor["name"], flavor["amount"], flavor["percentage"], flavor["type"], flavor["grams"]))

    # Load recipe by id from database
    def load(self):
        pass

    def get(self, recipe_id):
        sql = """SELECT * FROM recipe WHERE id = %s"""
        data = self.db.select_one(sql, recipe_id)

        print(data)

        if data:
            self.set(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9], data[10],
                     data[11])
            return self.data()
        else:
            return False
