import hmac
import hashlib
import json
import os

from fapi_logging.fapi_logging import retrieve_logger


def sig_verify(signature, req_body):
    logger = retrieve_logger()

    secret = bytes(os.getenv('SECRET'), 'utf-8')

    sig_vrfy = hmac.new(secret, req_body, hashlib.sha256).hexdigest()
    sig_vrfy = "sha256={}".format(sig_vrfy)

    logger.info('sig_verifiy: %s', sig_vrfy)
    return signature == sig_vrfy

