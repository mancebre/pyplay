from libraries.database import MyDB
import json


# TODO Learn more about this!
class Recipe:

    def __init__(self, amount=None, base=None, comment=None, desired_strength=None, flavor=None, nicotine=None, pg=None, vg=None, sleep_time=None, vape_ready=None, wvpqa=None):
        self.db = MyDB()

        if not nicotine:
            nicotine_obj = {
                "pg": None,
                "vg": None,
                "strength": None
            }
        else:
            nicotine_obj = json.loads(nicotine)

        if not flavor:
            flavor_obj = None
        else:
            flavor_obj = json.loads(flavor)

        self.amount = amount
        self.base = base
        self.comment = comment
        self.desired_strength = desired_strength
        self.flavor = flavor_obj
        self.nicotine_pg = nicotine_obj["pg"]
        self.nicotine_vg = nicotine_obj["vg"]
        self.nicotine_strength = nicotine_obj["strength"]
        self.pg = pg
        self.vg = vg
        self.sleep_time = sleep_time
        # No fucking idea why this don't work!!!
        self.vape_ready = 1 if vape_ready else 0
        self.wvpqa = wvpqa

        print(vape_ready)
        print(self.vape_ready)

    def set(self, amount, base, comment, desired_strength, flavor, nicotine, pg, vg, sleep_time, vape_ready, wvpqa):

        nicotine_obj = json.loads(nicotine)
        flavor_obj = json.loads(flavor)

        self.amount = amount
        self.base = base
        self.comment = comment
        self.desired_strength = desired_strength
        self.flavor = flavor_obj
        self.nicotine_pg = nicotine_obj["pg"]
        self.nicotine_vg = nicotine_obj["vg"]
        self.nicotine_strength = nicotine_obj["strength"]
        self.pg = pg
        self.vg = vg
        self.sleep_time = sleep_time
        # No fucking idea why this don't work!!!
        self.vape_ready = 1 if vape_ready else 0
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
        sql = """INSERT INTO `recipe` 
        (amount, desired_strength, pg, vg, nicotine_strength, nicotine_pg, nicotine_vg, wvpga, sleep_time, vape_ready, comment) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        result = self.db.insert(sql, (self.amount, self.desired_strength, self.pg, self.vg, self.nicotine_strength, self.nicotine_pg, self.nicotine_vg, self.wvpqa, self.sleep_time, self.vape_ready, self.comment))

        return result

    # Load recipe by id from database
    def load(self):
        pass
