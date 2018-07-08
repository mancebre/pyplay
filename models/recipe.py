from libraries.database import MyDB
import json


# TODO Learn more about this!
class Recipe:

    def __init__(self):
        self.db = MyDB()

    def set(self, amount, base, comment, desired_strength, flavor, nicotine, pg, vg, sleep_time, vape_ready, wvpqa):

        nicotine_obj = json.loads(nicotine)

        self.amount = amount
        self.base = base
        self.comment = comment
        self.desired_strength = desired_strength
        self.flavor = flavor
        self.nicotine_pg = nicotine_obj["pg"]
        self.nicotine_vg = nicotine_obj["vg"]
        self.nicotine_strength = nicotine_obj["strength"]
        self.pg = pg
        self.vg = vg
        self.sleep_time = sleep_time
        self.vape_ready = vape_ready
        self.wvpqa = wvpqa

    def data(self):
        return {
            "amount": self.amount,
            "base": self.base,
            "comment": self.comment,
            "desired_strength": self.desired_strength,
            "flavor": self.flavor,
            "nicotine_pg": self.nicotine_pg,
            "nicotine_vg": self.nicotine_vg,
            "nicotine_strength": self.nicotine_strength,
            "pg": self.pg,
            "vg": self.vg,
            "sleep_time": self.sleep_time,
            "vape_ready": self.vape_ready,
            "wvpqa": self.wvpqa
        }

    # Save recipe and return recipe id
    def save(self):
        pass

    # Load recipe by id from database
    def load(self):
        pass
