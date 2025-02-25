FROM python:3.13-slim

LABEL Maintainer="ashleycaselli"

ARG poetry_version

RUN pip3 install "poetry==$poetry_version"

WORKDIR /app
COPY pyproject.toml poetry.lock /app/

RUN poetry config virtualenvs.create false
RUN poetry install --only main --no-interaction

COPY src/ /app/

ENTRYPOINT ["python", "md_generator/pubsFromBib.py"]