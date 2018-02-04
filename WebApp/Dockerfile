FROM node:9.5-alpine

ENV appName WebApp

ADD $appName/ /$appName/
ADD docker_entrypoint.sh /
WORKDIR /$appName

RUN apk add --no-cache sudo
RUN npm -g config set user root
RUN apk add --no-cache --virtual .build-deps \
    build-base \
		gcc make libc-dev \
		python \
    && npm install -g @angular/cli \
    && npm install \
    && npm cache clean --force \
    && apk del --no-cache .build-deps \
    && rm -f .build-deps
RUN ng build

EXPOSE 4200

ENTRYPOINT ["/docker_entrypoint.sh"]
CMD ["ng", "serve", "--host", "0.0.0.0"]
