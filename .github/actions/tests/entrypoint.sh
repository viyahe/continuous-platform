#!/bin/sh
curl -L $REPORTER_BINARY_URL > /tmp/cc-test-reporter
chmod +x /tmp/cc-test-reporter
pipenv install --dev --deploy

/tmp/cc-test-reporter before-build
pipenv run pytest
PYTEST_EXIT_CODE=$?
/tmp/cc-test-reporter after-build --debug --exit-code $PYTEST_EXIT_CODE

exit $PYTEST_EXIT_CODE 
