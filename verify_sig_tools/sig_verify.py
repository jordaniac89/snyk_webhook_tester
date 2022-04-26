import hmac
import hashlib
import json

from fapi_logging.fapi_logging import retrieve_logger
from test_tools import test_model


def sig_verify(signature, req_body):
    logger = retrieve_logger()

    secret = bytes('secret_token_12345', 'utf-8')

    sig_vrfy = hmac.new(secret, req_body, hashlib.sha256).hexdigest()
    sig_vrfy = "sha256={}".format(sig_vrfy)

    logger.info('sig_verifiy: %s', sig_vrfy)
    return signature == sig_vrfy


if __name__ == '__main__':

    model_json = json.dumps(test_model.test_model, separators=(",", ":"))
    model_bytes = bytes(model_json, 'utf-8')

    secret = bytes('secret_token_12345', 'utf-8')

    sig_vrfy = hmac.new(secret, model_bytes, hashlib.sha256).hexdigest()
    sig_vrfy = "sha256={}".format(sig_vrfy)

