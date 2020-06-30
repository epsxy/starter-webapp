# Quick start

Install dependencies

```bash
pipenv install
```

# Dev mode

The following command will launch app listening on port `:5000`

```bash
pipenv run flask run
```

# Prod with gunicorn

```
pipenv run gunicorn main:server
```

# Using `pipenv`

```bash
# Start a virtual env
> pipenv shell

# Install a package
> pipenv install ${PACKAGE}

# Run a command
> pipenv run ${COMMAND}

# Exit a virtual env
> exit
```