#!/bin/sh
set -e
if [ -n "$GH_KEY" ]; then
  mkdir -p /root/.ssh
  ssh-keyscan -t rsa github.com > /root/.ssh/known_hosts
  echo "$GH_KEY" > /root/.ssh/id_rsa
  chmod 400 /root/.ssh/id_rsa
fi

pipenv install --dev --deploy
pipenv run pylint
