#snyk_webhook_tester

## Prerequisites
Python 3.8

## Quickstart
1) clone this project to a directory
2) from the project root `cd scripts_sh`
3) Run `bash env_gen.sh && bash startup.sh` - this will set up a python virtual environment, install dependencies, and start the uvicorn app
4) Import `pm_webhook_emulate.json` collection into your Postman environment
5) Do a post!

## Signature Verification
Signature verification should work out of the box. I'm using `secret_token_12345` to sign the request body of what's in `pm_webhook_emulate.json`.
You can use a different token/signature by:
1) going to the postman request -> Pre-request Script tab -> Change `secret_token` to something of your choice.
2) doing a post
3) retrieving the output from the console
4) adding the signature to the header `X-Hub-Signature`
5) in your project, update the `.env` file to match the secret you chose

NOTE! Make sure your JSON payload isn't formatted. It should be one string with no spaces. 


## Notes
This app uses FastAPI and the Pydantic data model. Requests are received as raw json, the signature verified, and then marshalled into a Pydantic model
for easier use.
