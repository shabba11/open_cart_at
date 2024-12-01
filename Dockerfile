FROM python:3.10-alpine

WORKDIR /app

COPY requirements.txt .

RUN pip install -U pip
RUN pip install -r requirements.txt

COPY . .

COPY config.json /app

ENV PYTEST_COMMAND="pytest"

CMD ["sh", "-c", "$PYTEST_COMMAND"]
