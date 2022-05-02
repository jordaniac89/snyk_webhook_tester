#!/usr/bin/env sh

cd ../

$(which python3) -m venv env
. env/bin/activate

pip install --upgrade pip
pip install -r requirements.txt