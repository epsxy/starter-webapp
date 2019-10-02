# Starter-webapp
[![Build Status](https://travis-ci.org/epsxy/starter-webapp.svg?branch=master)](https://travis-ci.org/epsxy/starter-webapp)


## Introduction

The goal of this project is to provide a ready-for-dev client/server projet, with the following features:

- Angular client
- NestJS server serving the client
- Authentication
- Tests (unit, end-to-end)
- Continuous Integration (TravisCI)
- Docker (generating images, etc)
- Internationalization (i18n)
- ORM (Sequelize, TypeORM)
- Mongo Database

## Pre-requisites

- yarn

## Getting started

```bash
$ yarn

# client
$ cd packages/client
$ yarn build
$ yarn lint
$ yarn test
$ yarn e2e
$ yarn start

# server
$ cd packages/server
$ yarn build
$ yarn test
$ yarn start
```
## Licence

The MIT Licence
