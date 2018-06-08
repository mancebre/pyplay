

from flask_restful import request
import jwt
from config import Config

# Usage
# encoded = jwt.encode({'some': 'payload'}, Config.SECRET_KEY, algorithm=Config.ALGORITHM)
#
# decoded = jwt.decode(encoded, Config.SECRET_KEY, algorithms=[Config.ALGORITHM])
#
# print("encoded", encoded)
# print("decoded", decoded)


class Auth:

    def authenticate(self):

        encoded = request.headers.get('Authorization')

        decoded = jwt.decode(encoded, Config.SECRET_KEY, algorithms=[Config.ALGORITHM], audience=Config.AUDIENCE)
        print("decoded", decoded)

