import os

from fastapi import FastAPI

app = FastAPI()

@app.get('/test')
def return_test():

    test1 = os.environ.get("test1")

    return test1

