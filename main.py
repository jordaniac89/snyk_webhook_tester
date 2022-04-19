import os

from fastapi import FastAPI

app = FastAPI()

@app.get('/test')
def return_test():

    return_val = '''
        Test 1: {os.environ.get("test1")
    '''

    return return_val

