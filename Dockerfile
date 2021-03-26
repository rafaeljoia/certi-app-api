FROM python:3-alpine
RUN apk add --virtual .build-dependencies \
            --no-cache \
            python3-dev \
            build-base \
            linux-headers \
            pcre-dev
RUN apk add --no-cache pcre
WORKDIR /project
COPY /project /project
COPY ./requirements.txt /project
RUN pip install -r /project/requirements.txt

RUN apk del .build-dependencies && rm -rf /var/cache/apk/*

EXPOSE 3000
CMD ["uwsgi", "--ini", "/project/wsgi.ini"]