import json
import os

from fastapi import FastAPI, Request, HTTPException

from fapi_logging.fapi_logging import retrieve_logger
from models import ProjectSnapshot

from verify_sig_tools.sig_verify import sig_verify

app = FastAPI(debug=True)

logger = retrieve_logger()


@app.get('/test', status_code=200)
async def return_test():
    return 'OK'


@app.post('/test_post', status_code=200)
async def do_post(request: Request):

    body = await request.body()

    signature = request.headers['X-Hub-Signature']
    event = request.headers['X-Snyk-Event']

    logger.debug('Got signature -> %s', signature)
    logger.debug('Got event -> %s', event)

    logger.debug('got secret %s', os.getenv('SECRET'))

    if event == 'project_snapshot/v0':

        if sig_verify(signature, body):
            logger.debug('Signature was verified')
        else:
            raise HTTPException(status_code=401, detail="Invalid Signature")

        ps = None
        try:
            ps = ProjectSnapshot.parse_raw(body)
            logger.info("orgid %s", ps.org.id)
        except Exception:
            raise HTTPException(status_code=500, detail="Invalid Request Body")

        if ps is not None:
            pass  # TODO: go to town!
    else:
        return {'msg': 'Ignoring event'}

