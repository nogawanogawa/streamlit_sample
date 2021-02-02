FROM python:3.7

WORKDIR /app/src

RUN apt update
RUN apt install -y curl
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
COPY pyproject.toml /app/src

RUN /root/.poetry/bin/poetry config virtualenvs.create false
RUN /root/.poetry/bin/poetry install

ENV PATH $PATH:/root/.poetry/bin


