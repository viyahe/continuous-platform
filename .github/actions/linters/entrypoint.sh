#!/bin/sh
pipenv install --dev --deploy
pipenv run black
pipenv run gitlint
pipenv run pylint
pipenv run pydocstyle

