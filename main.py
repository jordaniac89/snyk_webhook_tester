from fastapi import FastAPI

app = FastAPI()

@app.get('/test')
def return_test():
    return "SUCCESS!"

