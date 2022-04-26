#!env/bin/python3

import hashlib
import hmac
import json

from verify_sig_tools import test_payload

secret = bytes('secret_token_12345', 'utf-8')
req_body2 = bytes(json.dumps(test_payload, separators=(',', ':')), 'utf-8')


sig_vrfy = hmac.new(secret, req_body2, hashlib.sha256).hexdigest()
sig_vrfy = "sha256={}".format(sig_vrfy)

print(sig_vrfy)