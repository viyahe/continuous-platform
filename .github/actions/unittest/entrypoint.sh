#!/bin/sh
set -e
if [ -n "$GH_KEY" ]; then
  mkdir -p /root/.ssh
  ssh-keyscan -t rsa github.com > /root/.ssh/known_hosts
  echo "$GH_KEY" > /root/.ssh/id_rsa
  chmod 400 /root/.ssh/id_rsa
fi

curl -L $REPORTER_BINARY_URL > /tmp/cc-test-reporter
chmod +x /tmp/cc-test-reporter
pipenv install --dev --deploy

/tmp/cc-test-reporter before-build
pipenv run pytest
PYTEST_EXIT_CODE=$?
/tmp/cc-test-reporter after-build --debug --exit-code $PYTEST_EXIT_CODE

exit $PYTEST_EXIT_CODE 
