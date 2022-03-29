FROM python:3.8

# Required by CDK unit tests
RUN apt update && \
    apt install -y nodejs

RUN pip install --upgrade pip && \
    pip install pipenv

ENV PIPENV_VENV_IN_PROJECT=true

COPY "entrypoint.sh" "/entrypoint.sh"
RUN chmod +x /entrypoint.sh

ENTRYPOINT [ "/entrypoint.sh" ]
