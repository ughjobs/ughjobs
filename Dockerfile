FROM python:3-alpine3.6

ENV appName

ADD . /$appName
WORKDIR /$appName
RUN pip install -r contrib/dependencies.txt

CMD [ "python", "./manage.py runserver 0.0.0.0:8000" ]