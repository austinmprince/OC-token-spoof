# .\token_env\Scripts\Activate.ps1
from jose import JWTError, jwt
from decouple import Config, RepositoryEnv
from datetime import datetime, timedelta
import pem

DOTENVFILE = '.env.local'
env_config = Config(RepositoryEnv(DOTENVFILE))

private_key = open('private_key.pem', 'r').read()
public_key = open('public_key.pem', 'r').read()

secret = env_config.get("secret")
alg = env_config.get("algorithm")


token = {
  "phone_number": "1234567",
  "given_name": "Bert",
  "family_name": "Hair",
  "email": "admin@contosohelp.com",
  "locale": "zh-hk",
  "lwicontexts": {
    "PUID": {
      "value": "1055521783620212",
      "isDisplayable": True
    },
    "Locale": {
      "value": "fi-FI",
      "isDisplayable": True
    },
    "Product": {
      "value": "Xbox",
      "isDisplayable": True
    },
    "Issue": {
      "value": "Family-Online",
      "isDisplayable": True
    }
  },

  "iss": "https://sts.windows.net/fc85ef74-c8af-4f01-83d7-85576e32905a/",
}

expire = datetime.utcnow() + timedelta(minutes=15)

to_encode = token.copy()
to_encode.update({"exp": expire})
encoded_jwt = jwt.encode(to_encode, private_key, algorithm=alg)


print(encoded_jwt)
print(jwt.decode(encoded_jwt, public_key, algorithms=[alg]))


