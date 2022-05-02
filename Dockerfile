FROM python:3.10-slim

LABEL Maintainer="ashleycaselli"

ENV POETRY_VERSION=1.0.0

RUN pip3 install "poetry==$POETRY_VERSION"

WORKDIR /app
COPY pyproject.toml poetry.lock /app/

RUN poetry config virtualenvs.create false
RUN poetry install --no-dev --no-interaction

COPY src/ /app/

ENTRYPOINT ["python", "md_generator/pubsFromBib.py"]