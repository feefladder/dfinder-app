# build frontend stuff
FROM node:16.14 as build-deps
COPY web ./
RUN yarn install --frozen-lockfile
RUN yarn lint
# RUN yarn run test:unit
RUN yarn build

FROM python:3.10.4-alpine3.15 as backend

# configure docker container
ENV PYTHONDONTWRITEBYTECODE=1 \
    # make poetry create the virtual environment in the project's root
    # it gets named `.venv`
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    # do not ask any interactive question
    POETRY_NO_INTERACTION=1

# build backend stuff
RUN apk update && apk add gcc python3-dev libffi-dev openssl-dev git g++ cargo
RUN pip install poetry
COPY ./dfinder-app/pyproject.toml ./dfinder-app/poetry.lock /app/
WORKDIR /app/dfinder-app
# RUN poetry update # uncomment if dfinder repo changes
RUN poetry install --no-root --no-dev

FROM python:3.10.4-alpine3.15

RUN apk update && apk add nginx dumb-init libstdc++ && rm -rf /var/cache/apk/*

RUN mkdir -p /etc/nginx/locations.d
RUN chown -R nginx /etc/nginx/locations.d

RUN mkdir -p /var/www/html
COPY --from=build-deps /dist /var/www/html
COPY dfinder-app /app/dfinder-app
WORKDIR /app/dfinder-app/dfinder-app

RUN cp nginx/default.conf /etc/nginx/http.d

# RUN cp dfinder-app/dfinder-app/nginx/default.conf /etc/nginx/http.d/default.conf
COPY --from=backend /app /app/dfinder-app

ENTRYPOINT ["/usr/bin/dumb-init", "--"]
CMD ["sh", "-c", "nginx && ../.venv/bin/python -m uvicorn --host 0.0.0.0 --port 5000 --root-path /api main:app"]