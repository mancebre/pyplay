from libraries.database import MyDB
import json

# TODO Learn more about this!
class Recipe:

    def __init__(self):
        self.db = MyDB()

    def set(self, amount, base, comment, desired_strength, flavor, nicotine, pg, sleep_time, vape_ready, vg, wvpqa):

        nicotineObj = json.loads(nicotine)

        self.amount = amount
        self.base = base
        self.comment = comment
        self.desired_strength = desired_strength
        self.flavor = flavor
        self.nicotine_pg = nicotineObj["pg"]
        self.nicotine_vg = nicotineObj["vg"]
        self.nicotine_strength = nicotineObj["strength"]
        self.pg = pg
        self.vg = vg
        self.sleep_time = sleep_time
        self.vape_ready = vape_ready
        self.wvpqa = wvpqa

    # Save recipe and return recipe id
    def save(self):
        pass

    # Load recipe by id from database
    def load(self):
        pass


