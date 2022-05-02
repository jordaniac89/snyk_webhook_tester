#!/usr/bin/env sh

cd ../
. env/bin/activate
uvicorn main:app --env-file .env