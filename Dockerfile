FROM python:3-alpine3.6

ENV appName jobshop

ADD $appName/ /$appName
ADD requirements.txt /$appName
WORKDIR /$appName
RUN ls -aR
# Install build deps
RUN apk add --no-cache --virtual .build-deps \
		gcc \
		postgresql-dev \
		libc-dev \
	&& pip install -r requirements.txt \
	&& apk del --no-cache .build-deps

EXPOSE 5000

#CMD [ "python", "./manage.py runserver 0.0.0.0:8000" ]
ENTRYPOINT ["python"]

CMD ["-m", "main"]
