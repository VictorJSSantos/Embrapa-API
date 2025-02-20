FROM python:3.11-alpine3.20 AS builder

WORKDIR /code

COPY requirements-prod.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

FROM python:3.11-alpine3.20

WORKDIR /code

COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages

COPY --from=builder /usr/local/bin /usr/local/bin

COPY ./app /code/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]

