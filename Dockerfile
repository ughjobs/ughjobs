FROM python:3-alpine3.6

ENV appName jobshop

ADD __init__.py database* main.py json/  /$appName/
ADD requirements.txt /$appName
ADD docker_entrypoint.sh /
WORKDIR /$appName
RUN ls -aR
# Install build deps
RUN apk add --no-cache sudo
RUN apk add --no-cache --virtual .build-deps \
		gcc \
		postgresql-dev \
		libc-dev \
	&& pip install -r requirements.txt \
	&& apk del --no-cache .build-deps \
	&& rm -f .build-deps

EXPOSE 5000

#CMD [ "python", "./manage.py runserver 0.0.0.0:8000" ]
ENTRYPOINT ["/docker_entrypoint.sh"]
CMD ["python", "-m", "main"]
