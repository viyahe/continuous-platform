FROM python:3.8

RUN pip install --upgrade pip && \
    pip install pipenv

ENV PIPENV_VENV_IN_PROJECT=true

COPY "entrypoint.sh" "/entrypoint.sh"
RUN chmod +x /entrypoint.sh

ENTRYPOINT [ "/entrypoint.sh" ]
