import hmac
import hashlib
import json

rec_sig = "sha256=9338acf9bdb73ccdd07a97abfc969b83306580fa9946f9be70678e46faf64d2e"
body = b'{"webhookId":"7f9eef16-b69e-47f9-ac42-e7843b43cc20"}'
secret = b'secret_token_12345'

signature = hmac.new(secret, body, hashlib.sha256).hexdigest()

signature = "sha256={}".format(signature)

is_valid = signature == rec_sig

print(is_valid)


