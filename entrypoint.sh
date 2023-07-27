#! /bin/bash

pipenv run gunicorn --config gunicorn_config.py app:app