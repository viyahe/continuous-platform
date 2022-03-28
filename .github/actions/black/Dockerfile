FROM python:3.8-buster

RUN pip install -Iv black==20.8b1

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
