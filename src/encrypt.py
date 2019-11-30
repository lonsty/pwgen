# @Author: allen
# @Date: Nov 30 16:00 2019
import base64
import hashlib
import hmac
import re

# key = CONSUMER_SECRET& #If you dont have a token yet
key = bytes("password","ascii")

# The Base String as specified here:
msg = bytes("github","ascii") # as specified by oauth

hashed = hmac.new(key=key, msg=msg, digestmod=hashlib.sha256)
b64_hmac = base64.b64encode(hashed.digest()).decode()
result = re.sub(r'\W', '', b64_hmac)  # remove symbols

print(result)