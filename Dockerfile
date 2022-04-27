FROM python:3.10-slim

WORKDIR /app

LABEL Maintainer="ashleycaselli"

COPY Pipfile* ./
COPY .env.default ./.env

RUN pip install pipenv && \
  apt-get update && \
  apt-get install -y --no-install-recommends gcc python3-dev libssl-dev && \
  pipenv install --deploy --system && \
  apt-get remove -y gcc python3-dev libssl-dev && \
  apt-get autoremove -y && \
  pip uninstall pipenv -y

COPY ./ ./

CMD ["python", "./pubsFromBib.py"]