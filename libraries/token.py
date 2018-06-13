
import time
from config import Config
import jwt


class Token:
    def __init__(self, data):
        self.payload = {
            "iss":          "PyPlay",
            "iat":          time.time(),
            "exp":          self.set_token_expiry(self),
            "aud":          "www.vaperscuisine.com/",
            "sub":          data["user_data"]["email"],
            "user_id":      data["user_data"]["user_id"],
            "firstname":    data["user_data"]["firstname"],
            "lastname":     data["user_data"]["lastname"],
            "username":     data["user_data"]["username"],
            "email":        data["user_data"]["email"],
            "roles":        data["user_roles"]
        }
        self.token = str(jwt.encode(self.payload, Config.SECRET_KEY, algorithm=Config.ALGORITHM))

    @staticmethod
    def set_token_expiry(self):
        return int(time.time() + Config.TOKEN_EXPIRY)
