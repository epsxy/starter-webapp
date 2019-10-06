FROM alpine:latest
WORKDIR /srv

RUN apk add yarn nodejs

COPY ./package.json ./package.json
COPY ./packages/client/package.json ./packages/client/package.json
COPY ./packages/server/package.json ./packages/server/package.json

RUN yarn

COPY ./packages/client/dist ./packages/client/dist
COPY ./packages/server/dist ./packages/server/dist

ENTRYPOINT cd /srv && yarn workspace server start:prod