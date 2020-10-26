# BUILDER IMAGE
FROM python:3.9-slim-buster as builder

WORKDIR /usr/src/app

COPY ./api /usr/src/app/api
COPY ./migrations /usr/src/app/migrations
COPY ./.flaskenv /usr/src/app
COPY ./config.py /usr/src/app
COPY ./webstore.py /usr/src/app
COPY ./requirements.txt /usr/src/app
COPY ./entrypoint.sh /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update -yqq \
    && apt-get upgrade -yqq \
    && apt-get install -yqq --no-install-recommends \
        libpq-dev \
        build-essential \
    && pip install --upgrade pip \
    && pip install flake8 \
    && flake8 --ignore=E402,F401,W503 --exclude=migrations /usr/src/app \
    && pip wheel --no-cache-dir --wheel-dir=/usr/src/app/wheels -r /usr/src/app/requirements.txt

# FINAL IMAGE
FROM python:3.9-slim-buster as final

LABEL maintainer="Pedro Nilo <pedroniloz.nicola@gmail.com>"
LABEL application "WebStore API"
LABEL version "1.0"

RUN mkdir -p /home/webstore/api

ENV API_HOME=/home/webstore/api
ENV FLASK_ENV=production
ENV FLASK_DEBUG=0
ENV FLASK_APP=webstore:webstore_api
ENV SECRET_KEY=77tgFCdrEEdv77554##@3
ENV APP_FOLDER=$API_HOME
ENV DATABASE_URL=<provider>://<username>:<password>@<host>:<port>/<database>

WORKDIR $API_HOME

COPY --from=builder /usr/src/app $API_HOME

RUN useradd -ms /bin/bash -d $API_HOME manager \
    && apt-get update -yqq \
    && apt-get upgrade -yqq \
    && apt-get install -yqq --no-install-recommends \
        libpq-dev \
        netcat \
    && pip install --upgrade pip \
    && pip install --no-index --find-links=$API_HOME/wheels -r $API_HOME/requirements.txt \
    && chown -R manager: $API_HOME \
    && chmod +x $API_HOME/entrypoint.sh

EXPOSE 5000

USER manager

ENTRYPOINT ["/home/webstore/api/entrypoint.sh"]

CMD gunicorn --bind 0.0.0.0:5000 webstore:webstore_api --log-level=debug --log-file=-