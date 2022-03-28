FROM python:3.8

RUN pip install --upgrade pip && \
    pip install gitlint

COPY "entrypoint.sh" "/entrypoint.sh"
RUN chmod +x /entrypoint.sh

ENTRYPOINT [ "/entrypoint.sh" ]
