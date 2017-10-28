FROM python:3-alpine3.6

ENV appName ughjobs

ADD . /$appName
WORKDIR /$appName
RUN ls -aR
# Install build deps
RUN apk add --no-cache --virtual .build-deps \
		gcc \
		postgresql-dev \
		libc-dev \
	&& pip install -r contrib/dependencies.txt \
	&& apk del --no-cache .build-deps

EXPOSE 8000

CMD [ "python", "./manage.py runserver 0.0.0.0:8000" ]
